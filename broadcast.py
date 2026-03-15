from pyrogram import Client, filters
from database.users import get_users
import os

ADMINS = list(map(int, os.getenv("ADMINS").split()))

@Client.on_message(filters.command("broadcast") & filters.user(ADMINS))
async def broadcast(client, message):

    if not message.reply_to_message:
        return await message.reply("Reply to a message")

    users = await get_users()

    msg = message.reply_to_message

    for user in users:
        try:
            await msg.copy(user)
        except:
            pass

    await message.reply("Broadcast Completed")
