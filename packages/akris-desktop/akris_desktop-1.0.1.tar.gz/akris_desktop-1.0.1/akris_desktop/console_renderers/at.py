import tkinter as tk


class At:
    def __init__(self, output):
        self.output = output

    def render(self, response):
        peers = response.get("body")
        if len(peers) == 0:
            self.render_no_peers()
        else:
            for peer in response.get("body"):
                self.render_peer(peer)

    def render_peer(self, peer):
        self.output.configure(state="normal")
        self.output.insert(
            tk.END,
            "{}\t{}\t{}\n".format(
                peer.get("handle"), peer.get("address"), peer.get("active_at")
            ),
        )
        self.output.configure(state="disabled")

    def render_no_peers(self):
        self.output.configure(state="normal")
        self.output.insert(tk.END, "No peers found.\n")
        self.output.configure(state="disabled")
