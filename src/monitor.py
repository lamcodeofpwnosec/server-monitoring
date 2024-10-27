import os
import inotify_simple
from inotify_simple import INotify, flags
from scan import scan_file

def monitor_directory(directory_to_watch):
    inotify = INotify()
    wd = inotify.add_watch(directory_to_watch, flags.CREATE | flags.MODIFY)

    print(f"[INFO] Monitoring started on {directory_to_watch}")

    while True:
        for event in inotify.read():
            if event.mask & (flags.CREATE | flags.MODIFY):
                filename = event.name
                file_path = os.path.join(directory_to_watch, filename)
                print(f"[INFO] Detected file change: {file_path}")
                scan_file(file_path)  # Pindai file untuk mendeteksi jika berbahaya
