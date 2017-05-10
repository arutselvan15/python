'''
:Author: Arutselvan Muthusamy
:Contact: arut.selvan15@gmail.com
'''
__updated__ = 'yyyy-MM-dd'

from datastructures.queue import Queue

'''
  Childern line up in a circle and pass an item from neighbour to
  neighbour as fast as they can.  At a certain point in the game,
  the action is stopped and the child who has the item is removed
  from the circle.  Play continues until only one child is left
'''

def play(players, rounds):
  '''
    Play hot potato game
  '''
  que = Queue()
  for player in players:
    que.enqueue(player)

  while que.size() > 1:
    for _ in range(rounds):
      que.enqueue(que.dequeue())

    que.dequeue()

  print ("Last player in the filed : {} ".format(que.dequeue()))

if __name__ == '__main__':
  players = ['A', 'B', 'C', 'D', 'E', 'F']
  rounds = 5
  play(players, rounds)
