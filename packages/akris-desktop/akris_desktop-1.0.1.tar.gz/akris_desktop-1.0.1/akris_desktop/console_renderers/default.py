import tkinter as tk


class Default:
    def __init__(self, output):
        self.output = output
        pass

    def render(self, response):
        if response.get("body"):
            self.output.configure(state="normal")
            self.output.insert(tk.END, "{}\n".format(response.get("body")))
            self.output.configure(state="disabled")
