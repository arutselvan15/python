'''
:Author: Arutselvan Muthusamy
:Contact: arut.selvan15@gmail.com
'''
__updated__ = 'yyyy-MM-dd'

from .node import Node
from .linkedlist import LinkedList

class OrderedLinkedList(LinkedList):
  '''
    Ordered Linked list
  '''
  def add(self, data):
    node = Node(data)

    if self.head == None:
      self.head = node
    else:
      current = self.head
      previous = None
      added = False
      while not added:
        if current.data >= data:
          if previous:
            node.set_next(previous.get_next())
            previous.set_next(node)
          else:
            node.set_next(self.head)
            self.head = node
          added = True
        else:
          if current.next == None:
            current.set_next(node)
            added = True
          else:
            previous = current
            current = current.get_next()

  def search(self, data):
    found = False
    current = self.head
    while not found and current.next != None:
      if current.data <= data:
        if current.data == data:
          found = True
        else:
          current = current.get_next()
      else:
        break
    if found:
      print ("Item {} found in list...".format(data))
    else:
      print ("Item {} not found in list...".format(data))
