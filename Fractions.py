Sum= 0
String = ' '

N = int(input('N',))

for i in range(1,N):
    Sum = Sum + i/(i+1)
    if i != N :
        String = String + str(i) + '/' + str(i+1)  + ' + '
    else:
         String = String + str(i ) + '/' + str(i+1)
         
String = String +  ' = ' +  str(Sum)

print(String)