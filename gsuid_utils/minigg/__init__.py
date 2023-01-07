"""
MiniGG API 包装：
原神基础信息 v4/v5；
原神语音；
原神地图；
"""
from .models import Weapon as Weapon
from .models import WeaponCosts as WeaponCosts
from .models import WeaponStats as WeaponStats
from .request import get_map_data as get_map_data
from .request import get_weapon_info as get_weapon_info
from .request import get_weapon_costs as get_weapon_costs
from .request import get_weapon_stats as get_weapon_stats
from .exception import MiniggNotFoundError as MiniggNotFoundError

__all__ = ["request", "exception", "models"]
