import logging

class LogGen:
    @staticmethod

    def loggen():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        logging.basicConfig(filename="C://UmaRaniDundigalla//UmaRani_workspace//GUVI//Guvi_Projects//GUVI_Project2//Logs//OrangeHRM_1.log",
                            format = '%(asctime)s:%(levelname)s:%(message)s')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

