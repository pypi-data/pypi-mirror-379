class NewRefLinkListener:
    def __init__(self, app):
        self.app = app

    def render_message(self, message):
        if not message.get("ref_link_page_response"):
            return

        if message.get("ref_link_hash") not in [
            self.app.notebook.tab(t, "text") for t in self.app.ref_link_tabs
        ]:
            self.app.add_ref_link_tab(message.get("ref_link_hash"))
