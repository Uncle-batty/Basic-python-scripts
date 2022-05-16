import random as r

list_ = []
k = 0
for i in range(1,5):
    Num = r.randrange(k,100)
    k = Num
    list_.append(Num)

print(list_)