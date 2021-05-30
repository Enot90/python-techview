import asyncio
from config import MYSQL_CONFIG
from mysql_client import MySqlClient


class Worker:
    db: MySqlClient = MySqlClient()  # инициализация класса

    async def run(self):
        await self.db.connect(MYSQL_CONFIG)  # подкл к БД
        while True:
            print('Hello!')
            await asyncio.sleep(5)  # Каждые 5 сек будет писать и засыпать
