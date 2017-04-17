import logging

#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)

class AllMath:

    @classmethod
    def get_divisor(cls, number):
        print (number)

    @classmethod
    def gcd(cls, n1, n2):
        '''Greatest common divisior'''
        logging.debug("Tmp, n2, n2")
        while n2 != 0:
            temp = n2
            n2 = n1 % n2
            n1 = temp
            logging.debug("gcd : {},{},{}".format(temp,n2,n1))
        return n1


class Fraction:
    
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def __add__(self, f2):
        numerator = (self.numerator * f2.denominator) + (self.denominator * f2.numerator)
        denaminator = self.denominator * f2.denominator
        gcd = AllMath.gcd(numerator, denaminator)
        return Fraction(numerator // gcd, denaminator // gcd)

    def __sub__(self, f2):
        numerator = (self.numerator * f2.denominator) - (self.denominator * f2.numerator)
        denominator = self.denominator * f2.denominator
        gcd = AllMath.gcd(numerator, denominator)
        return Fraction(numerator // gcd, denominator // gcd)

    def show(self):
        print ("{}/{}".format(self.numerator, self.denominator))
