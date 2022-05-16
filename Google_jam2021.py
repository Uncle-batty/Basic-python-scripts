S = input('What is the string',)
x = 0 
y = 0 
Sum = 0

if 1<= len(S) <= 100 :
    for i in range(0,len(S)-1):
        j = i +1
        if S[i] + S[j] == 'CJ' : 
            x = x+1
        elif S[i] + S[j] == 'JC' : 
            y = y+1
            
        Sum = Sum +(x+y)
else:
    pass

print('Case #{x}: ' + str(Sum))