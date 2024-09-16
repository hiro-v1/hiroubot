from DanteUserbot import *
import asyncio
import os
from pyrogram.types import Message
from pyrogram import Client


from pyrogram.errors import *
from pyrogram.raw.functions.messages import DeleteHistory

@DANTE.UBOT("cc")
async def cc(client, message):
    reply = message.reply_to_message
    if reply and reply.sender_chat and reply.sender_chat != message.chat.id:
        aan = await message.reply("terjadi masalah saat menghapus semua pesan kamu")
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
    except:
        pass
    except Exception as ev:
        print(f"Error saat menghapus pesan: {ev}")
        await message.reply("Terjadi kesalahan saat menghapus pesan.")  # Memberi tahu user      

@DANTE.UBOT("clearall")
async def clearall(client, message):
    rep = message.reply_to_message
    dantekntl = await message.reply("proses")
    if len(message.command) < 2 and not rep:
        await message.reply("silahkan tunggu")
        return
    if len(message.command) == 1 and rep:
        who = rep.from_user.id
        try:
            info = await client.resolve_peer(who)
            await client.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
        except PeerIdInvalid:
            pass
        await message.reply("berhasil mengahapus semua chat")
    else:
        if message.command[1].strip().lower() == "all":
            biji = await client.get_chats_dialog("usbot")
            for kelot in biji:
                try:
                    info = await client.resolve_peer(kelot)
                    await client.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
                except PeerIdInvalid:
                    continue
                except FloodWait as e:
                    await asyncio.sleep(e.value)
                    info = await client.resolve_peer(kelot)
                    await client.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
            await message.reply("sukses menghapus seluruh chat kamu")
        elif message.command[1].strip().lower() == "bot":
            bijo = await client.get_chats_dialog("bot")
            for kelot in bijo:
                try:
                    info = await client.resolve_peer(kelot)
                    await client.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
                except PeerIdInvalid:
                    continue
                except FloodWait as e:
                    await asyncio.sleep(e.value)
                    info = await client.resolve_peer(kelot)
                    await client.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
            await message.reply("berhasil menghapus semua chat")
        else:
            who = message.text.split(None, 1)[1]
            try:
                info = await client.resolve_peer(who)
                await client.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
            except PeerIdInvalid:
                pass
            except FloodWait as e:
                await asyncio.sleep(e.value)
                info = await client.resolve_peer(who)
                await client.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
            await message.reply("gagal menghapus chat private kamu")
    return await dantekntl.delete()
        except Exception as ev:
            print(f"Error saat menghapus pesan: {ev}")  
            await message.reply("Terjadi kesalahan saat menghapus pesan.")
   
