from typing import Final


class MyMaths:
    PI: Final = 3.14

    def __init__(self, radius: int, length: int):
        self.radius = radius
        self.length = length
    
    def circle(self) -> float:
        return MyMaths.PI * self.radius * self.radius

    def square(self) -> int:
        return self.length * self.length



