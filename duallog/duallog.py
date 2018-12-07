#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Duallog

This module contains a function "setup()" that sets up dual logging. All 
subsequent log messages are sent both to the console and to a logfile. Log
messages are generated via the "logging" package.

Example:
    >>> import duallog
    >>> import logging
    >>> duallog.setup('mylogs')
    >>> logging.info('Test message')

If run, this module illustrates the usage of the duallog package.
"""


# Import required standard libraries.
import os
import logging
import datetime

def setup(logdir='log'):
    """ Set up dual logging to console and to logfile.

    When this function is called, it first creates the given directory. It then 
    creates a logfile and passes all log messages to come to it. The logfile
     name encodes the date and time when it was created, for example 
    "20181115-153559.txt". All messages with a log level of at least "warn" are
    also forwarded to the console.

    Args:
        logdir (str): path of the directory where to store the log files. Both a
            relative or an absolute path may be specified. If a relative path is
            specified, it is interpreted relative to the working directory.
            If no directory is given, the logs are written to a folder called 
            "log" in the working directory. 
    """

    # Validate the given directory.
    logdir = os.path.normpath(logdir)

    # Create a folder for the logfiles.
    if not os.path.exists(logdir):
        os.makedirs(logdir)

    # Construct the logfile name.
    t = datetime.datetime.now()
    logfile = '{year:04d}{mon:02d}{day:02d}-' \
        '{hour:02d}{min:02d}{sec:02d}.log'.format(
            year=t.year, mon=t.month, day=t.day, 
            hour=t.hour, min=t.minute, sec=t.second)
    logfile = os.path.join(logdir, logfile)

    # Set up logging to the logfile.
    logging.basicConfig(format='%(asctime)s %(levelname)-8s: %(message)s',
                        level=logging.DEBUG,
                        filename=logfile,
                        filemode='w')

    # Set up logging to the console.
    console = logging.StreamHandler()
    console.setLevel(logging.WARNING)
    formatter = logging.Formatter('%(levelname)s: %(message)s')
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)


if __name__ == '__main__':
    """Illustrate the usage of the duallog package."""

    # Set up dual logging.
    logdir = 'log'
    setup(logdir)

    # Generate some log messages.
    logging.debug('Debug messages are only sent to the logfile.')
    logging.info('Info messages are not shown on the console, too.')
    logging.warning('Warnings appear both on the console and in the logfile.')
    logging.error('Errors get the same treatment.')
    logging.critical('And critical messages, of course.')
