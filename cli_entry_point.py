#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lib import g910_gkey_mapper
import argparse
import os
from pathlib import Path
from lib.misc import create_config
from lib.misc import paths
from lib.misc import logger
from daemonize import Daemonize


log = logger.logger("launcher")


def main():
    parser = argparse.ArgumentParser(description="Support for Logitech G910 GKeys on Linux")
    parser.add_argument("--create-config", help="Creates config in "+paths.config_path, action='store_true', default=False)
    args = parser.parse_args()
    if args.create_config:
        create_config.create()
    else:
        if not paths.does_pid_exits():
            print("Starting g910-gkeys, logging at:", paths.logs_path)
            Daemonize(app="g910-keys", pid=paths.pid_path, action=g910_gkey_mapper.main, keep_fds=[logger.fh.stream.fileno()]).start()
        else:
            print("g910-keys daemon already exists on pid:",paths.read_pid())
            print("if you made sure that the program isn't running ('ps -p "+paths.read_pid()+" -o comm=' returns nothing) then manually remove pid file:")
            print()
            print("    rm "+paths.pid_path)
            print()
if __name__=="__main__":
    main()
