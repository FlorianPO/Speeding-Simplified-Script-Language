class LoggerCore:
    def __init__(self, name):
        self.name = name
        self.log_list = []
        self.log_levels = []

    def log(self, msg, level=0):
        self.log_list.append(msg)
        self.log_levels.append(level)

    def printLog(self, levels=[-1]):
        if (-1 in levels):
            for msg in self.log_list:
                print(msg)
        else:
            for lvl in self.log_levels:
                if (lvl in levels):
                    print(msg)

class Logger:
    _s = LoggerCore("Default logger") # static
   
class NoInstructionLeft(Exception):
    pass

class ErrorParsing(Exception):
    pass

