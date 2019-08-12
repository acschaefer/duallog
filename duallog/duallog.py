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


# Import required standard packages.
import datetime
import logging.handlers
import os


def setup(logdir='log', logname='log', minlevel=logging.WARNING, lformat=None):
    """ Set up dual logging to console and to logfile.

    When this function is called, it first creates the given directory. It then 
    creates a logfile and passes all log messages to come to it. The logfile
    name encodes the date and time when it was created, for example 
    "20181115-153559.txt". All messages with a log level of at least "WARNING" 
    are also forwarded to the console.

    Args:
        logdir: path of the directory where to store the log files. Both a
            relative or an absolute path may be specified. If a relative path is
            specified, it is interpreted relative to the working directory.
            If no directory is given, the logs are written to a folder called 
            "log" in the working directory. 
        logname: name of the log. Default 'log'. Will be attached at the start
            of the log filename followed by a dash char. For example: logname='test', the log file will
            be something like: test-20190227...
        minlevel: It defines the minlevel of the messages that will be shown on 
            the console. Default is WARNING. 
    """

    # Create the root logger.
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Validate the given directory.
    logdir = os.path.normpath(logdir)
    
    # if output directory is an existing file
    if os.path.isfile(logdir):
        logger.critical("Output directory is an existing file")
        raise FileExistsError
    # Create a folder for the logfiles.
    if not os.path.exists(logdir):
        os.makedirs(logdir)

    # Logfile name format
    if lformat is None:
        lformat = '{name}-{year:04d}{mon:02d}{day:02d}-' \
            '{hour:02d}{min:02d}{sec:02d}.log'

    # Construct the logfile name.
    t = datetime.datetime.now()
    logfile = lformat.format(
        year=t.year, mon=t.month, day=t.day,
        hour=t.hour, min=t.minute, sec=t.second, name=logname)
    logfile = os.path.join(logdir, logfile)

    # Set up logging to the logfile.
    filehandler = logging.handlers.RotatingFileHandler(
        filename=logfile,
        maxBytes=10 * 1024 * 1024,
        backupCount=100)
    filehandler.setLevel(logging.DEBUG)
    fileformatter = logging.Formatter(
        '%(asctime)s %(levelname)-8s: %(message)s')
    filehandler.setFormatter(fileformatter)
    logger.addHandler(filehandler)

    # Set up logging to the console.
    streamhandler = logging.StreamHandler()
    streamhandler.setLevel(minlevel)
    streamformatter = logging.Formatter('%(levelname)s: %(message)s')
    streamhandler.setFormatter(streamformatter)
    logger.addHandler(streamhandler)


if __name__ == '__main__':
    """Illustrate the usage of the duallog package.
    """

    # Set up dual logging.
    logdir = 'log'
    setup(logdir)

    # Generate some log messages.
    logging.debug('Debug messages are only sent to the logfile.')
    logging.info('Info messages are not shown on the console, too.')
    logging.warning('Warnings appear both on the console and in the logfile.')
    logging.error('Errors get the same treatment.')
    logging.critical('And critical messages, of course.')
