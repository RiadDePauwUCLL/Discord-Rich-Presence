from pypresence import Presence
from datetime import datetime
import time
import sys
import os
# import subprocess
# import psutil
# import ctypes

#process = subprocess.Popen(["K:\\Drift_City_Remastered_Alpha_01-2024\\Drift City Remastered Alpha\\DriftCity.exe"])

os.environ['PYTHONUNBUFFERED'] = '1'

now = datetime.utcnow()
epoch_time = int((now - datetime(1970, 1, 1)).total_seconds())

try:
      client_id = "1204922123705917492"
      RPC = Presence(client_id,pipe=0)
      print("Created Presence object.", flush=True)
      RPC.connect()
      print("Connected.", flush=True)
except Exception as e:
    print(f"An error occurred: {e}", flush=True)
    sys.exit(1)

print("Running Discord Rich Presence...", flush=True)

# if process is True:
while True:
      RPC.update(large_image="dcr",
      small_image="dcr2",
      large_text="gigachad",
      details="Bing Chilling",
      state="Chasing HUVs",
      start=epoch_time
      # buttons=[{"label":"Monke player","url":"https://www.youtube.com/watch?v=1yipP37b58c"}],
      )
      time.sleep(1)


RPC.close()
# else:
#       subprocess.Popen(["C:\XboxGames\Minecraft Launcher\Content\Minecraft.exe"])