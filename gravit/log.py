import time

class Log:
    def __init__(self, log=""):
        self.log = log

    def new_log(self, log):
        datetime = time.strftime("[%d/%m/%Y | %H:%M:%S] ", time.localtime(time.time()))
        self.log += "\n"+datetime+log

l = Log("Test log v1.0")
print(l.log)
l.new_log("The bacon is with the eggs !")
print(l.log)
time.sleep(5)
l.new_log("The bacon is with the eggs !")
print(l.log)

