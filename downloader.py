from yt_dlp import YoutubeDL
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, ID3NoHeaderError
import os

def postprocessor_hook(d):
    if d['status'] == 'finished':
        title = d.get('info_dict', {}).get('title', 'unknown title')
        print("Done downloading, now converting ...")
        file_dict = (d.get('info_dict', {})).get('__files_to_move', None)
        if file_dict:
            full_path = list(file_dict.values())
            if os.path.exists(full_path[0]):
                try:
                    tags = EasyID3(full_path[0])
                except ID3NoHeaderError:
                    ID3(full_path[0]).save()
                    tags = EasyID3(full_path[0])
                print(full_path[0])
                print(os.path.exists(full_path[0]))
                tags['title'] = title.split('-')[1].strip() if '-' in title else 'Unknown Title'
                tags['artist'] = title.split('-')[0].strip() if '-' in title else 'Unknown Artist'
                tags.save()


def download_mp3(url, outdir):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'postprocessor_hooks': [postprocessor_hook],
        'outtmpl': f'{outdir}/%(playlist_index)s-%(title)s.%(ext)s' if 'list=' in url else f'{outdir}/%(title)s.%(ext)s',
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])