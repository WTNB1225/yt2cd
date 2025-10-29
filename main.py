import argparse
from downloader import download_mp3

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="choose the YouTube URL you want to download as an MP3")
    parser.add_argument("-d", "--outdir", help="choose the directory where you want to download MP3 files")
    args = parser.parse_args()
    if not args.outdir:
        args.outdir = "./"
    download_mp3(args.url, args.outdir)

if __name__ == "__main__":
    main()
