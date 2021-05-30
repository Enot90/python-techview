# https://github.com/aio-libs/aiomysql
import aiomysql
from typing import Dict


class MySqlClient:
    pool: aiomysql.Pool

    async def connect(self, config: Dict):
        self.pool = await aiomysql.create_pool(**config)  # извлекаем из словаря

    def disconnect(self):
        self.pool.close()  # закрываем соед

    async def query(self, sql: str, *args, **kwargs):  # запрос в БД
        async with self.pool.acquire() as conn:  # получаем соед. из pool
            conn: aiomysql.Connection  # аннотация для посветки методов
            async with conn.cursor(aiomysql.DictCursor) as cur:
                cur: aiomysql.Cursor
                await cur.execute(sql, *args, **kwargs)
                result = await cur.fetchall()  # получаем результ выполненного запроса
                return result
