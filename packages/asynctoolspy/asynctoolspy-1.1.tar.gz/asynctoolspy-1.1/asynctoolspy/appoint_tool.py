import asyncio
import functools
from datetime import datetime, timedelta


def appoint_limit_async(limit: int, interval: int=0, pause: int=0):
    """
       The decorator that limits how often async function is called.

       :param:
       - limit (int): Maximum number of function call attempts in case of an error.
       - interval (int): The time interval in seconds during which function calls should be limited when working correctly.
       - pause (int): Pause between attempts to call a function in seconds in case of an error.

       :return:
       - wrapper (function): A wrapper function that limits how often the original function is called.

       Usage example №1:
       class MyClient:
            @appoint_limit_async(limit=5, interval=10, pause=2)
            async def my_method(self):
                # Your code for making an API request or I/O operation.

       Usage example №2:
       @appoint_limit_async(limit=5, interval=10, pause=2)
       async def my_function():
           # your code for making I/O operation
    """

    def decorator(func):
        last_call = datetime.min
        retries = 0

        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            nonlocal last_call, retries
            elapsed = datetime.now() - last_call
            if elapsed < timedelta(seconds=interval):
                await asyncio.sleep((timedelta(seconds=interval) - elapsed).total_seconds())
            last_call = datetime.now()
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                if retries <= limit:
                    retries += 1
                    await asyncio.sleep(pause)
                    return await wrapper(*args, **kwargs)
                raise Exception(f"Script error: {e}\n In functions: {func.__name__}")

        return wrapper

    return decorator


