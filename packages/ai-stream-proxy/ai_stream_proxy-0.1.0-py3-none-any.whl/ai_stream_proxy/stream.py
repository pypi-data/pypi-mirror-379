import asyncio
import json
from typing import Optional

import httpx
from tenacity import retry, stop_after_attempt, wait_random, RetryError


class StreamProxyStream:
    from .client import StreamProxyClient

    stream_id: str

    _client: StreamProxyClient
    _httpx_client: httpx.AsyncClient

    _cursor: int
    _streaming: bool
    _aborted: bool
    _finished: bool

    _finish_signal: asyncio.Semaphore

    _put_concurrency: asyncio.Semaphore

    _tasks: asyncio.TaskGroup
    """
    data tasks
    """

    _finish_task: Optional[asyncio.Task]
    """
    finish task for sending finish chunk
    """

    def __init__(self, *, client: StreamProxyClient, stream_id: str):
        self._client = client
        self.stream_id = stream_id
        self._tasks = asyncio.TaskGroup()
        self._httpx_client = httpx.AsyncClient(**self._client.httpx_async_client_options)
        self._cursor = 0
        self._streaming = True
        self._aborted = False
        self._finished = False
        self._finish_signal = asyncio.Semaphore(0)
        self._put_concurrency = asyncio.Semaphore(5)
        self._finish_task = None

    def enqueue(self, data: bytes):
        if not self._streaming:
            return

        range_string = f'bytes {self._cursor}-{self._cursor + len(data) - 1}'
        self._cursor += len(data)

        self._tasks.create_task(
            self._put(range_string, data),
            name=f'put {range_string}'
        )

    def finish(self, abort: bool, reason=""):
        if not self._streaming:
            return

        # finish() already called
        if self._finish_task is not None:
            return

        if abort:
            # abort all put requests
            self._streaming = False

        self._finish_task = asyncio.create_task(
            self._finish(abort, reason),
            name='finish'
        )

    async def _put(self, range_string: str, data: bytes):
        try:
            await self._put_data(range_string, data)
        except Exception as e:
            self._streaming = False
            print(f"aborting stream {self.stream_id}: {e}")
            self.finish(abort=True, reason=f"{e}")
            pass

    async def _finish(self, abort: bool, reason: str):
        try:
            await asyncio.gather(*self._tasks._tasks)
            self._streaming = False
            await self._post_stop_signal(abort=abort, reason=reason, final_size=self._cursor)
        except RetryError as e:
            print(e)
            pass
        finally:
            self._finished = True
            self._notify_finished()

    @retry(stop=stop_after_attempt(3), wait=wait_random(0.5, 1.5))
    async def _put_data(self, range_string: str, data: bytes):
        await self._put_concurrency.acquire()

        if not self._streaming:
            self._put_concurrency.release()
            return

        try:
            resp = await self._httpx_client.put(
                f'{self._client.server_url}/v2/streams/{self.stream_id}/content',
                headers={
                    'X-Content-Range': range_string
                },
                data=data
            )
        except Exception as e:
            print(f"{e}")
            raise e
        finally:
            self._put_concurrency.release()

        if resp.is_error:
            raise Exception(f'{resp.status_code}: f{resp.read().decode('utf-8')}')
        pass

    @retry(stop=stop_after_attempt(3), wait=wait_random(0.5, 1.5))
    async def _post_stop_signal(
            self,
            *,
            abort: bool,
            final_size: int,
            reason: str = ""
    ):
        resp = await self._httpx_client.post(
            f'{self._client.server_url}/v2/streams/{self.stream_id}/actions/stop',
            headers={
                'Content-Type': 'application/json'
            },
            data=json.dumps({
                'stop_state': 'abort' if abort else 'done',
                'stop_reason': reason,
                'final_size': final_size,
            })
        )
        if resp.is_error:
            raise Exception(f'{resp.status_code}: {resp.read()}')
        pass

    async def finish_stream(self):
        await asyncio.gather(*self._tasks._tasks)

    def _notify_finished(self):
        if self._finish_signal._waiters:
            for i in range(len(self._finish_signal._waiters)):
                self._finish_signal.release()

    async def _wait_for_finish(self):
        if self._finished:
            return
        await self._finish_signal.acquire()

    async def __aenter__(self):
        await self._tasks.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._tasks.__aexit__(exc_type, exc_val, exc_tb)
        await self._wait_for_finish()

    def __await__(self):
        return self._wait_for_finish().__await__()
