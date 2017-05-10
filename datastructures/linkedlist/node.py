'''
:Author: Arutselvan Muthusamy
:Contact: arut.selvan15@gmail.com
'''
__updated__ = 'yyyy-MM-dd'

class Node(object):
  '''
    Linked list Node
  '''
  def __init__(self, data):
    self.data = data
    self.next = None
    self.previous = None

  def get_next(self):
    return self.next

  def get_previous(self):
    return self.previous

  def set_next(self, node):
    self.next = node

  def set_previous(self, node):
    self.previous = node
