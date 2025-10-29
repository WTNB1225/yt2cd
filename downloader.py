from yt_dlp import YoutubeDL

def download_mp3(url, outdir):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'outtmpl': f'{outdir}/%(title)s.%(ext)s',
    }
    with YoutubeDL(ydl_opts) as ydl:
        res = ydl.download(url)