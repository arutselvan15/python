'''
Created on May 4, 2017

@author: Arun
'''
from itertools import permutations

'''
input: string
-get permutation combination of the string
-Kevin get 1 point for choice starts with vowels
-Stuart get 1 for non vowels
-Print winner, if its draw pint Draws
'''

def get_permutations(string):
    choices = []
    for i in range(1, len(string) + 1):
        options = list(permutations(string, i))
        choices += [''.join(t) for t in options ]
    return choices

def minion_game(string):
    vowels = ('A', 'E', 'I', 'O', 'U')
    non_vowels = ('B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','X','Z')
    players = {
        'Stuart' : {
            'choice' : [],
            'score' : 0
            },
       'Kevin' : {
            'choice' : [],
            'score' : 0
            }
    }
    choice = get_permutations(string)
    for word in choice:
        if word.startswith(vowels):
            players['Kevin']['choice'].append(word)
        elif word.startswith(non_vowels):
            players['Stuart']['choice'].append(word)
    
    for player in players:
        for choice in set(players[player]['choice']):
            index = 0
            while index >= 0:
                index = string.find(choice, index, len(string))
                if index >= 0:
                    index += 1
                    players[player]['score'] += 1
                else:
                    break
    
    if players['Kevin']['score'] == players['Stuart']['score']:
        print ("Draw")
    elif players['Kevin']['score'] > players['Stuart']['score']:
        print("Kevin {}".format(players['Kevin']['score']))
    else:
        print("Stuart {}".format(players['Stuart']['score']))

if __name__ == '__main__':
    s = 'AAA'
    minion_game(s)