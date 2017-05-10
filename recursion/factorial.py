'''
:Author: Arutselvan Muthusamy
:Contact: arut.selvan15@gmail.com
'''
__updated__ = 'yyyy-MM-dd'

def factorial(number):
  '''
    Factorial
    5 = 1*2*3*4*5
  '''
  if number <= 1:
    return 1
  else:
    return number * factorial(number - 1)

if __name__ == '__main__':
  number = 10
  print (factorial(number))
