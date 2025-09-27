import tkinter as tk
from .message_entry import MessageEntry, count_bytes


class DirectMessageEntry(MessageEntry):
    def __init__(self, root, app, handle):
        super().__init__(root, app)
        self.handle = handle

    def handle_slash_command(self, message):
        if message.startswith("/close"):
            self.app.close_tab(self.root)
            # Clear the text entry widget
            self.text.delete("1.0", tk.END)

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
                    {"command": "direct_text_m", "args": [self.handle, message]}
                )
                return

        self.app.api_client.send_command(
            {"command": "direct_text", "args": [self.handle, message]}
        )
