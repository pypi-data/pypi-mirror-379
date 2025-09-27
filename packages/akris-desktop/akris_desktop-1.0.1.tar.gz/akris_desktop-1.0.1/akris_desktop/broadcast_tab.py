import tkinter as tk

from .broadcast_message_entry import BroadcastMessageEntry
from .peers import Peers
from .broadcast_view import BroadcastView


class BroadcastTab(tk.Frame):
    def __init__(self, root, app):
        super().__init__(root)
        self.app = app
        self.toolbar_frame = tk.Frame(self, background="#333232")
        self.toolbar_frame.pack(side=tk.TOP, fill=tk.X)
        self.messages_and_peers_frame = tk.Frame(self)
        self.messages_and_peers_frame.pack(fill=tk.BOTH, expand=True)
        self.peers = Peers(self.messages_and_peers_frame, app)
        self.message_table = BroadcastView(self.messages_and_peers_frame, app, self)
        self.more_link = tk.Label(
            self.toolbar_frame,
            text=self.message_table.page_monitor.button_label(),
            fg="#00a1ff",
            cursor="hand2",
            background="#333232",
        )
        self.message_table.await_message_stats()
        self.more_link.pack(side=tk.LEFT)
        self.more_link.bind("<Button-1>", lambda e: self.message_table.load_previous())
        self.message_entry = BroadcastMessageEntry(self, app)
        self.app.register_message_listener(self.message_table)
        self.app.register_message_listener(self.peers)
