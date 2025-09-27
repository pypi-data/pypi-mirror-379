import hashlib
import random
import sqlite3
import json
import string
import time

import pytest
import pytest_mock
from akris_desktop.app import App
from akris.client import Client
import akris.lib.simple_graph_sqlite.database as db
from unittest.mock import MagicMock
from queue import Queue
import tkinter as tk

def generate_random_string(length):
    """Helper function to generate random strings of given length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_chat_messages(num_messages):
    """Generate a list of num_messages random chat messages."""
    messages = []
    prev_hash = ''
    for i in range(num_messages):
        timestamp = int(time.time())
        body = generate_random_string(20)
        hash = hashlib.sha256(body.encode()).hexdigest()
        handle = generate_random_string(10)
        netchain = prev_hash if prev_hash else ''
        message = {
            'command': 'broadcast_text',
            'timestamp': timestamp,
            'body': body,
            'message_hash': hash,
            'speaker': handle,
            'net_chain': netchain
        }
        messages.append(message)
        prev_hash = hash
    return messages

@pytest.fixture
def client():
    akris_path = '/home/awt/PycharmProjects/pine-beetle/tests/fixtures/akris.db'
    db.initialize(akris_path)
    connection = sqlite3.connect(akris_path)
    cursor = connection.cursor()
    latest_message = json.loads(cursor.execute("SELECT * FROM nodes ORDER BY json_extract(body, '$.timestamp') DESC LIMIT 1;").fetchone()[0])
    messages = db.traverse(akris_path, latest_message['message_hash'],
                                    neighbors_fn=db.find_inbound_neighbors, with_bodies=True)
    parsed_messages = []
    for message_row in messages:
        message = json.loads(message_row[2])
        if not message:
            pass
        else:
            message["command"] = "broadcast_text"
            parsed_messages.append(message)

    # parsed_messages = generate_chat_messages(1000)
    client = MagicMock(Client)
    client.message_queue = Queue()
    for message in parsed_messages:
        client.message_queue.put(message)

    yield client

    cursor.close()
    connection.close()

@pytest.fixture
def app(client):
    root = tk.Tk()
    app = App(root, client)
    yield app
    # root.destroy()


def test_display_broadcast_text(app):
    app.wait_visibility()
    app.check_message_queue()
    app.update()
    # assert(len(app.message_table.table.get_children()) == 40)
    app.mainloop()

def test_console_command(app):
    app.wait_visibility()
    app.check_message_queue()
    app.notebook.select(1)
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
