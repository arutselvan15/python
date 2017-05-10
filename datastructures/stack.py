'''
:Author: Arutselvan Muthusamy
:Contact: arut.selvan15@gmail.com
'''
__updated__ = 'yyyy-MM-dd'

class Stack(object):
  '''
    Stack - Datastructure for LIFO.  Last in first out, add and remove
    items at same end
  '''
  def __init__(self):
    self.items = []

  def is_empty(self):
    return self.items == []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    return self.items.pop()

  def peek(self):
    return self.items[len(self.items) - 1]

  def size(self):
    return len(self.items)

  def __str__(self):
    return str(self.items)
