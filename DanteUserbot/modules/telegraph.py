from DanteUserbot import *
from telegraph import Telegraph, exceptions, upload_file

__MODULE__ = "ᴛɢʀᴀᴘʜ"
__HELP__ = """<blockquote><b>
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛᴇʟᴇɢʀᴀᴘʜ 』</b>

  <b>• ᴄᴏᴍᴍᴀɴᴅ:</b> <code>{0}tg</code> [ʀᴇᴘʟʏ ᴍᴇᴅɪᴀ/ᴛᴇxᴛ]
  <b>• ᴇxᴘʟᴀɴᴀᴛɪᴏɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴘʟᴏᴀᴅ ᴍᴇᴅɪᴀ/ᴛᴇxᴛ ᴋᴇ ᴛᴇʟᴇɢʀᴀ.ᴘʜ
</b></blockquote>"""


@DANTE.UBOT("tg")
async def tg_cmd(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    XD = await message.reply(f"{prs}<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs . . .</b>")
    if not message.reply_to_message:
        return await XD.edit(
            f"{ggl}<b>ᴍᴏʜᴏɴ ʙᴀʟᴀs ᴋᴇ ᴘᴇsᴀɴ, ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ʟɪɴᴋ ᴅᴀʀɪ ᴛᴇʟᴇɢʀᴀᴘʜ.</b>"
        )
    telegraph = Telegraph()
    if message.reply_to_message.media:
        m_d = await dl_pic(client, message.reply_to_message)
        try:
            media_url = upload_file(m_d)
        except exceptions.TelegraphException as exc:
            return await XD.edit(f"<code>{exc}</code>")
        U_done = f"{sks}<b>ʙᴇʀʜᴀsɪʟ ᴅɪᴜᴘʟᴏᴀᴅ ᴋᴇ</b> <a href='https://telegra.ph/{media_url[0]}'>telegraph</a>"
        await XD.edit(U_done)
    elif message.reply_to_message.text:
        page_title = f"{client.me.first_name} {client.me.last_name or ''}"
        page_text = message.reply_to_message.text
        page_text = page_text.replace("\n", "<br>")
        try:
            response = telegraph.create_page(page_title, html_content=page_text)
        except exceptions.TelegraphException as exc:
            return await XD.edit(f"<code>{exc}</code>")
        wow_graph = f"{sks}<b>ʙᴇʀʜᴀsɪʟ ᴅɪᴜᴘʟᴏᴀᴅ ᴋᴇ</b> <a href='https://telegra.ph/{response['path']}'>telegraph</a>"
        await XD.edit(wow_graph)
