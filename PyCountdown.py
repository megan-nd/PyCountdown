import random
import sys
import time

consonants = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
vowels = ['A','E','I','O','U']
letters_list = []

def start():
    print('Its time for PyCountdown!')

def letters():
    for x in range(0,4):
        player_one()
        player_two()

def get_choice_from_player(player_name):
    for x in range(0,2):
      print(player_name + ', consonant or vowel?')
      ans = input()
      ans = ans.strip()
      if ans == 'consonant':
          letter = random.choice(consonants)
          print(letter)
          letters_list.append(letter)
          break
      elif ans == 'vowel':
          letter = random.choice(vowels)
          print(letter)
          letters_list.append(letter)
          break
      else:
          print(player_name + ', try again')

def player_one():
    get_choice_from_player('Player One')

def player_two():
    get_choice_from_player('Player Two')
        
def countdown():
    start()
    letters()
    # print all letters called
    print(letters_list)
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
