import tkinter as tk


class Peers(tk.Frame):
    def __init__(self, root, app):
        self.app = app
        self.frame = tk.Frame(
            root, borderwidth=0, highlightthickness=0, width=200, background="black"
        )
        self.frame.pack(side=tk.RIGHT, fill=tk.Y)

        # peer list
        self.peer_list = tk.Text(
            self.frame, highlightthickness=0, borderwidth=0, width=20
        )
        self.peer_list.configure(background="black", foreground="white")
        self.peer_list.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True, padx=10, pady=10)
        self.peer_list.config(state="disabled")
        self.peer_list.config(cursor="arrow")
        self.peer_list.tag_config("offline", font=("", "12", "italic"))
        self.peer_list.tag_config("online", font=("", "12"))
        self.peer_list.tag_bind("clickable", "<Button-1>", self.on_peer_click)
        self.peer_list.tag_bind(
            "clickable", "<Enter>", (lambda e: self.peer_list.config(cursor="hand2"))
        )
        self.peer_list.tag_bind(
            "clickable", "<Leave>", (lambda e: self.peer_list.config(cursor="xterm"))
        )

    def on_peer_click(self, event):
        # Get the index of the mouse pointer
        index = self.peer_list.index("@%s,%s" % (event.x, event.y))

        # Get the line number
        line_number = index.split(".")[0]

        # Get the line text
        handle = self.peer_list.get(f"{line_number}.0", f"{line_number}.end")
        print("clicked on peer: %s" % handle)
        self.app.open_direct_message_tab(handle)

    def render_message(self, message):
        self.peer_list.config(state="normal")
        if message["command"] == "presence":
            handle = message["handle"]
            if not handle in self.peer_list.get("1.0", tk.END).splitlines():
                self.peer_list.insert(tk.END, handle + "\n")
                self.tag_peer(handle, "clickable")
            if message["type"] == "online":
                self.tag_peer(handle, "online")
            elif message["type"] == "offline":
                self.tag_peer(handle, "offline")
            else:
                self.remove_peer(handle)
        self.peer_list.config(state="disabled")

    def tag_peer(self, handle, tag):
        peer_index = self.get_peer_index(handle)
        if peer_index:
            if tag == "offline":
                self.peer_list.tag_remove("online", peer_index, peer_index + "+1l")
                self.peer_list.tag_add("offline", peer_index, peer_index + "+1l")
            elif tag == "online":
                self.peer_list.tag_remove("offline", peer_index, peer_index + "+1l")
                self.peer_list.tag_add("online", peer_index, peer_index + "+1l")
            else:
                self.peer_list.tag_add(tag, peer_index, peer_index + "+1l")

    def get_peer_index(self, handle):
        for i, peer in enumerate(self.get_peers()):
            if peer == handle:
                return str(float(i) + 1.0)
        return None

    def get_peers(self):
        peers = self.peer_list.get("1.0", tk.END).splitlines()
        if len(peers) > 0:
            return peers[:-1]
        return []

    def remove_peer(self, handle):
        peer_index = self.get_peer_index(handle)
        self.peer_list.delete(peer_index, peer_index + "+1l")
