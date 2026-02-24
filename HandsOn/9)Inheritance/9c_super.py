class Logger:
    def log(self):
        print("Parent Log file")
class FileLogger(Logger):
    def log(self):
        super().log()
        print("Child Log file")

file_child=FileLogger()
file_child.log()
