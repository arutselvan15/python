from queue import Queue

'''
Childern line up in a circle and pass an item from neighbour to neighbour as fast as they can.  At a certain point in the game, the action is stopped and the child who has the item is removed from the circle.  Play continues until only one child is left
'''

def play(players, rounds):
    que = Queue()
    for player in players:
        que.enqueue(player)

    while que.size() > 1:
        for num in range(rounds):
            que.enqueue(que.dequeue())

        que.dequeue()

    print ("Last player in the filed : {} ".format(que.dequeue()))

if __name__ == '__main__':
    player_str = input("Enter players (comma seperated) :")
    players = player_str.split(',')
    rounds = int(input("Enter rounds:"))
    play(players, rounds)
