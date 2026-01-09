from sqlalchemy.ext.asyncio import create_async_engine, asyncsessionmaker
from sqlalchemy import declarative


engine = create_asyn_engine(
    "sqlite+aiosqlite:///tasks.db"
)

new_session = async_sessionmaker(engine, expire_on_commit=False)


class TaskTable()