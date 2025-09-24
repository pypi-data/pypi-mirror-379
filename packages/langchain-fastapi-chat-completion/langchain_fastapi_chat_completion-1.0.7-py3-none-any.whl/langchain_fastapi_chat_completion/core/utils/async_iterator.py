import asyncio
from typing import Any, AsyncIterator

NOPE = object()


async def _apreactivate(queue: asyncio.Queue, aiterator: AsyncIterator):
    async for it in aiterator:
        await queue.put(it)
    await queue.put(NOPE)


async def yield_from_queue(prefetched: Any, queue: asyncio.Queue):
    yield prefetched
    while (it := await queue.get()) is not NOPE:
        yield it


async def apreactivate(aiterator: AsyncIterator) -> AsyncIterator:
    queue = asyncio.Queue()
    task = asyncio.create_task(_apreactivate(queue, aiterator))

    while True:
        try:
            async with asyncio.Timeout(1):
                prefetched = await queue.get()
                break
        except TimeoutError:
            if task.done():
                await task

    return yield_from_queue(prefetched, queue)
