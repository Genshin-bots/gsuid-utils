from typing import Dict, List, Optional

from models import Bind
from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


class SQLA:
    def __init__(self, url: str, bot_id: str):
        self.bot_id = bot_id
        self.url = f'sqlite+aiosqlite:///{url}'
        self.engine = create_async_engine(self.url, pool_recycle=1500)
        self.session = sessionmaker(self.engine, class_=AsyncSession)()

    async def select_bind_data(self, user_id: str) -> Optional[Bind]:
        result = await self.session.execute(
            select(Bind).where(
                Bind.user_id == user_id and Bind.bot_id == self.bot_id
            )
        )
        data = result.scalars().all()
        return data[0] if data else None

    async def insert_bind_data(self, user_id: str, **data) -> int:
        new_uid = data['uid'] if 'uid' in data else ''
        if len(new_uid) != 9:
            return -1
        if self.user_exists(user_id):
            uid_list = await self.select_user_uid_list(user_id)
            uid_list.append(new_uid) if uid_list else 0
            data['uid'] = '_'.join(uid_list)
            await self.update_bind_data(user_id, data)
        else:
            new_data = Bind(user_id=user_id, bot_id=self.bot_id, **data)
            self.session.add(new_data)
        await self.session.flush()
        return 0

    async def delete_bind_data(self, user_id: str, **data) -> int:
        _uid = data['uid'] if 'uid' in data else ''
        if self.user_exists(user_id):
            uid_list = await self.select_user_uid_list(user_id)
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

    async def user_exists(self, user_id: str) -> bool:
        return bool(await self.select_bind_data(user_id))

    async def select_all_uid_list(self) -> List[str]:
        sql = select(Bind).where(Bind.bot_id == self.bot_id)
        result = await self.session.execute(sql)
        data: List[Bind] = result.scalars().all()
        uid_list: List[str] = []
        for item in data:
            uid_list.extend(item.uid.split("_") if item.uid else [])
        return uid_list

    async def select_user_uid_list(self, user_id: str) -> List[str]:
        data = await self.select_bind_data(user_id)
        return data.uid.split("_") if data and data.uid else []

    async def select_user_uid(self, user_id: str) -> Optional[str]:
        data = await self.select_user_uid_list(user_id)
        return data[0] if data else None

    async def update_bind_data(self, user_id: str, data: Optional[Dict]):
        sql = update(Bind).where(Bind.user_id == user_id)
        if data is not None:
            query = sql.values(**data)
            query.execution_options(synchronize_session='fetch')
            await self.session.execute(query)

    async def switch_uid(
        self, user_id: str, uid: Optional[str] = None
    ) -> Optional[List]:
        uid_list = await self.select_user_uid_list(user_id)
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
