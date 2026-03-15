import os
import subprocess

def install_ffmpeg():
    """Install FFmpeg automatically on Replit if not present"""
    try:
        # Check if ffmpeg is already installed
        subprocess.run(["ffmpeg", "-version"], check=True, stdout=subprocess.DEVNULL)
        print("FFmpeg already installed ✅")
    except subprocess.CalledProcessError:
        print("Installing FFmpeg...")
        # Update and install ffmpeg
        subprocess.run("apt update -y && apt install ffmpeg -y", shell=True, check=True)
        print("FFmpeg installed successfully ✅")

install_ffmpeg()
