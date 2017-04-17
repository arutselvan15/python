from all_math import AllMath
from all_math import Fraction

#print (AllMath.get_divisor(24))

def do_fraction():
    f1 = Fraction(1,4)
    f2 = Fraction(1,2)
    print ("Fraction 1 : {}".format(f1))
    print ("Fraction 2 : {}".format(f2))
    f3 = f1 + f2
    print("Fraction 1 + 2 : {}".format(f3))
    f4 = f1 - f2
    print ("Fraction 1 - 2 : {}".format(f4))

def do_gcd():
    print (AllMath.gcd(48, 180))

if __name__ == '__main__':
    do_fraction()
    #do_gcd()
