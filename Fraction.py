class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        if isinstance(numerator, str):
            if "/" in numerator:
                num = numerator.split("/")
                self.numerator = int(num[0])
                self.denominator = int(num[1])
            else:
                self.numerator = 0
                self.denominator = 0
        else:
            if (denominator ==0):
                raise ZeroDivisionError('Denominator is Zero')
            else:
                self.numerator = numerator
                self.denominator = denominator
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
        lowest_numerator = self.numerator / Fraction.gcd(self.numerator, self.denominator)
        return abs(int(lowest_numerator))
        pass

    def get_denominator(self):
        lowest_denominator = self.denominator / Fraction.gcd(self.numerator, self.denominator)
        return abs(int(lowest_denominator))
        pass

    def get_fraction(self):
        # TODO: make it compatible with inputs of the num/denom format
        #       the invalid checker 
        
        #for char in self:
        #    if 

        sign = (self.numerator) * (self.denominator)
        if (sign == 0):
            return "0"
        elif (sign > 0 ):       # should return [sign] + [numerator] + "/" + [denominator]
            return str(self.get_numerator()) + "/" + str(self.get_denominator())
        else:
            return "-" + str(self.get_numerator()) + "/" + str(self.get_denominator())
        pass