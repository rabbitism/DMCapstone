import os
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

train_info = pd.read_csv(os.sep.join(['.', 'Task6', 'Cache', 'hygiene.dat.additional.train']), header=None)
train_X = train_info[0]
print(train_X)
for line in train_X:
    print(line)