from __future__ import annotations

import sys
from typing import Literal, TypedDict

# https://peps.python.org/pep-0655/#usage-in-python-3-11
if sys.version_info >= (3, 11):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired


class EnkaData(TypedDict):
    playerInfo: PlayerInfo
    avatarInfoList: list[AvatarInfoListItem]
    ttl: int
    uid: str


class PlayerInfo(TypedDict):
    nickname: str
    level: int
    signature: str
    worldLevel: int
    nameCardId: int
    finishAchievementNum: int
    towerFloorIndex: int
    towerLevelIndex: int
    showAvatarInfoList: list[ShowAvatarInfoListItem]
    showNameCardIdList: NotRequired[list[int]]
    profilePicture: ProfilePicture


class ShowAvatarInfoListItem(TypedDict):
    avatarId: int
    level: int
    costumeId: NotRequired[int]


class ProfilePicture(TypedDict):
    avatarId: int


class AvatarInfoListItem(TypedDict):
    avatarId: int
    propMap: dict[str, PropMap]
    talentIdList: NotRequired[list[int]]
    fightPropMap: dict[str, float]
    skillDepotId: int
    inherentProudSkillList: list[int]
    skillLevelMap: dict[str, int]
    equipList: list[Equip]
    fetterInfo: FetterInfo


class Equip(TypedDict):
    itemId: int
    reliquary: NotRequired[Reliquary]
    weapon: Weapon
    flat: Flat


class Flat(TypedDict):
    # l10n
    nameTextMapHash: str
    setNameTextMapHash: NotRequired[str]

    # artifact
    reliquaryMainstat: NotRequired[Stat]
    reliquarySubstats: NotRequired[list[Stat]]
    equipType: Literal[
        "EQUIP_BRACER",
        "EQUIP_NECKLACE",
        "EQUIP_SHOES",
        "EQUIP_RING",
        "EQUIP_DRESS",
    ]

    # weapon
    weaponStats: NotRequired[list[Stat]]

    rankLevel: Literal[3, 4, 5]
    itemType: Literal["ITEM_WEAPON", "ITEM_RELIQUARY"]
    icon: str  # https://enka.network/ui/{Icon}.png


class Stat(TypedDict):
    mainPropId: NotRequired[str]
    appendPropId: NotRequired[str]
    statValue: float | int


class Weapon(TypedDict):
    level: int
    promoteLevel: int
    affixMap: dict[str, int]


class Reliquary(TypedDict):
    level: int
    mainPropId: int
    appendPropIdList: list[int]


class PropMap(TypedDict):
    type: int
    ival: str  # Ignore It!
    val: NotRequired[str]


class FetterInfo(TypedDict):
    expLevel: int
