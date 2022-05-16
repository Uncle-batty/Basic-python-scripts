X  = int(input('Input you integer to see if its prime: ', ))
temp = 0 

for i in range(2,X):
    if X % i == 0 :
        temp += 1

if temp == 0 :
    print(X,' Is a prime number'  )  
else:
            print(X, " is not prime these are the factors :")
            for J in range(1,X):
                 if X % i == 0 :
                     print(J)
print()
print('Y = 8X^2 + 1')
for X in range(-5,6):
    print(str(8*(X)**2 +1), ' = ', ' 8(',str(X),')^2 + 1')
    
                     
                     
                 
        