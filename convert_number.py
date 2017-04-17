from stack import Stack

def convert_number(user_input, base):
    stk = Stack()
    remainder_list = '0123456789ABCDEF'
    while user_input > 0:
        remainder = user_input % base
        stk.push(remainder_list[remainder])
        user_input = user_input // base
    result = ''
    while not stk.is_empty():
        result += str(stk.pop())
    print (result)

if __name__ == '__main__':
    user_input = int(input("Enter value :"))
    base = int(input("Enter base :"))
    convert_number(user_input, base)

