import asyncio

from worker import Worker

if __name__ == '__main__':
    w = Worker()  # Создаем экземпляр класса
    loop = asyncio.get_event_loop()  # создаем цикл событий
    loop.run_until_complete(w.run())  # запускаем корутину - асинх процесс


