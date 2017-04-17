
import sys

def binary_search(list_data, item):
    ''' binary search O(log n)
        divide and conquer stratergy 
        1 = n/2
        2 = n/4
        3 = n/8
        i = n/2i
    '''
    first = 0
    last = len(list_data) -1
    found = False
    while not found and first < last:
        middle = (first + last) // 2
        print ("List to search.. {}".format(list_data[first:last+1]))
        if list_data[middle] == item:
            found = True
        else:
            if list_data[middle] > item:
                last = middle - 1
            else:
                first = middle + 1

    print ("Item {} found in list : {}".format(item, found))


def usage():
    print ('''
        binarySearch
    ''')
if __name__ == '__main__':
    if len(sys.argv) > 1:
        action = sys.argv[1]
        if action == 'binarySearch':
            data = input("Enter list (comma separated):")
            item = input("Item to search :")
            binary_search([int(i) for i in data.split(',')], int(item))
    else:
        print ("arguments missing...")
        usage()
