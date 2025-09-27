import datetime
import re
import time
import tkinter as tk
from tkinter import ttk
import webbrowser
from functools import partial
from tkinter.font import Font
from akris.log_config import LogConfig

from .page_monitor import PageMonitor
from .text_utils import colorize
from .timeline import Timeline, Annotation, BEFORE

logger = LogConfig.get_instance().get_logger("akris_desktop.timeline_view")


# "unicode surrogates" seen in at least one message from phf - origin and purpose
# as yet unclear, but can't be rendered by the Text
def remove_unicode_surrogates(json_string):
    return re.sub(
        r"[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF\u2600-\u26FF\u2700-\u27BF\U000024C2-\U0001F251]",
        "X",
        json_string,
    )


def indexize(index):
    return str(float(index))


def is_new_day(timestamp1, timestamp2):
    # Convert the timestamps to datetime objects
    dt1 = datetime.datetime.fromtimestamp(timestamp1)
    dt2 = datetime.datetime.fromtimestamp(timestamp2)

    # Return True if the dates are different, False otherwise
    return dt1.date() != dt2.date()


class DuplicateMessageException(Exception):
    pass


class CustomText(tk.Text):
    def __init__(self, *args, scroll_handler=None, **kwargs):
        self.scroll_handler = scroll_handler
        super().__init__(*args, **kwargs)

    def yview(self, *args):
        self.scroll_handler(*args)
        return super().yview(*args)


class MultipartMessage:
    def __init__(self, message):
        self.parts = [message]
        self.of = message.get("of")

    def add_part(self, message):
        for part in self.parts:
            if message.get("n") < part.get("n"):
                self.parts.insert(self.parts.index(part), message)
                return
        self.parts.append(message)

    def is_complete(self):
        return len(self.parts) == self.of

    def assembled_body(self):
        body = ""
        for part in self.parts:
            body += part.get("body")
        return body


