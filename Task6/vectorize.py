from gensim.models import Word2Vec
import os
import numpy as np
import cv2

def vectorize_reviews(model, reviews: str, size:int):
    sentences = reviews.split('&#160;')
    result = np.zeros(shape=(size, size))
    for sentence in sentences:
        #print(sentence)
        image = vectorize_sentence(model, sentence, size)
        if (image.shape[0] * image.shape[1] == 0):
            continue
        result = result + image
    result = result / len(sentences)
    #print(result)
    return result
    
def vectorize_sentence_dense(model, sentence: str, size: int):
    
    words = sentence.split()
    dictionary = {}
    for word in words:
        if word in dictionary.keys():
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    dictionary_items = [item for item in dictionary.items()]
    items = []
    for item in dictionary_items:
        if item[0] not in model.wv.vocab:
            continue
        else:
            items.append(item)
    #items=sorted(dictionary.items(), key=lambda d: -d[1])
    #print(items)
    result = np.zeros(shape=(len(items), size))
    for i in range(len(items)):
        result[i] = model.wv[items[i][0]]*items[i][1]
    resized = cv2.resize(result, (size, size))
    #print(resized)
    return resized

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
    resized = cv2.resize(result, (size, size))
    return resized
    
    
if __name__ == "__main__":
    size = 10
    model_dir = os.sep.join(['.', 'Task6', 'Cache', 'model_'+str(size)+'.model'])
    model = Word2Vec.load(model_dir)
    vectorize_reviews(model, s, size)
    review_dir = os.sep.join(['.', 'Task6', 'Cache', 'hygiene.dat.test'])
    target_dir = os.sep.join(['.', 'Task6', 'Arrays', str(size)+'_test.npy'])
    result = []
    with open(review_dir, 'r') as review_f:
        reviews = review_f.readlines()
        for i in range(len(reviews)):
            print(i)
            image = vectorize_reviews(model, reviews[i], size)
            result.append(image)
    result = np.array(result)
    np.save(target_dir, result)
