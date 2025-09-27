import hashlib
import random
import sqlite3
import string
import time
import json

from akris_desktop.app import App
from locust.client import Client
from unittest.mock import MagicMock
from queue import Queue
import tkinter as tk


# def test_populate_peers():
#     root = tk.Tk()
#     client = MagicMock(Client)
#     client.message_queue = Queue()
#     for peer in generate_peers():
#         client.message_queue.put(peer)
#     app = App(root, client)
#     app.run()
#     root.mainloop()


def generate_peers():
    return [
        {
            "command": "peer",
            "status": "online",
            "handle": "asciilifeform",
        },
        {
            "command": "peer",
            "status": "online",
            "handle": "ben_vulpes",
        },
        {
            "command": "peer",
            "status": "online",
            "handle": "signpost",
        },
        {
            "command": "peer",
            "status": "online",
            "handle": "awt",
        },
    ]
