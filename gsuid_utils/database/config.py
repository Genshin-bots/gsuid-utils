from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


class SQLA:
    def __init__(self, url: str):
        self.url = f'sqlite+aiosqlite:///{url}'
        self.engine = create_async_engine(self.url, pool_recycle=1500)
        self.session = sessionmaker(self.engine, class_=AsyncSession)
