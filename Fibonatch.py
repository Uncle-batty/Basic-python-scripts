num_1 = 1
num_2 = 1

n = input('How many terms do u want to see: ',)

print(str(num_1))
print(str(num_2))


for i in range(3,int(n)+1):
    fib = int(num_1) + int(num_2)
    
    print(fib)
    
    num_1 = num_2
    num_2 = fib
    
