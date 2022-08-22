import asyncio

async def connect():
    reader, writer = await asyncio.open_connection('localhost', 8888)
    count = 0
    chunks = []
    while count < 256:
        writer.write("next".encode())
        await writer.drain()
        data = await reader.read(2048)
        chunks.append(data)
        if not data:
            break
        count += 1
    chunks = sorted(chunks)
    chunks = [i[1:] for i in chunks]
    return b"".join(chunks)