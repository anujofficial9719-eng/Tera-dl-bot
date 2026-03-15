import requests
import os

async def download_video(link, msg):

    file = "video.mp4"

    r = requests.get(link, stream=True)

    with open(file, "wb") as f:

        for chunk in r.iter_content(1024):

            if chunk:
                f.write(chunk)

    return file
