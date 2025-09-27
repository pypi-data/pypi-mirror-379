import re
import tkinter as tk

from akris_desktop import emojis


def bytes_for_char_utf_8(c):
    return len(c.encode("utf-8"))


def count_bytes(s):
    b = 0
    total = 0
    for i, c in enumerate(s):
        cs = bytes_for_char_utf_8(c)
        total += cs
    return total


class MessageEntry(tk.Frame):
    def __init__(self, root, app):
        self.root = root
        self.app = app

        # Create a resizable pane with vertical orientation
        self.frame = tk.Frame(root)
        self.frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.placehodler_text = "Write a message..."

        # Create a ScrolledText widget
        self.text = tk.Text(
            self.frame, wrap=tk.WORD, height=5, highlightthickness=0, padx=10, pady=10
        )
        self.text.configure(
            insertbackground="white", background="#333232", foreground="white"
        )
        self.text.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Add placeholder text
        self.text.insert(tk.END, self.placehodler_text)
        self.text.config(foreground="gray")

        self.context_menu = tk.Menu(root, tearoff=0)
        self.text.bind("<Button-3>", self.show_context_menu)
        self.configure_context_menu()

        # Bind events to the widget
        self.text.bind("<FocusIn>", self.on_entry_click)
        self.text.bind("<FocusOut>", self.on_focus_out)
        self.text.bind("<Return>", self.handle_enter)
        self.text.bind("<Tab>", self.autocomplete)
        self.text.bind("<Control-v>", self.handle_paste)

    def configure_context_menu(self):
        self.context_menu.add_command(
            label="Paste", command=lambda: self.handle_context_menu_paste()
        )
        self.context_menu.bind("<Leave>", lambda e: self.context_menu.unpost())

    def show_context_menu(self, event):
        self.context_menu.post(event.x_root, event.y_root)

    def handle_context_menu_paste(self):
        content = self.root.clipboard_get()
        clean_content = emojis.decode(content)
        self.text.insert(tk.INSERT, clean_content)

    def on_entry_click(self, event):
        if self.text.get("1.0", "end-1c") == self.placehodler_text:
            self.text.delete("1.0", tk.END)
            self.text.config(foreground="white")

    def on_focus_out(self, event):
        if self.text.get("1.0", "end-1c") == "":
            self.text.insert(tk.END, self.placehodler_text)
            self.text.config(foreground="#ECECEC")

    def ignore_enter(self, event):
        return "break"

    def handle_enter(self, event):
        if not (event.state & 1):  # Check if Shift is NOT pressed
            # Handle Enter key (send message)
            self.send_message()
        else:
            self.insert_new_line()
        return "break"

    def insert_new_line(self):
        # Insert a new line character at the current cursor position
        self.text.insert(tk.INSERT, "\n")

    def autocomplete(self, event) -> None:
        cursor_pos = self.text.index("insert")
        match = re.fullmatch(
            r"(.*\s)?([^\s:]+):? ?", self.text.get("0.0", self.text.index(tk.INSERT))
        )
        if match is None:
            return "break"
        preceding_text, last_word = match.groups()  # preceding_text can be None

        nicks = self.app.broadcast_tab.peers.get_peers()
        if last_word in nicks:
            completion = nicks[(nicks.index(last_word) + 1) % len(nicks)]
        else:
            try:
                completion = next(
                    username
                    for username in nicks
                    if username.lower().startswith(last_word.lower())
                )
            except StopIteration:
                return "break"

        if preceding_text:
            new_text = preceding_text + completion + " "
        else:
            new_text = completion + ": "
        self.text.delete("0.0", cursor_pos)
        self.text.insert("0.0", new_text)
        self.text.mark_set("insert", str(float(len(new_text))))
        return "break"

    def handle_paste(self, event):
        content = self.root.clipboard_get()
        clean_content = emojis.decode(content)
        self.text.insert(tk.INSERT, clean_content)
        return "break"

    def encode_action(self, message):
        pattern = r"\x01ACTION (.*?)\x01"
        if message.startswith("/me"):
            if len(message.encode("utf-8")) <= 325:
                pattern = r"^/me(.*)"
                match = re.search(pattern, message)
                if match:
                    predicate = match.group(1)
                    action_message = re.sub(pattern, f"\x01ACTION{predicate}\x01", message, count=1)
                    return action_message
        return message