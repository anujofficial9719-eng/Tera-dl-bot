from pyrogram import Client, filters
from database.users import add_user

PHOTO = "https://i.ibb.co/WpKRVMKy/7168219724-28094.jpg"

@Client.on_message(filters.command("start"))
async def start(client, message):

    await add_user(message.from_user.id)

    user_name = message.from_user.first_name

    text = f"""
Welcome back to **Anuj Bots!!** 👤

Hi **{user_name}** ! 🔄

Just send me any **TeraBox link**, and I'll download it for you instantly.
"""

    await message.reply_photo(
        photo=PHOTO,
        caption=text
    )
