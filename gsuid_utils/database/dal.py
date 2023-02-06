from typing import Dict, List, Literal, Optional

from utils import SERVER
from sqlalchemy.future import select
from sqlalchemy import delete, update
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func
from models import GsBind, GsPush, GsUser, GsCache
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


class SQLA:
    def __init__(self, url: str, bot_id: str):
        self.bot_id = bot_id
        self.url = f'sqlite+aiosqlite:///{url}'
        self.engine = create_async_engine(self.url, pool_recycle=1500)
        self.session = sessionmaker(self.engine, class_=AsyncSession)()

    #####################
    # GsBind 部分 #
    #####################
    async def select_bind_data(self, user_id: str) -> Optional[GsBind]:
        result = await self.session.execute(
            select(GsBind).where(
                GsBind.user_id == user_id and GsBind.bot_id == self.bot_id
            )
        )
        data = result.scalars().all()
        return data[0] if data else None

    async def insert_bind_data(self, user_id: str, **data) -> int:
        new_uid = data['uid'] if 'uid' in data else ''
        if len(new_uid) != 9:
            return -1
        if self.bind_exists(user_id):
            uid_list = await self.get_user_uid_list(user_id)
            uid_list.append(new_uid) if uid_list else 0
            data['uid'] = '_'.join(uid_list)
            await self.update_bind_data(user_id, data)
        else:
            new_data = GsBind(user_id=user_id, bot_id=self.bot_id, **data)
            self.session.add(new_data)
        await self.session.flush()
        return 0

    async def delete_bind_data(self, user_id: str, **data) -> int:
        _uid = data['uid'] if 'uid' in data else ''
        if self.bind_exists(user_id):
            uid_list = await self.get_user_uid_list(user_id)
            if uid_list and _uid in uid_list:
                uid_list.remove(_uid)
            else:
                return -1
            data['uid'] = '_'.join(uid_list)
            await self.update_bind_data(user_id, data)
            await self.session.flush()
            return 0
        else:
            return -1

    async def update_bind_data(self, user_id: str, data: Optional[Dict]):
        sql = update(GsBind).where(
            GsBind.user_id == user_id and GsBind.bot_id == self.bot_id
        )
        if data is not None:
            query = sql.values(**data)
            query.execution_options(synchronize_session='fetch')
            await self.session.execute(query)

    async def bind_exists(self, user_id: str) -> bool:
        return bool(await self.select_bind_data(user_id))

    async def get_all_uid_list(self) -> List[str]:
        sql = select(GsBind).where(GsBind.bot_id == self.bot_id)
        result = await self.session.execute(sql)
        data: List[GsBind] = result.scalars().all()
        uid_list: List[str] = []
        for item in data:
            uid_list.extend(item.uid.split("_") if item.uid else [])
        return uid_list

    async def get_user_uid_list(self, user_id: str) -> List[str]:
        data = await self.select_bind_data(user_id)
        return data.uid.split("_") if data and data.uid else []

    async def get_user_uid(self, user_id: str) -> Optional[str]:
        data = await self.get_user_uid_list(user_id)
        return data[0] if data else None

    async def switch_uid(
        self, user_id: str, uid: Optional[str] = None
    ) -> Optional[List]:
        uid_list = await self.get_user_uid_list(user_id)
        if uid_list and len(uid_list) >= 1:
            if uid and uid not in uid_list:
                return None
            elif uid:
                pass
            else:
                uid = uid_list[1]
            uid_list.remove(uid)
            uid_list.insert(0, uid)
            await self.update_bind_data(user_id, {'uid': '_'.join(uid_list)})
            return uid_list
        else:
            return None

    #####################
    # GsUser、GsCache 部分 #
    #####################

    async def select_user_data(self, uid: str) -> Optional[GsUser]:
        sql = select(GsUser).where(
            GsUser.uid == uid, GsUser.bot_id == self.bot_id
        )
        result = await self.session.execute(sql)
        return data[0] if (data := result.scalars().all()) else None

    async def select_cache_cookie(self, uid: str) -> Optional[str]:
        sql = select(GsCache).where(GsCache.uid == uid)
        result = await self.session.execute(sql)
        data: GsCache = result.scalars().one()
        return data.cookie if data else None

    async def delete_error_cache(self) -> bool:
        data = await self.get_all_error_cookie()
        for cookie in data:
            sql = delete(GsCache).where(GsCache.cookie == cookie)
            await self.session.execute(sql)
        return True

    async def insert_cache_data(
        self,
        cookie: str,
        uid: Optional[str] = None,
        mys_id: Optional[str] = None,
    ) -> bool:
        new_data = GsCache(cookie=cookie, uid=uid, mys_id=mys_id)
        self.session.add(new_data)
        await self.session.flush()
        return True

    async def insert_user_data(
        self, user_id: str, uid: str, cookie: str, stoken: Optional[str] = None
    ) -> bool:
        if await self.user_exists(uid):
            sql = (
                update(GsUser)
                .where(GsUser.uid == uid)
                .values(cookie=cookie, status=None)
            )
            await self.session.execute(sql)
        user_data = GsUser(
            uid=uid,
            cookie=cookie,
            stoken=stoken,
            user_id=user_id,
            bot_id=self.bot_id,
            sign_switch='off',
            push_switch='off',
            bbs_switch='off',
            region=SERVER.get(uid[0], 'cn_gf01'),
        )
        self.session.add(user_data)
        await self.session.flush()
        return True

    async def update_user_data(self, user_id: str, data: Optional[Dict]):
        sql = update(GsUser).where(
            GsUser.user_id == user_id and GsUser.bot_id == self.bot_id
        )
        if data is not None:
            query = sql.values(**data)
            query.execution_options(synchronize_session='fetch')
            await self.session.execute(query)

    async def delete_user_data(self, uid: str):
        if await self.user_exists(uid):
            sql = delete(GsUser).where(GsUser.uid == uid)
            await self.session.execute(sql)
            return True
        return False

    async def delete_cache(self):
        sql = (
            update(GsUser)
            .where(GsUser.status == 'limit30')
            .values(status=None)
        )
        empty_sql = delete(GsCache)
        await self.session.execute(sql)
        await self.session.execute(empty_sql)

    async def user_exists(self, uid: str) -> bool:
        data = await self.select_user_data(uid)
        return True if data else False

    async def update_user_stoken(self, uid: str, stoken: str) -> bool:
        if await self.user_exists(uid):
            sql = update(GsUser).where(GsUser.uid == uid).values(stoken=stoken)
            await self.session.execute(sql)
            await self.session.flush()
            return True
        return False

    async def update_switch_status(self, uid: str, data: Dict) -> bool:
        if await self.user_exists(uid):
            sql = update(GsUser).where(GsUser.uid == uid).values(**data)
            await self.session.execute(sql)
            await self.session.flush()
            return True
        return False

    async def update_error_status(self, cookie: str, err: str) -> bool:
        sql = update(GsUser).where(GsUser.cookie == cookie).values(status=err)
        await self.session.execute(sql)
        await self.session.flush()
        return True

    async def get_user_cookie(self, uid: str) -> Optional[str]:
        data = await self.select_user_data(uid)
        return data.cookie if data else None

    async def cookie_validate(self, uid: str) -> bool:
        data = await self.select_user_data(uid)
        return True if data and data.status is None else False

    async def get_user_stoken(self, uid: str) -> Optional[str]:
        data = await self.select_user_data(uid)
        return data.stoken if data and data.stoken else None

    async def get_all_user(self) -> List[GsUser]:
        sql = select(GsUser).where(GsUser.cookie)
        result = await self.session.execute(sql)
        data: List[GsUser] = result.scalars().all()
        return data

    async def get_all_cookie(self) -> List[str]:
        data = await self.get_all_user()
        return [_u.cookie for _u in data if _u.cookie]

    async def get_all_stoken(self) -> List[str]:
        data = await self.get_all_user()
        return [_u.stoken for _u in data if _u.stoken]

    async def get_all_error_cookie(self) -> List[str]:
        data = await self.get_all_user()
        return [_u.cookie for _u in data if _u.cookie and _u.status]

    async def get_random_cookie(self, uid: str) -> Optional[str]:
        # 有绑定自己CK 并且该CK有效的前提下，优先使用自己CK
        if await self.user_exists(uid) and await self.cookie_validate(uid):
            return await self.get_user_cookie(uid)
        # 自动刷新缓存
        await self.delete_error_cache()
        # 获得缓存库Ck
        cache_data = await self.select_cache_cookie(uid)
        if cache_data is not None:
            return cache_data
        # 随机取CK
        server = SERVER.get(uid[0], 'cn_gf01')
        sql = (
            select(GsUser)
            .where(GsUser.region == server)
            .order_by(func.random())
        )
        data = await self.session.execute(sql)
        user_list: List[GsUser] = data.scalars().all()
        for user in user_list:
            if not user.status:
                return user.cookie
            continue
        else:
            return None

    async def get_switch_status_list(
        self, switch: Literal['push', 'sign', 'bbs']
    ) -> List[GsUser]:
        _switch = getattr(GsUser, switch, GsUser.push_switch)
        sql = select(GsUser).filter(_switch != 'off')
        data = await self.session.execute(sql)
        data_list: List[GsUser] = data.scalars().all()
        return [user for user in data_list]

    #####################
    # GsPush 部分 #
    #####################
    async def insert_push_data(self, uid: str):
        push_data = GsPush(
            uid=uid,
            coin_push='off',
            coin_value=2100,
            coin_is_push='off',
            resin_push='on',
            resin_value=140,
            resin_is_push='off',
            go_push='off',
            go_value=120,
            go_is_push='off',
            transform_push='off',
            transform_value=140,
            transform_is_push='off',
        )
        self.session.add(push_data)
        await self.session.flush()

    async def update_push_data(self, uid: str, data: dict) -> bool:
        await self.push_exists(uid)
        sql = update(GsPush).where(GsPush.uid == uid).values(**data)
        await self.session.execute(sql)
        await self.session.flush()
        return True

    async def select_push_data(self, uid: str) -> GsPush:
        await self.push_exists(uid)
        sql = select(GsPush).where(GsPush.uid == uid)
        result = await self.session.execute(sql)
        return result.scalars().one()

    async def push_exists(self, uid: str) -> bool:
        sql = select(GsPush).where(GsPush.uid == uid)
        result = await self.session.execute(sql)
        data = result.scalars().one()
        if not data:
            await self.insert_push_data(uid)
        return True
