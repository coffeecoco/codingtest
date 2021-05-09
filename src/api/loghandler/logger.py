import os
import traceback
import logging
from pythonjsonlogger import jsonlogger



class _Registry:
    initialized = False
    logger = None


def unset_logger():
    del _Registry.logger
    _Registry.initialized = False


def get_logger(id=None):
    """ Setup and return common logger
        Logging level defaults to 'INFO' and is controlled by
        'LOG_LEVEL' environment variable
    """
    if _Registry.initialized:
        return _Registry.logger
    if id:
        logging.basicConfig(filename="{}".format(id), filemode="a")
        print("Logging to {}".format(id))
    logger = logging.getLogger()
    level = os.environ.get("LOGLEVEL", "INFO")
    logger.setLevel(logging.getLevelName(level))

    log_keys = [
        "message",
        "levelname",
    ]
    if not logger.handlers:
        logger.addHandler(logging.StreamHandler())
    for h_logger in logger.handlers:
        h_logger.setFormatter(
            jsonlogger.JsonFormatter(
                " ".join(["%({0:s})".format(k) for k in log_keys]), timestamp=True
            )
        )

    logging_defaults = {}


    # mark as initialized
    _Registry.initialized = True
    _Registry.logger = logging.LoggerAdapter(logger, logging_defaults)

    return _Registry.logger


def debug(message, id=None):
    get_logger(id).debug(message)


def info(message, id=None):
    get_logger(id).info(message)


def warn(message, id=None):
    get_logger(id).warning(message)


def log_error(message, id=None):
    get_logger(id).error(message)


def log_exception(message, id=None):
    """
    Logs error message and last exception stack trace with ERROR
    log level
    :param message:
    :return:
    """
    get_logger().error(message)
    get_logger().error(traceback.format_exc())
