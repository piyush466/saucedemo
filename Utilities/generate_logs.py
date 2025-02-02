import logging

class LogGen:

    @staticmethod
    def loggenerates():
        logger = logging.getLogger("names")
        logger.setLevel(logging.DEBUG)
        filehandle = logging.FileHandler(r"tests.log")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        filehandle.setFormatter(formatter)
        logger.addHandler(filehandle)
        return logger



