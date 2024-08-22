import random
import requests
from DanteUserbot import *

from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ᴀɪ"
__HELP__ = f"""<blockquote><b>
<b>『 chat GPT 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}ask</code>
  <b>• penjelasan:</b> buat pertanyaan contoh .ask dimana letak Antartika
</b></blockquote>"""


@DANTE.UBOT("ask")
async def chat_gpt(ubot, message):
    try:
        await ubot.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "Contoh :-\n\n/ask Dimana letak Antartika?"
            )
        else:
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://tofu-api.onrender.com/chat/{ubot}/{message}')

            try:
                # Check if "results" key is present in the JSON response
                if "answer" in response.json():
                    x = response.json()["answer"]                  
                    await message.reply_text(
                      f"{x}\n\nPertanyaan ini dijawab oleh ᴅᴀɴᴛᴇ ꭙ ᴜʙᴏᴛ",
                        parse_mode=ParseMode.MARKDOWN
                    )
                else:
                    await message.reply_text("No 'results' key found in the response.")
            except KeyError:
                # Handle any other KeyError that might occur
                await message.reply_text("Error accessing the response.")
    except Exception as e:
        await message.reply_text(f"**á´‡Ê€Ê€á´Ê€: {e} ")
      
import asyncio
import aiohttp
from pyrogram import Client, filters
from DanteMusic import app
from pymongo import MongoClient
from config import MONGO_DB_URI

DATABASE = MongoClient(MONGO_DB_URI)
db = DATABASE["MAIN"]["USERS"]
collection = db["members"]

def add_user_database(user_id: int):
    check_user = collection.find_one({"user_id": user_id})
    if not check_user:
        return collection.insert_one({"user_id": user_id})

async def chat_with_api(model, prompt):
    url = f"https://tofu-api.onrender.com/chat/{model}/{prompt}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                if data["code"] == 2:
                    return data["content"]
                else:
                    return "Ada masalah, tidak dapat memperoleh respons dari api"
            else:
                return "Ada masalah, tidak dapat mencari karena api ai eror"

@DANTE.UBOT("ask")
async def gptAi(client, message):
    split_text = message.text.split(None, 1)
    if len(split_text) < 2:
        await message.reply_text("cari: /gpt [printah]")
    else:
        response = await chat_with_api("gpt", split_text[1])
        await message.reply_text(response)
