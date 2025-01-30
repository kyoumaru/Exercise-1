class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        #TODO
        
        pass

    def gcd(a, b):
        #TODO
        if (a == 0 or b == 0):
            return 0
        elif (a == b):
            return a
        else:
            if (a > b):
                return Fraction.gcd(b, a-b)
            return Fraction.gcd(b, b-a)
        pass

    def get_numerator(self):
        #TODO
        pass

    def get_denominator(self):
        #TODO
        pass

    def get_fraction(self):
        #TODO
        pass