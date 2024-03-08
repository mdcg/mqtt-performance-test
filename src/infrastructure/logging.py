import logging


class Logger:
    def __init__(self, module):
        self.module = module
        self.logger = self._get_logger()

    def _get_logger(self):
        logger = logging.getLogger(self.module)
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter(
                fmt="[%(name)s] %(asctime)s - %(levelname)s : %(message)s",
                datefmt="%d/%m/%Y %I:%M:%S %p",
            )
        )
        logger.addHandler(handler)
        return logger

    def info(self, message, **kwargs):
        self.logger.info(message, **kwargs)

    def error(self, message, **kwargs):
        self.logger.error(message, **kwargs)

    def debug(self, message, **kwargs):
        self.logger.debug(message, **kwargs)

    def warn(self, message, **kwargs):
        self.logger.warning(message, **kwargs)
