'''
:Author: Arutselvan Muthusamy
:Contact: arut.selvan15@gmail.com
'''
__updated__ = 'yyyy-MM-dd'

def binary_search(list_data, item):
  '''
    Binary search O(log n)
    divide and conquer stratergy 
      1 = n/2
      2 = n/4
      3 = n/8
      i = n/2i
  '''
  if len(list_data) == 0:
    return False
  else:
    middle = len(list_data) // 2
    if list_data[middle] == item:
      return True
    else:
      if list_data[middle] < item:
        return binary_search(list_data[middle + 1:], item)
      else:
        return binary_search(list_data[:middle], item)

if __name__ == '__main__':
  list_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  item = 11
  print("Is item {} found in {} ? : {}".format(item, list_data, binary_search(list_data, item)))
