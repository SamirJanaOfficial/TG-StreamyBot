# © @SamirJana [ Github ]

from WebStreamer.bot import StreamBot
from WebStreamer.vars import Var
from WebStreamer.utils.human_readable import humanbytes
from WebStreamer.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
db = Database(Var.DATABASE_URL, Var.SESSION_NAME)

START_TEXT = """
🙋 ʜᴇʏ,{}\n
ɪ'ᴍ ᴀ ᴛᴇʟᴇɢʀᴀᴍ ꜰɪʟᴇꜱ ꜱᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋ ᴀꜱ ᴡᴇʟʟ ᴀꜱ ᴅᴅʟ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ ʙᴀꜱᴇᴅ ᴏɴ ᴘʏʀᴏɢʀᴀᴍ.\n
<i>ᴄʟɪᴄᴋ ʜᴇʟᴘ ꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ</i>\n\n
<b><u>🧑🏻‍💻 ʙᴏᴛ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://github.com/SamirJanaOfficial'>ꜱᴀᴍɪʀ ᴊᴀɴᴀ</a></b></u>"""

HELP_TEXT = """
- ꜱᴇɴᴅ ᴍᴇ ᴀɴʏ ꜰɪʟᴇ ᴏʀ ᴍᴇᴅɪᴀ ꜰʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ.
- ɪ'ʟʟ ᴘʀᴏᴠɪᴅᴇ ᴇxᴛᴇʀɴᴀʟ ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ !.
- ᴀʟꜱᴏ ɪ ᴀᴍ ꜱᴜᴘᴘᴏʀᴛᴇᴅ ɪɴ ᴄʜᴀɴɴᴇʟꜱ.
- ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴄʜᴀɴɴᴇʟ ᴀꜱ ᴀᴅᴍɪɴ ᴛᴏ ᴍᴀᴋᴇ ᴍᴇ ᴡᴏʀᴋᴀʙʟᴇ ᴀɴᴅ ᴛᴏ ɢᴇᴛ ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ ʙᴜᴛᴛᴏɴ!
- ᴀʟʟ ᴘʀᴏᴠɪᴅᴇᴅ ʟɪɴᴋꜱ ɪꜱ ᴘᴀʀᴍᴀɴᴇɴᴛ & ʜᴏꜱᴛᴇᴅ ᴏɴ ʜɪɢʜꜱᴘᴇᴇᴅ ꜱᴇʀᴠᴇʀ\n
<b><u>📬 ʀᴇᴘᴏʀᴛ ʙᴜɢꜱ ᴏʀ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ :<a href='https://github.com/SamirJanaOfficial'>[ ᴄʟɪᴄᴋ ʜᴇʀᴇ ]</a></b></u>"""

