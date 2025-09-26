# Copyright 2024 Ant Group Co., Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from abc import ABC, abstractmethod
from enum import Enum, unique
from typing import Union

import jax.numpy as jnp
import numpy as np

from secretflow.utils import sigmoid as appr_sig
from secretflow.utils.errors import InvalidArgumentError


@unique
class LinkType(Enum):
    Logit = 'Logit'
    Log = 'Log'
    Reciprocal = 'Reciprocal'
    Identity = 'Identity'


class Linker(ABC):
    @abstractmethod
    def link(self, mu: np.ndarray) -> np.ndarray:
        raise NotImplementedError()

    @abstractmethod
    def response(self, eta: np.ndarray) -> np.ndarray:
        raise NotImplementedError()

    @abstractmethod
    def response_derivative(self, mu: np.ndarray) -> np.ndarray:
        raise NotImplementedError()

    @abstractmethod
    def link_derivative(self, mu: np.ndarray) -> np.ndarray:
        raise NotImplementedError()


class LinkLogit(Linker):
    @staticmethod
    def link_type() -> Linker:
        return LinkType.Logit

    def link(self, mu: np.ndarray) -> np.ndarray:
        return jnp.log(mu / (1 - mu))

    def response(self, eta: np.ndarray) -> np.ndarray:
        return appr_sig.sr_sig(eta)

    def response_derivative(self, mu: np.ndarray) -> np.ndarray:
        return mu * (1 - mu)

    def link_derivative(self, mu: np.ndarray) -> np.ndarray:
        return 1 / self.response_derivative(mu)


class LinkLog(Linker):
    @staticmethod
    def link_type() -> Linker:
        return LinkType.Log

    def link(self, mu: np.ndarray) -> np.ndarray:
        return jnp.log(mu)

    def response(self, eta: np.ndarray) -> np.ndarray:
        return jnp.exp(eta)

    def response_derivative(self, mu: np.ndarray) -> np.ndarray:
        return mu

    def link_derivative(self, mu: np.ndarray) -> np.ndarray:
        return 1 / self.response_derivative(mu)


class LinkReciprocal(Linker):
    @staticmethod
    def link_type() -> Linker:
        return LinkType.Reciprocal

    def link(self, mu: np.ndarray) -> np.ndarray:
        return 1 / mu

    def response(self, eta: np.ndarray) -> np.ndarray:
        return 1 / eta

    def response_derivative(self, mu: np.ndarray) -> np.ndarray:
        return -jnp.square(mu)

    def link_derivative(self, mu: np.ndarray) -> np.ndarray:
        return 1 / self.response_derivative(mu)


class LinkIdentity(Linker):
    @staticmethod
    def link_type() -> Linker:
        return LinkType.Identity

    def link(self, mu: np.ndarray) -> np.ndarray:
        return mu

    def response(self, eta: np.ndarray) -> np.ndarray:
        return eta

    def response_derivative(self, mu: np.ndarray) -> np.ndarray:
        return jnp.ones(mu.shape)

    def link_derivative(self, mu: np.ndarray) -> np.ndarray:
        return jnp.ones(mu.shape)


def get_link(t: Union[LinkType, str]) -> Linker:
    if isinstance(t, str):
        assert t in [
            e.value for e in LinkType
        ], f"link type should in {[e.value for e in LinkType]}, but got {t}"
        t = LinkType(t)

    if t is LinkType.Logit:
        return LinkLogit()
    elif t is LinkType.Log:
        return LinkLog()
    elif t is LinkType.Reciprocal:
        return LinkReciprocal()
    elif t is LinkType.Identity:
        return LinkIdentity()
    else:
        raise InvalidArgumentError(f'Unsupported link: {t}')
