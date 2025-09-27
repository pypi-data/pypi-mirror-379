import tkinter as tk


class Knob:
    def __init__(self, output):
        self.output = output

    def render(self, response):
        knobs = response.get("body")
        for key, value in knobs.items():
            self.render_knob("{}:\t{}".format(key, value))

    def render_knob(self, knob):
        self.output.configure(state="normal")
        self.output.insert(tk.END, "{}\n".format(knob))
        self.output.configure(state="disabled")
