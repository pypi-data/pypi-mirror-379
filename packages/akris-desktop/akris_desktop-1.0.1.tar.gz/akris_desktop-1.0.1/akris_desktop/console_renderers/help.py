import tkinter as tk


class Help:
    def __init__(self, output):
        self.output = output

    def render(self, response):
        help_dict = response.get("body")
        for key, value in help_dict.items():
            self.render_help(value["help"])

    def render_help(self, error):
        self.output.configure(state="normal")
        self.output.insert(tk.END, "{}\n".format(error))
        self.output.configure(state="disabled")
