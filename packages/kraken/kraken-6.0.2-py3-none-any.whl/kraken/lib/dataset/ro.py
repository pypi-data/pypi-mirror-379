#
# Copyright 2015 Benjamin Kiessling
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
Utility functions for data loading and training of VGSL networks.
"""
from math import factorial
from typing import TYPE_CHECKING, Dict, Literal, Optional, Sequence, Union

import numpy as np
import torch
from torch.utils.data import Dataset

from kraken.lib.xml import XMLPage
from kraken.lib.dataset.utils import _get_type
from kraken.lib.exceptions import KrakenInputException

if TYPE_CHECKING:
    from os import PathLike

__all__ = ['PairWiseROSet', 'PageWiseROSet']

import logging

logger = logging.getLogger(__name__)


class PairWiseROSet(Dataset):
    """
    Dataset for training a reading order determination model.

    Returns random pairs of lines from the same page.
    """
    def __init__(self, files: Sequence[Union['PathLike', str]] = None,
                 mode: Optional[Literal['alto', 'page', 'xml']] = 'xml',
                 level: Literal['regions', 'baselines'] = 'baselines',
                 ro_id: Optional[str] = None,
                 valid_entities: Sequence[str] = None,
                 merge_entities: Dict[str, Sequence[str]] = None,
                 merge_all_entities: bool = False,
                 class_mapping: Optional[Dict[str, int]] = None) -> None:
        """
        Samples pairs lines/regions from XML files for training a reading order
        model .

        Args:
            mode: Selects type of data source files.
            level: Computes reading order tuples on line or region level.
            ro_id: ID of the reading order to sample from. Defaults to
                   `line_implicit`/`region_implicit`.
            valid_entities: Sequence of valid baseline/regions identifiers. If `None`
                             all are valid.
            merge_entities: Sequence of baseline/region identifiers to merge.  Note
                             that merging occurs after entities not in valid_*
                             have been discarded.
            merge_all_entities: Merges all entities types into default (after
                                filtering with valid_entities).
            class_mapping: Explicit class mapping to use. No sanity checks are
                           performed. Takes precedence over valid_*, merge_*.
        """
        super().__init__()

        self._num_pairs = 0
        self.failed_samples = []
        if class_mapping:
            self.class_mapping = class_mapping
            self.num_classes = len(class_mapping) + 1
            self.freeze_cls_map = True
            valid_entities = None
            merge_entities = None
            merge_all_entities = None
        else:
            self.num_classes = 1
            self.class_mapping = {}
            self.freeze_cls_map = False

        self.m_dict = merge_entities if merge_entities is not None else {}
        self.merge_all_entities = merge_all_entities
        self.valid_entities = valid_entities

        self.data = []

        if mode in ['alto', 'page', 'xml']:
            docs = []
            for file in files:
                try:
                    doc = XMLPage(file, filetype=mode)
                    if level == 'baselines':
                        if not ro_id:
                            ro_id = 'line_implicit'
                        order = doc.get_sorted_lines(ro_id)
                    elif level == 'regions':
                        if not ro_id:
                            ro_id = 'region_implicit'
                        order = doc.get_sorted_regions(ro_id)
                    else:
                        raise ValueError(f'Invalid RO type {level}')
                    _order = []
                    for el in order:
                        tag_val = _get_type(el.tags)
                        if self.valid_entities is None or tag_val in self.valid_entities:
                            tag = self.m_dict.get(tag_val, tag_val)
                            if self.merge_all_entities:
                                tag = None
                            elif tag not in self.class_mapping and self.freeze_cls_map:
                                continue
                            elif tag not in self.class_mapping:
                                self.class_mapping[tag] = self.num_classes
                                self.num_classes += 1
                            _order.append((tag, el))
                    docs.append((doc.image_size, _order))
                except KrakenInputException as e:
                    logger.warning(e)
                    continue

            for (w, h), order in docs:
                # traverse RO and substitute features.
                sorted_lines = []
                for tag, line in order:
                    line_coords = np.array(line.baseline) / (w, h)
                    line_center = np.mean(line_coords, axis=0)
                    cl = torch.zeros(self.num_classes, dtype=torch.float)
                    # if class is not in class mapping default to None class (idx 0)
                    cl[self.class_mapping.get(tag, 0)] = 1
                    line_data = {'type': tag,
                                 'features': torch.cat((cl,  # one hot encoded line type
                                                        torch.tensor(line_center, dtype=torch.float),  # line center
                                                        torch.tensor(line_coords[0, :], dtype=torch.float),  # start_point coord
                                                        torch.tensor(line_coords[-1, :], dtype=torch.float),  # end point coord)
                                                        )
                                                       )
                                 }
                    sorted_lines.append(line_data)
                if len(sorted_lines) > 1:
                    self.data.append(sorted_lines)
                    self._num_pairs += int(factorial(len(sorted_lines))/factorial(len(sorted_lines)-2))
                else:
                    logger.info(f'Page {doc} has less than 2 lines. Skipping')
        else:
            raise Exception('invalid dataset mode')

    def __getitem__(self, idx):
        lines = []
        while len(lines) < 2:
            lines = self.data[torch.randint(len(self.data), (1,))[0]]
        idx0, idx1 = 0, 0
        while idx0 == idx1:
            idx0, idx1 = torch.randint(len(lines), (2,))
        x = torch.cat((lines[idx0]['features'], lines[idx1]['features']))
        y = torch.tensor(0 if idx0 >= idx1 else 1, dtype=torch.float)
        return {'sample': x, 'target': y}

    def get_feature_dim(self):
        return 2 * self.num_classes + 12

    def __len__(self):
        return self._num_pairs


class PageWiseROSet(Dataset):
    """
    Dataset for training a reading order determination model.

    Returns all lines from the same page.
    """
    def __init__(self, files: Sequence[Union['PathLike', str]] = None,
                 mode: Optional[Literal['alto', 'page', 'xml']] = 'xml',
                 level: Literal['regions', 'baselines'] = 'baselines',
                 ro_id: Optional[str] = None,
                 valid_entities: Sequence[str] = None,
                 merge_entities: Dict[str, Sequence[str]] = None,
                 merge_all_entities: bool = False,
                 class_mapping: Optional[Dict[str, int]] = None) -> None:
        """
        Samples pairs lines/regions from XML files for evaluating a reading order
        model.

        Args:
            mode: Selects type of data source files.
            level: Computes reading order tuples on line or region level.
            ro_id: ID of the reading order to sample from. Defaults to
                   `line_implicit`/`region_implicit`.
            valid_entities: Sequence of valid baseline/regions identifiers. If `None`
                             all are valid.
            merge_entities: Sequence of baseline/region identifiers to merge.  Note
                             that merging occurs after entities not in valid_*
                             have been discarded.
            class_mapping: Explicit class mapping to use. No sanity checks are performed.
        """
        super().__init__()

        self.failed_samples = []
        if class_mapping:
            self.class_mapping = class_mapping
            self.num_classes = len(class_mapping) + 1
            self.freeze_cls_map = True
            valid_entities = None
            merge_entities = None
            merge_all_entities = False
        else:
            self.num_classes = 1
            self.class_mapping = {}
            self.freeze_cls_map = False

        self.m_dict = merge_entities if merge_entities is not None else {}
        self.merge_all_entities = merge_all_entities
        self.valid_entities = valid_entities

        self.data = []

        if mode in ['alto', 'page', 'xml']:
            docs = []
            for file in files:
                try:
                    doc = XMLPage(file, filetype=mode)
                    if level == 'baselines':
                        if not ro_id:
                            ro_id = 'line_implicit'
                        order = doc.get_sorted_lines(ro_id)
                    elif level == 'regions':
                        if not ro_id:
                            ro_id = 'region_implicit'
                        order = doc.get_sorted_regions(ro_id)
                    else:
                        raise ValueError(f'Invalid RO type {level}')
                    _order = []
                    for el in order:
                        tag_val = _get_type(el.tags)
                        if self.valid_entities is None or tag_val in self.valid_entities:
                            tag = self.m_dict.get(tag_val, tag_val)
                            if self.merge_all_entities:
                                tag = None
                            elif tag not in self.class_mapping and self.freeze_cls_map:
                                continue
                            elif tag not in self.class_mapping:
                                self.class_mapping[tag] = self.num_classes
                                self.num_classes += 1
                            _order.append((tag, el))
                    docs.append((doc.image_size, _order))
                except KrakenInputException as e:
                    logger.warning(e)
                    continue

            for (w, h), order in docs:
                # traverse RO and substitute features.
                sorted_lines = []
                for tag, line in order:
                    line_coords = np.array(line.baseline) / (w, h)
                    line_center = np.mean(line_coords, axis=0)
                    cl = torch.zeros(self.num_classes, dtype=torch.float)
                    # if class is not in class mapping default to None class (idx 0)
                    cl[self.class_mapping.get(tag, 0)] = 1
                    line_data = {'type': tag,
                                 'features': torch.cat((cl,  # one hot encoded line type
                                                        torch.tensor(line_center, dtype=torch.float),  # line center
                                                        torch.tensor(line_coords[0, :], dtype=torch.float),  # start_point coord
                                                        torch.tensor(line_coords[-1, :], dtype=torch.float),  # end point coord)
                                                        )
                                                       )
                                 }
                    sorted_lines.append(line_data)
                if len(sorted_lines) > 1:
                    self.data.append(sorted_lines)
                else:
                    logger.info(f'Page {doc} has less than 2 lines. Skipping')
        else:
            raise Exception('invalid dataset mode')

    def __getitem__(self, idx):
        xs = []
        ys = []
        for i in range(len(self.data[idx])):
            for j in range(len(self.data[idx])):
                if i == j and len(self.data[idx]) != 1:
                    continue
                xs.append(torch.cat((self.data[idx][i]['features'],
                                     self.data[idx][j]['features'])))
                ys.append(torch.tensor(0 if i >= j else 1, dtype=torch.float))
        return {'sample': torch.stack(xs), 'target': torch.stack(ys), 'num_lines': len(self.data[idx])}

    def get_feature_dim(self):
        return 2 * self.num_classes + 12

    def __len__(self):
        return len(self.data)
