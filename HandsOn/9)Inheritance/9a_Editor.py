class Writer:
    def write(self,text):
        self.content+=text+ "\n"
class Reader:
    def read(self):
        return self.content
class Editor(Writer,Reader):
    def __init__(self):
        self.content=""

obj=Editor()
obj.write("Hello OOPS")
obj.write("Inheritance")
print("Contents read")
print(obj.read())
