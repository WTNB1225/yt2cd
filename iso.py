import subprocess

def create_iso(iso_filename, volume, source_dir):
    cmd = ["mkisofs", "-o", iso_filename, "-V", volume, "-J", "-R", source_dir]
    subprocess.run(cmd, check=True)