from db.postgres import async_session


async def get_async_db():
    async with async_session() as db:
        yield db
