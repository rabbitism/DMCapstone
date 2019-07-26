import os

with open(os.sep.join(['.','Task6', 'Dataset', 'hygiene.dat']), 'r', encoding='utf-8') as f:
    content = f.readlines()
    for i in range(10):
        print(content[i])
        print(len(content[i]))