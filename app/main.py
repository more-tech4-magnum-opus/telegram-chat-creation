from fastapi import FastAPI
from schema import OkOutput, CreateChatInput
from service import create_channel
app = FastAPI()

@app.post('/create-chat')
async def create_chat(chat_data: CreateChatInput):
    await create_channel(chat_data.chat_name, chat_data.users)
    return OkOutput(ok=True)