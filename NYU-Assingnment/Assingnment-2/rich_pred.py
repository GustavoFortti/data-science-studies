#import os

#cmd = 'cat data/*.txt | sort -n > predicted_diversities.txt'

#os.system(cmd)

from functools import reduce

sar_parameters = [[22.7, 0.3], [1.2, 0.163, 0.009], [14.36, 21.16], [85.91, 42.57], [1082.45, 1.59, 390000000]]


somatorio = []
				  
for i in sar_parameters:
    somatorio.append(reduce(lambda x, y: x + y, i))
  
print(somatorio)
