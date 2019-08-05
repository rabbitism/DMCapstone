import torch
import torch.nn as nn
import numpy as np
import torch.utils.data as Data
import os
import random



##############
size = 20
##############

torch.manual_seed(1)

EPOCH = 2
BATCH_SIZE = 100
LR = 0.001

training_dir = os.sep.join(['.', 'Task6', 'Arrays', 'image', str(size) + '_train.npy'])
testing_dir = os.sep.join(['.', 'Task6', 'Arrays', 'image', str(size) + '_test.npy'])
training_label_dir = os.sep.join(['.', 'Task6', 'Cache', 'hygiene.dat.labels.train'])

class ReviewData(Data.Dataset):

    def __init__(self, data_path: str, label_path:str):
        self.data = np.load(data_path)
        self.label = []
        with open(label_path, 'r') as label_f:
            content = label_f.readlines()
            for label in content:
                self.label.append((int)(label))
        
    def __getitem__(self, index):
        array, label = self.data[index], self.label[index]
        return torch.tensor([array], dtype=torch.float32), label

    def __len__(self):
        return len(self.data)
        

total_data = ReviewData(training_dir, training_label_dir)

train_data, validation_data = torch.utils.data.random_split(total_data, [len(total_data) - 100, 100])
print(len(train_data))
print(len(validation_data))

train_loader = Data.DataLoader(dataset=train_data, batch_size=BATCH_SIZE, shuffle=True)

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Sequential(  #(1, size, size)
            nn.Conv2d(
                in_channels=1,      
                out_channels=16,    
                kernel_size=5,      
                stride=1,          
                padding=2,      
            ),      #(16, size, size)
            nn.ReLU(),    
            nn.MaxPool2d(kernel_size=2), #(16, size/2, size/2)    
        )
        self.conv2 = nn.Sequential(  #input: (16, size/2, size/2)
            nn.Conv2d(16, 32, 5, 1, 2),  #(32, size/2, size/2)
            nn.ReLU(),  
            nn.MaxPool2d(2),  # (32, size/4, size/4)
        )
        self.out = nn.Linear(32 * (int)(size/4) * (int)(size/4), 10)   

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = x.view(x.size(0), -1)   
        output = self.out(x)
        return output

cnn = CNN()
print(cnn)

optimizer = torch.optim.Adam(cnn.parameters(), lr=LR)
loss_func = nn.CrossEntropyLoss()
"""
for i in range(100):
    print(i)
    for step, (b_x, b_y) in enumerate(train_loader):
        #print(step, b_x, b_y)
        #b_x = torch.tensor(b_x, dtype=torch.float32)
        output = cnn(b_x)
        loss = loss_func(output, b_y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
"""
"""
count  = 0
for i in range(100):
    data, label = validation_data[i]
    
    result=cnn(torch.unsqueeze(data, dim=1))
    result = 0 if result[0][0] > result[0][1] else 1
    if (result == label):
        count+=1
    print(result, label)
print(count/100)
"""

"""
test_data = np.load(testing_dir)
print(len(test_data))
with open('./Task6/Results/'+str(size)+'epoch_result.txt', 'a') as f:
    f.write('Bunni'+'\n')
    for data in test_data:
        data = torch.tensor([[data]], dtype=torch.float32)
        #data = torch.unsqueeze(data, dim=2)
        result = cnn(data)
        label = 0 if result[0][0]>result[0][1] else 1
        print(label)
        f.write(str(label) + '\n')
    f.close()
"""

"""
with open('./Task6/Cache/'+str(size)+'_nn_array_train.txt', 'a') as f:
    f.write('Bunni'+'\n')
    for data, label in total_data:
        data = torch.unsqueeze(data, dim=1)
        result = cnn(data)
        result = result[0].tolist()
        print(result)
        for number in result:
            f.write(str(number) + ', ')
        f.write('\n')
    f.close()
""""""

""""""
test_data = np.load(testing_dir)
print(len(test_data))
with open('./Task6/Cache/'+str(size)+'_nn_array_test.txt', 'a') as f:
    f.write('Bunni'+'\n')
    for data in test_data:
        data = torch.tensor([[data]], dtype=torch.float32)
        #data = torch.unsqueeze(data, dim=2)
        result = cnn(data)
        result = result[0].tolist()
        print(result)
        for number in result:
            f.write(str(number) + ', ')
        f.write('\n')
    f.close()
"""

