
# (c) @SamirJana

import asyncio
from WebStreamer.bot import StreamBot
from WebStreamer.utils.database import Database
from WebStreamer.utils.human_readable import humanbytes
from WebStreamer.vars import Var
from pyrogram import filters, Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
db = Database(Var.DATABASE_URL, Var.SESSION_NAME)


@StreamBot.on_message(filters.private & (filters.document | filters.video | filters.audio) & ~filters.edited, group=4)
async def private_receive_handler(c: Client, m: Message):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await c.send_message(
            Var.BIN_CHANNEL,
            f"ɴᴇᴡ ᴜꜱᴇʀ ᴊᴏɪɴᴇᴅ : \n\nɴᴀᴍᴇ : [{m.from_user.first_name}](tg://user?id={m.from_user.id}) ꜱᴛᴀʀᴛᴇᴅ ʏᴏᴜʀ ʙᴏᴛ !!"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await c.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await c.send_message(
                    chat_id=m.chat.id,
                    text="__ꜱᴏʀʀʏ, ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜꜱᴇ ᴍᴇ. ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ᴏᴡɴᴇʀ__\n\n **ʜᴇ Wɪʟʟ Hᴇʟᴘ Yᴏᴜ**[ ʜᴇʟᴘ ](https://github.com/SamirJanaOfficial).",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await c.send_message(
                chat_id=m.chat.id,
                text="""ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜꜱᴇ ᴍᴇ 🔐""",
                reply_markup=InlineKeyboardMarkup(
                    [[ InlineKeyboardButton("ᴊᴏɪɴ ɴᴏᴡ 🔓", url=f"https://t.me/{Var.UPDATES_CHANNEL}") ]]
                ),
                parse_mode="HTML"
            )
            return
        except Exception:
            await c.send_message(
                chat_id=m.chat.id,
                text="**ꜱᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ. ᴄᴏɴᴛᴀᴄᴛ ᴍʏ ᴏᴡɴᴇʀ**",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    try:
        log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
        stream_link = "https://{}/{}".format(Var.FQDN, log_msg.message_id) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}".format(Var.FQDN,
                                    Var.PORT,
                                    log_msg.message_id)
        file_size = None
        if m.video:
            file_size = f"{humanbytes(m.video.file_size)}"
        elif m.document:
            file_size = f"{humanbytes(m.document.file_size)}"
        elif m.audio:
            file_size = f"{humanbytes(m.audio.file_size)}"

        file_name = None
        if m.video:
            file_name = f"{m.video.file_name}"
        elif m.document:
            file_name = f"{m.document.file_name}"
        elif m.audio:
            file_name = f"{m.audio.file_name}"

        msg_text ="""
𝐁𝐫𝐮𝐡! 😁\n
<u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 ! 🤓</u>\n
<b>📂 ꜰɪʟᴇ ɴᴀᴍᴇ :</b> <i>{}</i>\n
<b>📦 ꜰɪʟᴇ ꜱɪᴢᴇ :</b> <i>{}</i>\n
<b>📥 ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ  :</b> <i>{}</i>\n
<b>❗️ ɴᴏᴛᴇ : ᴛʜɪꜱ ʟɪɴᴋ ɪꜱ ᴘᴀʀᴍᴀɴᴇɴᴛ</b>"""

        await log_msg.reply_text(text=f"**ʀᴇQᴜᴇꜱᴛᴇᴅ ʙʏ :** [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n**ᴜꜱᴇʀ ɪᴅ :** `{m.from_user.id}`\n**ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ :** {stream_link}", disable_web_page_preview=True, parse_mode="Markdown", quote=True)
        await m.reply_text(
            text=msg_text.format(file_name, file_size, stream_link),
            parse_mode="HTML", 
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("ᴅᴏᴡɴʟᴏᴀᴅ ɴᴏᴡ 📥", url=stream_link)]]),
            quote=True
        )
    except FloodWait as e:
        print(f"Sleeping for {str(e.x)}s")
        await asyncio.sleep(e.x)
        await c.send_message(chat_id=Var.BIN_CHANNEL, text=f"ɢᴏᴛ ꜰʟᴏᴏᴅᴡᴀɪᴛ ᴏꜰ {str(e.x)}s from [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n\n**ᴜꜱᴇʀ ɪᴅ :** `{str(m.from_user.id)}`", disable_web_page_preview=True, parse_mode="Markdown")


@StreamBot.on_message(filters.channel & (filters.document | filters.video) & ~filters.edited, group=-1)
async def channel_receive_handler(bot, broadcast):
    if int(broadcast.chat.id) in Var.BANNED_CHANNELS:
        await bot.leave_chat(broadcast.chat.id)
        return
    try:
        log_msg = await broadcast.forward(chat_id=Var.BIN_CHANNEL)
        stream_link = "https://{}/{}".format(Var.FQDN, log_msg.message_id) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}".format(Var.FQDN,
                                    Var.PORT,
                                    log_msg.message_id)
        await log_msg.reply_text(
            text=f"**ᴄʜᴀɴɴᴇʟ ɴᴀᴍᴇ:** `{broadcast.chat.title}`\n**ᴄʜᴀɴɴᴇʟ ɪᴅ:** `{broadcast.chat.id}`\n**ʀᴇQᴜᴇꜱᴛᴇᴅ ᴜʀʟ:** {stream_link}",
            # text=f"**ᴄʜᴀɴɴᴇʟ ɴᴀᴍᴇ:** `{broadcast.chat.title}`\n**ᴄʜᴀɴɴᴇʟ ɪᴅ:** `{broadcast.chat.id}`\n**ʀᴇQᴜᴇꜱᴛᴇᴅ ᴜʀʟ:** https://t.me/TGStreamyBot?start=udreamtoosmall_{str(log_msg.message_id)}",
            quote=True,
            parse_mode="Markdown"
        )
        await bot.edit_message_reply_markup(
            chat_id=broadcast.chat.id,
            message_id=broadcast.message_id,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ 📥", url=stream_link)]])
            # [[InlineKeyboardButton("ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ 📥", url=f"https://t.me/TGStreamyBot?start=udreamtoosmall_{str(log_msg.message_id)}")]])
        )
    except FloodWait as w:
        print(f"Sleeping for {str(w.x)}s")
        await asyncio.sleep(w.x)
        await bot.send_message(chat_id=Var.BIN_CHANNEL,
                             text=f"ɢᴏᴛ ꜰʟᴏᴏᴅᴡᴀɪᴛ ᴏꜰ {str(w.x)}s from {broadcast.chat.title}\n\n**ᴄʜᴀɴɴᴇʟ ɪᴅ:** `{str(broadcast.chat.id)}`",
                             disable_web_page_preview=True, parse_mode="Markdown")
    except Exception as e:
        await bot.send_message(chat_id=Var.BIN_CHANNEL, text=f"**#ᴇʀʀᴏʀ_ᴛʀᴀᴄᴇʙᴀᴄᴋ:** `{e}`", disable_web_page_preview=True, parse_mode="Markdown")
        print(f"ᴄᴀɴ'ᴛ ᴇᴅɪᴛ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ!\nᴇʀʀᴏʀ: {e}")
