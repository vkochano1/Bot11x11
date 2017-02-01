import logging


class LoggerConfig(object):
    FORMAT =  "%(asctime)-15s  %(levelname) %(name)-8s %(message)s"
    def __init__(self):
        logging.basicConfig(filename = './out.log', level=logging.INFO, format = LoggerConfig.FORMAT)
        


loggerConfig = LoggerConfig()
