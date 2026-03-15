🚀 TeraBox Downloader Telegram Bot

<p align="center"><img src="https://img.shields.io/badge/Python-3.11-blue">
<img src="https://img.shields.io/badge/Library-Pyrogram-green">
<img src="https://img.shields.io/badge/Database-MongoDB-brightgreen">
<img src="https://img.shields.io/badge/License-MIT-yellow">
<img src="https://img.shields.io/badge/Maintained-Yes-success"></p>A powerful Telegram Bot built using Python and Pyrogram that allows users to download and stream TeraBox videos directly on Telegram.

The bot automatically downloads files from TeraBox links and uploads them back to Telegram with streaming support, progress tracking, and high-speed uploads.

---

✨ Features

- ⚡ Fast TeraBox Downloader
- 🎬 2GB Video Upload Support
- 📊 Real-Time Progress Bar
- 👥 MongoDB User Database
- 📢 Broadcast System for Admins
- 📈 User Statistics Command
- 🔒 Admin Control System
- 🌐 24/7 Hosting Support
- 📺 Streaming Enabled Videos
- 🧩 Clean Modular Code Structure

---

🛠 Tech Stack

Technology| Purpose
Python| Core Programming Language
Pyrogram| Telegram Bot Framework
MongoDB| User Database
Flask| Keep Alive Server
Requests / Aiohttp| File Downloading

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

1️⃣ Clone Repository

git clone [https://github.com/anujofficial9719-eng/terabox-bot](https://github.com/anujofficial9719-eng/Tera-dl-bot/tree/main)
cd Tera-dl-bot

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run The Bot

python bot.py

---

☁️ Deploy

You can deploy this bot on:

- 🚀 Render
- 🚀 Koyeb
- 🚀 Railway
- 🚀 VPS

Recommended Python Version:

Python 3.11

---

👨‍💻 Admin Commands

Command| Description
"/stats"| Show total users
"/broadcast"| Send message to all users

---

📊 Bot Workflow

1️⃣ User sends a TeraBox link
2️⃣ Bot downloads the file
3️⃣ Bot uploads video to Telegram
4️⃣ User receives streamable video

---

⚡ Performance

- Fast download system
- Optimized upload handling
- Streaming supported videos
- Efficient memory usage

---

🔒 Security

- Admin-only commands
- MongoDB user storage
- Exception handling system

---

⚠️ Disclaimer

This project is intended for educational purposes only.

The developer is not responsible for misuse of this software.

---

❤️ Support

If you like this project:

⭐ Star the repository
🍴 Fork the project
📢 Share with others

---

👑 Credits

- Python
- Pyrogram
- Telegram API

---

📜 License

This project is licensed under the MIT License.
