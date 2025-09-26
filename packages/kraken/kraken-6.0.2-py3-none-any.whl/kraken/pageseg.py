#
# Copyright 2015 Benjamin Kiessling
#           2014 Thomas M. Breuel
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing
# permissions and limitations under the License.
"""
kraken.pageseg
~~~~~~~~~~~~~~

Layout analysis methods.
"""
import logging
import uuid
from typing import Callable, List, Optional, Tuple, Union

import numpy as np
import PIL
from scipy.ndimage import gaussian_filter, maximum_filter, uniform_filter

from kraken.containers import BBoxLine, Segmentation
from kraken.lib import morph, sl
from kraken.lib.exceptions import KrakenInputException
from kraken.lib.segmentation import reading_order, topsort
from kraken.lib.util import get_im_str, is_bitonal, pil2array

__all__ = ['segment']

logger = logging.getLogger(__name__)


class record(object):
    """
    Simple dict-like object.
    """
    def __init__(self, **kw):
        self.__dict__.update(kw)
        self.label: int = 0
        self.bounds: List = []
        self.mask: np.ndarray = None


def find(condition):
    "Return the indices where ravel(condition) is true"
    res, = np.nonzero(np.ravel(condition))
    return res


def binary_objects(binary: np.ndarray) -> np.ndarray:
    """
    Labels features in an array and segments them into objects.
    """
    labels, _ = morph.label(binary)
    objects = morph.find_objects(labels)
    return objects


def estimate_scale(binary: np.ndarray) -> float:
    """
    Estimates image scale based on number of connected components.
    """
    objects = binary_objects(binary)
    bysize = sorted(objects, key=sl.area)
    scalemap = np.zeros(binary.shape)
    for o in bysize:
        if np.amax(scalemap[o]) > 0:
            continue
        scalemap[o] = sl.area(o)**0.5
    scale = np.median(scalemap[(scalemap > 3) & (scalemap < 100)])
    return scale


def compute_boxmap(binary: np.ndarray, scale: float,
                   threshold: Tuple[float, int] = (.5, 4),
                   dtype: str = 'i') -> np.ndarray:
    """
    Returns grapheme cluster-like boxes based on connected components.
    """
    objects = binary_objects(binary)
    bysize = sorted(objects, key=sl.area)
    boxmap = np.zeros(binary.shape, dtype)
    for o in bysize:
        if sl.area(o)**.5 < threshold[0]*scale:
            continue
        if sl.area(o)**.5 > threshold[1]*scale:
            continue
        boxmap[o] = 1
    return boxmap


def compute_lines(segmentation: np.ndarray, scale: float) -> List[record]:
    """Given a line segmentation map, computes a list
    of tuples consisting of 2D slices and masked images."""
    logger.debug('Convert segmentation to lines')
    lobjects = morph.find_objects(segmentation)
    lines = []
    for i, o in enumerate(lobjects):
        if o is None:
            continue
        if sl.dim1(o) < 2*scale or sl.dim0(o) < scale:
            continue
        mask = (segmentation[o] == i+1)
        if np.amax(mask) == 0:
            continue
        result = record()
        result.label = i+1
        result.bounds = o
        result.mask = mask
        lines.append(result)
    return lines


