import subprocess

def install_ffmpeg():
    try:
        subprocess.run(["ffmpeg", "-version"], check=True, stdout=subprocess.DEVNULL)
        print("FFmpeg already installed ✅")
    except subprocess.CalledProcessError:
        print("Installing FFmpeg...")
        subprocess.run("apt update -y && apt install ffmpeg -y", shell=True, check=True)
        print("FFmpeg installed successfully ✅")
