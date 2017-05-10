'''
:Author: Arutselvan Muthusamy
:Contact: arut.selvan15@gmail.com
'''
__updated__ = 'yyyy-MM-dd'

def sum_list_of_numbers(num_list):
  '''
    Sum the list of numbers
  '''
  if len(num_list) == 1:
    return num_list[0]
  else:
    return num_list[0] + sum_list_of_numbers(num_list[1:])

if __name__ == '__main__':
  number = 12345
  digit2list = lambda num: map(int, str(num))
  print (sum_list_of_numbers(digit2list(number)))
