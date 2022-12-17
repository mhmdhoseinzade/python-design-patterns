import copy

class prototype :

    def __init__(self) :
        self._object = {}

    def register(self , name , attr):
        self._object[name]=attr
        

    def unregister(self , name):
        del self._object[name]

    def clone(self , name , attr):
        obj = copy.deepcopy(self._object[name])
        print(obj.__dict__)
        obj.__dict__.update(attr)
        print(obj.__dict__)

        return obj 

class Bird :
    "bird"

Prototype = prototype()
Prototype.register("bird",Bird())

duck = Prototype.clone("bird" , {"name" : "duck"})

print(type(duck), duck.name)
        