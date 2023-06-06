import gi
import gc

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib
import os
import subprocess
import time

from pathlib import Path
import shutil

UI_FILE = "installer.glade"

running_folder = os.path.dirname(os.path.abspath(__file__))

assets = "/Extras/"