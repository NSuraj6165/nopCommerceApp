import logging
class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger(__name__)
        filehandler = logging.FileHandler("Logs\\automation.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger