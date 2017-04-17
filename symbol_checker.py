
from stack import Stack

def symbol_checker():
    user_input = input("Enter input: ")
    open_symbols = '{[('
    close_symbols = '}])'
    is_valid = True
    stk = Stack()
    for symbol in user_input:
        if symbol in open_symbols:
            stk.push(symbol)
        else:
            if stk.is_empty():
                is_valid = False
                break
            else:
                open_symbol = stk.pop()
                if not open_symbols.index(open_symbol) == close_symbols.index(symbol):
                    is_valid = False
                    break
    if is_valid:
        print ("Symbols matching...")
    else:
        print ("Invalid symbol pattern...")

if __name__ == '__main__':
    symbol_checker()
