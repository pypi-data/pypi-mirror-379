from .timeline_view import TimelineView, MultipartMessage


class RefLinkView(TimelineView):
    def __init__(self, root, app, message_hash, tab):
        super().__init__(root, app)
        self.tab = tab
        self.title = None
        self.message_hash = message_hash
        self.text.tag_configure("reflink_highlight", foreground="black", background="#FAF182")

    def render_message(self, message):
        super().render_message(message)

        if not message.get("ref_link_page_response"):
            return

        if self.message_hash != message.get("ref_link_hash"):
            return

        if message.get("command") == "broadcast_text_m":
            self.filter[message.get("message_hash")] = True
            if not message.get("text_hash") in self.multipart_staging:
                self.multipart_staging[message.get("text_hash")] = MultipartMessage(
                    message
                )
            else:
                self.multipart_staging[message.get("text_hash")].add_part(message)

            multipart_message = self.multipart_staging[message.get("text_hash")]
            if multipart_message.is_complete():
                message["body"] = multipart_message.assembled_body()
                del self.multipart_staging[message.get("text_hash")]
            else:
                return

        # set the title from the linked message
        if message.get("message_hash") == self.message_hash:
            self.title = message.get("body")[0:15]
            self.app.notebook.tab(self.tab, text=self.title)

        if self.is_hearsay(message):
            message["hearsay"] = True

        self.filter[message.get("message_hash")] = True
        self.add_message(message)

        if message.get("end"):
            self.text.see(f"{self.highlighed_line_index}.0")

    def highlight_line(self, line_index):
        self.text.tag_add("reflink_highlight", f"{line_index}.0", f"{line_index + 1}.0")
        self.text.see(f"{line_index}.0")

    def add_message(self, message):
        super().add_message(message)
        if message.get("message_hash") == self.message_hash:
            line_index = self.timeline.calculate_message_index(message)
            self.highlighed_line_index = line_index
            self.highlight_line(line_index)
