class Fracao:
    def __init__(self, num, den):
        self.num = num
        self.den = den
    def __repr__(self):
        return str(self.num) + '/' + str(self.den)