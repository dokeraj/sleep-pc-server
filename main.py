import os
import threading

import pystray
from PIL import Image

import sleep_controller

"""
HOW TO PACKAGE this project into EXE:

python -m PyInstaller --onefile --paths "C:\\Users\\numsi\\PycharmProjects\\sleep-pc-server\\venv\\Lib\\site-packages" main.py -w

- DON'T USE THE `-w` flag if you don't want the exe to be caught as a virus - but you will have to deal with a cmd screen
"""
"""
how to run this app:
1. Open the windows environment variables and set the following variables:
    - SERVER_HOST_IP    (where this will be your IP address of your PC)
    - SERVER_HOST_PORT  (where this will be the port your PC will be listening on)
    - put the `Bang_icon.png` into the same folder as the `.exe` file
"""

# READ THE ENV VARS:
SERVER_HOST_IP = os.environ.get('SERVER_HOST_IP', "127.0.0.1")
SERVER_HOST_PORT = os.environ.get('SERVER_HOST_PORT', "12345")


def on_exit(icon, item):
    icon.stop()
    os._exit(1)


image = Image.open("""./Bang_icon.png""")
menu = (pystray.MenuItem("Exit", on_exit),)

icon = pystray.Icon("spcs", image, f"Sleep PC Server running on IP: {SERVER_HOST_IP} and PORT: {SERVER_HOST_PORT}",
                    menu)
threading.Thread(target=icon.run).start()

print("Started sleep-pc-server API")
sleep_controller.runApi(SERVER_HOST_IP, SERVER_HOST_PORT)
