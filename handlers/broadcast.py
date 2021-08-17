import asyncio
from pyrogram import Client
from pyrogram.types import Dialog, Chat, Message
from config import SUDO_USERS
from helpers.filters import command
from callsmusic.callsmusic import client as USER


@Client.on_message(command("broadcast"))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("`starting broadcast...`")
        if not message.reply_to_message:
            await wtf.edit("please reply to a message to do broadcast!")
            return
        lmao = message.reply_to_message.text
        async for dialog in USER.iter_dialogs():
            try:
                await USER.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`global cast...` \n\n**sent to:** `{sent}` chats \n**failed in:** {failed} chats")
                await asyncio.sleep(3)
            except:
                failed=failed+1
                #await wtf.edit(f"`broadcasting...` \n\n**sent to:** `{sent}` chats \n**failed in:** {failed} chats")
                
            
        await message.reply_text(f"`gcast succesfully` \n\n**sent to:** `{sent}` chats \n**failed in:** {failed} chats")
