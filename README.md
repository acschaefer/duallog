![Image showing logs](./duallog.jpg)

# The duallog package

Python package to enable simultaneous logging to console and logfile.

## How to install duallog?

To install the duallog package, perform the following two steps:
1. Download and unpack this repository.
2. From within the repository folder, run `python setup.py install`.

## How to use duallog?

Using duallog is very simple, as illustrated in the following minimal example script.

```python
# Import the duallog package to set up simultaneous logging to screen and console.
import duallog

# Import the logging package to generate log messages.
import logging

# Set up dual logging and tell duallog where to store the logfiles.
duallog.setup('mylogs')

# Generate log messages.
logging.debug('Debug messages like this are written to the logfile only.')
logging.info('The same is true for info messages.')
logging.warn('This helps the user focus on important messages, like this warn message ...')
logging.error('... or on this error message.')
logging.critical('All messages with levels of at least \"warn\" are written to both file and console.')
```
