#
# 20,000 Light Years Into Space
# This game is licensed under GPL v2, and copyright (C) Jack Whitham 2006-07 and Tux Penguin 2020.
#

import pickle, startup, os, extra, primitives


CFG_VERSION = "1.5"

class Config:
    def __init__(self):
        self.version = CFG_VERSION
        (w, h, fs) = primitives.RESOLUTIONS[ 0 ]
        self.resolution = (w, h)
        self.fullscreen = False
        self.mute = True
        self.font_scale = fs
        self.seen_before = False

cfg = Config()

FILENAME = None

def Initialise(delete_file):
    global cfg, FILENAME

    home = extra.Get_Home()
    if ( home == None ):
        FILENAME = "config.dat"
    else:
        FILENAME = os.path.join(home, ".lightyears.cfg")

    if delete_file:
        # Don't load old configuration
        Save()
        return

    try:
        f = open(FILENAME, "rb")
        cfg2 = pickle.load(f)
        f.close()
        if cfg2.version == CFG_VERSION:
            # Configuration is valid, we can use it.
            cfg = cfg2
    except Exception:
        pass

def Save():
    global cfg, FILENAME

    try:
        f = open(FILENAME, "wb")
        pickle.dump(cfg, f)
        f.close()
    except Exception:
        pass

