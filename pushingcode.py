# Define a Mixin for logging
class LoggerMixin:
    def log(self, message):
        print(f"[LOG]: {message}")

# Define another Mixin for serialization
import json
class JsonSerializableMixin:
    def to_json(self):
        return json.dumps(self.__dict__)

# A base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Final class with mixins
class Employee(Person, LoggerMixin, JsonSerializableMixin):
    def __init__(self, name, age, emp_id):
        super().__init__(name, age)
        self.emp_id = emp_id

    def work(self):
        self.log(f"{self.name} is working...")
