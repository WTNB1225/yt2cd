import argparse
from downloader import download_mp3
from iso import create_iso

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="choose the YouTube URL you want to download as an MP3")
    parser.add_argument("iso_name", help="choose the name of the output ISO file")
    parser.add_argument("volume", help="choose the volume name for the ISO file")
    parser.add_argument("-d", "--outdir", help="choose the directory where you want to download MP3 files")
    args = parser.parse_args()
    if not args.outdir:
        args.outdir = "./"
    download_mp3(args.url, args.outdir)
    create_iso(args.iso_name, args.volume, args.outdir)

if __name__ == "__main__":
    main()
