import requests
from pyrogram.types import InputMediaPhoto, Message
import io
from pyrogram import Client, filters
from pyrogram.types import Message

from DanteUserbot import *

__MODULE__ = "ᴛᴏᴏʟs"
__HELP__ = f"""
**--chat GPT--**
<blockquote><b>
  <b>• perintah:</b> <code>{PREFIX[0]}ask</code>
  <b>• penjelasan:</b> buat pertanyaan contoh .ask dimana letak Antartika

tambahan:
  <b>• perintah:</b> <code>{PREFIX[0]}cp</code>
  <b>• penjelasan:</b> dapatkan poto profil couple pasangan.
  
</b></blockquote>"""

def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None
      

async def tanya(client, text):
    url = "https://itzpire.com/ai/botika"
    params = {
        "q": f"{text}",
        "user": f"{client.me.first_name}",
        "model": "alicia"
    }
    headers = {'accept': 'application/json'}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        msg = data["result"]
        return f"<blockquote>{msg}</blockquote>"
    else:
        return "Server error, gatau ah"

@DANTE.UBOT("ask")
async def gpt(client, message: Message):
    text = get_text(message)
    if not text:
        return await message.reply("perintah anda salah, gunakan .ask pertanyaan")
    pros = await message.reply("tunggu..")
    hasil = await tanya(client, text)
    return await pros.edit(hasil)
  
async def ambil_ppcp(client, text):
    url = "https://itzpire.com/search/pinterest?query=cewe"
     params = {"q": f"{text}"}

    headers = {'accept': 'application/json'}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        msg = data["result"]
        return f"<blockquote>{msg}</blockquote>"
    else:
        return "Server error, gatau ah"
      

@DANTE.UBOT("cp")
async def handle_ppcp(client: Client, message: Message):
    await ambil_ppcp(message)

async def pinterest(client, message: Message):
   if not text:
        return await message.reply("perintah anda salah, gunakan .cp gambar")
    pros = await message.reply("menjawab..")
    hasil = await ambil_ppcp(client, text)
    return await pros.edit(hasil)
 
@DANTE.UBOT("pinter")
async def pinter(client, message: Message):
  text = message.text.split(" ")
  
  if len(text) < 3:
    
    return await message.reply(".pinter iya gua pinter lu GOBLOK")
    
    message = text[1]
    
    gambar_url, deskripsi = await pinterest(message)
    
    if gambar_url:
        await message.reply_photo(photo=gambar_url, caption=f"<blockquote> link = <code>{deskripsi}</code></blockquote>")
    else:
        await message.reply("Gambar tidak tersedia atau tidak ada hasil.")
