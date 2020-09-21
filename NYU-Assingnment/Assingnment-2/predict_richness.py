import os

cmd = 'cat data/*.txt | sort -n > predicted_diversities.txt'

os.system(cmd)
