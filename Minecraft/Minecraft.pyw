from pypresence import Presence
import time
import random
import sys
import math
import os

os.startfile (r"C:\XboxGames\Minecraft Launcher\Content\Minecraft.exe")
client_id = "1162435192171016232"
RPC = Presence(client_id,pipe=0)
RPC.connect()

while True:
      RPC.update(large_image="minecraft",
      large_text="Minin'",
      details="Minecraft",
      state="Minin' xdddddddd",
      start=int(time.time()),
      buttons=[{"label":"Monke player","url":"https://www.youtube.com/watch?v=1yipP37b58c"}],
      )

      time.sleep(3600)
      RPC.close()

      