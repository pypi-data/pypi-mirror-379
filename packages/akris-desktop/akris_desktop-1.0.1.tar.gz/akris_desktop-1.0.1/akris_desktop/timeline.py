import bisect
from akris.log_config import LogConfig

logger = LogConfig.get_instance().get_logger("akris.timeline")

BEFORE = 0
AFTER = 1


class Annotation:
    def __init__(self, timestamp, content, position=AFTER):
        self.content = content
        self.timestamp = timestamp
        self.position = position


class TimestampGroup:
    def __init__(self):
        self.messages = []

    def add_message(self, new_message):
        # sort results with identical timestamps by message hash
        # this is kind of a heuristic because messages with identical timestamps are not
        # guaranteed to be descendents or antecedents of one another
        added = False
        for existing_message in self.messages:
            # if new_message is a descendent of message
            if existing_message.get("message_hash") in [
                new_message.get("net_chain"),
                new_message.get("self_chain"),
            ]:
                self.messages.append(new_message)
                added = True
                break

            # new_message is an antecedent of message
            if new_message["message_hash"] in [
                existing_message.get("net_chain"),
                existing_message.get("self_chain"),
            ]:
                self.messages.insert(self.messages.index(existing_message), new_message)
                added = True
                break
        if not added:
            self.messages.append(new_message)

    def count(self):
        message_count = len(self.messages)
        newline_count = 0
        multiline_header_count = 0
        for message in self.messages:
            newline_count += message.get("body").count("\n")

        # we must account for the multiline message headers as well
        for message in self.messages:
            if message.get("body").count("\n") > 0:
                multiline_header_count += 1

        return message_count + newline_count + multiline_header_count

    def newlines_before(self, message):
        message_index = self.messages.index(message)
        newline_count = 0
        for message in self.messages[:message_index]:
            newline_count += message.get("body").count("\n")
        return newline_count


class Timeline:
    def __init__(self):
        self.ordered_timestamps = []
        self.annotations = {}
        self.timestamp_groups = {}

    def get_line_count(self, message):
        if "\n" in message.get("body"):
            return 0

        # need to add one for the header
        return message.get("body").count("\n") + 1

    def calculate_message_index(self, message):
        ts = message.get("timestamp")
        tsg = self.get_timestamp_group(ts)

        index = 0
        index += self.antecedent_timestamp_group_count(ts)
        index += tsg.messages.index(message)
        index += tsg.newlines_before(message)
        index += self.count_annotations_before_ts_group(ts)

        # Text indexing starts at 1
        index += 1
        return index

    def calculate_annotation_index(self, annotation):
        ts = annotation.timestamp
        index = 0
        index += self.antecedent_timestamp_group_count(ts)
        index += self.count_earlier_annotations(ts)
        if annotation.position == AFTER:
            index += self.get_timestamp_group(ts).count()

        # Text indexing starts at 1
        index += 1
        return index

    def antecedent_timestamp_group_count(self, timestamp):
        count = 0
        for ts in self.timestamp_groups:
            if ts < timestamp:
                count += self.timestamp_groups[ts].count()
        return count

    def get_antecedent_timestamp(self, timestamp):
        previous_ts = None
        for ts in self.ordered_timestamps:
            if ts < timestamp:
                previous_ts = ts
        return previous_ts

    def get_decedent_timestamp(self, timestamp):
        decedent_ts = None
        for ts in reversed(self.ordered_timestamps):
            if ts > timestamp:
                decedent_ts = ts
        return decedent_ts

    def add_message(self, message):
        ts = message["timestamp"]
        if ts not in self.ordered_timestamps:
            bisect.insort(self.ordered_timestamps, ts)
        tsg = self.get_timestamp_group(ts)
        tsg.add_message(message)
        return self.calculate_message_index(message)

    def add_annotation(self, annotation):
        self.annotations[annotation.timestamp] = annotation
        return self.calculate_annotation_index(annotation)

    def remove_annotation(self, annotation):
        annotations_copy = self.annotations.copy()
        for ts in annotations_copy:
            if annotations_copy[ts].content == annotation.content:
                del self.annotations[ts]

    def annotated(self, timestamp):
        return self.annotations.get(timestamp)

    def get_annotation(self, content):
        for ts in self.annotations:
            if self.annotations[ts].content == content:
                return self.annotations[ts]

    def get_first_timestamp(self):
        return self.ordered_timestamps[0]

    def get_last_timestamp(self):
        return self.ordered_timestamps[-1]

    def get_timestamp_group(self, timestamp):
        if not self.timestamp_groups.get(timestamp):
            tsg = TimestampGroup()
            self.timestamp_groups[timestamp] = tsg
            return tsg
        else:
            return self.timestamp_groups[timestamp]

    def count_earlier_annotations(self, timestamp):
        count = 0
        for ts in self.annotations:
            if ts < timestamp:
                count += 1
        return count

    def count_annotations_before_ts_group(self, timestamp):
        count = 0
        for ts in self.annotations:
            if ts < timestamp:
                count += 1
        if self.annotations.get(timestamp):
            if self.annotations[timestamp].position == BEFORE:
                count += 1
        return count
