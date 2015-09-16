#!/usr/bin/env python

__author__ = 'chengshaoming@hikvision.com.cn'

import logging
import os
import sys
#import inspect

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Logger:

    LEVELS = {
                'debug' : logging.DEBUG,
                'info' : logging.INFO,
                'warning' : logging.WARNING,
                'error' : logging.ERROR,
                'critical' : logging.CRITICAL
             }

    def __init__(self, level):
        self.logger = logging.getLogger('testlog')

        str_handler = logging.StreamHandler(sys.stdout)
        file_handle = logging.FileHandler('test.log') 
        #formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s' )
        formatter = logging.Formatter('%(asctime)s %(message)s' )

        str_handler.setFormatter(formatter)
        self.logger.addHandler(str_handler)
        self.logger.addHandler(file_handle)
        self.logger.setLevel(self.LEVELS[level])


    def i(self, msg):
        #self.logger.info('I/(%s-%s:%s)=> %s' % (str(__file__).split("/")[-1], __name__, inspect.stack()[1][2], msg))

        filename, line, function = self.logger.findCaller()
        self.logger.info('I/(%s:%s)=> %s' % (os.path.basename(filename), line, msg))

    def d(self, msg):
        #self.logger.debug('D/(%s-%s:%s)=> \x1b[1;34m%s\x1b[0m' % (str(__file__).split("/")[-1], __name__, inspect.stack()[1][2], msg))

        filename, line, function = self.logger.findCaller()
        self.logger.debug('\x1b[1;34mD/(%s:%s)=> %s\x1b[0m' % (os.path.basename(filename), line, msg))

    def w(self, msg):
        #self.logger.warning('W/(%s-%s:%s)=> \x1b[1;33m%s\x1b[0m' % (str(__file__).split("/")[-1], __name__, inspect.stack()[1][2], msg))

        filename, line, function = self.logger.findCaller()
        self.logger.warning('\x1b[1;33mW/(%s:%s)=> %s\x1b[0m' % (os.path.basename(filename), line, msg))

    def e(self, msg):
        #self.logger.error('E/(%s-%s:%s)=> \x1b[1;35m%s\x1b[0m' % (str(__file__).split("/")[-1], __name__, inspect.stack()[1][2], msg))

        filename, line, function = self.logger.findCaller()
        self.logger.error('\x1b[1;35mE/(%s:%s)=> %s\x1b[0m' % (os.path.basename(filename), line, msg))

    def c(self, msg):
        #self.logger.critical('C/(%s-%s:%s)=> \x1b[1;31m%s\x1b[0m' % (str(__file__).split("/")[-1], __name__, inspect.stack()[1][2], msg))

        filename, line, function = self.logger.findCaller()
        self.logger.critical('\x1b[1;31mC/(%s:%s)=> %s\x1b[0m' % (os.path.basename(filename), line, msg))

Log = Logger('debug')

if __name__ == "__main__":
    Log.i("Test for info level log formatter print")
    Log.d("Test for debug level log formatter print")
    Log.w("Test for warning level log formatter print")
    Log.e("Test for error level log formatter print")
    Log.c("Test for critical level log formatter print")