class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
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
        return str(abs(lowest_numerator))
        pass

    def get_denominator(self):
        lowest_denominator = self.denominator / Fraction.gcd(self.numerator, self.denominator)
        return str(abs(lowest_denominator))
        pass

    def get_fraction(self):
        # TODO: make it compatible with inputs of the num/denom format
        #       the invalid checker
        #       dividing by 0

        #if (self.numerator ):       # checks if not number
        #    return 0
        sign = (self.numerator) * (self.denominator)
        if (sign == 0):
            return 0
        elif (sign > 0 ):       # should return [sign] + [numerator] + "/" + [denominator]
            return Fraction.get_numerator() + "/" + Fraction.get_denominator()
        else:
            return "-" + Fraction.get_numerator() + "/" + Fraction.get_denominator()
        pass