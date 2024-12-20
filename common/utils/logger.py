from abc import ABCMeta, abstractmethod
from singleton_metaclass import SingletonMeta
import logging


class SingletonABCMeta(ABCMeta, SingletonMeta):
    def __new__(cls, name, bases, namespace):
        return super().__new__(cls, name, bases, namespace)


class BaseLogger(metaclass=SingletonABCMeta):
    @abstractmethod
    def debug(self, message: str):
        pass

    @abstractmethod
    def info(self, message: str):
        pass

    @abstractmethod
    def warning(self, message: str):
        pass

    @abstractmethod
    def error(self, message: str):
        pass

    @abstractmethod
    def critical(self, message: str):
        pass


class Logger(BaseLogger):
    def __init__(self):
        print('<Logger init> initializing logger...')
        self._logger = logging.getLogger('my_logger')
        self._logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler('my_log_file.log')
        file_handler.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        self._logger.addHandler(file_handler)
        self._logger.addHandler(console_handler)

    def debug(self, message: str):
        self._logger.debug(message)

    def info(self, message: str):
        self._logger.info(message)

    def warning(self, message: str):
        self._logger.warning(message)

    def error(self, message: str):
        self._logger.error(message)

    def critical(self, message: str):
        self._logger.critical(message)
