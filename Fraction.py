class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        #TODO
        
        pass

    def gcd(a, b):
        #TODO
        if (a == 0):
            return b
        elif (b == 0):
            return a
        else:
            return Fraction.gcd(b, b%a)
        
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