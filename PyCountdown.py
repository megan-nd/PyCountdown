import random
import sys
import time

consonant = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
vowel = ['A','E','I','O','U']


def start():
    print('Its time for PyCountdown!')

def letters():
    for x in range(0,4):
        player_one()
        player_two()

def player_one():
    print('Player One, consonant or vowel?')
    ans = input()
    ans = ans.strip()
    if ans == 'consonant':
        print(random.choice(consonant))
    elif ans == 'vowel':
        print(random.choice(vowel))
    else:
        print('Player One, try again')
    ans = input()
    ans = ans.strip()

def player_two():
    print('Player Two, consonant or vowel?')
    ans = input()
    ans = ans.strip()
    if ans == 'consonant':
        print(random.choice(consonant))
    elif ans == 'vowel':
        print(random.choice(vowel))
    else:
        print('Player Two, try again')
    ans = input()
    ans = ans.strip()
        
def countdown():
    start()
    letters()
    # print all letters called
    print('You have 30 seconds. Good luck!')
    time.sleep(15)
    print('15 seconds left..')
    time.sleep(10)
    print('5 seconds')
    time.sleep(1)
    print('4')
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('Time\'s up!')
    print('Player One, how many letters?')
    ans1 = input()
    print('Player Two, how many letters?')
    ans2 = input()
    if ans1 > ans2:
        print('Player Two, what is your word?')
        ans = input()
        ans = ans.strip()
    else:
        print('Player One, what is your word?')
        ans = input()
        ans = ans.strip()
    # word validity?
    


countdown()

sys.stdin.readline()
