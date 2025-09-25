import asyncio
import inspect

class AsyncIterWrapper:
    """
        Asynchronous iterator wrapper for any iterable collection, with optional delay and callback processing.

        :param:
        - data (Iterable): The collection of data to iterate over asynchronously (e.g., list, string, set, etc.).
        - delay (int | float, optional): Delay in seconds between yielding elements. Defaults to 0 (no delay).
        - callback (callable, optional): A function to process each element before yielding. Can be synchronous or asynchronous. Defaults to None.

        :return:
        - AsyncIterWrapper: An asynchronous iterator supporting the async for protocol.

        Usage example #1:
        async def multiply(x):
            await asyncio.sleep(0.1)
            return x * 2

        data = [1, 2, 3]
        async for item in AsyncIterWrapper(data, delay=0.5, callback=multiply):
            print(item)  # Outputs 2, 4, 6 with a 0.5 second delay between items

        Usage example #2 (with asynchronous HTTP requests):
        import aiohttp

        async def fetch_url(url):
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    return await response.text()

        urls = ["https://example.com", "https://httpbin.org/get"]
        async for content in AsyncIterWrapper(urls, callback=fetch_url):
            print(content)  # Prints the HTML/text content of each URL

        """

    def __init__(self, data, delay=0, callback=None):
        self._it = iter(data)
        self.delay = delay
        self.callback = callback

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            value = next(self._it)
            if self.delay:
                await asyncio.sleep(self.delay)
            if self.callback:
                result = self.callback(value)
                if inspect.isawaitable(result):
                    value = await result
                else:
                    value = result
            return value
        except StopIteration:
            raise StopAsyncIteration
