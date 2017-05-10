'''
:Author: Arutselvan Muthusamy
:Contact: arut.selvan15@gmail.com
'''
__updated__ = 'yyyy-MM-dd'

from .orderedlinkedlist import OrderedLinkedList

l = OrderedLinkedList()

l.add(40)
l.traverse()
l.add(90)
l.traverse()
l.add(20)
l.traverse()
l.add(70)
l.traverse()
l.add(10)
l.traverse()
print ("Is empty : {}".format(l.is_empty()))
print ("Size : {}".format(l.list_size()))
print ("Traverse")
l.traverse()
print ("Remove 40")
l.remove(40)
print ("Traverse")
l.traverse()
print ("Search 70 and 100")
l.search(70)
l.search(100)

