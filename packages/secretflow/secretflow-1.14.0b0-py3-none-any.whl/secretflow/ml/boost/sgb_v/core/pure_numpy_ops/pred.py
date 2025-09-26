# Copyright 2023 Ant Group Co., Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from functools import reduce
from typing import List

import numpy as np


def init_pred(base: float, samples: int) -> np.ndarray:
    shape = (samples, 1)
    return np.full(shape, base, order='F')


def sigmoid(pred: np.ndarray) -> np.ndarray:
    # Note that if you change the sigmoid calculation mode,
    # please revise the logic at `secretflow/component/model_export/serving_utils/train_model_converter.py sgb_converter`
    # simultaneously to keep the sigmoid calculation logic consistent for the online prediction
    return 1 / (1 + np.exp(-pred))


def predict_tree_weight(selects: List[np.ndarray], weights: np.ndarray) -> np.ndarray:
    """
    get final pred for this tree.

    Args:
        selects: leaf nodes' sample selects from each model handler.
        weights: leaf weights.

    Return:
        pred
    """
    # get final leaf selects based on collective information
    select = reduce(np.multiply, selects)
    assert (
        select.shape[1] == weights.shape[0]
    ), f"select {select.shape}, weights {weights.shape}"
    return np.matmul(select, weights).reshape((select.shape[0]), 1)
