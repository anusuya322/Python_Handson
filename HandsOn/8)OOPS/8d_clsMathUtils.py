class MathUtils:
    @staticmethod
    def add(a,b):
        return a+b
    @classmethod
    def cls_name(cls):
        return cls.__name__

print(MathUtils.add(7,7))
print(MathUtils.cls_name())
