from __future__ import annotations

from typing import Dict, List, Literal, Optional, TypedDict


class QrCodeUrl(TypedDict):
    url: str


class QrCodePayload(TypedDict):
    proto: str
    raw: str
    ext: str


class CheckQrCode(TypedDict):
    stat: str
    payload: Dict[QrCodePayload]


class GameToken(TypedDict):
    token_type: int
    token: str


class UserInfoLinks(TypedDict):
    thirdparty: str
    union_id: str
    nickname: str


class UserInfo(TypedDict):
    aid: str
    mid: str
    account_name: str
    email: str
    is_email_verify: int
    area_code: str
    mobile: str
    safe_area_code: str
    safe_mobile: str
    realname: str
    identity_code: str
    rebind_area_code: str
    rebind_mobile: str
    rebind_mobile_time: str
    links: List[UserInfoLinks]


class GetStokenByGameToken(TypedDict):
    token: GameToken
    user_info: str


class GetCookieToken(TypedDict):
    uid: str
    cookie_token: str


class MiHoYoBBSInfoListData(TypedDict):
    name: str
    type: int
    value: str


class MiHoYoBBSInfoListDataSwitches(TypedDict):
    switch_id: int
    is_public: bool
    switch_name: str


class MiHoYoBBSInfoList(TypedDict):
    has_role: bool
    game_id: int
    game_role_id: str
    nickname: str
    region: str
    level: int
    background_image: str
    is_public: bool
    data: List[MiHoYoBBSInfoListData]
    region_name: str
    url: str
    data_switches: List[MiHoYoBBSInfoListDataSwitches]
    h5_data_switches: List
    background_color: str


class MihoyoBBSInfo(TypedDict):
    list: List[MiHoYoBBSInfoList]


class GetAuthKeyByCookie(TypedDict):
    sign_type: int
    sign_type: int
    authkey: str


class SingleGachaLog(TypedDict):
    uid: str
    gacha_type: str
    item_id: str
    count: str
    time: str
    name: str
    lang: str
    item_type: str
    rank_type: str
    id: str


class GachaLogByAuthkey(TypedDict):
    page: str
    size: str
    total: str
    list: List[SingleGachaLog]
    region: str


class CardOptsData(TypedDict):
    adjs: List
    titles: List
    items: List
    data_version: str


PropsData = TypedDict(
    'PropsData',
    {
        "66a": str,
        "50a": str,
        "53b": str,
        "pre_69b": str,
        "49a": str,
        "52b": str,
        "pre_71b": str,
        "37": str,
        "48a": str,
        "57": str,
    }
)


class RegTimeData(TypedDict):
    data: str
    card_opts: CardOptsData
    props: PropsData
    data_version: int
    prop_version: int


class GetHk4eToken(TypedDict):
    game: str
    region: str
    game_uid: str
    game_biz: str
    level: int
    nickname: str
    region_name: str


class GcgCovers(TypedDict):
    id: int
    image: str


class GcgInfo(TypedDict):
    level: int
    nickname: str
    avatar_card_num_gained: int
    avatar_card_num_total: int
    action_card_num_gained: int
    action_card_num_total: int
    covers: List[GcgCovers]


class DailyDataExpeditions(TypedDict):
    avatar_side_icon: str
    status: str
    remained_time: str


class TransformsRecoveryData(TypedDict):
    Day: int
    Hour: int
    Minute: int
    Second: int
    reached: bool


class DailyDataTransformers(TypedDict):
    obtained: bool
    recovery_time: TransformsRecoveryData
    wiki: str
    noticed: bool
    latest_job_id: str


class DailyData(TypedDict):
    current_resin: int
    max_resin: int
    resin_recover_time: str
    finished_task_num: int
    total_task_num: int
    is_extra_task_reward_received: bool
    remain_resin_discount_num: int
    resin_discount_num_limit: int
    current_expedition_num: int
    max_expedition_num: int
    expeditions: List[DailyDataExpeditions]
    current_home_coin: int
    max_home_coin: int
    home_coin_recover_time: str
    calendar_url: str
    transformer: DailyDataTransformers


class PlayerRoleData(TypedDict):
    AvatarUrl: str
    nickname: str
    region: str
    level: int


class PlayerAvatarsData(TypedDict):
    id: int
    image: str
    name: str
    element: str
    fetter: int
    level: int
    rarity: int
    actived_constellation_num: int
    card_image: str
    is_chosen: bool


class PlayerStatsData(TypedDict):
    active_day_number: int
    achievement_number: int
    anemoculus_number: int
    geoculus_number: int
    avatar_number: int
    way_point_number: int
    domain_number: int
    spiral_abyss: int
    precious_chest_number: int
    luxurious_chest_number: int
    exquisite_chest_number: int
    common_chest_number: int
    electroculus_number: int
    magic_chest_number: int
    dendroculus_number: int


class PlayerCityExplorationsData(TypedDict):
    pass


class PlayerWorldExplorationsOfferings(TypedDict):
    name: str
    level: int
    icon: str


