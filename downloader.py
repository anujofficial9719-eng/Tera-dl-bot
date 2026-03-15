import yt_dlp
import re

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


async def download_video(url, msg):

    url = normalize_link(url)

    await msg.edit("Extracting video link...")

    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "outtmpl": "video.%(ext)s",
        "quiet": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        info = ydl.extract_info(url, download=True)

        filename = ydl.prepare_filename(info)

        if not filename.endswith(".mp4"):
            filename = filename.rsplit(".",1)[0] + ".mp4"

    await msg.edit("Download complete")

    return filename
