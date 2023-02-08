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


class Stoken(TypedDict):
    name: str
    token: str


class GetStokenByLoginTicket(TypedDict):
    List: List[Stoken]


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
