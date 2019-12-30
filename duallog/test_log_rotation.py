#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test script for the duallog module.

Checks whether log rotation works properly.
"""


# Import required packages.
import logging
import duallog

# Modify duallog log rotation parameters.
duallog.maxBytes = 100*1024
duallog.backupCount = 10


# Write many log messages to file to test log rotation.
duallog.setup('logtest')

for n in range(1, 50000):
    logging.error('This is test log message no. {:05d}.'.format(n))
