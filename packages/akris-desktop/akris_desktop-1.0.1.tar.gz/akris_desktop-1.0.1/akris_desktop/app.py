import importlib
import logging
import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from akris_desktop.broadcast_tab import BroadcastTab
from akris_desktop.direct_tab import DirectTab
from akris_desktop.ref_link_tab import RefLinkTab
from akris_desktop.console import Console
from akris_desktop.message_stats_listener import MessageStatsListener
from akris_desktop.new_handle_listener import NewHandleListener
from akris_desktop.new_ref_link_listener import NewRefLinkListener
from akris_desktop.handle_set_listener import HandleSetListener
from akris_desktop.timeline_view import DuplicateMessageException

logger = logging.getLogger("akris_desktop")


class App(tk.Frame):
    def __init__(self, root=None, api_client=None, options=None):
        super().__init__(root)
        try:
            with importlib.resources.path("akris_desktop", "images") as resource_path:
                ico = Image.open(os.path.join(resource_path, "locust_icon.png"))
                photo = ImageTk.PhotoImage(ico)
                root.wm_iconphoto(False, photo)
        except FileNotFoundError:
            logger.exception("icon file missing.")
        self.disable_multipart = options.disable_multipart
        self.remote_station = options.remote_station
        self.handle = None
        self.root = root
        self.root.title("Akris")
        self.root.configure(bg="black")
        self.configure(bg="black")
        self.api_client = api_client
        self.message_detail = None
        self.new_handle_listener = NewHandleListener(self)
        self.new_ref_link_listener = NewRefLinkListener(self)
        self.handle_set_listener = HandleSetListener(self)
        self.message_listeners = []
        self.direct_tabs = []
        self.ref_link_tabs = []
        self.message_stats = None
        self.pack(fill=tk.BOTH, expand=True)
        root.protocol("WM_DELETE_WINDOW", self.on_close)

        # create notebook
        style = ttk.Style()
        style.configure("TNotebook", background="#333232", bordercolor="black")
        style.configure("TNotebook.Tab", background="#2C2A2A", foreground="darkgray")
        style.map(
            "TNotebook.Tab",
            background=[("selected", "#333232")],
            foreground=[("selected", "white")],
        )
        self.notebook = ttk.Notebook(self, style="TNotebook")
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # create main tab
        self.broadcast_tab = BroadcastTab(self.root, self)
        self.broadcast_tab.configure(bg="black")
        self.notebook.add(self.broadcast_tab, text="broadcast messages")
        self.console_tab = tk.Frame(self.root)
        self.console_tab.configure(bg="black")
        self.notebook.add(self.console_tab, text="console")

        # setup console tab
        self.console_frame = tk.Frame(self.console_tab)
        self.console_frame.pack(fill=tk.BOTH, expand=True)
        self.console = Console(self.console_frame, self.api_client)

        # register message listeners
        self.register_message_listener(self.console)
        self.register_message_listener(self.new_handle_listener)
        self.register_message_listener(self.new_ref_link_listener)
        self.register_message_listener(self.handle_set_listener)
        self.register_message_listener(MessageStatsListener(self))
        self.api_client.send_command({"command": "message_stats", "args": []})
        self.api_client.send_command({"command": "version_info", "args": []})
        self.api_client.send_command({"command": "knob", "args": ["handle"]})
        self.api_client.send_command({"command": "report_presence", "args": []})

    def add_direct_message_tab(self, handle):
        # check if tab already exists
        for tab in self.direct_tabs:
            if tab.handle == handle:
                self.notebook.select(tab)
                return
        dm_tab = DirectTab(self.root, handle, self)
        self.direct_tabs.append(dm_tab)
        self.notebook.insert(1, dm_tab, text=handle)
        return dm_tab

    def add_ref_link_tab(self, message_hash):
        # check if tab already exists
        for tab in self.ref_link_tabs:
            if tab.message_hash == message_hash:
                self.notebook.select(tab)
                return
        ref_link_tab = RefLinkTab(self.root, message_hash, self)
        self.ref_link_tabs.append(ref_link_tab)
        self.notebook.insert(1, ref_link_tab, text=ref_link_tab.title())
        self.notebook.select(ref_link_tab)
        return ref_link_tab

    def open_direct_message_tab(self, handle):
        tab = self.add_direct_message_tab(handle)
        self.notebook.select(tab)

    def close_ref_link_tab(self, tab):
        self.ref_link_tabs.remove(tab)
        self.notebook.forget(tab)
        self.unregister_message_listener(tab.message_table)
        self.notebook.select(self.broadcast_tab)

    def close_tab(self, tab):
        self.direct_tabs.remove(tab)
        self.notebook.forget(tab)
        self.unregister_message_listener(tab.message_table)
        self.notebook.select(self.broadcast_tab)

    def register_message_listener(self, listener):
        self.message_listeners.append(listener)

    def unregister_message_listener(self, listener):
        self.message_listeners.remove(listener)

    def check_message_queue(self):
        # check the queue and perform actions if needed
        if not self.api_client.message_queue.empty():
            while not self.api_client.message_queue.empty():
                message = self.api_client.message_queue.get()
                for listener in self.message_listeners:
                    try:
                        listener.render_message(message)
                    except DuplicateMessageException:
                        pass

    def run(self):
        self.check_message_queue()
        self.root.after(
            100, self.run
        )  # schedule the function to be called again in 1 second

    def on_close(self):
        logger.info("closing")
        self.root.destroy()
        self.root.quit()
        if not self.remote_station:
            self.api_client.shutdown_station()
            return

        self.api_client.disconnect()
