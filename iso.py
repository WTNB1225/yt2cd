import subprocess
import os

def create_iso(iso_filename, volume, source_dir):
    files = sorted(
        [os.path.join(source_dir, f) for f in os.listdir(source_dir)],
        key=lambda f: os.path.getctime(f)
    )
    cmd = ["mkisofs", "-o", iso_filename, "-V", volume, "-J", "-R"] + files
    subprocess.run(cmd, check=True)