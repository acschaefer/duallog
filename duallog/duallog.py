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


# Define the default logging directory.
defaultdir = 'log'


def setup(logdir=defaultdir):
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
    logdir = logdir.strip().rstrip('\\/') + '/'
    if not logdir:
        logdir = defaultdir

    # Create a folder for the logfiles.
    if not os.path.exists(logdir):
        os.mkdir(logdir)

    # Construct the logfile name.
    t = datetime.datetime.now()
    logfile = '{logdir}{year:04d}{mon:02d}{day:02d}-' \
        '{hour:02d}{min:02d}{sec:02d}.log'.format(
            logdir=logdir, year=t.year, mon=t.month, day=t.day, 
            hour=t.hour, min=t.minute, sec=t.second)

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
    logdir = 'logtest'
    setup(logdir)

    # Generate some log messages.
    logging.warning(
        'This function illustrates how to use the duallog package.')
    logging.warning(
        'All messages are sent to both the console and a logfile in the folder '
        '\"{}\".'.format(logdir))
    logging.warn(
        'The logfile\'s name encodes the time when the program was started.')
    logging.warning(
        'The duallog package treats different log levels differently.')
    logging.debug(
        'Debug messages like this are written to the logfile, but not printed '
        'on screen.')
    logging.info(
        'Info messages like this get the same treatment.')
    logging.warning(
        'Warn messages like this one are important. '
        'They are both sent to the logfile and shown on screen.')
    logging.error(
        'The same holds for error messages like this one ...')
    logging.critical(
        '... and for critical messages, of course.')
    logging.warning(
        'Have a look at the debug and info messages the logfile in the folder '
        '\"{}\".'.format(logdir))
    logging.warning(
        'They are not sent to the screen in order not to clutter the display.')
    