# The duallog package

Python package to enable simultaneous logging to console and logfile.

## How to install duallog?

You can install duallog using [pip](https://www.w3schools.com/python/python_pip.asp), or you can install from source.
Below you find instructions for both ways.

### Installation via `pip`

In the terminal, run `pip install duallog`.

### Installation from source

1. Download and unpack this repository.
2. Open a terminal and navigate to the repository. 
3. Execute `python setup.py install` from within the repository.

## How to use duallog?

Using duallog is very simple, as illustrated in the following minimal example script.

```python
# Import the duallog package to set up simultaneous logging to screen and console.
import duallog

# Import the logging package to generate log messages.
import logging

# Set up dual logging and tell duallog where to store the logfiles.
duallog.setup('logtest')

# Generate some log messages.
logging.warn('This function illustrates how to use the duallog package.')
logging.warn('All messages are sent to both the console and a logfile in the folder \"{}\".'.format(logdir))
logging.warn('The logfile\'s name encodes the time when the program was started.')
logging.warn('The duallog package treats different log levels differently.')
logging.debug('Debug messages like this are written to the logfile, but not printed on screen.')
logging.info('Info messages like this get the same treatment.')
logging.warn('Warn messages like this one are important. They are both sent to the logfile and shown on screen.')
logging.error('The same holds for error messages like this one ...')
logging.critical('... and for critical messages, of course.')
logging.warn('Have a look at the debug and info messages the logfile in the folder \"{}\".'.format(logdir))
logging.warn('They are not sent to the screen in order not to clutter the display.')
```

The corresponding output on the console and in the logfile looks like this:

![](./duallog_screenshot.png)
[Duallog screenshot](https://github.com/acschaefer/duallog/blob/master/duallog_screenshot.png)
