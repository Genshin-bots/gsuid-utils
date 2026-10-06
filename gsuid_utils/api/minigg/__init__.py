"""
MiniGG API 包装：
原神基础信息 v4/v5；
原神语音；
原神地图；
"""

from .models import Weapon as Weapon  # noqa: F401
from .models import WeaponCosts as WeaponCosts  # noqa: F401
from .models import WeaponStats as WeaponStats  # noqa: F401
from .request import get_map_data as get_map_data  # noqa: F401
from .request import get_weapon_info as get_weapon_info  # noqa: F401
from .request import get_weapon_costs as get_weapon_costs  # noqa: F401
from .request import get_weapon_stats as get_weapon_stats  # noqa: F401
from .exception import MiniggNotFoundError as MiniggNotFoundError  # noqa: F401

__all__ = ["request", "exception", "models"]
