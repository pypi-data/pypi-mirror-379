# Copyright 2022 Ant Group Co., Ltd.
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
import math
from typing import List, Union

import secretflow as sf
from secretflow.data.vertical import VDataFrame
from secretflow.device import PYU, SPU, DeviceObject
from secretflow.preprocessing.scaler import StandardScaler
from secretflow.utils.blocked_ops import block_compute_vdata


class PearsonR:
    """
    Calculate pearson product-moment correlation coefficient for vertical slice dataset
    by using secret sharing.

    more detail for PearsonR:
    https://en.wikipedia.org/wiki/Pearson_correlation_coefficient

    For large dataset(large than 10w samples & 200 features)
    Recommend use [Ring size: 128, Fxp: 40] options for SPU device.

    Attributes:

        device: SPU Device
    """

    def __init__(self, device: Union[SPU, PYU]):
        self.device = device

    def pearsonr(
        self,
        data: Union[VDataFrame, DeviceObject],
        standardize: bool = True,
        infeed_elements_limit: int = 20000000,
    ):
        """
        Attributes:

            data : VDataFrame or DeviceObject
                vertical slice dataset or pyu object of dataframe liked
            standardize: bool
                if you need standardize dataset. dataset must be standardized
                please keep standardize=True, unless dataset is already standardized.
                standardize purpose:
                - reduce the result number of matrix xtx, avoid overflow in secret sharing.
                - after standardize, the variance is 1 and the mean is 0, which can simplify the calculation.
        """

        if standardize:
            scaler = StandardScaler()
            vdata = scaler.fit_transform(data)
        else:
            vdata = data
        rows = vdata.shape[0]
        cols = vdata.shape[1]
        row_number = max([math.ceil(infeed_elements_limit / cols), 1])

        xTx = block_compute_vdata(
            vdata, row_number, self.device, lambda x: x.T @ x, lambda x, y: x + y
        )

        xtx = sf.reveal(xTx)
        return xtx / (rows - 1)
