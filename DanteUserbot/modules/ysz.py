import re

import requests
from pyrogram import enums
from unidecode import unidecode

from DanteUserbot import *

percakapan = {}


def ini_font(txt):
    msg = unidecode(txt)
    return txt != msg


def cobain(text):
    pattern = (
        r"[\u10E6\u0336\u20E0\u034B\u0300-\u036F]|"
        r"[A-Za-z0-9]\u0336|"
        r"[A-Za-z0-9]\u20E0|"
        r"[A-Za-z0-9]\u034B|"
        r"»[A-Za-z0-9]»|"
        r"≋[A-Za-z0-9]≋|"
        r"[A-Za-z][0-9]|[0-9][A-Za-z]|"
        r"(\w)\1{2}|.*\d{3}|"
        r"[^\w\s\U0001F300-\U0001F5FF\U0001F600-\U0001F64F\U0001F680-\U0001F6FF\U00002600-\U000026FF\U00002700-\U000027BF\U0001F900-\U0001F9FF\U0001F1E6-\U0001F1FF]{3}$|"
        r"»[A-Za-z0-9]»|≋[A-Za-z0-9]≋|[A-Za-z][0-9]|[0-9][A-Za-z]|"
        r"[░]|"
        r"(\w)\1{2,}|.*\d{3,}|[^\w\s]{3,}"
        r"[@{2,}]+|"
        r"[\u2000-\u206F\u20A0-\u20CF\u2200-\u22FF\u2600-\u26FF\u2700-\u27BF]|"
        r"[\u0300-\u036F\u1DC0-\u1DFF\u20D0-\u20FF\uFE20-\uFE2F]|"
        r"[\u0100-\u017F\u0370-\u03FF\u0400-\u04FF]"
    )
    return bool(re.search(pattern, text))


def send_simtalk(msg):
    params = {"text": msg, "lc": "id"}
    response = requests.post("https://api.simsimi.vn/v1/simtalk", data=params).json()
    return response.get("message")


@DANTE.UBOT("onx")
async def _(client, msg, _):
    txt = msg.text if msg.text else msg.caption
    rep = msg.reply_to_message or msg
    cek_grup = dB.get_list_from_var(client.me.id, "chats", "chat_id")
    if msg.chat.id not in cek_grup:
        return
    if txt.startswith(("!", "/", "?", "@", "#")):
        return
    await client.send_chat_action(msg.chat.id, enums.ChatAction.TYPING)
    try:
        if msg.reply_to_message:
            user = rep.from_user if rep.from_user else rep.sender_chat
            csfont = ini_font(txt)
            if csfont:
                return
            dobel = cobain(txt)
            if dobel:
                return
            if user.id == client.me.id:
                anu = send_simtalk(txt)
                await msg.reply(anu)
            elif user.id != client.me.id:
                return
        elif not msg.reply_to_message:
            csfont = ini_font(txt)
            if csfont:
                return
            dobel = cobain(txt)
            if dobel:
                return
            anu = send_simtalk(txt)
            await msg.reply(anu)

    except Exception as e:
        return await msg.reply(str(e))
    return await client.send_chat_action(msg.chat.id, enums.ChatAction.CANCEL)
