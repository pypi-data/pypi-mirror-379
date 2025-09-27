import tkinter as tk

from .ref_link_view import RefLinkView


class RefLinkTab(tk.Frame):
    def __init__(self, root, message_hash, app):
        super().__init__(root)
        self.toolbar_frame = tk.Frame(self, background="#333232")
        self.close_link = tk.Label(
            self.toolbar_frame,
            text="🗙",
            fg="white",
            cursor="hand2",
            background="red",
        )
        self.close_link.pack(side=tk.RIGHT)
        self.close_link.bind("<Button-1>", lambda e: self.app.close_ref_link_tab(self))
        # self.close_button = ttk.Button(self.toolbar_frame, text="close", command=lambda: self.app.close_ref_link_tab(self))
        # self.close_button.pack(side=tk.RIGHT)
        self.toolbar_frame.pack(side=tk.TOP, fill=tk.X)
        self.message_hash = message_hash
        self.app = app
        self.messages_frame = tk.Frame(self)
        self.messages_frame.pack(fill=tk.BOTH, expand=True)
        self.message_table = RefLinkView(self.messages_frame, app, message_hash, self)
        self.app.register_message_listener(self.message_table)

    def title(self):
        title = self.message_table.title
        if not title:
            return self.message_hash[0:15]
        return title
