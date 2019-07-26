from gensim.models import Word2Vec
import os
import time
import sys

class MySentence(object):

    def __init__(self, dirname:str):
        self.dirname = dirname

    def __iter__(self):
        count = 0
        for line in open(self.dirname, 'r'):
            count += 1
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), count)
            sentences = line.split('&#160;')
            for sentence in sentences:
                #print(sentence)
                print('.', end='')
                yield sentence.split()
            print(" ")

def train(size):
    print(size)
    sentences = MySentence(os.sep.join(['.', 'Task6', 'Cache', 'hygiene.dat']))
    model = Word2Vec(sentences, min_count=10, size=size)
    model.save(os.sep.join(['.', 'Task6', 'Cache', 'model_'+str(size)+'.model']))

if __name__ == "__main__":
    size = (int)(sys.argv[1])
    train(size)