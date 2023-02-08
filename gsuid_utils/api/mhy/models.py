from __future__ import annotations

import sys
from typing import Dict, List, TypedDict

# https://peps.python.org/pep-0655/#usage-in-python-3-11
if sys.version_info >= (3, 11):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired


################
# Token Models #
################


class CookieTokenInfo(TypedDict):
    uid: str
    cookie_token: str


class StokenInfo(TypedDict):
    token_type: NotRequired[int]
    name: NotRequired[str]
    token: str


class GameTokenInfo(TypedDict):
    token: StokenInfo
    user_info: UserInfo


class LoginTicketInfo(TypedDict):
    List: List[StokenInfo]


class AuthKeyInfo(TypedDict):
    sign_type: int
    sign_type: int
    authkey: str


class Hk4eLoginInfo(TypedDict):
    game: str
    region: str
    game_uid: str
    game_biz: str
    level: int
    nickname: str
    region_name: str


################
# 扫码登录相关 #
################


class QrCodeUrl(TypedDict):
    url: str


class Payload(TypedDict):
    proto: str
    raw: str
    ext: str


class QrCodeStatus(TypedDict):
    stat: str
    payload: Dict[Payload]


################
# UserInfo相关 #
################


class UserLinks(TypedDict):
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
    links: List[UserLinks]


################
# 米游社信息相关 #
################


class GameList(TypedDict):
    name: str
    type: int
    value: str


class SwitchInfo(TypedDict):
    switch_id: int
    is_public: bool
    switch_name: str


class BBSInfo(TypedDict):
    has_role: bool
    game_id: int
    game_role_id: str
    nickname: str
    region: str
    level: int
    background_image: str
    is_public: bool
    data: List[GameList]
    region_name: str
    url: str
    data_switches: List[SwitchInfo]
    h5_data_switches: List
    background_color: str


class MihoyoBBSInfo(TypedDict):
    list: List[BBSInfo]


################
# 抽卡记录相关 #
################


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


class GachaLog(TypedDict):
    page: str
    size: str
    total: str
    list: List[SingleGachaLog]
    region: str


################
# 注册时间相关 #
################


class CardOpts(TypedDict):
    adjs: List[int]
    titles: List[int]
    items: List[int]
    data_version: str


Props = TypedDict(
    'Props',
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
    },
)


class RegTime(TypedDict):
    data: str
    card_opts: CardOpts
    props: Props
    data_version: int
    prop_version: int


################
# 七圣召唤相关 #
################


class CardCovers(TypedDict):
    id: int
    image: str


class GcgInfo(TypedDict):
    level: int
    nickname: str
    avatar_card_num_gained: int
    avatar_card_num_total: int
    action_card_num_gained: int
    action_card_num_total: int
    covers: List[CardCovers]


################
# 每月札记相关 #
################


class DayData(TypedDict):
    current_primogems: int
    current_mora: int
    last_primogems: int
    last_mora: int


class GroupBy(TypedDict):
    action_id: int
    action: str
    num: int
    percent: int


class MonthData(TypedDict):
    current_primogems: int
    current_mora: int
    last_primogems: int
    last_mora: int
    current_primogems_level: int
    primogems_rate: int
    mora_rate: int
    group_by: List[GroupBy]


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
    day_data: DayData
    month_data: MonthData
    lantern: bool


################
# 签到相关 #
################


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
