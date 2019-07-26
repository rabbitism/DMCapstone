from gensim.models import Word2Vec
import os

class MySentence(object):

    def __init__(self, dirname:str):
        self.dirname = dirname

    def __iter__(self):
        for line in open(self.dirname, 'r'):
            sentences = line.split('&#160;')
            for sentence in sentences:
                print(sentence)
                yield sentence.split()

def train():
    sentences = MySentence(os.sep.join(['.', 'Task6', 'Cache', 'hygiene.dat']))
    model = Word2Vec(sentences, min_count=10, size=100)
    model.save(os.sep.join(['.', 'Task6', 'Cache', 'model.model']))

if __name__ == "__main__":
    train()