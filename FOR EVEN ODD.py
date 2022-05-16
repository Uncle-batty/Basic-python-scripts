n = int(input(""))
LIST = []
LIST_ = []
for i in range(n):
    Value = int(input(""))
    if Value %2 ==0 :
        LIST.append(Value)
    else:
        LIST_.append(Value)
        
print(LIST)
print(LIST_)