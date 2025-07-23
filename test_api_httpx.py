import httpx
import asyncio

async def ask():
    async with httpx.AsyncClient() as client:
        question = "What is my total sales?"
        response = await client.post("http://localhost:8000/chat", json={"question": question})
        print("Bot:", response.json()["answer"])

asyncio.run(ask())