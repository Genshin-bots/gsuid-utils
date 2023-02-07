"""
MiniGG API 响应模型。
"""
# TODO: - @KimigaiiWuyi 补文档
from __future__ import annotations

import sys
from typing import List, TypedDict

# https://peps.python.org/pep-0655/#usage-in-python-3-11
if sys.version_info >= (3, 11):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired

# https://peps.python.org/pep-0613
if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

R: TypeAlias = List[str]


class FandomUrl(TypedDict):
    fandom: str


class Image(TypedDict):
    image: str
    nameicon: str
    namegacha: str
    icon: str
    nameawakenicon: str
    awakenicon: str


class AscendItem(TypedDict):
    name: str
    count: int


class WeaponCosts(TypedDict):
    ascend1: List[AscendItem]
    ascend2: List[AscendItem]
    ascend3: List[AscendItem]
    ascend4: List[AscendItem]
    ascend5: List[AscendItem]
    ascend6: List[AscendItem]


class Weapon(TypedDict):
    name: str
    description: str
    weapontype: str
    rarity: str
    baseatk: int
    substat: str
    subvalue: str
    effectname: str
    effect: str
    r1: R
    r2: R
    r3: R
    r4: R
    r5: R
    weaponmaterialtype: str
    images: Image
    url: NotRequired[FandomUrl]
    version: str
    costs: WeaponCosts


class WeaponStats(TypedDict):
    level: int
    ascension: int
    attack: float
    specialized: float
