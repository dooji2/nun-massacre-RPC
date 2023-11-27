# File: nmdrpc.py
# Project: nun-massacre-RPC
# File Created: Monday, ‎November ‎27, ‎2023, ‏‎4:45:37 PM
# Author: Dooji (doojisbasement@gmail.com)
# GitHub: https://github.com/dooji2
# Discord: dooji_

# Last Modified: ‎Monday, ‎November ‎27, ‎2023, ‏‎5:00:04 PM
# Modified By: Dooji (doojisbasement@gmail.com)

# Copyright (c) 2023 Dooji

from pypresence import Presence
import time
import psutil

client_id = "1178686408743989388"
RPC = Presence(client_id)
RPC.connect()

start_time = time.time()

while True:
    game_process = "Nun Massacre.exe"
    is_running = any(
        process.name() == game_process for process in psutil.process_iter(attrs=["name"])
    )

    if is_running:
        elapsed_time = int(time.time() - start_time)

        presence_data = {
            "start": int(start_time),
            "large_image": "nmi",
            "large_text": "Nun Massacre",
        }

        RPC.update(**presence_data)
    else:
        RPC.clear()

    time.sleep(1)
