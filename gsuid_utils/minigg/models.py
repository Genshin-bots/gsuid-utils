"""
MiniGG API 响应模型。
"""
# TODO: - @KimigaiiWuyi 补文档
from __future__ import annotations

import sys
from typing import TypeAlias, TypedDict

# https://peps.python.org/pep-0655/#usage-in-python-3-11
if sys.version_info >= (3, 11):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired

R: TypeAlias = list[str]


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
    ascend1: list[AscendItem]
    ascend2: list[AscendItem]
    ascend3: list[AscendItem]
    ascend4: list[AscendItem]
    ascend5: list[AscendItem]
    ascend6: list[AscendItem]


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
