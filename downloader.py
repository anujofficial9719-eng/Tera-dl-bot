import yt_dlp
import asyncio

def normalize_link(url):
    """Convert any Terabox/Terashare mirror link to main terabox.com link"""
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


async def download_video(url, msg):
    """Download video from Terabox/Terashare and merge audio+video"""
    url = normalize_link(url)
    await msg.edit("🔍 Extracting video link...")

    # yt-dlp options
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",  # best video + best audio
        "merge_output_format": "mp4",          # merge into mp4
        "outtmpl": "video.%(ext)s",            # output filename
        "progress_hooks": [lambda d: asyncio.get_event_loop().create_task(progress_hook(d, msg))],
        "quiet": True,
        "noplaylist": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    await msg.edit("✅ Download complete")
    return "video.mp4"


async def progress_hook(d, msg):
    """Show live download progress in Telegram"""
    if d['status'] == 'downloading':
        total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate')
        downloaded = d.get('downloaded_bytes', 0)

        if total_bytes:
            percent = downloaded / total_bytes * 100
            await msg.edit(f"⏬ Downloading... {percent:.1f}%")
