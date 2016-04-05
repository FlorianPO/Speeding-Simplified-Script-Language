# -*- coding: utf-8 -*-

# Parsing logger
class Logger:
    def __init__(self, name, trace=True):
        self.trace = trace
        self.name = name
        self.log_list = []
        self.logerror_list = []
        self.logast_list = []
        self.alllog_list = []

    def _log(self, msg, list):
        list.append(msg)
        self.alllog_list.append(msg)
        if (self.trace):
            print(msg)

    def _print(self, list):
        for msg in list:
            print(msg)

    def log(self, msg):         self._log(msg, self.log_list)
    def logError(self, msg):    self._log(msg, self.logerror_list)
    def logAST(self, msg):      self._log(msg, self.logast_list)

    def printLog(self):         self._print(self.log_list)
    def printLogError(self):    self._print(self.logerror_list)
    def printLogAST(self):      self._print(self.logast_list)
    def printAllLog(self):      self._print(self.alllog_list)
