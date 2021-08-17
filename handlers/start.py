from time import time
from datetime import datetime
from config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME
from helpers.filters import command, sudo_only
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from helpers.decorators import authorized_users_only


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>┗┓ ʜᴀɪ!! {message.from_user.first_name} sᴀʏᴀ ᴀᴅᴀʟᴀʜ [{BOT_NAME}](https://t.me/{BOT_USERNAME}) ┏┛\n
sᴀʏᴀ ᴀᴅᴀʟᴀʜ ᴍᴜsɪᴄ ʙᴏᴛ ʏᴀɴɢ sᴀɴɢᴀᴛ ᴄᴀɴɢɢɪʜ,sᴀʏᴀ ᴀᴋᴀɴ ᴍᴇᴍʙᴀɴᴛᴜ ᴀɴᴅᴀ ᴍᴇʀɪᴀʜᴋᴀɴ ɢʀᴏᴜᴘ ᴀɴᴅᴀ.
sᴀʏᴀ ᴍᴇᴍᴘᴜɴʏᴀɪ ғɪᴛᴜʀ ᴘʀᴀᴋᴛɪs sᴇᴘᴇʀᴛɪ:
┏━━━━━━━━━━━━━━
┣• ᴍᴇᴍᴜᴛᴀʀ ᴍᴜsɪᴄ.
┣• ᴍᴇɴᴅᴏᴡɴʟᴏᴀᴅ ʟᴀɢᴜ.
┣• ᴍᴇɴᴄᴀʀɪ ʟᴀɢᴜ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪᴘᴜᴛᴀʀ ᴀᴛᴀᴜ ᴅɪᴅᴏᴡɴʟᴏᴀᴅ.
┗━━━━━━━━━━━━━━
ᴋᴇᴛɪᴋ » /help « ᴀᴛᴀᴜ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ](https://t.me/rakasupport) ᴊɪᴋᴀ ᴛɪᴅᴀᴋ ᴘᴀʜᴀᴍ!
ᴛʜᴀɴᴋs ᴛᴏ 🤖[owner](https://t.me/knsgnwn)
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ ᴛᴀᴍʙᴀʜᴋᴀɴ sᴀʏᴀ ᴋᴇ ɢʀᴏᴜᴘ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                         "ᴀssɪsᴛᴇɴᴛ", url=f"https://t.me/{ASSISTANT_NAME}"
                    ),
                    InlineKeyboardButton(
                        "ʀᴇᴘᴏ", url="https://github.com/rakaanjay/KGMusicBot"
                    )
                ]
            ]
        ),
     disable_web_page_preview=False
    )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""I'm online!\n<b>Up since:</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ʀᴇᴘᴏ", url="https://github.com/rakaanjay/KGMusicBot"
                    ),
                    InlineKeyboardButton(
                        "ɢʀᴏᴜᴘ", url="https://t.me/instagramindonesia1"
                    )
                ]
            ]
        )
    )


@Client.on_message(command("help") & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.mention()}!
\n/play (judul lagu) - Untuk Memutar lagu yang Anda minta melalui YouTube
/playlist - Untuk Menampilkan daftar putar Lagu sekarang
/current - Untuk Menunjukkan  Lagu sekarang yang sedang diputar
/song (judul lagu) - Untuk Mendownload lagu dari YouTube
/lyric (judul lagu) - Untuk Mencari lirik lagu
/search (judul video) - Untuk Mencari Video di YouTube dengan detail
/video (judul video) - Untuk Mendownload Video di YouTube dengan detail
\n**Admins Only:**
/player - Open music player settings panel
/pause - Untuk Menjeda pemutaran Lagu
/resume - Untuk Melanjutkan pemutaran Lagu yang di pause
/skip - Untuk Menskip pemutaran lagu ke Lagu berikutnya
/end - Untuk Memberhentikan pemutaran Lagu
/userbotjoin - Untuk Mengundang asisten ke obrolan Anda
/reload - Untuk Merefresh admin list
ᴛʜᴀɴᴋs ᴛᴏ 🤖[owner](https://t.me/knsgnwn)
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ɢʀᴏᴜᴘ", url="https://t.me/sinihadehh"
                    ),
                    InlineKeyboardButton(
                        "ᴄʜᴀɴɴᴇʟ", url="https://t.me/rakasupport"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, m: Message):
    start = time()
    m_reply = await m.reply_text("Pinging...")
    delta_ping = time() - start
    await m_reply.edit_text(
        f"🏓 **PONG!!**\n"
        f"`{delta_ping * 1000:.3f} ms`"
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & sudo_only & ~filters.edited)
async def get_uptime(client: Client, m: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m.reply_text(
        f"🤖\n"
        f"• **Uptime:** `{uptime}`\n"
        f"• **Start Time:** `{START_TIME_ISO}`"
    )
