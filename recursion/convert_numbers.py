'''
:Author: Arutselvan Muthusamy
:Contact: arut.selvan15@gmail.com
'''
__updated__ = 'yyyy-MM-dd'

def convert_numbers(value, base):
  '''
    Convert number into different base format
    2 : Binary
    8 : Octal
    16 : Hex
  '''
  conversion = '0123456789ABCDEF'
  if base > value:
    return str(conversion[value])
  else:
    return convert_numbers(value // base, base) + str(conversion[value % base])

if __name__ == '__main__':
  number = 123
  base = 2
  print (convert_numbers(number, base))
