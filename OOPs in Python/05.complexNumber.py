class complexNumber:
    def __init__ (self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag < 0:
            return f"{self.real} - {abs(self.imag)}i"
        else: return f"{self.real} + {self.imag}i"
    


c1 = complexNumber(3,-4)
print(c1)