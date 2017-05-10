'''
:Author: Arutselvan Muthusamy
:Contact: arut.selvan15@gmail.com
'''
__updated__ = 'yyyy-MM-dd'

from .node import Node

'''
  Linked list is a linear collection of data elements, called nodes, each
  pointing to the next node by means of a pointer. It is a data structure
  consisting of a group of nodes which together represent a sequence. Under
  the simplest form, each node is composed of data and a reference (in other
  words, a link) to the next node in the sequence. This structure allows for
  efficient insertion or removal of elements from any position in the sequence
  during iteration. More complex variants add additional links, allowing
  efficient insertion or removal from arbitrary element references.

  Linked lists are among the simplest and most common data structures. They
  can be used to implement several other common abstract data types,
  including lists (the abstract data type), stacks, queues, associative
  arrays, and S-expressions, though it is not uncommon to implement the
  other data structures directly without using a list as the basis of
  implementation.

'''
class LinkedList(object):
  '''
    Linked list
  '''
  def __init__(self):
    self.head = None

  def add(self, data):
    node = Node(data)
    if self.head == None:
      self.head = node
    else:
      node.next = self.head
      self.head = node

  def traverse(self):
    if self.head is None:
      print ("List is empty...")
    else:
      current = self.head
      end_of_list = False
      display = ''
      while not end_of_list:
        display += ' => {}'.format(current.data)
        if current.next == None:
          end_of_list = True
        else:
          current = current.get_next()
      print (display)

  def is_empty(self):
    return self.head == None

  def list_size(self):
    size1 = 0
    current = self.head
    while current != None:
      size1 += 1
      current = current.get_next()
    print ("Size of list: {}".format(size1))

  def search(self, data):
    if self.head is None:
      print ("List is empty...")
    else:
      current = self.head
      found = False
      while not found and current.next != None:
        if current.data == data:
          found = True
        else:
          current = current.get_next()
      print ("Is {} item found : {}".format(data, found))

  def remove(self, data):
    if self.head is None:
      print ("List is empty...")
    else:
      current = self.head
      previous = None
      removed = False
      while not removed and current.next != None:
        if current.data == data:
          if previous is None:
            self.head = current.get_next()
          else:
            previous.next = current.get_next()
          removed = True

        else:
          previous = current
          current = current.get_next()
      if removed:
        print ("Item {} removed successfully...".format(data))
      else:
        print ("Item {} not found in the list.".format(data))

  def __str__(self):
    return str(self.traverse())
