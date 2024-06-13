from DanteUserbot import *
import asyncio
import importlib

from pyrogram.enums import SentCodeType
from pyrogram.errors import *
from pyromod import listen

from pykeyboard import InlineKeyboard
from pyrogram.types import *
from pyrogram.raw import functions


@DANTE.CALLBACK("cl_ad")
async def cl_ad(client, callback_query):
    user_id = callback_query.from_user.id
    if user_id in ubot._get_my_id:
        buttons = [
            [
                InlineKeyboardButton("ᴍᴇɴᴜ", callback_data="help_back"),
                InlineKeyboardButton("ɪɴғᴏ", callback_data="cl_info")
            ],
            [
                InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="cl_close")
            ],
        ]
        return await callback_query.edit_message_text(
            f"""
<b>☎️ Menu Bantuan</b>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        
@DANTE.CALLBACK("cl_info")
async def cl_info(client, callback_query):
    user_id = callback_query.from_user.id
    if user_id in ubot._get_my_id:
        buttons = [
            [
                InlineKeyboardButton("ᴋᴇᴍʙᴀʟɪ", callback_data="cl_ad")
            ],
        ]        
        return await callback_query.edit_message_text(
            f"""
<b>☎️ silahkan hubungi: <a href=tg://openmessage?user_id={OWNER_ID}>admin</a> jika bot kamu delay atau butuh bantuan mengenai bot</b>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        
@DANTE.CALLBACK("cl_close")       
async def cl_close(client, callback_query):
    user_id = callback_query.from_user.id
    if user_id in ubot._get_my_id:
        return await callback_query.edit_message_text(
            f"""
⚠️ Menu Ditutup!</b>
""",
            disable_web_page_preview=True,
        )
