import datetime
import time


class PageMonitor:
    def __init__(self):
        self.days_before = 1

    def in_window(self, message):
        now = time.time()
        ts = message.get("timestamp")
        if (
            ts
            >= (
                datetime.datetime.fromtimestamp(now)
                - datetime.timedelta(days=self.days_before)
            ).timestamp()
        ):
            return True

    def button_label(self):
        return f"《 prev {self.days_before + 1} days"
