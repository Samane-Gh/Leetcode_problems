import numpy as np
prieces = np.array([])
print(' please Enter length of array :')
len = int(input())
for i in range(0,len):
    number = int(input())
    prieces.append(number)
print(prieces)

max = prieces.max()