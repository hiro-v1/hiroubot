from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
from DanteUserbot import *

__MODULE__ = "ᴅᴇʟᴄʜᴀᴛ"
__HELP__ = """<blockquote><b>
<b>『 Clear semua chat 』</b>

  <b>• delchat:</b> <code>{0}delchat</code></code>
  <b>• Example:</b> hapus seluruh chat kamu.
  </b></blockquote> """

@DANTE.UBOT("cc")
async def _(c: nlx, m, _):
    org = await c.extract_user(m)
    if not org:
        a = await m.reply(_("prof_1").format(em.gagal))
        await asyncio.sleep(2)
        return await a.delete()
    user = await c.get_users(org)
    await m.delete()
    return await c.delete_user_history(m.chat.id, user.id)

@DANTE.UBOT("cc")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    rep = m.reply_to_message
    mek = await m.reply("proses")
    if len(m.command) < 2 and not rep:
        await m.reply(_("").format(em.gagal))
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
