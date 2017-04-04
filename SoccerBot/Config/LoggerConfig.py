import logging


class LoggerConfig(object):
    FORMAT =  "%(asctime)-15s  %(levelname)s %(name)-8s %(message)s"
    def __init__(self, user):
	filename = './%s.log' % user
        logging.basicConfig(filename = filename, level=logging.INFO, format = LoggerConfig.FORMAT)
        



