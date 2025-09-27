import tkinter as tk


class Error:
    def __init__(self, output):
        self.output = output

    def render(self, response):
        error = response.get("body")
        self.render_error(error)

    def render_error(self, error):
        self.output.configure(state="normal")
        self.output.tag_remove("sel", "1.0", tk.END)
        self.output.mark_set(tk.INSERT, tk.END)
        start = self.output.index(tk.INSERT)
        self.output.insert(tk.END, "{}\n".format(error))
        end = "{}.end".format(int(float(start)))
        self.output.tag_add("error", start, end)
        self.output.configure(state="disabled")
