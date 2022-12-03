import copy
class Singleton():
    "The Singleton Class"
    value = []
    def __new__(cls):
        return cls
 # def __init__(self):
 # print("in init")
    @staticmethod
    def static_method():
        
        "Use @staticmethod if no inner variables required"

    @classmethod
    def class_method(cls):

        print(cls.value)


print(f"id(Singleton)\t= {id(Singleton)}")

OBJECT1 = Singleton()
print(f"id(OBJECT1)\t= {id(OBJECT1)}")

OBJECT2 = copy.deepcopy(OBJECT1)
print(f"id(OBJECT2)\t= {id(OBJECT2)}")

OBJECT3 = Singleton()
print(f"id(OBJECT1)\t= {id(OBJECT3)}")