def compute_separators_morph(binary: np.ndarray, scale: float, sepwiden: int = 10, maxcolseps: int = 2) -> np.ndarray:
    """Finds vertical black lines corresponding to column separators."""
    logger.debug('Finding vertical black column lines')
    d0 = int(max(5, scale/4))
    d1 = int(max(5, scale)) + sepwiden
    thick = morph.r_dilation(binary, (d0, d1))
    vert = morph.rb_opening(thick, (10*scale, 1))
    vert = morph.r_erosion(vert, (d0//2, sepwiden))
    vert = morph.select_regions(vert, sl.dim1, min=3, nbest=2*maxcolseps)
    vert = morph.select_regions(vert, sl.dim0, min=20*scale, nbest=maxcolseps)
    return vert


def compute_colseps_conv(binary: np.ndarray, scale: float = 1.0,
                         minheight: int = 10, maxcolseps: int = 2) -> np.ndarray:
    """
    Find column separators by convolution and thresholding.

    Args:
        binary:
        scale:
        minheight:
        maxcolseps:

    Returns:
        Separators
    """
    logger.debug(f'Finding max {maxcolseps} column separators')
    # find vertical whitespace by thresholding
    smoothed = gaussian_filter(1.0*binary, (scale, scale*0.5))
    smoothed = uniform_filter(smoothed, (5.0*scale, 1))
    thresh = (smoothed < np.amax(smoothed)*0.1)
    # find column edges by filtering
    grad = gaussian_filter(1.0*binary, (scale, scale*0.5), order=(0, 1))
    grad = uniform_filter(grad, (10.0*scale, 1))
    grad = (grad > 0.5*np.amax(grad))
    # combine edges and whitespace
    seps = np.minimum(thresh, maximum_filter(grad, (int(scale), int(5*scale))))
    seps = maximum_filter(seps, (int(2*scale), 1))
    # select only the biggest column separators
    seps = morph.select_regions(seps, sl.dim0, min=minheight*scale,
                                nbest=maxcolseps)
    return seps


def compute_black_colseps(binary: np.ndarray, scale: float, maxcolseps: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Computes column separators from vertical black lines.

    Args:
        binary: Numpy array of the binary image
        scale:
        maxcolseps:

    Returns:
        (colseps, binary):
    """
    logger.debug('Extract vertical black column separators from lines')
    seps = compute_separators_morph(binary, scale, maxcolseps)
    colseps = np.maximum(compute_colseps_conv(binary, scale, maxcolseps=maxcolseps), seps)
    binary = np.minimum(binary, 1-seps)
    return colseps, binary


def compute_white_colseps(binary: np.ndarray, scale: float, maxcolseps: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Computes column separators either from vertical black lines or whitespace.

    Args:
        binary: Numpy array of the binary image
        scale:

    Returns:
        colseps:
    """
    return compute_colseps_conv(binary, scale, maxcolseps=maxcolseps)


def norm_max(v: np.ndarray) -> np.ndarray:
    """
    Normalizes the input array by maximum value.
    """
    return v/np.amax(v)


def compute_gradmaps(binary: np.ndarray, scale: float, gauss: bool = False):
    """
    Use gradient filtering to find baselines

    Args:
        binary:
        scale:
        gauss: Use gaussian instead of uniform filtering

    Returns:
        (bottom, top, boxmap)
    """
    # use gradient filtering to find baselines
    logger.debug('Computing gradient maps')
    boxmap = compute_boxmap(binary, scale)
    cleaned = boxmap*binary
    if gauss:
        grad = gaussian_filter(1.0*cleaned, (0.3*scale, 6*scale), order=(1, 0))
    else:
        grad = gaussian_filter(1.0*cleaned, (max(4, 0.3*scale),
                                             scale), order=(1, 0))
        grad = uniform_filter(grad, (1, 6*scale))
    bottom = norm_max((grad < 0)*(-grad))
    top = norm_max((grad > 0)*grad)
    return bottom, top, boxmap


def compute_line_seeds(binary: np.ndarray, bottom: np.ndarray, top: np.ndarray,
                       colseps: np.ndarray, scale: float, threshold: float = 0.2) -> np.ndarray:
    """
    Base on gradient maps, computes candidates for baselines and xheights.
    Then, it marks the regions between the two as a line seed.
    """
    logger.debug('Finding line seeds')
    vrange = int(scale)
    bmarked = maximum_filter(bottom == maximum_filter(bottom, (vrange, 0)),
                             (2, 2))
    bmarked = bmarked * (bottom > threshold*np.amax(bottom)*threshold)*(1-colseps)
    tmarked = maximum_filter(top == maximum_filter(top, (vrange, 0)), (2, 2))
    tmarked = tmarked * (top > threshold*np.amax(top)*threshold/2)*(1-colseps)
    tmarked = maximum_filter(tmarked, (1, 20))
    seeds = np.zeros(binary.shape, 'i')
    delta = max(3, int(scale/2))
    for x in range(bmarked.shape[1]):
        transitions = sorted([(y, 1) for y in find(bmarked[:, x])] +
                             [(y, 0) for y in find(tmarked[:, x])])[::-1]
        transitions += [(0, 0)]
        for ls in range(len(transitions)-1):
            y0, s0 = transitions[ls]
            if s0 == 0:
                continue
            seeds[y0-delta:y0, x] = 1
            y1, s1 = transitions[ls+1]
            if s1 == 0 and (y0-y1) < 5*scale:
                seeds[y1:y0, x] = 1
    seeds = maximum_filter(seeds, (1, int(1+scale)))
    seeds = seeds * (1-colseps)
    seeds, _ = morph.label(seeds)
    return seeds


def remove_hlines(binary: np.ndarray, scale: float, maxsize: int = 10) -> np.ndarray:
    """
    Removes horizontal black lines that only interfere with page segmentation.

        Args:
            binary:
            scale:
            maxsize: maximum size of removed lines

        Returns:
            numpy.ndarray containing the filtered image.

    """
    logger.debug('Filtering horizontal lines')
    labels, _ = morph.label(binary)
    objects = morph.find_objects(labels)
    for i, b in enumerate(objects):
        if sl.width(b) > maxsize*scale:
            labels[b][labels[b] == i+1] = 0
    return np.array(labels != 0, 'B')


def rotate_lines(lines: np.ndarray, angle: float, offset: int) -> np.ndarray:
    """
    Rotates line bounding boxes around the origin and adding and offset.
    """
    logger.debug(f'Rotate line coordinates by {angle} with offset {offset}')
    angle = np.radians(angle)
    r = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
    p = np.array(lines).reshape((-1, 2))
    offset = np.array([2*offset])
    p = p.dot(r).reshape((-1, 4)).astype(int) + offset
    x = np.sort(p[:, [0, 2]])
    y = np.sort(p[:, [1, 3]])
    return np.column_stack((x.flatten(), y.flatten())).reshape(-1, 4)


def segment(im: PIL.Image.Image,
            text_direction: str = 'horizontal-lr',
            scale: Optional[float] = None,
            maxcolseps: float = 2,
            black_colseps: bool = False,
            no_hlines: bool = True,
            pad: Union[int, Tuple[int, int]] = 0,
            mask: Optional[np.ndarray] = None,
            reading_order_fn: Callable = reading_order) -> Segmentation:
    """
    Segments a page into text lines.

    Segments a page into text lines and returns the absolute coordinates of
    each line in reading order.

    Args:
        im: A bi-level page of mode '1' or 'L'
        text_direction: Determines principal text direction for heuristic
                        reading order determination and value for line
                        orientation. Passed-through value for Segmentation
                        container class.
        scale: Scale of the image. Will be auto-determined if set to `None`.
        maxcolseps: Maximum number of whitespace column separators
        black_colseps: Whether column separators are assumed to be vertical
                       black lines or not
        no_hlines: Switch for small horizontal line removal.
        pad: Padding to add to line bounding boxes. If int the same padding is
             used both left and right. If a 2-tuple, uses (padding_left,
             padding_right).
        mask: A bi-level mask image of the same size as `im` where 0-valued
              regions are ignored for segmentation purposes. Disables column
              detection.
        reading_order_fn: Function to call to order line output. Callable
                          accepting a list of slices (y, x) and a text
                          direction in (`rl`, `lr`).

    Returns:
        A :class:`kraken.containers.Segmentation` class containing reading
        order sorted bounding box-type lines as
        :class:`kraken.containers.BBoxLine` records.

    Raises:
        KrakenInputException: if the input image is not binarized or the text
                              direction is invalid.
    """
    im_str = get_im_str(im)
    logger.info(f'Segmenting {im_str}')

    if im.mode != '1' and not is_bitonal(im):
        logger.error(f'Image {im_str} is not bi-level')
        raise KrakenInputException(f'Image {im_str} is not bi-level')

    # rotate input image for vertical lines
    if text_direction.startswith('horizontal'):
        angle = 0
        offset = (0, 0)
    elif text_direction == 'vertical-lr':
        angle = 270
        offset = (0, im.size[1])
    elif text_direction == 'vertical-rl':
        angle = 90
        offset = (im.size[0], 0)
    else:
        logger.error(f'Invalid text direction \'{text_direction}\'')
        raise KrakenInputException(f'Invalid text direction {text_direction}')

    logger.debug(f'Rotating input image by {angle} degrees')
    im = im.rotate(angle, expand=True)

    a = pil2array(im)
    binary = np.array(a > 0.5*(np.amin(a) + np.amax(a)), 'i')
    binary = 1 - binary

    _, ccs = morph.label(1 - binary)
    if ccs > np.dot(*im.size)/(30*30):
        logger.warning(f'Too many connected components for a page image: {ccs}')
        return {'text_direction': text_direction, 'boxes':  []}

    if not scale:
        scale = estimate_scale(binary)

    if no_hlines:
        binary = remove_hlines(binary, scale)
    # emptyish images will cause exceptions here.

    try:
        if mask:
            if mask.mode != '1' and not is_bitonal(mask):
                logger.error('Mask is not bitonal')
                raise KrakenInputException('Mask is not bitonal')
            mask = mask.convert('1')
            if mask.size != im.size:
                logger.error(f'Mask size {mask.size} doesn\'t match image size {im.size}')
                raise KrakenInputException(f'Mask size {mask.size} doesn\'t match image size {im.size}')
            logger.info('Masking enabled in segmenter. Disabling column detection.')
            mask = mask.rotate(angle, expand=True)
            colseps = pil2array(mask)
        elif black_colseps:
            colseps, binary = compute_black_colseps(binary, scale, maxcolseps)
        else:
            colseps = compute_white_colseps(binary, scale, maxcolseps)
    except ValueError:
        logger.warning(f'Exception in column finder (probably empty image) for {im_str}')
        return {'text_direction': text_direction, 'boxes':  []}

    bottom, top, boxmap = compute_gradmaps(binary, scale)
    seeds = compute_line_seeds(binary, bottom, top, colseps, scale)
    llabels = morph.propagate_labels(boxmap, seeds, conflict=0)
    spread = morph.spread_labels(seeds, maxdist=scale)
    llabels = np.where(llabels > 0, llabels, spread*binary)
    segmentation = llabels*binary

    lines = compute_lines(segmentation, scale)
    order = reading_order_fn([line.bounds for line in lines], text_direction[-2:])
    lsort = topsort(order)
    lines = [lines[i].bounds for i in lsort]
    lines = [(s2.start, s1.start, s2.stop, s1.stop) for s1, s2 in lines]

    if isinstance(pad, int):
        pad = (pad, pad)
    lines = [(max(x[0]-pad[0], 0), x[1], min(x[2]+pad[1], im.size[0]), x[3]) for x in lines]
    lines = [BBoxLine(id=f'_{uuid.uuid4()}', bbox=line) for line in rotate_lines(lines, 360-angle, offset).tolist()]

    return Segmentation(text_direction=text_direction,
                        imagename=getattr(im, 'filename', None),
                        type='bbox',
                        regions=None,
                        line_orders=None,
                        lines=lines,
                        script_detection=False)
