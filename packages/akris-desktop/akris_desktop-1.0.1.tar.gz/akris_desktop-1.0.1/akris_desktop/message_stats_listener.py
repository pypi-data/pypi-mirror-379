class MessageStatsListener:
    def __init__(self, app):
        self.app = app

    def render_message(self, message):
        if message.get("command") in ["console_response"]:
            if message.get("type") == "message_stats":
                self.app.message_stats = {
                    "latest_broadcast_message_timestamp": message.get(
                        "latest_broadcast_message_timestamp"
                    ),
                    "direct_message_timestamps": message.get(
                        "direct_message_timestamps"
                    ),
                }
