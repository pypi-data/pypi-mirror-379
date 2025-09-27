import datetime
import time

from .timeline_view import TimelineView


class DirectView(TimelineView):
    def __init__(self, root, handle, app, tab):
        self.handle = handle
        self.tab = tab
        super().__init__(root, app)

    def minimum_days_before(self):
        latest_ts = self.app.message_stats.get("direct_message_timestamps", {}).get(
            self.handle
        )
        if not latest_ts:
            return 1
        latest_message_date = datetime.datetime.fromtimestamp(latest_ts)
        now = datetime.datetime.now()
        return (now - latest_message_date).days + 1

    def render_message(self, message):
        # check for duplicates
        super().render_message(message)

        if message.get("ref_link_page_response"):
            return

        # is this a direct_text?
        if message.get("command") not in ["direct_text", "direct_text_m"]:
            return

        # is this the right dm tab?
        if not (
            message.get("handle") == self.handle
            or message.get("speaker") == self.handle
        ):
            return

        # if this is a realtime message or get_data response, update the window if it's in range
        self.update_window(message)

        # is this a realtime message or get_data response?
        if not message.get("page_response"):
            return

        # add message to filter and render
        self.filter[message.get("message_hash")] = True
        self.add_message(message)

    def load_page(self, command):
        if command == "page_up":
            self.app.api_client.send_command(
                {
                    "command": command,
                    "args": [time.time(), self.page_monitor.days_before, self.handle],
                }
            )

    def update_window(self, message):
        if not message.get("page_response"):
            if self.page_monitor.in_window(message):
                self.should_refresh_window = True
