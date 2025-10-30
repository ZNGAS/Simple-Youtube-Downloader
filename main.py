import yt_dlp

url = input("Enter URL:")
mode = input("Enter mode (video/audio):")
if mode == "video":
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4',  # 需要 ffmpeg
        'noplaylist': True,
        'concurrent_fragment_downloads': 5,
    }
elif mode == "audio":
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

