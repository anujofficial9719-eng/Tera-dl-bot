import os
from pyrogram import Client, filters
from pyrogram.types import Message
from dotenv import load_dotenv

from downloader import download_video
from progress import progress_bar
from web import keep_alive
from database.users import add_user, get_users, total_users

load_dotenv("config.env")

api_id = int(os.getenv("TELEGRAM_API"))
api_hash = os.getenv("TELEGRAM_HASH")
bot_token = os.getenv("BOT_TOKEN")

ADMINS = list(map(int, os.getenv("ADMINS").split()))

app = Client(
    "teraboxbot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

# START

@app.on_message(filters.command("start"))
async def start(client, message):

    await add_user(message.from_user.id)

    await message.reply_text(
        "👋 Send any Terabox link\n\nI will download and send video."
    )

# LINK HANDLER

@app.on_message(filters.text)
async def link_handler(client, message: Message):

    link = message.text

    msg = await message.reply("Downloading...")

    try:

        file = await download_video(link, msg)

        await client.send_video(
            chat_id=message.chat.id,
            video=file,
            caption="Downloaded by Bot",
            supports_streaming=True
        )

        os.remove(file)

        await msg.delete()

    except Exception as e:

        await msg.edit(f"Error: {e}")

# STATS

@app.on_message(filters.command("stats") & filters.user(ADMINS))
async def stats(client, message):

    users = await total_users()

    await message.reply(
        f"Total Users: {users}"
    )

# BROADCAST

@app.on_message(filters.command("broadcast") & filters.user(ADMINS))
async def broadcast(client, message):

    if not message.reply_to_message:
        return await message.reply("Reply to message")

    users = await get_users()

    msg = message.reply_to_message

    for user in users:

        try:
            await msg.copy(user)
        except:
            pass

    await message.reply("Broadcast Done")

if __name__ == "__main__":

    keep_alive()

    app.run()
