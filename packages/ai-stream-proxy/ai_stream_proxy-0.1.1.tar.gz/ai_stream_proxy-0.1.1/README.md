## Usage

```python
import asyncio

if __name__ == '__main__':
    from ai_stream_proxy import StreamProxyClient
    async def main():
        client = StreamProxyClient(
            server_url="http://127.0.0.1:3000",
            httpx_async_client_options={'proxy': 'http://127.0.0.1:7890'}
        )

        await client.delete_stream(stream_id='test')

        await client.create_stream(
            stream_id='test',
            message_id='haha',
            content_type='claude-code-stream-json+include-partial-messages'
        )

        async with client.new_stream(stream_id="test") as stream:
            with open('some-claude-code-output.jsonl', 'r') as f:
                while True:
                    chunk = f.read(4096)
                    if not chunk:
                        break
                    stream.enqueue(chunk.encode('utf-8'))
            stream.finish(abort=False, reason="Finish")

        await client.wait_for_current_streams()


    asyncio.run(main())
```