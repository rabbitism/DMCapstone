from gensim.models import Word2Vec
import os
import numpy as np
import cv2

def vectorize_reviews(reviews: str, size:int):
    sentences = reviews.split('&#160;')
    result = np.zeros(shape=(size, size))
    for sentence in sentences:
        image = vectorize_sentence(sentence)
        result = result + image
    result = result / len(sentences)
    print(result)
    return result
    
def vectorize_sentence(sentence: str, size: int):
    model_dir = os.sep.join(['.', 'Task6', 'Cache', 'model_'+str(size)+'.model'])
    model = Word2Vec.load(model_dir)
    words = sentence.split()
    dictionary = {}
    for word in words:
        if word in dictionary.keys():
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    items = [item for item in dictionary.items()]
    #items=sorted(dictionary.items(), key=lambda d: -d[1])
    #print(items)
    result = np.zeros(shape=(len(items), size))
    for i in range(len(items)):
        result[i] = model[items[i][0]]*items[i][1]
    resized = cv2.resize(result, (size, size))
    print(resized)
    return resized
    
    
if __name__ == "__main__":
    s = """baguett roll excel although havent tri yet im excit dozenplus type fill croissant offer ridicul low price&#160;chees without ham&#160;blueberri without cream chees&#160;chocol almond&#160;could danger&#160;bad bakeri habit least q bakeri wont go broke get fat&#160;ive tri four differ banh mi ill agre matthew basic one somewhat american&#160;mushroom interest chicken bbq pork obvious&#160;made good place get food inlaw seem exot scari&#160;note self dont publish facebook inlaw might see&#160;q bakeri locat two divid street make slight pain get worth stop want afford varieti use locat favorit bahn mi shop seattl king baguett saw one year pho restaur new bahn mi joint taken resid&#160;dream king baguett chicken bahn mi danc head quick rush inat first examin q bakeri lot welcom old king baguett&#160;varieti bake good case bahn mi regular deli sandwich avail&#160;pork teriyaki chicken bahn mi found didnt quit hit mark plus side q bakeri stingi meat meat flavor juici&#160;teriyaki chicken especi interest ive never bahn mi like quit enjoy&#160;also q bakeri merci light mayonnais&#160;side sandwich lack much kick&#160;tast like american bahn mi asian flavor tone way&#160;baguett also kind disapoint chewi crustyfor brand new place howev think q bakeri lot potenti look forward tri near futur yum alway alway look forward visit famili seattl wa get type bake goodi qs known banh mis usual order banh mi cha lua custom servic get better english obvious second languag mani establish day arent anyway love place&#160;most go vietnames sandwich&#160;usual go veggi one theyr full flavor tofu great assort veggi&#160;dont feel like ive sandwich bread eat actual feel like ive eaten veggi&#160;husband get meat sandwich&#160;say like qs sandwich chicken shred sandwich bigger store great better lit better arrang tidier somehav live franc eaten way though manyapatisseri add qs pastri select tast pretti awesom im talk straight delici pain au chocolat pain aux raisin&#160;also sort candi jar sesam treat&#160;one 2 tabl w 4 6 chair eat&#160;theyr open til 7pm&#160;also take card make handi dont cashon star littl tough communic folk sinc dont speak vietnames&#160;wouldnt problem except weve end wrong food overal great littl place&#160;ill total bring parent come visit weekend thank idea matthewp brought mom came visit love&#160;natur rent never vietnames sandwich great way introduc magic banh mi"""
    vectorize_sentence(s, 20)