class Node(object):

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

class LinkedList(object):

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

class OrderedLinkedList(LinkedList):

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



