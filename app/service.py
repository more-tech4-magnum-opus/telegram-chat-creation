from config import api_hash, api_id
import asyncio
from pyrogram import Client
from pyrogram.raw.functions.messages import create_chat
from pyrogram.raw.types import InputUser
from typing import List
import multiprocessing


async def create_channel(channel_name: str, users: List[str]):
    async with Client("my_account", api_id, api_hash) as app:
        print(users)
        await app.create_group(channel_name, users)
        #['firesieht', 's4nspie', 'dubrovin_vladimir', 'Nazvan']
        #create_chat.CreateChat(users=[InputUser(user_id='firesieht')], title='auto generate chat')


def sync_service_create_channel(channel_name: str, users: List[str]):
    p = multiprocessing.Process(target=lambda channel_name, users: asyncio.run(create_channel(channel_name=channel_name, users=users)), args=(channel_name, users))
    p.run()
    #asyncio.run(create_channel(channel_name=channel_name, users=users))
