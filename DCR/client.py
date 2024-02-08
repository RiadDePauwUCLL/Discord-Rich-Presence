import subprocess
from pathlib import *
from sys import platform
import json
guestOS = json.load(open("staticConstant.json"))

class vmware(object):
    DCrunpath = None
    output = None
    def __init__(self, DCpath):
        if platform.lower() == "win32":
            DCpath = DCpath.replace('\"', "")
            DCpath = DCpath.replace("\'", "")
            self.DCrunpath = Path(DCpath).joinpath("DriftCity.exe")
        else:
            self.DCrunpath = DCpath
    def updateOutput(self):
        output = subprocess.run([str(self.DCrunpath), "list"], stdout=subprocess.PIPE)
        output = output.stdout.decode("utf-8")
        if platform.lower() == "win32":
            output = output.split("\r\n")
        else:
            output = output.split("\n")
        self.output = [x for x in output if len(x)] # Don't rely on always having a blank element at the end, thanks CorpNewt
    def runCount(self):
        return len(self.output) - 1
    def isRunning(self):
        if self.runCount() > 0:
            return True
        else:
            return False
    def getRunningVMPath(self, index = None):
        if self.isRunning() == False:
            return None
        # Thanks to CorpNewt for the fix
        elif index != None:
            return self.output[index + 1]
        else:
            return self.output[1:]
    def getVMProperty(self, path, property):
        dcr_game = Path(path)
        value = None
        for line in dcr_game.read_text().split("\n"):
            if property in line:
                value = line[len(property) + 4:][:-1]
                break
        return value
    def getRunningVMProperty(self, index, property):
        return self.getVMProperty(self.getRunningVMPath(index), property)
    def getGuestName(self, path):
        return self.getVMProperty(path, "displayName")
    def getRunningGuestName(self, index):
        return self.getRunningVMProperty(index, "displayName")
    def getGuestOS(self, path, raw=None):
        if raw == None or raw == False:
            property = self.getVMProperty(path, "guestOS")
            return guestOS.get(property, "Unknown")
        else:
            return self.getVMProperty(path, "guestOS")
    def getRunningGuestOS(self, index, raw=None):
        if raw == None or raw == False:
            property = self.getRunningVMProperty(index, "guestOS")
            return guestOS.get(property, "Unknown")
        else:
            return self.getRunningVMProperty(index, "guestOS")