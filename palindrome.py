from dequeue import Deque

def check_palindrome(word):
    deque = Deque()

    for c in word:
        deque.add_rear(c)

    is_palindrome = True

    while deque.size() > 1:
        first_char = deque.remove_front()
        last_char = deque.remove_rear()
        if not first_char == last_char:
            is_palindrome = False
            break

    print ("Is Palindrome : {}".format(is_palindrome))

if __name__ == '__main__':
    word = input("Enter word to check palindrome:")
    check_palindrome(word)
