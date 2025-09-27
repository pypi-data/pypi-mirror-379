import tkinter as tk


class Wot:
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
        if peer.get("address") and peer.get("port"):
            address = "{}:{}".format(peer.get("address"), peer.get("port"))
        else:
            address = "<address not configured>"
        self.output.configure(state="normal")
        self.output.insert(
            tk.END, "{}\t{}\n".format(" ".join(peer.get("handles")), address)
        )
        if len(peer.get("keys")) > 0:
            for key in peer.get("keys"):
                self.output.insert(tk.END, "\t{}\n".format(key))
        self.output.configure(state="disabled")

    def render_no_peers(self):
        self.output.configure(state="normal")
        self.output.insert(tk.END, "No peers found.\n")
        self.output.configure(state="disabled")
