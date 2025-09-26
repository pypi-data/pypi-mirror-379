# -*- coding: utf-8 -*-
import unittest
from pathlib import Path

from PIL import Image
from pytest import raises

from kraken.lib.exceptions import KrakenInputException
from kraken.pageseg import segment

thisfile = Path(__file__).resolve().parent
resources = thisfile / 'resources'

class TestPageSeg(unittest.TestCase):

    """
    Tests of the page segmentation functionality
    """
    def test_segment_color(self):
        """
        Test correct handling of color input.
        """
        with raises(KrakenInputException):
            with Image.open(resources / 'input.jpg') as im:
                segment(im)

    def test_segment_bw(self):
        """
        Tests segmentation of bi-level input.
        """
        with Image.open(resources / 'bw.png') as im:
            seg = segment(im)
            self.assertEqual(seg.type, 'bbox')
            # test if line count is roughly correct
            self.assertAlmostEqual(len(seg.lines), 30, msg='Segmentation differs '
                                   'wildly from true line count', delta=5)
            # check if lines do not extend beyond image
            for line in seg.lines:
                box = line.bbox
                self.assertLess(0, box[0], msg='Line x0 < 0')
                self.assertLess(0, box[1], msg='Line y0 < 0')
                self.assertGreater(im.size[0], box[2], msg='Line x1 > {}'.format(im.size[0]))
                self.assertGreater(im.size[1], box[3], msg='Line y1 > {}'.format(im.size[1]))
