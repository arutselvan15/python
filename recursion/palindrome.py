'''
:Author: Arutselvan Muthusamy
:Contact: arut.selvan15@gmail.com
'''
__updated__ = 'yyyy-MM-dd'

def palindrome(string):
  '''
    Palindrome
  '''
  if len(string) < 2:
    return True
  else:
    if string[0] == string[-1]:
      return palindrome(string[1:-1])
    else:
      return False

if __name__ == '__main__':
  word = 'madam'
  print ("Is '{}' palindrome: {}".format(word, palindrome(word)))
