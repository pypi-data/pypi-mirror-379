from akris.log_config import LogConfig

logger = LogConfig.get_instance().get_logger("akris_desktop.broadcast_view")

from .timeline_view import TimelineView, MultipartMessage


class BroadcastView(TimelineView):
    def __init__(self, root, app, tab):
        super().__init__(root, app)
        self.tab = tab
        self.root = root

    def render_message(self, message):
        super().render_message(message)

        if message.get("ref_link_page_response"):
            return

        if message.get("command") == "message_update":
            # if we already have this message we need to remove it and update it when the page refresh arrives
            if self.page_monitor.in_window(message):
                if message.get("message_hash") in self.filter:
                    self.remove_message(message)
                    del self.filter[message.get("message_hash")]
                    self.should_refresh_window = True

        if message["command"] not in ["broadcast_text", "broadcast_text_m"]:
            return

        # if this is a realtime message or get_data response, check if we should refresh the window
        if not message.get("page_response") and not message.get(
            "ref_link_page_response"
        ):
            if self.page_monitor.in_window(message):
                self.should_refresh_window = True
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

        if self.is_hearsay(message):
            message["hearsay"] = True

        # track only messages that are page responses
        self.filter[message.get("message_hash")] = True
        self.add_message(message)
