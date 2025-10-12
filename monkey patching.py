class Dog:
    def sound(self):
        return "Woof!"

# Normal behavior
d = Dog()
print(d.sound())   # Output: Woof!


# Monkey patching: changing behavior at runtime
def new_sound(self):
    return "Meow!"   # like a cat

Dog.sound = new_sound   # Replacing the method

print(d.sound())   # Output: Meow!
