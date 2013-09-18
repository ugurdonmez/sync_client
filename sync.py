import pyinotify
import subprocess

wm = pyinotify.WatchManager() # Watch Manager
mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE | pyinotify.IN_MODIFY # watched events

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        subprocess.call(["rsync", "-vrc", "./folder/", "/mnt/samba/"])

    def process_IN_DELETE(self, event):
        subprocess.call(["rsync", "-vrc", "./folder/", "/mnt/samba/"])
    
    def process_IN_MODIFY(self, event):
        subprocess.call(["rsync", "-vrc", "./folder/", "/mnt/samba/"])

handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch('./folder/', mask, rec=True)

notifier.loop()