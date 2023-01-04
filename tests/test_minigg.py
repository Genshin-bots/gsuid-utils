import pytest


@pytest.mark.asyncio
async def test_get_weapon_info():
    from gsuid_utils.minigg import Weapon, get_weapon_info

    data = await get_weapon_info("天目影打刀")
    assert isinstance(data, dict)
    assert data == Weapon(
        **{
            "name": "天目影打刀",
            "description": "传说中连以神速见长的天狗都能斩落的名士订制的刀。",
            "weapontype": "单手剑",
            "rarity": "4",
            "baseatk": 41,
            "substat": "攻击力",
            "subvalue": "12",
            "effectname": "岩藏之胤",
            "effect": (
                "施放元素战技后，获得1个胤种，该效果每5秒至多触发一次。胤种持续30秒，至多同时存在3个。"
                "施放元素爆发后，会清除持有的所有胤种，并在2秒之后，基于消耗的胤种数量，每个为该角色恢复{0}点元素能量。"
            ),
            "r1": ["6"],
            "r2": ["7.5"],
            "r3": ["9"],
            "r4": ["10.5"],
            "r5": ["12"],
            "weaponmaterialtype": "",
            "costs": {
                "ascend1": [
                    {"name": "摩拉", "count": 5000},
                    {"name": "远海夷地的瑚枝", "count": 3},
                    {"name": "混沌机关", "count": 3},
                    {"name": "破旧的刀镡", "count": 2},
                ],
                "ascend2": [
                    {"name": "摩拉", "count": 15000},
                    {"name": "远海夷地的玉枝", "count": 3},
                    {"name": "混沌机关", "count": 12},
                    {"name": "破旧的刀镡", "count": 8},
                ],
                "ascend3": [
                    {"name": "摩拉", "count": 20000},
                    {"name": "远海夷地的玉枝", "count": 6},
                    {"name": "混沌枢纽", "count": 6},
                    {"name": "影打刀镡", "count": 6},
                ],
                "ascend4": [
                    {"name": "摩拉", "count": 30000},
                    {"name": "远海夷地的琼枝", "count": 3},
                    {"name": "混沌枢纽", "count": 12},
                    {"name": "影打刀镡", "count": 9},
                ],
                "ascend5": [
                    {"name": "摩拉", "count": 35000},
                    {"name": "远海夷地的琼枝", "count": 6},
                    {"name": "混沌真眼", "count": 9},
                    {"name": "名刀镡", "count": 6},
                ],
                "ascend6": [
                    {"name": "摩拉", "count": 45000},
                    {"name": "远海夷地的金枝", "count": 4},
                    {"name": "混沌真眼", "count": 18},
                    {"name": "名刀镡", "count": 12},
                ],
            },
            "images": {
                "nameicon": "UI_EquipIcon_Sword_Bakufu",
                "namegacha": "UI_Gacha_EquipIcon_Sword_Bakufu",
                "icon": (
                    "https://upload-os-bbs.mihoyo.com/game_record"
                    "/genshin/equip/UI_EquipIcon_Sword_Bakufu.png"
                ),
                "nameawakenicon": "UI_EquipIcon_Sword_Bakufu_Awaken",
                "awakenicon": (
                    "https://upload-os-bbs.mihoyo.com/game_record"
                    "/genshin/equip/UI_EquipIcon_Sword_Bakufu_Awaken.png"
                ),
            },
            "url": {
                "fandom": (
                    "https://genshin-impact.fandom.com"
                    "/wiki/Amenoma_Kageuchi"
                )
            },
            "version": "2.0",
        }
    )


@pytest.mark.asyncio
async def test_get_weapon_info_list():
    from gsuid_utils.minigg import get_weapon_info

    data = await get_weapon_info("1")
    assert isinstance(data, list)
    assert data == ["学徒笔记", "新手长枪", "无锋剑", "猎弓", "训练大剑"]


@pytest.mark.asyncio
async def test_get_weapon_costs():
    from gsuid_utils.minigg import get_weapon_costs

    data = await get_weapon_costs("天目影打刀")
    assert isinstance(data, dict)
    assert data == {
        "ascend1": [
            {"name": "摩拉", "count": 5000},
            {"name": "远海夷地的瑚枝", "count": 3},
            {"name": "混沌机关", "count": 3},
            {"name": "破旧的刀镡", "count": 2},
        ],
        "ascend2": [
            {"name": "摩拉", "count": 15000},
            {"name": "远海夷地的玉枝", "count": 3},
            {"name": "混沌机关", "count": 12},
            {"name": "破旧的刀镡", "count": 8},
        ],
        "ascend3": [
            {"name": "摩拉", "count": 20000},
            {"name": "远海夷地的玉枝", "count": 6},
            {"name": "混沌枢纽", "count": 6},
            {"name": "影打刀镡", "count": 6},
        ],
        "ascend4": [
            {"name": "摩拉", "count": 30000},
            {"name": "远海夷地的琼枝", "count": 3},
            {"name": "混沌枢纽", "count": 12},
            {"name": "影打刀镡", "count": 9},
        ],
        "ascend5": [
            {"name": "摩拉", "count": 35000},
            {"name": "远海夷地的琼枝", "count": 6},
            {"name": "混沌真眼", "count": 9},
            {"name": "名刀镡", "count": 6},
        ],
        "ascend6": [
            {"name": "摩拉", "count": 45000},
            {"name": "远海夷地的金枝", "count": 4},
            {"name": "混沌真眼", "count": 18},
            {"name": "名刀镡", "count": 12},
        ],
    }


@pytest.mark.asyncio
async def test_get_weapon_info_not_found():
    from gsuid_utils.minigg import MiniggNotFoundError, get_weapon_info

    with pytest.raises(MiniggNotFoundError) as exc_info:
        await get_weapon_info("111111111111111111111")
        exc = exc_info.value
        assert exc.raw == {
            "errcode": "10002",
            "errmsg": "不存在该武器或武器类别，可@机器人并发送 功能 获取完整帮助",
        }


@pytest.mark.asyncio
async def test_get_weapon_stats():
    from gsuid_utils.minigg import WeaponStats, get_weapon_stats

    data = await get_weapon_stats("天目影打刀", stats=50)
    assert isinstance(data, dict)
    assert data == WeaponStats(
        **{
            "level": 50,
            "ascension": 2,
            "attack": 238.34463634235,
            "specialized": 0.3574800029960272,
        }
    )


@pytest.mark.asyncio
async def test_get_weapon_stats_value_error():
    from gsuid_utils.minigg import get_weapon_stats

    with pytest.raises(ValueError) as exc_info:
        await get_weapon_stats("天目影打刀", stats=99)
        exc = exc_info.value
        assert exc.args[0] == "stats must <= 90 and > 0"
