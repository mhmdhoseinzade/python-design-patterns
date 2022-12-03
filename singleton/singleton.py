class Singleton:
    _instance = None
    def __new__(cls , *args , **kwargs):
        
        if not isinstance (cls._instance,cls):
            cls._instance = super().__new__(cls, *args ,**kwargs)
        return cls._instance

        
obgect1 = Singleton()
obgect2 = Singleton()

print(id(obgect1))
print(id(obgect2))

