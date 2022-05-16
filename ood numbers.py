import numpy as np
sum = 0 
for I in np.arange(2001, 5000, 2):
    sum = sum + I
    print(I)
    print(sum)