# The Minion Game
# https://www.hackerrank.com/challenges/the-minion-game/problem

scores = {}
scores['kevinScore'] = 0
scores['stuartScore'] = 0
scores['words'] = {}

def isVowel(letter):
    vowels = ['a','e','i','o','u']
    if letter.lower() in vowels:
        return True
    else:
        return False

def getWords(i,string):
    j = 0 
    while j <= len(string[i:]):
        w = string[i:][:j]
        if len(w) > 0 :
            # print(w)
            wc = 0
            if w in scores['words']:
                wc = scores['words'][w]
            scores['words'][w] = wc+1
        j+=1
    
def getAllWords(string):
    i = 0 
    while i <= len(string):
        getWords(i,string)
        i+=1


def calculateScores():
    for key in scores['words'].keys():
        if isVowel(key[:1]):
            scores['kevinScore'] += scores['words'][key]
        else:
            scores['stuartScore'] += scores['words'][key]

def determineWinner():
    if scores['kevinScore'] > scores['stuartScore']:
        print('Kevin',scores['kevinScore'])
    elif scores['kevinScore'] < scores['stuartScore']:
        print('Stuart',scores['stuartScore'])
    else:
        print('Tie')

def minion_game(string):
    getAllWords(string)
    calculateScores()
    determineWinner()
    # print('words',scores['words'])
    # print('Kevin',scores['kevinScore'])
    # print('Stuart',scores['stuartScore'])


    

if __name__ == '__main__':
    s = input()
    # s = 'ANANANA'
    minion_game(s)