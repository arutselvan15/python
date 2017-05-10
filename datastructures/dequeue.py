'''
:Author: Arutselvan Muthusamy
:Contact: arut.selvan15@gmail.com
'''
__updated__ = 'yyyy-MM-dd'

class Deque():
  '''
    Deque - Datastructure capable of add/remove items at both end
  '''
  def __init__(self):
    self.items = []

  def is_empty(self):
    return self.items == []

  def add_rear(self, item):
    self.items.insert(0, item)

  def add_front(self, item):
    self.items.append(item)

  def remove_rear(self):
    return self.items.pop(0)

  def remove_front(self):
    return self.items.pop()

  def size(self):
    return len(self.items)

  def __str__(self):
    return str(self.items)

