import time

async def progress_bar(current, total, msg, start):

    percent = current * 100 / total

    bar = "█" * int(percent / 5) + "░" * (20 - int(percent / 5))

    text = f"""

Uploading...

[{bar}]

{percent:.2f}%

"""

    try:
        await msg.edit(text)
    except:
        pass
