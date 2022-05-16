Column_A = ['A', "B",'C','','','F','']
Column_B = ['', "",'','D','E','','G']
Column_C = ['', "",'','','','','']

print('column C')

for i in range(len(Column_C)):
    if (Column_A[i] !='') :
        Column_C[i] = Column_A[i]
        print(Column_C[i])
    elif (Column_B[i] !='') :
        Column_C[i] = Column_B[i]
        print(Column_C[i])
        

        
