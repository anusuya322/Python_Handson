from abc import ABC, abstractmethod
class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass
    @abstractmethod
    def write(self,data):
        pass
class TextFileHandler(FileHandler):
    def read(self):
        with open("text.txt","r") as f:
            print(f.read())
    def write(self,data):
        with open("text.txt","w") as f:
            f.write(data)
class CSVFileHandler(FileHandler):
    def read(self):
        with open("csv.csv","r") as f:
            print(f.read())
    def write(self,data):
        with open("csv.csv","w") as f:
            f.write(data)

t=TextFileHandler()
t.write("Hello, this is text file.")
t.read()
c=CSVFileHandler()
c.write("Hello, this is csv file.")
c.read()