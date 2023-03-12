from patterns import Singleton
import logging

class Logger(metaclass=Singleton)
    logging.basicConfig(level=logging.INFO, filename="py_log.log",
        format="%(asctime)s %(levelname)s %(message)s")

    def log(self, message):
        self.logging.error("ERROR: " + message)