class TimelineView(tk.Frame):
    def __init__(self, root, app):
        super().__init__(root)
        self.message_at_index = {}
        self.root = root
        self.app = app
        self.timeline = Timeline()
        self.frame = tk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.text = CustomText(
            self.frame,
            wrap=tk.WORD,
            highlightthickness=0,
            padx=10,
            pady=10,
            scroll_handler=self.handle_scroll,
            borderwidth=0,
        )
        self.configure_scrollbar_style()
        self.scrollbar = ttk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Associate the Scrollbar with the Text widget
        self.text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text.yview)

        self.text.configure(state="disabled")
        self.text.pack(fill=tk.BOTH, expand=True)
        self.text.configure(
            background="black", foreground="white", font=("Courier New", 10)
        )
        self.context_menu = tk.Menu(root, tearoff=0)
        self.configure_context_menu()

        # tooltip display
        self.tooltip_label = None

        # configuration
        self.configure_tags()
        self.configure_bindings()

        self.character_insertion_index = 0

        # we need to keep track of this in order to determine when
        # to move to the end after receiving a new non page_response
        # message
        self.hit_bottom = True
        self.hit_top = False

        # paging
        self.filter = {}
        self.should_refresh_window = True
        self.page_monitor = PageMonitor()

        # for assembly of multipart messages
        self.multipart_staging = {}

    def show_tooltip(self, text):
        if self.tooltip_label:
            self.hide_tooltip()
        self.tooltip_label = tk.Label(self.root, fg="black", background="white", borderwidth=1, height=1, padx=0, pady=0)
        self.tooltip_label.place(x=0, y=0)
        self.tooltip_label.config(text=text, width=len(text))

    def hide_tooltip(self):
        if self.tooltip_label:
            self.tooltip_label.place_forget()
            self.tooltip_label.destroy()
            self.tooltip_label = None

    def await_message_stats(self):
        while not self.app.message_stats:
            self.root.after(100, self.await_message_stats)
            return
        self.page_monitor.days_before = self.minimum_days_before()
        self.tab.more_link.config(text=self.page_monitor.button_label())
        self.start_refresh_loop()

    def minimum_days_before(self):
        latest_ts = self.app.message_stats.get("latest_broadcast_message_timestamp")
        if not latest_ts:
            return 1
        latest_message_date = datetime.datetime.fromtimestamp(latest_ts)
        now = datetime.datetime.now()
        return (now - latest_message_date).days + 1

    def start_refresh_loop(self):
        if self.should_refresh_window:
            self.should_refresh_window = False
            self.load_page("page_up")

        self.root.after(500, self.start_refresh_loop)

    def render_message(self, message):
        if self.filter.get(message.get("message_hash")):
            raise DuplicateMessageException()

    def load_previous(self):
        self.hit_top = False
        self.page_monitor.days_before += 1
        self.tab.more_link.config(text=self.page_monitor.button_label())
        self.should_refresh_window = True

    def load_page(self, command):
        if command == "page_up":
            # Get the line number of the first visible line
            self.app.api_client.send_command(
                {
                    "command": command,
                    "args": [time.time(), self.page_monitor.days_before],
                }
            )

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

    def configure_tags(self):
        lmargin = tk.font.Font(family="Courier New", size=11).measure(
            "[08:05:35]   asciilifeform | "
        )
        self.text.tag_configure(
            "speaker", font=Font(family="Courier New", weight="bold")
        )
        self.text.tag_configure(
            "text", font=Font(family="Courier New"), lmargin2=lmargin
        )
        self.text.tag_configure(
            "highlight_speaker", foreground="#E3ED1C", background="#D60D93"
        )
        self.text.tag_configure("ref_link", underline=True)
        self.text.tag_configure("url", underline=True)
        self.text.tag_configure("multiline_header", font=("", "11", "bold italic"))
        self.text.tag_configure("date_break", foreground="#1CEAED")
        self.text.tag_configure("timestamp", foreground="#B9BFC0")
        self.text.tag_configure("highlight", background="#D60D93")
        self.text.tag_configure("hearsay", foreground="#F6D12D")

    def configure_bindings(self):
        self.text.tag_bind(
            "ref_link", "<Button-1>", partial(self.on_ref_link_leftclick, "ref_link")
        )
        self.text.tag_bind(
            "ref_link", "<Enter>", (lambda e: self.text.config(cursor="hand2"))
        )
        self.text.tag_bind(
            "ref_link", "<Leave>", (lambda e: self.text.config(cursor="xterm"))
        )
        self.text.tag_bind("url", "<Button-1>", partial(self.on_link_leftclick, "url"))
        self.text.tag_bind(
            "url", "<Enter>", (lambda e: self.text.config(cursor="hand2"))
        )
        self.text.tag_bind(
            "url", "<Leave>", (lambda e: self.text.config(cursor="xterm"))
        )
        self.text.tag_bind(
            "timestamp", "<Enter>", (lambda e: self.text.config(cursor="hand2"))
        )
        self.text.tag_bind(
            "timestamp", "<Leave>", (lambda e: self.text.config(cursor="xterm"))
        )
        self.text.tag_bind(
            "multiline_header", "<Enter>", (lambda e: self.text.config(cursor="hand2"))
        )
        self.text.tag_bind(
            "multiline_header", "<Leave>", (lambda e: self.text.config(cursor="xterm"))
        )
        self.text.tag_bind("timestamp", "<Button-1>", (lambda e: self.copy_ref_link(e)))
        self.text.tag_bind("multiline_header", "<Button-1>", (lambda e: self.copy_ref_link(e)))
        self.text.bind("<Prior>", self.handle_page_up)

    def configure_context_menu(self):
        self.context_menu.add_command(
            label="Copy", command=lambda: self.copy_selected_text()
        )
        self.context_menu.bind("<Leave>", lambda e: self.context_menu.unpost())
        self.text.bind("<Button-3>", self.show_context_menu)

    def copy_ref_link(self, event):
        index = int(event.widget.index(f"@{event.x},{event.y}").split(".")[0])
        self.root.clipboard_clear()
        line = self.text.get(f"{index}.0", f"{index}.end")
        logger.info(line)
        message = self.message_at_index.get(index)
        self.root.clipboard_append(f"pest://{message.get('message_hash')}")

    def handle_scroll(*args):
        self = args[0]
        if len(args) == 3:
            if args[1] == "moveto":
                pos = self.text.yview()
                if pos[0] == 0.0:
                    if not self.hit_top:
                        self.hit_top = True
                if pos[1] == 1.0:
                    if not self.hit_bottom:
                        self.hit_bottom = True
                        self.hit_top = False
                else:
                    self.hit_bottom = False

    def get_insertion_index(self, line_index):
        return "{}.{}".format(line_index, self.character_insertion_index)

    def insert_text(self, text, line_index, tags=()):
        self.inserting_text = True
        self.text.configure(state="normal")
        self.text.insert(
            self.get_insertion_index(line_index),
            text,
            tags,
        )
        self.text.configure(state="disabled")
        self.character_insertion_index += len(text)

        def not_inserting():
            self.inserting_text = False

        self.root.after(500, not_inserting)

    def render_timestamp(self, timestamp, line_index, message):
        message_info_tag = f"message-info-{message.get('message_hash')}"
        tags = ["timestamp", message_info_tag]
        if message.get("hearsay"):
            tags.append("hearsay")
        msg_datetime = datetime.datetime.fromtimestamp(timestamp).strftime("%H:%M:%S")
        self.insert_text("[{}] ".format(msg_datetime), line_index, tags)
        self.bind_reporting_peers_tooltip(message_info_tag, message)

    def bind_reporting_peers_tooltip(self, message_info_tag, message):
        reporting_peers = message.get("reporting_peers")
        if reporting_peers:
            formatted_reporting_peers = ", ".join(reporting_peers)
            self.text.tag_bind(message_info_tag, "<Enter>", partial(self.on_timestamp_enter, formatted_reporting_peers))
            self.text.tag_bind(message_info_tag, "<Leave>", self.on_timestamp_leave)

    def render_speaker(self, message, is_action, line_index):
        if is_action:
            speaker = "*"
        else:
            speaker = message.get("speaker")
        body = message.get("body")
        tags = ["speaker"]
        justified_speaker = f"{speaker:>{15}}"
        if not is_action:
            self.text.tag_configure("colorize_" + speaker, foreground=colorize(speaker))
        if self.app.handle in body and not self.app.handle == message.get("speaker"):
            tags.append("highlight_speaker")
        else:
            tags.append("colorize_" + speaker)
        self.insert_text(
            justified_speaker,
            line_index,
            tags,
        )

    def render_divider(self, line_index):
        tags = []
        self.insert_text(
            " | ",
            line_index,
            tags,
        )

    def render_body(self, message, line_index):
        formatted_body = remove_unicode_surrogates(message.get("body"))
        self.insert_text(
            f"{formatted_body}\n",
            line_index,
            ("text",),
        )

    def extract_action_message(self, speaker, body):
        pattern = r"\x01ACTION (.*?)\x01"
        match = re.search(pattern, body)
        if match:
            return f"{speaker} {match.group(1)}"
        else:
            return body

    def render_annotation(self, annotation, line_index):
        self.character_insertion_index = 0
        self.insert_text(f"{annotation.content}\n", line_index, ("text", "date_break"))

    def render_multiline_header(self, message, line_index):
        self.character_insertion_index = 0
        ts = message.get("timestamp")
        msg_date = datetime.datetime.fromtimestamp(ts).strftime("%m/%d")
        msg_time = datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S")

        message_info_tag = f"message-info-{message.get('message_hash')}"
        tags = ["text", "multiline_header", message_info_tag]
        if message.get("hearsay"):
            tags.append("hearsay")
        self.insert_text(
            f"On {msg_date} at {msg_time} {message.get('speaker')} wrote:\n",
            line_index,
            tags,
        )
        reporting_peers = message.get("reporting_peers")
        if reporting_peers:
            formatted_reporting_peers = ", ".join(reporting_peers)
            self.text.tag_bind(message_info_tag, "<Enter>", partial(self.on_timestamp_enter, formatted_reporting_peers))
            self.text.tag_bind(message_info_tag, "<Leave>", self.on_timestamp_leave)

    def render_multiline(self, message, line_index):
        start = indexize(line_index + 1)
        body = message.get("body")
        lines = body.split("\n")
        for i, line in enumerate(lines):
            self.character_insertion_index = 0
            url_info = self.replace_bracket_pairs(line_index + i + 1, line)
            line_body = url_info.get("body")
            self.insert_text(f"{line_body}\n", line_index + i + 1, ("text",))
            self.tag_bracket_pairs(url_info)
        end = self.text.index(self.get_insertion_index(line_index + len(lines) + 1))
        self.find_and_tag_ref_links(self.text, start, end)
        self.find_and_tag_urls(self.text, start, end)

    def render_line(self, message, line_index):
        # initialize character insertion index
        self.character_insertion_index = 0
        is_action = False
        start = indexize(line_index)
        if "\x01" in message.get("body"):
            message["body"] = self.extract_action_message(
                message.get("speaker"), message.get("body")
            )
            is_action = True
        self.render_timestamp(message.get("timestamp"), line_index, message)
        self.render_speaker(message, is_action, line_index)
        self.render_divider(line_index)
        url_info = self.replace_bracket_pairs(line_index, message.get("body"))
        message["body"] = url_info.get("body")
        self.render_body(message, line_index)
        self.tag_bracket_pairs(url_info)

        end = self.text.index(self.get_insertion_index(line_index))

        self.find_and_tag_ref_links(self.text, start, end)
        self.find_and_tag_urls(self.text, start, end)
        self.reposition(message)

    def add_message(self, message):
        self.add_date_change(message.get("timestamp"))
        index = self.timeline.add_message(message)
        self.message_at_index[index] = message
        if "\n" in message.get("body"):
            self.render_multiline_header(message, index)
            self.render_multiline(message, index)
        else:
            self.render_line(message, index)

    def remove_message(self, message):
        logger.info("*********************** remove_message()")
        logger.info(message)
        index = self.timeline.calculate_message_index(message)
        line_count = self.timeline.get_line_count(message)
        self.text.configure(state="normal")
        self.text.delete(
            indexize(index),
            indexize(index + line_count),
        )
        self.text.configure(state="disabled")

    def add_date_change(self, timestamp):
        antecedent_timestamp = self.timeline.get_antecedent_timestamp(timestamp)
        decedent_timestamp = self.timeline.get_decedent_timestamp(timestamp)
        if antecedent_timestamp:
            if is_new_day(antecedent_timestamp, timestamp):
                self.insert_date_change(timestamp)
        if decedent_timestamp:
            if is_new_day(timestamp, decedent_timestamp):
                self.insert_date_change(decedent_timestamp)

    def insert_date_change(self, timestamp):
        if not self.timeline.annotated(timestamp):
            date = datetime.datetime.fromtimestamp(timestamp).strftime("%A, %B %d, %Y")
            annotation = Annotation(timestamp, f"--- {date} ---", BEFORE)
            self.remove_existing_annotation(annotation)
            annotation_index = self.timeline.add_annotation(annotation)
            self.render_annotation(annotation, annotation_index)

    def remove_existing_annotation(self, annotation):
        existing_annotation = self.timeline.get_annotation(annotation.content)
        if existing_annotation:
            existing_annotation_index = self.timeline.calculate_annotation_index(
                existing_annotation
            )
            self.delete_line(existing_annotation_index)
            self.timeline.remove_annotation(existing_annotation)

    def delete_line(self, line_index):
        self.text.configure(state="normal")
        start = f"{line_index}.0"
        end = f"{line_index + 1}.0"
        self.text.delete(start, end)
        self.text.configure(state="disabled")

    # handle positioning after receiving page responses
    def reposition(self, message):
        if not self.hit_bottom:
            return

        if self.hit_top:
            if not message.get("end"):
                return

        self.text.see("end")

    def find_and_tag_ref_links(self, textwidget: tk.Text, start: str, end: str) -> None:
        search_start = start
        while True:
            match_start = textwidget.search(
                r"\mpest://[a-zA-Z0-9=/+]", search_start, end, nocase=True, regexp=True
            )
            if not match_start:
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
            textwidget.tag_add("ref_link", match_start, match_end)
            search_start = f"{match_end} + 1 char"

    def replace_bracket_pairs(self, line_index, body):
        positions = []

        def url_replacer(m):
            url = m.group(1)
            text = m.group(2)

            positions.append(
                {
                    "url": url,
                    "match_start": f"{line_index}.{self.character_insertion_index + match.start()}",
                    "match_end": f"{line_index}.{self.character_insertion_index + match.start() + len(text)}",
                    "tag_name": f"url-{url}",
                }
            )
            return text

        pattern = r'\[([^\[\]]+?)\]\[([^\[\]]+?)\]'
        match = re.search(pattern, body)
        while (match):
            body = re.sub(pattern, url_replacer, body, count=1)
            match = re.search(pattern, body)
        return {
            "body": body,
            "positions": positions
        }

    def tag_bracket_pairs(self, url_info):
        positions = url_info.get("positions")
        for position in positions:
            self.text.tag_add("url", position.get("match_start"), position.get("match_end"))
            self.text.tag_add(position.get("tag_name"), position.get("match_start"), position.get("match_end"))
            if position.get("url").startswith("pest://"):
                self.text.tag_bind(position.get("tag_name"), "<Button-1>",
                                   partial(self.on_named_ref_link_click, position.get("url")))
            else:
                self.text.tag_bind(position.get("tag_name"), "<Button-1>",
                                   partial(self.on_named_link_click, position.get("url")))
            self.text.tag_bind(position.get("tag_name"), "<Enter>", partial(self.on_link_enter, position.get("url")))
            self.text.tag_bind(position.get("tag_name"), "<Leave>", self.on_link_leave)

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

    def on_ref_link_leftclick(self, tag, event):
        tag_range = event.widget.tag_prevrange(tag, "current + 1 char")
        assert tag_range
        start, end = tag_range
        text = event.widget.get(start, end)
        message_hash = text.split("pest://")[1]
        self.app.api_client.send_command(
            {"command": "page_around", "args": [message_hash]}
        )

    def on_named_ref_link_click(self, url, event):
        message_hash = url.split("pest://")[1]
        self.app.api_client.send_command(
            {"command": "page_around", "args": [message_hash]}
        )

    def on_named_link_click(self, url, event):
        webbrowser.open(url)

    def on_link_leftclick(self, tag, event):
        # To test this, set up 3 URLs, and try clicking first and last char of middle URL.
        # That finds bugs where it finds the wrong URL, or only works in the middle of URL, etc.
        tag_range = event.widget.tag_prevrange(tag, "current + 1 char")
        assert tag_range
        start, end = tag_range
        text = event.widget.get(start, end)
        webbrowser.open(text)

    def copy_selected_text(self):
        # Get the selected text
        selected_text = self.text.get("sel.first", "sel.last")

        # Copy the selected text to the clipboard
        self.text.clipboard_clear()
        self.text.clipboard_append(selected_text)

    def show_context_menu(self, event):
        self.context_menu.post(event.x_root, event.y_root)

    def handle_page_up(self, event):
        self.text.yview_scroll(-1, "pages")
        if self.text.yview()[0] == 0.0:
            pass

    def highlight_line(self, line_index):
        self.text.tag_add("highlight", f"{line_index}.0", f"{line_index + 1}.0")

    def on_link_enter(self, url, event):
        self.show_tooltip(url)

    def on_link_leave(self, event):
        self.hide_tooltip()

    def on_timestamp_enter(self, reporting_peers, event):
        self.show_tooltip(reporting_peers)

    def on_timestamp_leave(self, event):
        self.hide_tooltip()

    def is_hearsay(self, message):
        if message.get("immediate"):
            return False

        if message.get("speaker") == self.app.handle:
            return False

        return True