ABOUT_TEXT = """
<b>🙏🏻 ᴍʏ ɴᴀᴍᴇ :</b> 𝐓𝐆-𝐒𝐓𝐑𝐄𝐀𝐌𝐘\n
<b>🔹 ꜱᴏᴜʀᴄᴇ-ᴄᴏᴅᴇ :</b> <a href='https://github.com/SamirJanaOfficial'>𝐍𝐨𝐭 𝐏𝐮𝐛𝐥𝐢𝐜 𝐘𝐞𝐭</a>\n
<b>🔸 ɢɪᴛʜᴜʙ : <a href='https://github.com/SamirJanaOfficial'>ᴅᴏ ꜰᴏʟʟᴏᴡ</a></b>"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('𝐇𝐞𝐥𝐩', callback_data='help'),
        InlineKeyboardButton('𝐀𝐛𝐨𝐮𝐭', callback_data='about'),
        InlineKeyboardButton('𝐂𝐥𝐨𝐬𝐞', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('𝐇𝐨𝐦𝐞', callback_data='home'),
        InlineKeyboardButton('𝐀𝐛𝐨𝐮𝐭', callback_data='about'),
        InlineKeyboardButton('𝐂𝐥𝐨𝐬𝐞', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('𝐇𝐨𝐦𝐞', callback_data='home'),
        InlineKeyboardButton('𝐀𝐛𝐨𝐮𝐭', callback_data='help'),
        InlineKeyboardButton('𝐂𝐥𝐨𝐬𝐞', callback_data='close')
        ]]
    )

@StreamBot.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    else:
        await update.message.delete()


@StreamBot.on_message(filters.command('start') & filters.private & ~filters.edited)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"**ɴᴇᴡ ᴜꜱᴇʀ ᴊᴏɪɴᴇᴅ :** \n\n__ᴍʏ ɴᴇᴡ ᴜꜱᴇʀ__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __ꜱᴛᴀʀᴛᴇᴅ ʏᴏᴜʀ ʙᴏᴛ !!__"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="__ꜱᴏʀʀʏ, ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜꜱᴇ ᴍᴇ. ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ᴏᴡɴᴇʀ__\n\n **ʜᴇ Wɪʟʟ Hᴇʟᴘ Yᴏᴜ**[ ʜᴇʟᴘ ](https://github.com/SamirJanaOfficial).",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<i>ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜꜱᴇ ᴍᴇ 🔐</i>",
                    reply_markup=InlineKeyboardMarkup(
                        [[
                            InlineKeyboardButton("ᴊᴏɪɴ ɴᴏᴡ 🔓", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]]
                    ),
                    parse_mode="HTML"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="ꜱᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ ᴄᴏɴᴛᴀᴄᴛ ᴍʏ ᴏᴡɴᴇʀ <b><a href='https://github.com/SamirJanaOfficial'>[ ᴄᴏɴᴛᴀᴄᴛ ]</a></b>",
                    parse_mode="HTML",
                    disable_web_page_preview=True)
                return
        await m.reply_text(
            text=START_TEXT.format(m.from_user.mention),
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
              )                                                                         
                                                                                       
                                                                            
    else:
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**ꜱᴏʀʀʏ, ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜꜱᴇ ᴍᴇ. ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ᴏᴡɴᴇʀ** [ꜱᴀᴍɪʀ ᴊᴀɴᴀ](https://github.com/SamirJanaOfficial).",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜꜱᴇ ᴍᴇ**!\n\n**ᴅᴜᴇ ᴛᴏ ᴏᴠᴇʀʟᴏᴀᴅ, ᴏɴʟʏ ᴄʜᴀɴɴᴇʟ ꜱᴜʙꜱᴄʀɪʙᴇʀꜱ ᴄᴀɴ ᴜꜱᴇ ᴛʜᴇ ʙᴏᴛ**!",
                    reply_markup=InlineKeyboardMarkup(
                        [[
                          InlineKeyboardButton("🤖 ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**ꜱᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ ᴄᴏɴᴛᴀᴄᴛ ᴍʏ ᴏᴡɴᴇʀ. ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ** [ꜱᴀᴍɪʀ ᴊᴀɴᴀ](https://github.com/SamirJanaOfficial).",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, message_ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link = "https://{}/{}".format(Var.FQDN, get_msg.message_id) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.message_id)

        msg_text ="""
𝐁𝐫𝐮𝐡! 😁\n
<u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 ! 🤓</u>\n
<b>📂 ꜰɪʟᴇ ɴᴀᴍᴇ :</b> <i>{}</i>\n
<b>📦 ꜰɪʟᴇ ꜱɪᴢᴇ :</b> <i>{}</i>\n
<b>📥 ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ  :</b> <i>{}</i>\n
<b>❗️ ɴᴏᴛᴇ : ᴛʜɪꜱ ʟɪɴᴋ ɪꜱ ᴘᴀʀᴍᴀɴᴇɴᴛ</b>"""

        await m.reply_text(
            text=msg_text.format(file_name, file_size, stream_link),
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("ᴅᴏᴡɴʟᴏᴀᴅ ɴᴏᴡ 📥", url=stream_link)]])
        )


@StreamBot.on_message(filters.private & filters.command(["about"]))
async def start(bot, update):
    await update.reply_text(
        text=ABOUT_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=ABOUT_BUTTONS
    )


@StreamBot.on_message(filters.command('help') & filters.private & ~filters.edited)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**ɴᴇᴡ ᴜꜱᴇʀ ᴊᴏɪɴᴇᴅ :**\n\n__ᴍʏ ɴᴇᴡ ᴜꜱᴇʀ__ [{message.from_user.first_name}](tg://user?id={message.from_user.id}) __ꜱᴛᴀʀᴛᴇᴅ ʏᴏᴜʀ ʙᴏᴛ !!__"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="__ꜱᴏʀʀʏ, ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜꜱᴇ ᴍᴇ. ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ᴏᴡɴᴇʀ__\n\n **ʜᴇ Wɪʟʟ Hᴇʟᴘ Yᴏᴜ**<b><a href='https://github.com/SamirJanaOfficial'>[ ʜᴇʟᴘ ]</a></b>",
                    parse_mode="HTML",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜꜱᴇ ᴍᴇ!**\n\n__ᴅᴜᴇ ᴛᴏ ᴏᴠᴇʀʟᴏᴀᴅ, ᴏɴʟʏ ᴄʜᴀɴɴᴇʟ ꜱᴜʙꜱᴄʀɪʙᴇʀꜱ ᴄᴀɴ ᴜꜱᴇ ᴛʜᴇ ʙᴏᴛ!__",
                reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton("🤖 ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="__ꜱᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ. ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ__ [ꜱᴀᴍɪʀ ᴊᴀɴᴀ](https://github.com/SamirJanaOfficial).",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text=HELP_TEXT,
        parse_mode="HTML",
        disable_web_page_preview=True,
        reply_markup=HELP_BUTTONS
        )
