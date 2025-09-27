class NewHandleListener:
    def __init__(self, app):
        self.app = app

    def render_message(self, message):
        if message.get("ref_link_page_response"):
            return

        if message["command"] in ["direct_text", "direct_text_m"]:
            handle = message.get("handle")
            if handle in self.app.broadcast_tab.peers.get_peers():
                if handle not in [
                    self.app.notebook.tab(t, "text") for t in self.app.direct_tabs
                ]:
                    self.app.add_direct_message_tab(handle)
