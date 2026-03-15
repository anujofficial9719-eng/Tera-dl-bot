import yt_dlp
import asyncio

def normalize_link(url):
    mirrors = [
        "1024terabox.com",
        "teraboxapp.com",
        "terasharelink.com",
        "terashare.net",
        "teraboxlink.com"
    ]
    for m in mirrors:
        if m in url:
            url = url.replace(m, "terabox.com")
    return url

async def progress_hook(d, msg):
    if d['status'] == 'downloading':
        total = d.get('total_bytes') or d.get('total_bytes_estimate')
        downloaded = d.get('downloaded_bytes', 0)
        if total:
            percent = downloaded / total * 100
            await msg.edit(f"⏬ Downloading... {percent:.1f}%")

async def download_video(url, msg):
    url = normalize_link(url)
    await msg.edit("🔍 Extracting video link...")
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "outtmpl": "video.%(ext)s",
        "progress_hooks": [lambda d: asyncio.get_event_loop().create_task(progress_hook(d, msg))],
        "quiet": True,
        "noplaylist": True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    await msg.edit("✅ Download complete")
    return "video.mp4"
