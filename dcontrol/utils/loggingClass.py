import logging


class LoggingClass:
    __slots__ = ['_log']

    @property
    def log(self):
        try:
            return self._log
        except AttributeError:
            self._log = logging.getLogger(self.__class__.__name__)
            return self._log