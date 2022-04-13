import os
import datetime
try:
    import psutil
    PSUTIL = True
except:
    PSUTIL = False

class Log:
    def __init__(self,
                 file=f"logs/{datetime.datetime.now().year}-{datetime.datetime.now().month}-{datetime.datetime.now().day}-{datetime.datetime.now().second}.log"):
        self.path = file
        self.log(f"===Session started===")
        try:
            os.makedirs("logs")
        except:
            pass
    def log(self, text):
        try:
            file = open(self.path, "r")
            content = file.read()
            file.close()
        except FileNotFoundError:
            content = ""
        file = open(self.path, "w")
        file.write(
            content + f"[{datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}-{datetime.datetime.now().year}.{datetime.datetime.now().month}.{datetime.datetime.now().day}] {text} \n"
        )
        file.close()

    def tasklog(self, pid=os.getpid()):
        if not PSUTIL:
            return False
        try:
            file = open(self.path, "r")
            content = file.read()
            file.close()
        except FileNotFoundError:
            content = ""
        try:
            process = psutil.Process(pid=pid)
        except:
            self.log("Failed to Tasklog")
        file = open(self.path, "w")
        file.write(
            content + f"[{datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}-{datetime.datetime.now().year}.{datetime.datetime.now().month}.{datetime.datetime.now().day}] CPU: {process.cpu_percent()}%/100%; MEM: {process.memory_info()[0] / 2 ** 30} GB\n")
        file.close()

    def crush_dump(self,error,comment="Critical error",recomends="restart application"):
        self.log("A game was crushed")
        temp = Log(f"logs/{datetime.datetime.now().hour}-{datetime.datetime.now().minute}-{datetime.datetime.now().second}-{datetime.datetime.now().year}-{datetime.datetime.now().month}-{datetime.datetime.now().day}-dump.log")
        temp.log("Crush dump")
        temp.log(f"Check {self.path} to check log")
        temp.tasklog()
        temp.log(f"Error: {error}")
        temp.log(f"What doing: {comment}")
        temp.log(f"Try to {recomends}")