class PlayerWorldExplorationsData(TypedDict):
    level: int
    exploration_percentage: int
    icon: str
    name: str
    type: str
    offerings: List[PlayerWorldExplorationsOfferings]
    id: int
    parent_id: int
    map_url: str
    strategy_url: str
    background_image: str
    inner_icon: str
    cover: str


class PlayerHomesData(TypedDict):
    level: int
    visit_num: int
    comfort_num: int
    item_num: int
    name: str
    icon: str
    comfort_level_name: str
    comfort_level_icon: str


class PlayerInfo(TypedDict):
    role: PlayerRoleData
    avatars: List[PlayerAvatarsData]
    stats: PlayerStatsData
    city_explorations: List[PlayerCityExplorationsData]
    world_explorations: List[PlayerWorldExplorationsData]
    homes: List[PlayerHomesData]


class PlayerDetailAvatarWeapon(TypedDict):
    id: int
    name: str
    icon: str
    type: int
    rarity: int
    level: int
    promote_level: int
    type_name: str
    desc: str
    affix_level: int


class PlayerDetailAvatarReliquariesSetAffixes(TypedDict):
    activation_number: int
    effect: str


class PlayerDetailAvatarReliquariesSet(TypedDict):
    id: int
    name: str
    affixes: List[PlayerDetailAvatarReliquariesSetAffixes]


class PlayerDetailAvatarReliquaries(TypedDict):
    id: int
    name: str
    icon: str
    pos: int
    rarity: int
    level: int
    set: PlayerDetailAvatarReliquariesSet
    pos_name: str


class PlayerDetailAvatarConstellations(TypedDict):
    id: int
    name: str
    icon: str
    effect: str
    is_actived: bool
    pos: int


class PlayerDetailAvatarCostumes(TypedDict):
    id: int
    name: str
    icon: str


class PlayerDetailAvatarData(TypedDict):
    id: int
    image: str
    name: str
    element: str
    fetter: int
    level: int
    rarity: int
    weapon: PlayerDetailAvatarWeapon
    reliquaries: List[PlayerDetailAvatarReliquaries]
    constellations: List[PlayerDetailAvatarConstellations]
    actived_constellation_num: int
    costumes: Optional[List[PlayerDetailAvatarCostumes]]
    external: Optional[str]


class PlayerDetailInfo(TypedDict):
    avatars: List[PlayerAvatarsData]
    role: PlayerRoleData


class SpiralAbyssAvatar(TypedDict):
    avatar_id: int
    avatar_icon: str
    value: int
    rarity: int


class SpiralAbyssRankAvatar(TypedDict):
    avatar_id: int
    avatar_icon: str
    value: int
    rarity: int


class SpiralAbyssFloorBattle(TypedDict):
    index: int
    timestamp: str
    avatars: List[SpiralAbyssAvatar]


class SpiralAbyssFloorLevel(TypedDict):
    index: int
    star: int
    max_star: int
    battles: List[SpiralAbyssFloorBattle]


class SpiralAbyssFloor(TypedDict):
    index: int
    icon: str
    is_unlock: bool
    settle_time: str
    star: int
    max_star: int
    levels: List[SpiralAbyssFloorLevel]


class SpiralAbyssInfo(TypedDict):
    schedule_id: int
    start_time: str
    end_time: str
    total_battle_times: int
    total_win_times: int
    max_floor: str
    reveal_rank: List[SpiralAbyssAvatar]
    defeat_rank: List[SpiralAbyssAvatar]
    damage_rank: List[SpiralAbyssAvatar]
    take_damage_rank: List[SpiralAbyssRankAvatar]
    normal_skill_rank: List[SpiralAbyssRankAvatar]
    energy_skill_rank: List[SpiralAbyssRankAvatar]
    floors: List[SpiralAbyssFloor]
    total_star: int
    is_unlock: bool


class MonthlyAwardDayData(TypedDict):
    current_primogems: int
    current_mora: int
    last_primogems: int
    last_mora: int


class MonthlyAwardMonthGroupBy(TypedDict):
    action_id: int
    action: str
    num: int
    percent: int


class MonthlyAwardMonthData(TypedDict):
    current_primogems: int
    current_mora: int
    last_primogems: int
    last_mora: int
    current_primogems_level: int
    primogems_rate: int
    mora_rate: int
    group_by: List[MonthlyAwardMonthGroupBy]


class MonthlyAward(TypedDict):
    uid: int
    region: str
    account_id: str
    nickname: str
    date: str
    month: str
    optional_month: List[int]
    data_month: int
    data_last_month: int
    day_data: MonthlyAwardDayData
    month_data: MonthlyAwardMonthData
    lantern: bool


class MihoyoBBSSign(TypedDict):
    code: str
    risk_code: int
    gt: str
    challenge: str
    success: int


class SignInfo(TypedDict):
    total_sign_day: int
    today: str
    is_sign: bool
    first_bind: bool
    is_sub: bool
    month_first: bool
    sign_cnt_missed: int
    month_last_day: bool


class SignAward(TypedDict):
    icon: str
    name: str
    cnt: int


class SignList(TypedDict):
    month: int
    awards: List[SignAward]
    resign: bool


class Stoken(TypedDict):
    name: str
    token: str


class GetStokenByLoginTicket(TypedDict):
    List: List[Stoken]
