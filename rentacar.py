

class Rental:
    def __init__(self, number_of_days, car):
        self._number_of_days = number_of_days
        self._car = car

    def number_of_days(self):
        return self._number_of_days

    def car(self):
        return self._car



class Car:
    def __init__(self, type, size, registration):
        self._type = type
        self._size = size
        self._registration = registration

    def type(self):
        return self._type

    def size(self):
        return self._size

    def registration(self):
        return self._registration


