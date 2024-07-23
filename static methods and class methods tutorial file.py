from typing import Self
from datetime import date
'''
# Create class
class Calculator:
    # initiator
    def __init__(self, version: int):
        self.version = version
    
    # considered instance method as refers to self
    def description(self):
        print(f'Currently running Calculator on version: {self.version}')

    # static method can be used anywhere that doesn't rely on the class
    @staticmethod
    def add_numbers(self, *numbers: float) -> float:
        return sum(numbers)
'''   
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def description(self) -> str:
        return f'{self.name} is {self.age} years old.'
    
    @classmethod
    def age_from_year(cls, name: str, birth_year: int) -> Self:
        current_year: int = date.today().year
        age: int = current_year - birth_year
        return cls(name, age)
    


if __name__ == '__main__':
    #calc1 = Calculator(10)
    #calc2 = Calculator(200)

    #calc1.description()
    #calc2.description()

    #print(Calculator.add_numbers(10, 20, 30))
    ihsaan = Person.age_from_year('Ihsaan', 2009)
    print(ihsaan.description())