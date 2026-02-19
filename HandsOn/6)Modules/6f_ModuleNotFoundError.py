try:
    import utilities.demo as d
    print("Python")
except ModuleNotFoundError:
    print("No module is found in this name")
    print("Fallback")
    def demo():
        print("Default fallback executed")
    demo()