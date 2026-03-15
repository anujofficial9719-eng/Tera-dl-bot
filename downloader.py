import yt_dlp

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

    await msg.edit("🔍 Extracting video link...")

    ydl_opts = {
        "format": "best",
        "merge_output_format": "mp4",
        "outtmpl": "video.mp4",
        "quiet": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    await msg.edit("✅ Download complete")

    return "video.mp4"
