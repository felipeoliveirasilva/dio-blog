import asyncio
import os

import pytest_asyncio
from httpx import AsyncClient, ASGITransport

os.environ.setdefault("DATABASE_URL", "sqlite:///tests.db")  # noqa


@pytestasyncio.fixture
async def db(request):
    from src.database import database, engine, metadata  # noqa
    from src.models.post import posts  # noqa

    await database.connect()
    metadata.create_all(engine)

    def teardown():
        async def _teardown():
            await database.disconnect()
            try:
                metadata.drop_all(engine)
            except FileNotFoundError:
                pass

        asyncio.run(_teardown())

    request.addfinalizer(teardown)
