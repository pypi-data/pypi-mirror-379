#!/usr/bin/env python3

import time
import os
import logging
import tkinter as tk
import argparse

PEST_HOST = "0.0.0.0"
PEST_PORT = 8080
API_HOST = "127.0.0.1"
API_PORT = 8081
AKRIS_DATA_PATH = os.path.join(os.path.expanduser("~"), ".akris")
AKRIS_DATABASE_NAME = "akris.db"


def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pest-host", default=PEST_HOST, help="pest station host")
    parser.add_argument("--api-host", default=API_HOST, help="api service host")
    parser.add_argument("--pest-port", default=PEST_PORT, type=int, help="pest station port")
    parser.add_argument("--api-port", default=API_PORT, type=int, help="api service port")
    parser.add_argument("--akris-data-path", default=AKRIS_DATA_PATH, help="path at which to locate persistent Akris data")
    parser.add_argument("--akris-database-name", default=AKRIS_DATABASE_NAME, help="name to use for the Akris database file")
    parser.add_argument("--disable-multipart", action='store_true', default=False, help="disable sending multipart messages")
    parser.add_argument("--remote-station", action='store_true', default=False, help="connect to a remote station rather than spinning up a local one")
    return parser.parse_args()


def main():
    """Main entry point for akris-desktop command."""
    options = get_options()

    from akris.log_config import LogConfig
    LogConfig(data_path=options.akris_data_path).get_logger("akris_desktop.main")
    from akris.station import Station
    from akris import client
    from akris_desktop.app import App

    logging.basicConfig(level=logging.INFO)

    if not options.remote_station:
        station = Station(
            tcp_host=options.api_host,
            tcp_port=options.api_port,
            udp_port=options.pest_port,
            host=options.pest_host,
            data_path=options.akris_data_path,
            database_name=options.akris_database_name,
        )
        station.start()
        while not station.ready():
            time.sleep(0.1)

    c = client.Client(host=options.api_host, port=int(options.api_port))
    root = tk.Tk()
    root.configure(bg="black")
    app = App(root, c, options=options)
    app.run()
    root.mainloop()
    if not options.remote_station:
        station.stop()


if __name__ == '__main__':
    main()