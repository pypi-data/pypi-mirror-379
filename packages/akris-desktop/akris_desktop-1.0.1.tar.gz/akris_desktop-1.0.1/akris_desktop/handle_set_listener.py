class HandleSetListener:
    def __init__(self, app):
        self.app = app

    def render_message(self, message):
        # set handle on init
        if message.get("command") in ["console_response"]:
            if message.get("name") == "handle":
                self.app.handle = message.get("value")
            return