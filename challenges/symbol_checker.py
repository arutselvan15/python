'''
:Author: Arutselvan Muthusamy
:Contact: arut.selvan15@gmail.com
'''
__updated__ = 'yyyy-MM-dd'

from datastructures.stack import Stack

def symbol_checker(user_input):
  '''
    Check {[( symbols matching has proper open and end 
  '''
  open_symbols = '{[('
  close_symbols = '}])'
  is_valid = True

  stk = Stack()

  for symbol in user_input:
    if symbol in open_symbols:
      stk.push(symbol)
    else:
      if stk.is_empty():
        is_valid = False
        break
      else:
        open_symbol = stk.pop()
        if not open_symbols.index(open_symbol) == close_symbols.index(symbol):
          is_valid = False
          break

  if is_valid:
    print ("Symbols matching...")
  else:
    print ("Invalid symbol pattern...")

if __name__ == '__main__':
  user_input = '{([])}'
  symbol_checker(user_input)
