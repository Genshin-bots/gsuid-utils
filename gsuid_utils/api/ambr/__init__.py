"""
安柏计划 API 包装：
书籍信息；
角色信息;
武器信息;
"""
from .models import AmbrBook as AmbrBook
from .models import AmbrWeapon as AmbrWeapon
from .models import AmbrCharacter as AmbrCharacter
from .models import AmbrBookDetail as AmbrBookDetail
from .request import get_story_data as get_story_data
from .request import get_all_book_id as get_all_book_id
from .request import get_book_volume as get_book_volume
from .request import get_ambr_char_data as get_ambr_char_data
from .request import get_ambr_event_info as get_ambr_event_info
from .request import get_ambr_weapon_data as get_ambr_weapon_data

__all__ = ["request", "models", "utils"]
