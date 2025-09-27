import tkinter as tk


class Notifications(tk.Frame):
    def __init__(self, root, app, timeline_view):
        super().__init__(root, bg="black", borderwidth=0, height=30, pady=10, padx=0)
        self.app = app
        self.root = root
        self.timeline_view = timeline_view
        self.load_more_button = None

    def display_load_previous(self):
        if not self.load_more_button:
            self.load_more_button = tk.Button(
                self,
                text="more...",
                command=self.timeline_view.load_previous,
                height=1,
                pady=0,
                padx=0,
            )
            self.load_more_button.pack(side=tk.RIGHT)

    def clear(self):
        if self.load_more_button:
            self.load_more_button.destroy()
            self.load_more_button = None
