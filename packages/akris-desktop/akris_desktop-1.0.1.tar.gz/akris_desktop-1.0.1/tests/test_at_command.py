import time

import pytest
from akris_desktop.app import App
from akris.client import Client
from unittest.mock import MagicMock
from queue import Queue
import tkinter as tk


@pytest.fixture
def client():
    client = MagicMock(Client)
    client.message_queue = Queue()
    timestamp = int(time.time())
    messages = [
        {
            'command': 'console_response',
            'type': 'at',
            'body': [
                {
                    'handle': 'atahualpa',
                    'address': '122.122.0.1:8081',
                    'active_at': '2023-05-21 07:13:26.541438',
                    'active_at_unixtime': 1684678406
                }
            ]
        }
    ]
    for message in messages:
        client.message_queue.put(message)

    yield client

@pytest.fixture
def app(client):
    root = tk.Tk()
    app = App(root, client)
    app.wait_visibility()
    app.check_message_queue()
    app.notebook.select(1)
    yield app
    # root.destroy()


def test_at_command(app):
    app.console.entry.focus_force()
    app.console.entry.insert(0, 'at')
    app.update()
    app.console.entry.event_generate('<Return>')
    app.update()
    assert(app.api_client.send_command.called_with({
        'command': 'at',
        'args': []
    }))
    app.mainloop()

def test_at_response_display(app):
    app.update()
    app.mainloop()
