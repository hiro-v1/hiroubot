from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
from pyrogram.errors import *
from pyrogram.raw.functions.messages import DeleteHistory
from DanteUserbot import *

__MODULE__ = "ᴅᴇʟᴄʜᴀᴛ"
__HELP__ = """<blockquote><b>
<b>『 Clear semua chat 』</b>

  <b>• delchat:</b> <code>{0}delchat</code></code>
  <b>• Example:</b> hapus seluruh chat kamu.
  </b></blockquote> """

@DANTE.UBOT("cc")
async def cc(client: Client, message: Message):
    org = await client.extract_user(message)
    if not org:
        a = await message.reply.text("proses")
        await asyncio.sleep(2)
        return await a.delete()
    user = await client.get_users(org)
    await message.delete()
    return await client.delete_user_history(message.chat.id, user.id)


@DANTE.UBOT("clchat")
async def clchat(client: Client, message: Message):
    rep = message.reply_to_message
    mek = await message.reply.text("proses")
    if len(message.command) < 2 and not rep:
        await message.reply.text("gagal menghapus chat")
        return
    if len(message.command) == 1 and rep:
        who = rep.from_user.id
        try:
            info = await client.resolve_peer(who)
            await client.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
        except PeerIdInvalid:
            pass
        await message.reply("berhasil menghapus seluruh chat kamu")
    else:
        if message.command[1].strip().lower() == "all":
            biji = await client.get_chats_dialog("usbot")
            for kelot in biji:
                try:
                    info = await client.resolve_peer(kelot)
                    await message.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
                except PeerIdInvalid:
                    continue
            await message.reply.text("sukses").format(len(biji))
        elif message.command[1].strip().lower() == "bot":
            bijo = await client.get_chats_dialog("bot")
            for kelot in bijo:
                try:
                    info = await client.resolve_peer(kelot)
                    await client.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
                except PeerIdInvalid:
                    continue
            await message.reply.text("sukses").format(bijo)
        else:
            who = message.text.split(None, 1)[1]
            try:
                info = await client.resolve_peer(who)
                await c.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
            except PeerIdInvalid:
                pass
            await message.reply.text("berhasil").format(who)
    await mek.delete()
    return
