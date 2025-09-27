import datetime
import tkinter as tk
import random
import webbrowser
from functools import partial
from tkinter.font import Font


class Master(tk.Frame):
    def __init__(self, root, app):
        self.app = app
        self.chain = app.timeline
        self.frame = tk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.table = tk.Text(
            self.frame, wrap=tk.WORD, highlightthickness=0, padx=10, pady=10
        )
        self.table.configure(state="disabled")
        self.table.tag_configure("speaker", font=Font(family="Courier New"))
        self.table.tag_config("text", font=Font(family="Courier New"), lmargin2=260)
        self.table.pack(fill=tk.BOTH, expand=True)
        self.table.configure(background="black", foreground="white")
        self.table.tag_configure("url", underline=True)
        self.table.tag_bind(
            "url", "<Button-1>", partial(self._on_link_leftclick, "url")
        )
        self.table.tag_bind(
            "url", "<Enter>", (lambda e: self.table.config(cursor="hand2"))
        )
        self.table.tag_bind(
            "url", "<Leave>", (lambda e: self.table.config(cursor="xterm"))
        )
        self.context_menu = tk.Menu(root, tearoff=0)
        self.context_menu.add_command(
            label="Copy", command=lambda: self.copy_selected_text()
        )
        self.context_menu.bind("<Leave>", lambda e: self.context_menu.unpost())
        self.table.bind("<Button-3>", self.show_context_menu)

    def insert(self, message, index):
        msg_datetime = datetime.datetime.fromtimestamp(message["timestamp"]).strftime(
            "%H:%M:%S"
        )
        self.table.configure(state="normal")
        start = index
        message["index"] = str(index)
        datetime_str = "[{}] ".format(msg_datetime)
        self.table.insert(index, datetime_str)
        speaker = f"{message['speaker']:>{15}}"
        self.table.tag_configure(
            "colorize_" + speaker, foreground=self.colorize(speaker)
        )
        self.table.insert(
            "{}.{}".format(int(float(index)), len(datetime_str)),
            speaker,
            ("speaker", "colorize_" + speaker),
        )
        body = "{}".format(
            ": " + message["body"],
        )
        self.table.insert(
            "{}.{}".format(int(float(index)), len(datetime_str) + len(speaker)),
            "{}{}".format(body, "\n"),
            ("text",),
        )
        end = self.table.index(tk.INSERT)
        self.table.configure(state="disabled")
        self.find_and_tag_urls(self.table, start, end)
        self.table.see(tk.END)

    def render_message(self, message):
        if message["command"] == "broadcast_text":
            # self.chain.add_message(message)
            # index = self.chain.index(message["message_hash"])
            # self.insert(message, index)
            pass

    def colorize(self, speaker):
        # Set the seed based on the peer name
        random.seed(speaker)

        # Generate random RGB values for lighter colors
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        # Generate the color code
        color_code = "#{:02X}{:02X}{:02X}".format(r, g, b)

        return color_code

    def find_and_tag_urls(self, textwidget: tk.Text, start: str, end: str) -> None:
        search_start = start
        while True:
            match_start = textwidget.search(
                r"\mhttps?://[a-z0-9:]", search_start, end, nocase=True, regexp=True
            )
            if not match_start:  # empty string means not found
                break

            url = textwidget.get(match_start, f"{match_start} lineend")

            url = url.split()[0]
            url = url.split("'")[0]
            url = url.split('"')[0]
            url = url.split("`")[0]

            # URL, and URL. URL? URL! (also URL). (also URL.)
            url = url.rstrip(".,?!")
            if "(" not in url:  # urls can contain spaces (e.g. wikipedia)
                url = url.rstrip(")")
            url = url.rstrip(".,?!")

            # [url][foobar]
            if "]" in url:
                pos = url.find("]")
                if pos < url.find("["):
                    url = url[:pos]

            match_end = f"{match_start} + {len(url)} chars"
            textwidget.tag_add("url", match_start, match_end)
            search_start = f"{match_end} + 1 char"

    def _on_link_leftclick(self, tag, event):
        # To test this, set up 3 URLs, and try clicking first and last char of middle URL.
        # That finds bugs where it finds the wrong URL, or only works in the middle of URL, etc.
        tag_range = event.widget.tag_prevrange(tag, "current + 1 char")
        assert tag_range
        start, end = tag_range
        text = event.widget.get(start, end)
        webbrowser.open(text)

    def copy_selected_text(self):
        # Get the selected text
        selected_text = self.table.get("sel.first", "sel.last")

        # Copy the selected text to the clipboard
        self.table.clipboard_clear()
        self.table.clipboard_append(selected_text)

    def show_context_menu(self, event):
        self.context_menu.post(event.x_root, event.y_root)
