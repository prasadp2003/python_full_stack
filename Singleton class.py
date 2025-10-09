class Singleton:
    _instance = None   # store single instance

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Test
obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)   # True → only one instance
