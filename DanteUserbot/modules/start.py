from .. import *
import asyncio
from datetime import datetime
from gc import get_objects
from time import time
from DanteUserbot import bot, ubot
from pyrogram.errors.exceptions.bad_request_400 import UserBannedInChannel
from pyrogram.raw.functions import Ping
from pytgcalls import __version__ as pytg
from pyrogram import __version__ as pyr
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from DanteUserbot import *

PONG = """
<b>❏ PONG!!🏓</b>
<b>╰•{pong} ms</b>
"""

async def send_msg_to_owner(client, message):
    if message.from_user.id == OWNER_ID:
        return
    else:
        buttons = [
            [
                InlineKeyboardButton(
                    "👤 profil", callback_data=f"profil {message.from_user.id}"
                ),
                InlineKeyboardButton(
                    "jawab 💬", callback_data=f"jawab_pesan {message.from_user.id}"
                ),
            ],
        ]
        await client.send_message(
            OWNER_ID,
            f"<a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>\n\n<code>{message.text}</code>",
            reply_markup=InlineKeyboardMarkup(buttons),
        )

from pyrogram.errors.exceptions.bad_request_400 import ReactionInvalid

async def ping_cmd(client, message):
    try:
        start = datetime.now()
        await client.invoke(Ping(ping_id=0))
        end = datetime.now()
        uptime = await get_time((time() - start_time))
        delta_ping = round((end - start).microseconds / 10000, 2)
        pong = await EMO.PING(client)
        uptim = await EMO.UPTIME(client)
        menti = await EMO.MENTION(client)
        _ping = f"""
❏ <b><u>PONG!!</b></u>🏓
├• <b>{pong}Pong:</b> <code>{str(delta_ping).replace('.', ',')} ms</code>
├• <b>{uptim}Uptime: <code>{uptime}</code></b>
╰• <b>{menti}Owners:</b> <a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a>
"""
        await message.reply_text(_ping)
    except UserBannedInChannel:
        pass

async def start_cmd(client, message):
    await add_served_user(message.from_user.id)
    await send_msg_to_owner(client, message)
    if len(message.command) < 2:
        buttons = Button.start(message)
        msg = MSG.START(message)
        await message.reply(msg, reply_markup=InlineKeyboardMarkup(buttons))
    else:
        txt = message.text.split(None, 1)[1]
        msg_id = txt.split("_", 1)[1]
        send = await message.reply("<b>tunggu sebentar...</b>")
        if "secretMsg" in txt:
            try:
                m = [obj for obj in get_objects() if id(obj) == int(msg_id)][0]
            except Exception as error:
                return await send.edit(f"<b>❌ error:</b> <code>{error}</code>")
            user_or_me = [m.reply_to_message.from_user.id, m.from_user.id]
            if message.from_user.id not in user_or_me:
                return await send.edit(
                    f"<b>❌ pesan ini bukan untukmu <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>"
                )
            else:
                text = await client.send_message(
                    message.chat.id,
                    m.text.split(None, 1)[1],
                    protect_content=True,
                    reply_to_message_id=message.id,
                )
                await send.delete()
                await asyncio.sleep(120)
                await message.delete()
                await text.delete()
        elif "copyMsg" in txt:
            try:
                m = [obj for obj in get_objects() if id(obj) == int(msg_id)][0]
            except Exception as error:
                return await send.edit(f"<b>❌ error:</b> <code>{error}</code>")
            id_copy = int(m.text.split()[1].split("/")[-1])
            if "t.me/c/" in m.text.split()[1]:
                chat = int("-100" + str(m.text.split()[1].split("/")[-2]))
            else:
                chat = str(m.text.split()[1].split("/")[-2])
            try:
                get = await client.get_messages(chat, id_copy)
                await get.copy(message.chat.id, reply_to_message_id=message.id)
                await send.delete()
            except Exception as error:
                await send.edit(error)


@DANTE.UBOT("ping")
async def _(client, message):
    await ping_cmd(client, message)

@DANTE.UBOT("dping")
async def _(client, message: Message):
    user = message.from_user
    start = datetime.now()
    await client.invoke(Ping(ping_id=0))
    end = datetime.now()
    uptime = await get_time((time() - start_time))
    delta_ping = round((end - start).microseconds / 1000, 2)
    memek = f"<code>{str(delta_ping).replace('.', ',')}</code>"
    rpk = f"[{user.first_name} {user.last_name or ''}](tg://user?id={user.id})"
    pm_msg = await get_vars(client.me.id, "KONTOL_PING") or PONG
    await message.reply(pm_msg.format(pong=memek, mention=rpk))

@DANTE.UBOT("set")
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    if len(message.command) < 3:
        return await message.reply(
            f"{ggl}<code>{message.text.split()[0]}</code> <b>[query] [value]</b>"
        )
    query = {"pong": "KONTOL_PING"}
    if message.command[1].lower() not in query:
        return await message.reply(f"<b>{ggl}query yang di masukkan tidak valid</b>")
    query_str, value_str = (
        message.text.split(None, 2)[1],
        message.text.split(None, 2)[2],
    )
    value = query[query_str]
    if value_str.lower() == "none":
        value_str = False
    await set_vars(client.me.id, value, value_str)
    return await message.reply(
        f"<b>{brhsl}done bro!</b>"
    )

@DANTE.BOT("start")
async def _(client, message):
    await start_cmd(client, message)
