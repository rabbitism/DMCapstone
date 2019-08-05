import os
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

size = 20

train_info = pd.read_csv(os.sep.join(['.', 'Task6', 'Cache', 'hygiene.dat.additional.train']), header=None)
train_X = train_info.loc[:, 2:3]
x_vector = pd.read_csv(os.sep.join(['.', 'Task6', 'Cache', str(size) + '_nn_array_train.txt']), header=None)
print(x_vector.shape)
train_X = pd.concat([train_X, x_vector.loc[:,0:9]], axis=1).values
print(train_X.shape)
train_Y = pd.read_csv(os.sep.join(['.', 'Task6', 'Cache', 'hygiene.dat.labels.train']), header=None)
train_Y = train_Y.values.ravel()
print(train_Y.shape)

classifier = RandomForestClassifier(max_depth=20, max_features='auto', n_estimators=100)
classifier.fit(train_X, train_Y)
print(classifier.feature_importances_)

test_info = pd.read_csv(os.sep.join(['.', 'Task6', 'Cache', 'hygiene.dat.additional.test']), header=None)
test_X = test_info.loc[:, 2:3]
test_vector = pd.read_csv(os.sep.join(['.', 'Task6', 'Cache', str(size) + '_nn_array_test.txt']), header=None)
test_X = pd.concat([test_X, test_vector.loc[:,0:9]], axis=1).values
#print(test_X)
predictions = classifier.predict(test_X)
print(predictions)
with open(os.sep.join(['.', 'Task6', 'Results', str(size)+"_rf.txt"]), 'a') as f:
    f.write('Bunni'+'\n')
    for p in predictions:
        f.write(str(p) + '\n')
    f.close()