# Define a custom metaclass
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name} using Meta")
        return super().__new__(cls, name, bases, dct)

# Use the metaclass in a class
class MyClass(metaclass=Meta):
    pass
