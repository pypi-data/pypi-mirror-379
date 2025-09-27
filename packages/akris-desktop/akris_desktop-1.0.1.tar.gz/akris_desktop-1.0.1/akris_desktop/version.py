import os

current_path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(current_path, "VERSION")) as version_file:
    VERSION = version_file.read().strip()
