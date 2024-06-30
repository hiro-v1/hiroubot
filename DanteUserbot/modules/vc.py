__MODULE__ = "ᴠᴄᴛᴏᴏʟs"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴠᴄᴛᴏᴏʟꜱ 』</b>

• Perintah: <code>{0}startvc</code>
• Penjelasan: Untuk memulai voice chat grup.

• Perintah: <code>{0}stopvc</code>
• Penjelasan: Untuk mengakhiri voice chat grup.

"""


from asyncio import sleep
from pytgcalls import PyTgCalls
from contextlib import suppress
from random import randint
from typing import Optional

from pyrogram import Client, enums
from pytgcalls.types import MediaStream
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.types import Message
from DanteUserbot import *

async def get_group_call(

    client: Client, message: Message, err_msg: str = ""

) -> Optional[InputGroupCall]:
    chat_peer = await client.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (
                await client.invoke(GetFullChannel(channel=chat_peer))
            ).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await client.invoke(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await eor(message, f"<emoji id =5929358014627713883>❌</emoji> **No group call Found** {err_msg}")
    return False

@DANTE.UBOT("startvc")
async def opengc(client: Client, message: Message):
    ky = await eor(message, "`Processing....`")
    vctitle = get_arg(message)
    if message.chat.type == "channel":
        chat_id = message.chat.title
    else:
        chat_id = message.chat.id
    args = f"<b>Active Voice Chat</b>\n • <b>Chat</b> : {message.chat.title}"
    try:
        if not vctitle:
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                )
            )
        else:
            args += f"\n • <b>Title:</b> {vctitle}"
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                    title=vctitle,
                )
            )
        await ky.edit(args)
    except Exception as e:
        await ky.edit(f"<b>INFO:</b> `{e}`")

@DANTE.UBOT("stopvc")
async def end_vc_(client: Client, message: Message):
    ky = await eor(message, f"<emoji id=6010111371251815589>⏳</emoji> `Processing....`")
    if not (group_call := await get_group_call(client, message, err_msg=", Error...")):
        return
    await client.invoke(DiscardGroupCall(call=group_call))
    await ky.edit(f"<b>Voice Chat Ended</b>\n • <b>Chat</b> : {message.chat.title}")

@DANTE.UBOT("jvc")
async def joinvc(client, message):
    if message.from_user.id != client.me.id:
        ky = await message.reply("<code>Processing....</code>")
    else:
        ky = await eor(message, "<code>Processing....</code>")
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    with suppress(ValueError):
        chat_id = int(chat_id)
    try:
        await client.call_py.play(chat_id)
    except Exception as e:
        return await ky.edit(f"ERROR: {e}")
    await ky.edit(
        f"❏ <b>Berhasil Join Voice Chat</b>\n└ <b>Chat :</b><code>{message.chat.title}</code>"
    )
    await sleep(1)
    await ky.delete()

@DANTE.UBOT("lvc")
async def leavevc(client, message):
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    try:
        await client.call_py.leave_call(chat_id)
    except Exception as e:
        return await message.reply_text("**❏ Berhasil Meninggalkan Voice Chat <emoji id=5798623990436074786>✅</emoji>**")
        await message.reply()
        await message.delete()
