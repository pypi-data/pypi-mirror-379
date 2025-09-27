import importlib
import os
import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk
from akris_desktop.console_renderers.at import At
from akris_desktop.console_renderers.default import Default
from akris_desktop.console_renderers.error import Error
from akris_desktop.console_renderers.help import Help
from akris_desktop.console_renderers.knob import Knob
from akris_desktop.console_renderers.search import Search
from akris_desktop.console_renderers.version_info import VersionInfo
from akris_desktop.console_renderers.wot import Wot


class Console(tk.Frame):
    def __init__(self, root, api_client):
        super().__init__(root)
        self.root = root
        self.history = []
        self.history_index = 0
        self.frame = tk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.api_client = api_client
        self.output = tk.Text(
            self.frame, wrap=tk.WORD, highlightthickness=0, padx=10, pady=10
        )
        self.configure_scrollbar_style()
        self.scrollbar = ttk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.output.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.output.yview)
        self.output.character_insertion_index = 0
        self.output.configure(state="disabled")
        self.output.configure(background="black", foreground="green")
        self.output.pack(fill=tk.BOTH, expand=True)

        # Setup the context menus
        self.output_context_menu = tk.Menu(self.output, tearoff=0)
        self.configure_output_context_menu()

        self.entry = tk.Entry(self.frame, highlightthickness=0)
        self.entry.configure(
            insertbackground="green", background="black", foreground="green"
        )
        self.entry.pack(fill=tk.X)

        # Setup the entry context menus
        self.entry_context_menu = tk.Menu(self.output, tearoff=0)
        self.configure_entry_context_menu()


        # Bind events to the widget
        self.entry.bind("<Return>", self.handle_enter)
        self.entry.bind("<Up>", self.handle_up_arrow)
        self.entry.bind("<Down>", self.handle_down_arrow)

        # Setup tags:
        self.output.tag_configure("error", foreground="red")
        self.output.tag_configure("search_term", font=tk.font.Font(size=11, weight="bold"))
        lmargin2 = tk.font.Font(size=11).measure("nGsDUOHFRCmP0mG1h/KCDOSLM3hY4KBxthI2XF6B7D4=              awt | ")
        self.output.tag_configure("body", lmargin2=lmargin2)

        try:
            with importlib.resources.path("akris_desktop", "images") as images_path:
                self.insert_image(os.path.join(images_path, "pixelated_green_flag.png"))
            self.insert_message({"body": "\n\n"})
        except FileNotFoundError:
            pass

        # Setup renderers:
        self.renderers = {
            "at": At(self.output),
            "error": Error(self.output),
            "help": Help(self.output),
            "knob": Knob(self.output),
            "search": Search(self.output, self.api_client),
            "version_info": VersionInfo(self.output),
            "wot": Wot(self.output),
        }

    def render_message(self, message):
        if message["command"] == "console_response":
            self.renderers.get(message.get("type"), Default(self.output)).render(
                message
            )
            self.output.see(tk.END)

    def configure_entry_context_menu(self):
        self.entry_context_menu.add_command(
            label="Paste", command=lambda: self.handle_entry_context_menu_paste()
        )
        self.entry_context_menu.bind("<Leave>", lambda e: self.entry_context_menu.unpost())
        self.entry.bind("<Button-3>", self.show_entry_context_menu)

    def show_entry_context_menu(self, event):
        self.entry_context_menu.post(event.x_root, event.y_root)

    def handle_entry_context_menu_paste(self):
        content = self.root.clipboard_get()
        self.entry.insert(tk.INSERT, content)

    def configure_output_context_menu(self):
        self.output_context_menu.add_command(
            label="Copy", command=lambda: self.copy_output_selected_text()
        )
        self.output_context_menu.bind("<Leave>", lambda e: self.output_context_menu.unpost())
        self.output.bind("<Button-3>", self.show_output_context_menu)

    def copy_output_selected_text(self):
        # Get the selected text
        selected_text = self.output.get("sel.first", "sel.last")

        # Copy the selected text to the clipboard
        self.output.clipboard_clear()
        self.output.clipboard_append(selected_text)

    def show_output_context_menu(self, event):
        self.output_context_menu.post(event.x_root, event.y_root)

    def configure_scrollbar_style(self):
        style = ttk.Style()
        style.theme_use("default")
        style.configure(
            "TScrollbar",
            foreground="darkgray",
            troughcolor="black",
            background="darkgray",
            arrowcolor="white",
            bordercolor="black",
        )
    def insert_message(self, message):
        self.output.configure(state="normal")
        self.output.insert(tk.END, message["body"])
        self.output.configure(state="disabled")

    def insert_image(self, image_path):
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        self.output.image_create("insert", image=photo)
        self.output.image = photo


    def handle_enter(self, event):
        if event.state == 0:
            # Handle Enter key (send message)
            self.execute_command()
        return "break"

    def handle_up_arrow(self, event):
        # if the index is 0, do nothing
        # Get the clipboard content and insert it into the Text widget
        if len(self.history) > 0:
            self.entry.delete("0", tk.END)
            self.entry.insert("0", self.history[self.history_index])
            if self.history_index > 0:
                self.history_index -= 1

    def handle_down_arrow(self, event):
        # Get the clipboard content and insert it into the Text widget
        self.entry.delete("0", tk.END)
        if self.history_index < len(self.history) - 1:
            self.history_index += 1
            self.entry.insert("0", self.history[self.history_index])

    def execute_command(self):
        # Get the text from the text entry widget
        command_string = self.entry.get()
        args = command_string.split(" ")[1:]
        command = command_string.split(" ")[0]
        if command == "search":
            args = [" ".join(args)]
        if command == "searchs":
            args = command_string.split(" ")[2:]
            speaker = command_string.split(" ")[1]
            args = [speaker, " ".join(args)]

        # Log the command to the command history
        self.history.append(command_string)
        self.history_index = len(self.history) - 1

        # Clear the text entry widget
        self.entry.delete("0", tk.END)

        self.insert_message({"body": "> " + command_string + "\n"})
        self.api_client.send_command({"command": command, "args": args})

    def configure_scrollbar_style(self):
        pass
