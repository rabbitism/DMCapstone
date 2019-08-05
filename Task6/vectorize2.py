import numpy as np
from gensim.models import Word2Vec
import os
import cv2

def vectorize_sentence(model, sentence: str, size: int):
    words = sentence.split()
    filtered = []
    for word in words:
        if (word in model.wv.vocab):
            filtered.append(word)
    result = np.zeros(shape=(len(filtered), size))
    for i in range(len(filtered)):
        result[i] = model.wv[filtered[i]]
    if (result.shape[0] * result.shape[1] == 0):
         return result
    result = np.average(result, axis=0)
    #print(result.shape)
    return result

if __name__ == "__main__":
    size = 50
    s = "world food"
    model_dir = os.sep.join(['.', 'Task6', 'Cache', 'model_'+str(size)+'.model'])
    model = Word2Vec.load(model_dir)
    result = vectorize_sentence(model, s, size)
    review_dir = os.sep.join(['.', 'Task6', 'Cache', 'hygiene.dat.test'])
    target_dir = os.sep.join(['.', 'Task6', 'Arrays', str(size)+'_test.npy'])
    print(result)
    result = []
    with open(review_dir, 'r') as review_f:
        reviews = review_f.readlines()
        print(len(reviews))
        for i in range(len(reviews)):
            print(i)
            image = vectorize_sentence(model, reviews[i], size)
            result.append(image)
        
    result = np.array(result)
    np.save(target_dir, result)