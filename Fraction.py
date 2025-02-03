class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        if isinstance(numerator, str):
            if "." in numerator:
                    self.numerator = 0
                    self.denominator = 0
            else:
                if "/" in numerator:
                    num = numerator.split("/",1)
                    try:
                        self.numerator = int(num[0])
                        self.denominator = int(num[1])
                    except:
                        self.numerator = 0
                        self.denominator = 0
                else:
                    self.numerator = 0
                    self.denominator = 0
        else:
            if (denominator ==0):
                raise ZeroDivisionError('Denominator is Zero')
            else:
                if not isinstance(numerator, int):
                    self.numerator = 0
                    self.denominator = 0
                else:
                    self.numerator = numerator
                    self.denominator = denominator
        pass

    def gcd(a, b):
        if (a == 0):
            return 0
        if (b == 0):
            return 0
        
        a = abs(a)
        b = abs(b)
        
        while(b):
            a, b = b, a % b
        return a
    
        pass

    def get_numerator(self):
        lowest_numerator = self.numerator / Fraction.gcd(self.numerator, self.denominator)
        return int(lowest_numerator)
        pass

    def get_denominator(self):
        lowest_denominator = self.denominator / Fraction.gcd(self.numerator, self.denominator)
        return int(lowest_denominator)
        pass

    def get_fraction(self):
        sign = (self.numerator) * (self.denominator)
        if (sign == 0):
            return "0"
        elif (sign > 0 ):
            return str(abs(self.get_numerator())) + "/" + str(abs(self.get_denominator()))
        else:
            return "-" + str(abs(self.get_numerator())) + "/" + str(abs(self.get_denominator()))
        pass