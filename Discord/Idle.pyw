from pypresence import Presence
import time
import random

client_id = "1162435192171016232"
RPC = Presence(client_id,pipe=0)
RPC.connect()

        #RPC.update(details="Quote:", state=random.choice(quotes))

while True:
        RPC.update(large_image="1",
        large_text="Vibin'",
        details="Baiken Enjoyer",
        state="Chillin'",
        start=int(time.time()),
        buttons=[{"label":"Monke player","url":"https://www.youtube.com/watch?v=1yipP37b58c"}]
        )
        
        time.sleep(1800)

        RPC.update(large_image="2",
        large_text="Vibin'",
        details="Baiken Enjoyer",
        state="Chillin'",
        start=int(time.time()),
        buttons=[{"label":"Monke player","url":"https://www.youtube.com/watch?v=1yipP37b58c"}]
        )
        
        time.sleep(1800)

        time.sleep(1800)

        RPC.update(large_image="3",
        large_text="Vibin'",
        details="Baiken Enjoyer",
        state="Chillin'",
        start=int(time.time()),
        buttons=[{"label":"Monke player","url":"https://www.youtube.com/watch?v=1yipP37b58c"}]
        )
        
        time.sleep(1800)

        time.sleep(1800)

        RPC.update(large_image="4",
        large_text="Vibin'",
        details="Baiken Enjoyer",
        state="Chillin'",
        start=int(time.time()),
        buttons=[{"label":"Monke player","url":"https://www.youtube.com/watch?v=1yipP37b58c"}]
        )
        
        time.sleep(1800)
        RPC.update(large_image="5",
        large_text="Vibin'",
        details="Baiken Enjoyer",
        state="Chillin'",
        start=int(time.time()),
        buttons=[{"label":"Monke player","url":"https://www.youtube.com/watch?v=1yipP37b58c"}]
        )
        
        time.sleep(1800)

        RPC.update(large_image="6",
        large_text="Vibin'",
        details="Baiken Enjoyer",
        state="Chillin'",
        start=int(time.time()),
        buttons=[{"label":"Monke player","url":"https://www.youtube.com/watch?v=1yipP37b58c"}]
        )
        
        time.sleep(1800)

        RPC.update(large_image="7",
        large_text="Vibin'",
        details="Baiken Enjoyer",
        state="Chillin'",
        start=int(time.time()),
        buttons=[{"label":"Monke player","url":"https://www.youtube.com/watch?v=1yipP37b58c"}]
        )
        
        time.sleep(1800)

        RPC.update(large_image="8",
        large_text="Vibin'",
        details="Baiken Enjoyer",
        state="Chillin'",
        start=int(time.time()),
        buttons=[{"label":"Monke player","url":"https://www.youtube.com/watch?v=1yipP37b58c"}]
        )
        
        time.sleep(1800)
        RPC.close()