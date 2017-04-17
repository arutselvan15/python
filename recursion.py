import sys

def sum_list_of_numbers(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + sum_list_of_numbers(num_list[1:])

def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * factorial(number - 1)

def value_conversion(value, base):
    conversion = '0123456789ABCDEF'
    if base > value:
        return str(conversion[value])
    else:
        return value_conversion(value // base, base) + str(conversion[value % base])
def palindrome(string):
    if len(string) < 2:
        return True
    else:
        if string[0] == string[-1]:
            return palindrome(string[1:-1])
        else:
            return False

def binary_search(list_data, item):
    if len(list_data) == 0:
        return False
    else:
        middle = len(list_data) // 2
        if list_data[middle] == item:
            return True
        else:
            if list_data[middle] < item:
                return binary_search(list_data[middle + 1:], item)
            else:
                return binary_search(list_data[:middle], item)
    
def usage():
    print ('''
    Recursion
        action : 
            sum_of_list
            factorial
            conversion (binary 2, oct 8, hex 16)
            palindrome
            binarysearch
    ''')

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        action = sys.argv[1]
        if action == 'sum_of_list':
            user_input = input("Enter list of number (comma seperator):")
            user_list = [int(num.strip()) for num in user_input.split(',')]
            print (sum_list_of_numbers(user_list))
        elif action == 'factorial':
            user_input = input("Enter number to find factorial:")
            print (factorial(int(user_input)))
        elif action == 'conversion':
            user_input = input("Enter number to convert :")
            base = input("Enter base :")
            print (value_conversion(int(user_input), int(base)))
        elif action == 'palindrome':
            user_input = input("Enter string to check palindrome:")
            print ("Is palindrome: {}".format(palindrome(user_input)))
        elif action == 'binarysearch':
            list_data = input("Enter list data (comma separated):")
            list_data = [int(i) for i in list_data.split(',')]
            item = input("Item to search:")
            print("Is item {} found ? : {}".format(item, binary_search(list_data, int(item)))
        elif action in ['usage', 'help']:
            usage()
        else:
            usage()
    else:
        usage()
    
