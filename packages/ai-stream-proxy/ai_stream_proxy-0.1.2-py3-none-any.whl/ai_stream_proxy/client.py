import asyncio
import json
from typing import Any

import httpx


class StreamProxyClient:
    _living_streams: dict[str, Any]
    _http_client: httpx.AsyncClient
    server_url: str
    httpx_async_client_options: dict

    def __init__(
            self, *,
            server_url: str,
            httpx_async_client_options: dict | None
    ):
        self._living_streams = {}
        self.server_url = server_url
        self.httpx_async_client_options = httpx_async_client_options or {}
        self._http_client = httpx.AsyncClient(**httpx_async_client_options or {})

    async def delete_stream(self, *, stream_id: str):
        response = await self._http_client.delete(f'{self.server_url}/v2/streams/{stream_id}')
        if response.is_error:
            raise Exception(f"{response.status_code}: {response.read().decode('utf-8')}")

    async def create_stream(self, *, stream_id: str, message_id: str, content_type: str):
        response = await self._http_client.post(
            f'{self.server_url}/v2/streams',
            headers={
                'Content-Type': 'application/json'
            },
            data=json.dumps({
                'stream_id': stream_id,
                'message_id': message_id,
                'content_type': content_type
            })
        )
        if response.is_error:
            raise Exception(f"{response.status_code}: {response.read().decode('utf-8')}")

    def new_stream(
            self,
            *,
            stream_id: str
    ):
        from .stream import StreamProxyStream
        stream = StreamProxyStream(client=self, stream_id=stream_id)
        self._living_streams[stream_id] = stream

        async def wait_for_stream_finish():
            await stream
            del self._living_streams[stream_id]

        asyncio.create_task(wait_for_stream_finish())
        return stream

    async def wait_for_current_streams(self):
        await asyncio.gather(*self._living_streams.values())
