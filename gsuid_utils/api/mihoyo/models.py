from __future__ import annotations

import sys
from typing import List, Literal, TypedDict, NotRequired

# https://peps.python.org/pep-0655/#usage-in-python-3-11
if sys.version_info >= (3, 11):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired


# Response about https://api-takumi-record.mihoyo.com/game_record/app/genshin/api/index
# and https://api-takumi-record.mihoyo.com/game_record/app/genshin/api/character
# 玩家、武器、圣遗物、角色模型


class MihoyoRole(TypedDict):
    AvatarUrl: str
    nickname: str
    region: str
    level: int


class MihoyoWeapon(TypedDict):
    id: int
    name: str
    icon: str
    type: int
    rarity: int
    level: int
    promote_level: int
    type_name: Literal['单手剑', '双手剑', '长柄武器', '弓', '法器']
    desc: str
    affix_level: int


class ReliquaryAffix(TypedDict):
    activation_number: int
    effect: str


class ReliquarySet(TypedDict):
    id: int
    name: str
    affixes: List[ReliquaryAffix]


class MihoyoReliquary(TypedDict):
    id: int
    name: str
    icon: str
    pos: int
    rarity: int
    level: int
    set: ReliquarySet
    pos_name: str


class MihoyoConstellation(TypedDict):
    id: int
    name: str
    icon: str
    effect: str
    is_actived: bool
    pos: int


class MihoyoCostume(TypedDict):
    id: int
    name: str
    icon: str


class MihoyoAvatar(TypedDict):
    id: int
    image: str
    icon: NotRequired[str]
    """在api/character接口有"""
    name: str
    element: Literal[
        'Geo', 'Anemo', 'Dendro', 'Electro', 'Pyro', 'Cryo', 'Hydro'
    ]
    fetter: int
    level: int
    rarity: int
    weapon: NotRequired[MihoyoWeapon]
    """在api/character接口有"""
    reliquaries: NotRequired[List[MihoyoReliquary]]
    """在api/character接口有"""
    constellations: NotRequired[List[MihoyoConstellation]]
    """在api/character接口有"""
    actived_constellation_num: int
    costumes: NotRequired[List[MihoyoCostume]]
    """在api/character接口有"""
    card_image: NotRequired[str]
    """在api/index接口有"""
    is_chosen: NotRequired[bool]
    """在api/index接口有"""


# Response from https://api-takumi-record.mihoyo.com/game_record/app/genshin/api/spiralAbyss


class AbyssAvatar(TypedDict):
    avatar_id: int
    avatar_icon: str
    value: int
    rarity: int


class AbyssBattleAvatar(TypedDict):
    id: int
    icon: str
    level: int
    rarity: t


class AbyssBattle(TypedDict):
    index: int
    timestamp: str
    avatars: List[AbyssBattleAvatar]


class AbyssLevel(TypedDict):
    index: int
    star: int
    max_star: int
    battles: List[AbyssBattle]


class AbyssFloor(TypedDict):
    index: int
    icon: str
    is_unlock: bool
    settle_time: str
    star: int
    max_star: int
    levels: List[AbyssFloor]


class AbyssData(TypedDict):
    schedule_id: int
    start_time: str
    end_time: str
    total_battle_times: int
    total_win_times: int
    max_floor: str
    reveal_rank: List[AbyssAvatar]
    defeat_rank: List[AbyssAvatar]
    damage_rank: List[AbyssAvatar]
    take_damage_rank: List[AbyssAvatar]
    normal_skill_rank: List[AbyssAvatar]
    energy_skill_rank: List[AbyssAvatar]
    floors: List[AbyssFloor]
    total_star: int
    is_unlock: bool


# Response from https://api-takumi-record.mihoyo.com/game_record/app/genshin/api/dailyNote


class Expedition(TypedDict):
    avatar_side_icon: str
    status: Literal['Ongoing', 'Finished']
    remained_time: int


class RecoveryTime(TypedDict):
    Day: int
    Hour: int
    Minute: int
    Second: int
    reached: bool


class Transformer(TypedDict):
    obtained: bool
    recovery_time: RecoveryTime
    wiki: str
    noticed: bool
    latest_job_id: str


class DailyNoteData(TypedDict):
    current_resin: int
    max_resin: int
    resin_recovery_time: int
    finished_task_num: int
    total_task_num: int
    is_extra_task_reward_received: bool
    remain_resin_discount_num: int
    resin_discount_num_limit: int
    current_expedition_num: int
    max_expedition_num: int
    expeditions: List[Expedition]
    current_home_coin: int
    max_home_coin: int
    home_coin_recovery_time: int
    calendar_url: str
    transformer: Transformer


# Response from https://api-takumi.mihoyo.com/game_record/app/genshin/api/index


class Stats(TypedDict):
    active_day_number: int
    achievement_number: int
    anemoculus_number: int
    geoculus_number: int
    avatar_number: int
    way_point_number: int
    domain_number: int
    spiral_abyss: str
    precious_chest_number: int
    luxurious_chest_number: int
    exquisite_chest_number: int
    common_chest_number: int
    electroculus_number: int
    magic_chest_number: int
    dendroculus_number: int


class Offering(TypedDict):
    name: str
    level: int
    icon: str


class WorldExploration(TypedDict):
    level: int
    exploration_percentage: int
    icon: str
    name: str
    type: str
    offerings: List[Offering]
    id: int
    parent_id: int
    map_url: str
    strategy_url: str
    background_image: str
    inner_icon: str
    cover: str


class Home(TypedDict):
    level: int
    visit_num: int
    comfort_num: int
    item_num: int
    name: str
    icon: str
    comfort_level_name: str
    comfort_level_icon: str


class IndexData(TypedDict):
    role: MihoyoRole
    avatars: List[MihoyoAvatar]
    stats: Stats
    city_explorations: List
    world_explorations: List[WorldExploration]
    homes: List[Home]
