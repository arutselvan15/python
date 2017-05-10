'''
:Author: Arutselvan Muthusamy
:Contact: arut.selvan15@gmail.com
'''
__updated__ = 'yyyy-MM-dd'

def gcd(n1, n2):
  '''
    Greatest common divisior
  '''
  while n2 != 0:
    temp = n2
    n2 = n1 % n2
    n1 = temp
  return n1

if __name__ == '__main__':
  n1 = 88
  n2 = 153
  print("GCD of {} and {} is : {}".format(n1, n2, gcd(n1, n2)))
