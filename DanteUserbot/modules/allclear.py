from DanteUserbot import *
import asyncio
import os
from pyrogram.types import Message
from pyrogram import Client


from pyrogram.errors import *
from pyrogram.raw.functions.messages import DeleteHistory

__MODULE__ = "ᴄʟᴇᴀʀ ᴄʜᴀᴛ"

__HELP__ = f"""<blockquote><b>
<b>『 ᴄʟᴇᴀʀ ᴄʜᴀᴛ ɢʀᴏᴜᴘ 』</b>

  <b>• ᴄᴏᴍᴍᴀɴᴅ:</b> <code>{PREFIX[0]}cc</code>
  <b>• ᴇxᴘʟᴀɴᴀᴛɪᴏɴ:</b> hapus chat digroup replay ke users atau diri sendiri 
</b></blockquote>"""


@DANTE.UBOT("cc")
async def cc(client, message):
    reply = message.reply_to_message
    if reply and reply.sender_chat and reply.sender_chat != message.chat.id:
        aan = await message.reply("proses..")
        await asyncio.sleep(0.3)
        return await aan.delete()
    if len(message.command) == 2:
        user = message.text.split(None, 1)[1]
    elif len(message.command) == 1 and reply:
        user = message.reply_to_message.from_user.id
    else:
        aa = await message.reply("silahkan tunggu..")
        await asyncio.sleep(0.3)
        return await aa.delete()
    await message.delete()
    try:
        return await client.delete_user_history(message.chat.id, user)
    except Exception as ev:
        print(f"Error saat menghapus pesan: {ev}")
        await message.reply("berhasil menghapus semua pesan pengguna.")  # Memberi tahu user      


async def (client, message):
    rep = m.reply_to_message
    mek = await m.reply(_("proses").format(em.proses))
    if len(m.command) < 2 and not rep:
        await m.reply(_("auend_1").format(em.gagal))
        return
    if len(m.command) == 1 and rep:
        who = rep.from_user.id
        try:
            info = await c.resolve_peer(who)
            await c.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
        except PeerIdInvalid:
            pass
        await m.reply(_("auend_2").format(em.sukses, who))
    else:
        if m.command[1].strip().lower() == "all":
            biji = await c.get_chats_dialog("usbot")
            for kelot in biji:
                try:
                    info = await c.resolve_peer(kelot)
                    await c.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
                except PeerIdInvalid:
                    continue
            await m.reply(_("auend_3").format(em.sukses, len(biji)))
        elif m.command[1].strip().lower() == "bot":
            bijo = await c.get_chats_dialog("bot")
            for kelot in bijo:
                try:
                    info = await c.resolve_peer(kelot)
                    await c.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
                except PeerIdInvalid:
                    continue
            await m.reply(_("auend_4").format(em.sukses, len(bijo)))
        else:
            who = m.text.split(None, 1)[1]
            try:
                info = await c.resolve_peer(who)
                await c.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
            except PeerIdInvalid:
                pass
            await m.reply(_("auend_2").format(em.sukses, who))
    await mek.delete()
    return
