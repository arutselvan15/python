'''
:Author: Arutselvan Muthusamy
:Contact: arut.selvan15@gmail.com
'''
__updated__ = 'yyyy-MM-dd'

class Queue(object):
  '''
    Queue - Datastructure for FIFO.  First in first out, add items at one
    and remove at other end
  '''
  def __init__(self):
    self.items = []

  def is_empty(self):
    return self.items == []

  def enqueue(self, item):
    self.items.insert(0, item)

  def dequeue(self):
    return self.items.pop()

  def size(self):
    return len(self.items)

  def __str__(self):
    return str(self.items)
