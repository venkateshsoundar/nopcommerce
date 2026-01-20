import logging

class Log_Maker:

    @staticmethod
    def log_generator():
        logging.basicConfig(filename=".\\logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',force=True)
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger 