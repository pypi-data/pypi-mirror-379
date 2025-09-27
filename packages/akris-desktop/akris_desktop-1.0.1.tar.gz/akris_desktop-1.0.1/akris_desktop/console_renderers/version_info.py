import tkinter as tk


class VersionInfo:
    def __init__(self, output):
        self.output = output

    def render(self, response):
        akris_version = response.get("version")
        pest_version = response.get("pest_version")
        earliest_supported_pest_version = response.get(
            "earliest_supported_pest_version"
        )
        body = (
            "Welcome to the Akris Desktop Pest console!\n\n"
            f"Akris station version: {akris_version}\n"
            f"Pest version: {hex(pest_version)}\n"
            f"Minimum pest version: {hex(earliest_supported_pest_version)}\n\n"
            f"Enter a pest command below or type help for a list of supported commands.\n\n"
        )

        self.output.configure(state="normal")
        self.output.insert(tk.END, body)
        self.output.configure(state="disabled")
