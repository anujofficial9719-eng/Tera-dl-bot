from pyrogram import Client, filters
from database.users import total_users
import os

ADMINS = list(map(int, os.getenv("ADMINS").split()))

@Client.on_message(filters.command("stats") & filters.user(ADMINS))
async def stats(client, message):

    users = await total_users()

    await message.reply(
        f"Total Users: {users}"
    )
