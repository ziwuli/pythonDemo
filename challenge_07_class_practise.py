"""Create a class called Car, including properties such as color, brand, speed, etc., and methods such as
acceleration, braking, etc.
"""


class Car:
    def __init__(self, color, brand, speed):
        self._color = color
        self._brand = brand
        self._speed = speed

    def __str__(self) -> str:
        return f"{self._color},{self._speed},{self._brand} car is braking"

    @property
    def color(self):
        return self._color

    @property
    def brand(self):
        return self._brand

    @property
    def speed(self):
        return self._speed

    @color.setter
    def color(self, color):
        self._color = color

    def braking(self):
        print(f"{self._color},{self._speed},{self._brand} car is braking")


class SuperCar(Car):

    def braking(self):
        print(f"superCar:{self._color},{self._speed},{self._brand} car is braking")


if __name__ == '__main__':
    superCar = SuperCar("red", "WM", 150)
    superCar.color = "green"
    superCar.braking()
    car = Car("red", "WM", 150)
    car.color = "blue"
    car.braking()
    print(car)
    print(superCar)
