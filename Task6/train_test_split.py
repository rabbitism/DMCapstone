import os

review_dir = os.sep.join(['.', 'Task6', 'Cache', 'hygiene.dat'])
label_dir = os.sep.join(['.', 'Task6', 'Dataset', 'hygiene.dat.labels'])
data_dir = os.sep.join(['.', 'Task6', 'Dataset', 'hygiene.dat.additional'])

train_review_dir = os.sep.join(['.', 'Task6', 'Cache', 'hygiene.dat.train'])
train_label_dir = os.sep.join(['.', 'Task6', 'Cache', 'hygiene.dat.labels.train'])
train_data_dir = os.sep.join(['.', 'Task6', 'Cache', 'hygiene.dat.additional.train'])

test_review_dir = os.sep.join(['.', 'Task6', 'Cache', 'hygiene.dat.test'])
test_data_dir = os.sep.join(['.', 'Task6', 'Cache', 'hygiene.dat.additional.test'])


def main():
    with open(label_dir, 'r') as labels_f, open(review_dir, 'r') as reviews_f, open(data_dir, 'r') as data_f:
        #print(len(data.readlines()))
        #length = len(labels_f.readlines())
        labels = labels_f.readlines()
        reviews = reviews_f.readlines()
        data = data_f.readlines()
        #print(labels)
        length = len(labels)
        """"""
        for i in range(length - 1):
            print(i, labels[i])
            if (labels[i][0] in ["0", "1"]):
                with open(train_review_dir, 'a') as train_review_f, open(train_label_dir, 'a') as train_label_f, open(train_data_dir, 'a') as train_data_f:
                    train_review_f.write(reviews[i])
                    train_label_f.write(labels[i])
                    train_data_f.write(data[i])
            else:
                with open(test_review_dir, 'a') as test_review_f, open(test_data_dir, 'a') as test_data_f:
                    test_review_f.write(reviews[i])
                    test_data_f.write(data[i])
        """
        labels_f.close()
        reviews_f.close()
        data_f.close()
        train_review_f.close()
        train_label_f.close()
        train_data_f.close()
        test_review_f.close()
        test_data_f.close()
        """
        """"""
                
                


if __name__ == "__main__":
    main()