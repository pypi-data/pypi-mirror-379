import re
import tkinter as tk
from functools import partial
from ..timeline_view import remove_unicode_surrogates

class SearchResult:
    def __init__(self, record):
        (
            self.speaker,
            self.recipient_handle,
            self.body,
            self.base64_message_hash
         ) = record

class Search:
    def __init__(self, output, api_client):
        self.output = output
        self.search_results = {}
        self.api_client = api_client
        self.output.tag_bind("message_hash", "<Button-1>", partial(self.on_message_hash_click, "message_hash"))
        self.output.tag_bind(
            "message_hash", "<Enter>", (lambda e: self.output.config(cursor="hand2"))
        )
        self.output.tag_bind(
            "message_hash", "<Leave>", (lambda e: self.output.config(cursor="xterm"))
        )

    def render(self, search_results):
        if len(search_results.get("body")) == 0:
            self.insert_text("No results\n")

        for search_result in search_results.get("body"):
            self.render_search_result(SearchResult(search_result))

    def on_message_hash_click(self, tag, event):
        tag_range = event.widget.tag_prevrange(tag, "current + 1 char")
        assert tag_range
        start, end = tag_range
        message_hash = event.widget.get(start, end).rstrip()
        search_result = self.search_results[message_hash]
        if search_result.recipient_handle:
            args = [message_hash, search_result.recipient_handle]
        else:
            args = [message_hash]
        self.api_client.send_command(
            {"command": "page_around", "args": args}
        )

    def render_search_result(self, search_result):
        self.search_results[search_result.base64_message_hash] = search_result
        self.output.character_insertion_index = 0
        self.render_message_hash(search_result.base64_message_hash)
        self.render_speaker(search_result.speaker)
        self.render_body(search_result.body)
        # line_index = int(self.output.index(tk.END).split(".")[0])
        # self.output.tag_add("error", f"{int(line_index)-2}.0", self.output.index(tk.END))

    def render_message_hash(self, message_hash):
        self.insert_text(
            f"{message_hash}",
            ("message_hash",),
        )

    def render_speaker(self, speaker):
        justified_speaker = f"{speaker:>{20}}"
        self.insert_text(
            f"{justified_speaker} | ",
        )

    def render_body(self, body):
        body = remove_unicode_surrogates(body)
        positions = self.replace_search_terms(body)
        self.insert_text(
            f"{positions.get('body')}\n",
            ("body",),
        )
        for position in positions["positions"]:
            self.tag_search_terms(position)

    def tag_search_terms(self, position):
        self.output.tag_add(
            "search_term",
            position["match_start"],
            position["match_end"],
        )

    def replace_search_terms(self, body):
        line_index = int(self.output.index(tk.END).split(".")[0]) - 1
        positions = []
        pattern = r'<<([^<>]+)>>'
        match = re.search(pattern, body)
        while match:
            body = re.sub(pattern, r'\1', body, count=1)
            positions.append({
                "match_start": f"{line_index}.{self.output.character_insertion_index + match.start()}",
                "match_end": f"{line_index}.{self.output.character_insertion_index + match.start() + len(match.group(1))}",
            })
            match = re.search(pattern, body)
        return {
            "body": body,
            "positions": positions,
        }

    def insert_text(self, text, tags=()):
        self.output.configure(state="normal")
        line_index = self.output.index(tk.END).split(".")[0]
        self.output.insert(
            self.get_insertion_index(line_index),
            text,
            tags,
        )
        self.output.configure(state="disabled")
        self.output.character_insertion_index += len(text)

    def get_insertion_index(self, line_index):
        return "{}.{}".format(line_index, self.output.character_insertion_index)
