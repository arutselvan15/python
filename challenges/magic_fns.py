'''
:Author: Arutselvan Muthusamy
:Contact: arut.selvan15@gmail.com
'''
__updated__ = 'yyyy-MM-dd'

def gcd(n1, n2):
  '''Greatest common divisior'''
  while n2 != 0:
    temp = n2
    n2 = n1 % n2
    n1 = temp
  return n1

class Fraction(object):
  '''
    Math Fraction (using magic methods)
  '''
  def __init__(self, numerator, denominator):
    self.numerator = numerator
    self.denominator = denominator

  def __str__(self):
    return str(self.numerator) + "/" + str(self.denominator)

  def __add__(self, f2):
    numerator = (self.numerator * f2.denominator) + (self.denominator * f2.numerator)
    denaminator = self.denominator * f2.denominator
    gcd1 = gcd(numerator, denaminator)
    return Fraction(numerator // gcd1, denaminator // gcd1)

  def __sub__(self, f2):
    numerator = (self.numerator * f2.denominator) - (self.denominator * f2.numerator)
    denominator = self.denominator * f2.denominator
    gcd1 = gcd(numerator, denominator)
    return Fraction(numerator // gcd1, denominator // gcd1)

  def show(self):
    print ("{}/{}".format(self.numerator, self.denominator))

if __name__ == '__main__':
  f1 = Fraction(1, 4)
  f2 = Fraction(1, 2)
  print ("Fraction 1 : {}".format(f1))
  print ("Fraction 2 : {}".format(f2))
  f3 = f1 + f2
  print("Fraction 1 + 2 : {}".format(f3))
  f4 = f1 - f2
  print ("Fraction 1 - 2 : {}".format(f4))
