from yt_dlp import YoutubeDL

def download_mp3(url, out_dir):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'outtmpl': f'{out_dir}/%(title)s.%(ext)s',
    }
    with YoutubeDL(ydl_opts) as ydl:
        res = ydl.download(url)
        print("-----------------------")
        print(res)

tmp = "https://www.youtube.com/watch?v=SAWzXkV3hHo"
download_mp3([tmp], "musics")