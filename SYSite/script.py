from pprint import pprint
from pysnap import get_file_extension, Snapchat
import os.path
import json
import time
import os 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SYSite.settings") 
from snapyak.models import Image

from pysnap.utils import (encrypt, decrypt, decrypt_story,
                          make_media_id, request)

MEDIA_IMAGE = 0
MEDIA_VIDEO = 1
MEDIA_VIDEO_NOAUDIO = 2

FRIEND_CONFIRMED = 0
FRIEND_UNCONFIRMED = 1
FRIEND_BLOCKED = 2
PRIVACY_EVERYONE = 0
PRIVACY_FRIENDS = 1

def process_snap(s, snap, path, quiet=False):
    extension=get_file_extension(snap['media_type'])
    if extension !='jpg':
        return
    ctime=time.time()
    filename = '{0}.{1}'.format(ctime, extension)
    abspath = os.path.abspath(os.path.join(path, filename))
    if os.path.isfile(abspath):
        return
    data = s.get_blob(snap['id'])
    if data is None:
        return
    with open(abspath, 'wb') as f:
        f.write(data)
        if not quiet:
            print('Saved: {0}'.format(abspath))
    image=Image(sid=snap['id'], time=ctime, path='images/{0}.jpg'.format(ctime))
    image.save()

def init():
    s=Snapchat()
    s.login('snapstanford', 'C4rdinal')
    s.update_privacy(False)
    while True:
        snaps = s.get_snaps(4)
        for snap in snaps:
            process_snap(s,snap, "/home/kevin/Documents/SnapYak/SYSite/static/images/", False)
            s.mark_viewed(snap['id'])
        print "checking"

def testSave():
    s=Snapchat()
    s.login('snapstanford', 'C4rdinal')
    snaps=s.get_snaps()
    for snap in snaps:
        process_snap(s,snap, "/home/kevin/Pysnap/saved", False)
    if s.clear_feed:
        print"cleared"
init()