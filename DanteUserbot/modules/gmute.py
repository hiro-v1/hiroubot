import asyncio

from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import ChatPermissions, ChatPrivileges, Message
from pyrogram.errors import *
from pyrogram.types import *
from DanteUserbot import *


unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)

@DANTE.UBOT("gmute")
async def gmute_user(client, message):
    user_id = await extract_user(message)
    ky = await message.reply(f"<b>Processing....</b>")
    cmd = message.command
    if not message.reply_to_message and len(cmd) == 1:
        await ky.edit(
            f"**Gunakan format: <code>gmute</code> [user_id/username/balas ke user].**"
        )
    elif len(cmd) == 1:
        message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        cmd[1]
    try:
        user = await client.get_users(user_id)
    except PeerIdInvalid:
        await ky.edit(f"**Tidak dapat menemukan user tersebut.**")
        return
    prik = user.id
    prok = await get_seles()
    gua = client.me.id
    udah = await is_gmuteh_user(gua, prik)
    if prik in OWNER_ID:
        return await ky.edit(
            f"**Anda tidak bisa gmute dia karena dia pembuat saya.**"
        )
    elif prik in prok:
        return await ky.edit(
            f"**Anda tidak bisa gmute dia, karna dia adalah Admin Userbot Anda.**"
        )
    elif udah:
        return await ky.edit(f"**Pengguna ini sudah di gmute.**")
    elif prik not in prok and prik not in OWNER_ID:
        try:
            common_chats = await client.get_common_chats(user.id)
            await add_gmuteh_user(gua, prik)
            for i in common_chats:
                await i.restrict_member(user.id, ChatPermissions())
        except BaseException:
            pass
    return await ky.edit(
        f"**<a href='tg://user?id={prik}'>{user.first_name}</a> globally gmuted!**"
    )


@DANTE.UBOT("ungmute")
async def ungmute_user(client, message):
    user_id = await extract_user(message)
    ky = await message.reply(f"<b>Processing....</b>")
    cmd = message.command
    if not message.reply_to_message and len(cmd) == 1:
        await ky.edit(
            f"**Gunakan format: <code>ungmute</code> [user_id/username/reply to user].**"
        )
    elif len(cmd) == 1:
        message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        cmd[1]
    try:
        user = await client.get_users(user_id)
    except PeerIdInvalid:
        await ky.edit(f"**Tidak menemukan user tersebut.**")
        return
    prik = user.id
    gua = client.me.id
    udah = await is_gmuteh_user(gua, prik)
    if not udah:
        return await ky.edit(f"**Tidak ada pengguna ditemukan.**")
    try:
        common_chats = await client.get_common_chats(user.id)
        await remove_gmuteh_user(gua, prik)
        for i in common_chats:
            await i.unban_member(user.id)
    except BaseException:
        pass
    return await ky.edit(
        f"**<a href='tg://user?id={prik}'>{user.first_name}</a> globally ungmuted!**"
    )


@DANTE.UBOT("listgmute")
async def _(client, message):
    ky = await message.reply(f"<b>Processing....</b>")
    gua = client.me.id
    total = await get_gmuteh_count(gua)
    if total == 0:
        return await ky.edit(f"**Belum ada pengguna yang digmute.**")
    msg = f"**Total Gmute:** \n\n"
    tl = 0
    org = await get_gmuteh_users(gua)
    for i in org:
        tl += 1
        try:
            user = await client.get_users(i)
            user = user.first_name if not user.mention else user.mention
            msg += f"{tl}• {user}\n"
        except Exception:
            msg += f"{tl}• {i}\n"
            continue
    if tl == 0:
        return await ky.edit(f"**Belum ada pengguna yang digmute.**")
    else:
        return await ky.edit(msg)


@ubot.on_message(filters.incoming & filters.group)
async def globals_check(client, message):
    if not message:
        return
    if not message.from_user:
        return
    gua = client.me.id
    dia = message.from_user.id
    chat_id = message.chat.id
    masuk = await is_gmuteh_user(gua, dia)
    if not masuk:
        return

    elif masuk:
        try:
            await message.delete()
        except errors.RPCError:
            pass
        try:
            await client.restrict_chat_member(chat_id, dia, ChatPermissions())
        except BaseException:
            pass

    message.continue_propagation()
