🚀 Terabox Downloader Telegram Bot

A powerful Telegram Bot built with Python & Pyrogram that allows users to download and stream Terabox videos directly on Telegram.

This bot automatically downloads Terabox files and uploads them to Telegram with streaming support and progress tracking.

---

✨ Features

- ⚡ Fast Terabox Downloader
- 🎬 2GB Video Upload Support
- 📊 Real-Time Progress Bar
- 👥 MongoDB User Database
- 📢 Broadcast System for Admins
- 📈 User Statistics Command
- 🔒 Admin Control
- 🌐 24/7 Hosting Support
- 📺 Streaming Enabled Videos
- 🧩 Modular Code Structure

---

🛠 Tech Stack

- Python 3.10+
- Pyrogram
- MongoDB
- Flask (Keep Alive Server)
- Requests / Aiohttp

---

📂 Project Structure

terabox-pro-bot
│
├── bot.py
├── downloader.py
├── progress.py
├── web.py
├── config.py
├── requirements.txt
├── runtime.txt
├── config.env
│
└── database
    └── users.py

---

⚙️ Environment Variables

Create a file named config.env

TELEGRAM_API=123456
TELEGRAM_HASH=your_api_hash
BOT_TOKEN=your_bot_token

MONGO_URL=your_mongodb_url

ADMINS=123456789

DUMP_CHAT_ID=-100xxxxxxxx
FSUB_ID=-100xxxxxxxx

---

📦 Installation

Clone the repository

git clone https://github.com/anujofficial9719-eng/terabox-bot
cd terabox-bot

Install requirements

pip install -r requirements.txt

Run the bot

python bot.py

---

☁️ Deploy

You can deploy this bot on:

- Render
- Koyeb
- Railway
- VPS

Recommended Python version:

Python 3.11

---

👨‍💻 Admin Commands

Command| Description
"/stats"| Show total users
"/broadcast"| Send message to all users

---

📊 Bot Workflow

1️⃣ User sends Terabox link
2️⃣ Bot downloads file
3️⃣ Bot uploads video to Telegram
4️⃣ User receives streamable video

---

⚠️ Disclaimer

This project is created for educational purposes only.
The developer is not responsible for misuse of the bot.

---

❤️ Support

If you like this project:

⭐ Star the repository
🍴 Fork it
📢 Share with others

---

👑 Credits

- Python
- Pyrogram
- Telegram API

---

📜 License

This project is licensed under the MIT License.
