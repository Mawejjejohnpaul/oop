class Vehicle:
    def __init__(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def toString(self):
        return f"The vehicle is {self.color}."


if __name__ == "__main__":
    Vehicle1 = Vehicle("blue")
    print(Vehicle1.getColor())

    print(Vehicle1.toString())