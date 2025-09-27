import tkinter as tk

from .direct_message_entry import DirectMessageEntry
from .direct_view import DirectView


class DirectTab(tk.Frame):
    def __init__(self, root, handle, app):
        super().__init__(root)
        self.handle = handle
        self.app = app
        self.toolbar_frame = tk.Frame(self, background="#333232")
        self.toolbar_frame.pack(side=tk.TOP, fill=tk.X)
        self.close_link = tk.Label(
            self.toolbar_frame,
            text="🗙",
            fg="white",
            cursor="hand2",
            background="red",
        )
        self.close_link.pack(side=tk.RIGHT)
        self.close_link.bind("<Button-1>", lambda e: self.app.close_tab(self))
        self.messages_and_peers_frame = tk.Frame(self)
        self.messages_and_peers_frame.pack(fill=tk.BOTH, expand=True)
        self.message_table = DirectView(
            self.messages_and_peers_frame, handle, app, self
        )
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
        self.message_entry = DirectMessageEntry(self, app, handle)
        self.app.register_message_listener(self.message_table)
