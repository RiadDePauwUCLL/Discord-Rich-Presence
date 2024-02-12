#!/usr/bin/env python
from pypresence import Presence, InvalidPipe # For rich presence
from datetime import datetime # For epoch time
from time import sleep
from pathlib import Path # For reading files
from DCR import DCR
from time import sleep
from sys import platform
import json, subprocess, sys

process = subprocess.Popen(["C:\\Program Files (x86)\\VMware\\VMware Workstation\\DCR.exe"])

def clear() -> bool:
    global epoch_time, STATUS, LASTSTATUS, running
    epoch_time = 0
    RPC.clear()
    STATUS = None
    LASTSTATUS = None
    if running:
        print("Stopped running Drift City.")
        running = False
    return running

running = False

# load JSON settings file
if Path("settings.json").is_file() and Path("settings.json").stat().st_size != 0:
    # Settings file found
    settings = json.load(open("settings.json", encoding="utf-8"))
else:
    Path("settings.json").touch()
    settings = {}

# Get client ID
if settings.get("clientID"):
    # client ID found in settings.json and it's not blank (NoneType/blank strings == False)
    clientID = settings.get("clientID")
elif Path("clientID.txt").is_file():
    # Client ID found in legacy file
    client_ID = Path("clientID.txt").read_text(encoding="utf-8")
else:
    # Prompt for ID
    clientID = input("Enter client ID: ")
    settings["clientID"] = clientID

# get game
game = []
if "DCR" in settings and settings.get("DCR").get("enabled", True):
    game.append("DCR")
    settings["DCR"]["enabled"] = True

if not game:
    if Path("game.txt").is_file():
        # Client ID found in legacy file
        game = Path("game.txt").read_text(encoding="utf-8")
        game = game.casefold().split("\n")
    else:
        game = ["DCR", "hyper-v", "virtualbox"]
        settings.update({'DCR': {'enabled': True}, 'hyper-v': {'enabled': True}, 'virtualbox': {'enabled': True}})

if "DCR" in game:
    # Get path to VMware
    if platform.lower() == "win32":
        if "DCR" in settings and settings["DCR"].get("path"):
            # VMware path found in settings.json and it's not blank (NoneType/blank strings == False)
            gamepath = settings["DCR"].get("path")
        elif Path("vmwarePath.txt").is_file():
            # VMware path found in legacy file
            gamepath = Path("vmwarePath.txt").read_text(encoding="utf-8")
            settings["DCR"]["path"] = gamepath
        elif Path("C:/Program Files (x86)/VMware/VMware Workstation/DriftCity.exe").is_file():
            print("Using C:/Program Files (x86)/VMware/VMware Workstation as path.")
            gamepath = Path("C:/Program Files (x86)/VMware/VMware Workstation")
            settings["DCR"]["path"] = gamepath.as_posix()
        elif Path("C:/Program Files/VMware/VMware Workstation/DriftCity.exe").is_file():
            print("Using C:/Program Files/VMware/VMware Workstation as path.")
            gamepath = Path("C:/Program Files/VMware/VMware Workstation")
            settings["DCR"]["path"] = gamepath.as_posix()
        else:
            # Prompt for path
            gamepath = input("Enter path to VMware Workstation folder: ")
            settings["DCR"]["path"] = gamepath
    else:
        gamepath = Path("DriftCity")

# Get large image key
# if settings.get("largeImage"):
#     largeimage = settings.get("largeImage")
# elif Path("largeImage.txt").is_file():
#     # Large image key found in legacy file
#     largeimage = Path("largeImage.txt").read_text(encoding="utf-8")
#     settings["largeImage"] = largeimage
# else:
#     # None found, ignore
#     largeimage = "xpcat"
# # Get small image key
# if settings.get("smallImage"):
#     smallimage = settings.get("smallImage")
# else:
#     # None found, ignore
#     smallimage = "xpcat"

settingsPath = Path("settings.json")
json.dump(settings, Path("settings.json").open(mode="w",), indent="\t")

if "DCR" in game:
    # Initialize VMware
    DCR = DCR(gamepath)

# Set up RPC
RPC = Presence(clientID)
try:
    RPC.connect()
except InvalidPipe:
    print("Waiting for Discord...")
    while True:
        try:
            RPC.connect()
            print("Connected to RPC.")
            break
        except InvalidPipe:
            pass
        sleep(5)
else:
    print("Connected to RPC.")
# RPC.connect()
# print("Connected to RPC.")
# Create last sent status so we don't spam Discord
LASTSTATUS = None
STATUS = None
# Set time to 0 to update on next change
epoch_time = 0

# Warning
print("Please note that Discord has a 15 second ratelimit in sending Rich Presence updates.")

# Run on a loop
while True:
    # Run DriftCity list, capture output, and split it up
    STATUS = None
    if "DCR" in game:
        DCR.updateOutput()
        if DCR.isRunning() == False:
            # No VMs running, clear rich presence and set time to update on next change
            clear()
        elif DCR.runCount() > 1:
            running = True
            # Too many VMs to fit in field
            STATUS = "Playing with"
            # Get party count so we can show how many are running
            party = [DCR.runCount(), DCR.runCount()]
            GAME = "Drift City Remastered"
        else:
            running = True
            # Init variable
            displayName = DCR.getRunningGuestName(0)
            STATUS = "Driving in " + displayName # Set status
            vmcount = None # Only 1 VM, so set vmcount to None
            GAME = "Drift City Remastered"

    if STATUS != LASTSTATUS and STATUS != None: # To prevent spamming Discord, only update when something changes
        print("Rich presence updated locally; new rich presence is: " + STATUS + " (using " + GAME + ")") # Report of status change, before ratelimit
        print(game)
        # if "virtualbox" in game and virtualbox.isRunning() and virtualbox.runCount() == 1:
        #     epoch_time = virtualbox.getVMuptime(0)
        if epoch_time == 0: # Only change the time if we stopped running VMs before
            # Get epoch time
            now = datetime.utcnow()
            epoch_time = int((now - datetime(1970, 1, 1)).total_seconds())
        # if largeimage is "xpcat":
        #     largetext = "Gigachad"
        else:
            largetext = "DUNNOOOOOOOOOOOOOOOOOOOOO XDXD XD XWD XD XD DX DXDX XD XD X DX DXD X D!"
        # The big RPC update
        RPC.update(state=STATUS, details="Collecting items in " + GAME, small_image="dcr2", large_image="dcr", small_text=GAME, large_text="gigachad", start=epoch_time, party_size=party)
        LASTSTATUS = STATUS # Update last status to last status sent
    sleep(1)
