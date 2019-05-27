class square:
    def __init__(self, length=0):
        self.length = length

    def getArea(self):
        if type(self.length) not in [int, float]:
            raise ValueError("Square length should be non-negative real number")
        if self.length <0:
            raise ValueError("Square length should be non-negative real number")
        return self.length**2

    def getPerimeter(self):
        return 4*self.length
