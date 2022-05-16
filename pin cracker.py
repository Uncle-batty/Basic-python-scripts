#bank pin cracker
import time as time
pin = input("Enter your pin:")
pin2 ='    '
found = 'n'
x = 0
while found != 'y':
    starttime = time.time()
   
    if x == 1:
                y = '1'
    elif x == 2:
                y = '2'
    elif x ==3:
                y = '3'
    elif x ==4:
                y = '4'
    elif x ==5:
                y = '5'
    elif x ==6:
                y = '6'
    elif x ==7:
                y = '7'
    elif x ==8:
                y = '8'
    elif x ==9:
                y = '9'
    elif x == 0:
                y = '0'
    print(x)       
    if pin[0] == y:
            pin2 = y +pin2[1] + pin2[2] + pin2[3]
    if pin[1] == y:
            pin2 = pin2[0] + y + pin2[2] + pin2[3]
    if pin[2] == y:
            pin2 = pin2[0] + pin2[1] + y  + pin2[3]
    if pin[3] == y:
            pin2 = pin2[0] + pin2[1]  + pin2[2] + y
    else :
        print(y)
    
    x = x +1  
    if x == 10 :
        seconds = time.time()-starttime
        if pin2 == pin :
            found = 'y'
            print('Cracked ' + pin2 + ' in ' + str(seconds) + ' seconds')
        else :
            print(' not Cracked - last recored =' + pin2 + ' in ' + str(seconds) + ' seconds')
            found = 'y'
            
        

