# Debugging and Exceptions 
## Catching exceptions   
    try: 
        ... 
    except <Exception>: 
        ...

## Raising exceptions 
    raise <Exception> 

## Writing tracebacks out to files 
import traceback
Get the error trace with `traceback.format_exc()`

## Assertions 
For programmer errors!

    assert <boolean condition>, <message to display on failure>

Disable using `-O` option when running program.

## Logging 

Basic syntax (Log messages will print to console.)

    import logging 
    # Specify the lowest level messages you want to see, and the format of log messages.
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
    logging.debug(<message>)
    # After this line, Disable all log messages lower than critical: 
    logging.disable(loggig.CRITICAL)

To log to a file:

    logging.basicConfig(filename=<filename>, level=<logging level>, format=<format>)
