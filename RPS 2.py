import random

print('this is rock paper sizor')
print('the rules are as follows')
print('Rock beats sizor')
print('Sizor beats paper')
print('and')
print('Paper beats rock')
print('R = Rock P = Paper S = Sizor ')

random = random.randint(1,3)

if random == 1 :
    Com_c = 'R'
elif random == 2 :
    Com_c = 'P'
else :
    Com_c = 'S'
    
User_c = input("Lets play:")

print('COM : ' + Com_c)
if User_c == Com_c :
    print('its a draw')
    
if (User_c == 'R' and Com_c == 'S') or  (User_c == 'P' and Com_c == 'R') or (User_c == 'S' and Com_c == 'P') :
    print('You have won')
elif (User_c == 'S' and Com_c == 'R') or  (User_c == 'R' and Com_c == 'P') or (User_c == 'P' and Com_c == 'S') :
    print('You have lost')    

    
    