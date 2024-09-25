import requests
from pyrogram import Client, filters
from pyrogram.types import Message

from DanteUserbot import *

__MODULE__ = "ᴀɪ"
__HELP__ = f"""<blockquote><b>
<b>『 chat GPT 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}ask</code>
  <b>• penjelasan:</b> buat pertanyaan contoh .ask dimana letak Antartika
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
      
async def tanya(text):
    url = "https://widipe.com/v2/gpt4"
    params = {'text': text}
    headers = {'accept': 'application/json'}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
    if 'result' in data:
        return data['result']
    else:
        return f"{response.text}"

async def tebakkata(text):
    url = "https://widipe.com/tebakkata"
    params = {'text': text}
    headers = {'accept': 'application/json'}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
    if 'result' in data:
        return data['result']
    else:
        return f"{response.text}"
      
@DANTE.UBOT("tebak")
async def tebakkata(client, message: Message):
    text = get_text(message)
    if not text:
        return await message.reply("Example: .ask dimana kamu berada")
    pros = await message.reply("proses..")
    hasil = await tebakkata(text)
    return await pros.edit(hasil)

