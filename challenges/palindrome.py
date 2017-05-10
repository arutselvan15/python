'''
:Author: Arutselvan Muthusamy
:Contact: arut.selvan15@gmail.com
'''
__updated__ = 'yyyy-MM-dd'

from datastructures.dequeue import Deque

def check_palindrome(word):
  '''
    Palindrome
  '''
  deque = Deque()

  for c in word:
    deque.add_rear(c)

  is_palindrome = True

  while deque.size() > 1:
    first_char = deque.remove_front()
    last_char = deque.remove_rear()
    if not first_char == last_char:
      is_palindrome = False
      break

  print ("Is '{}' a Palindrome : {}".format(word, is_palindrome))

if __name__ == '__main__':
  word = 'madam'
  check_palindrome(word)
