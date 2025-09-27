import tkinter as tk
from .message_entry import MessageEntry, count_bytes


class BroadcastMessageEntry(MessageEntry):
    def __init__(self, root, app):
        super().__init__(root, app)

    def handle_slash_command(self, message):
        pass

    def send_message(self):
        # Get the text from the text entry widget
        message = self.text.get("1.0", tk.END).rstrip("\n")
        if message[0] == "/":
            message = self.encode_action(message)

        # Clear the text entry widget
        self.text.delete("1.0", tk.END)

        if not self.app.disable_multipart:
            # count the number of bytes in the message body
            # if necessary send a multipart message
            if count_bytes(message) > 324:
                self.app.api_client.send_command(
                    {"command": "broadcast_text_m", "args": [message]}
                )
                return

        self.app.api_client.send_command(
            {"command": "broadcast_text", "args": [message]}
        )
