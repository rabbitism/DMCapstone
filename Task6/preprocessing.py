import string
import os

import nltk
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import TreebankWordTokenizer

from nltk.corpus import stopwords

def stem_paragraph(stemmer, tokenizer, reviews:str):
    sentences = reviews.split("&#160;")
    result = []
    for sentence in sentences:
        stemmed_sentence = stem_sentence(stemmer, tokenizer, sentence)
        result.append(stemmed_sentence)
    return "&#160;".join(result)


def stem_sentence(stemmer, tokenizer, reviews:str):
    sentences = reviews.lower()
    #print(sentences)
    remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
    no_punctuation = sentences.translate(remove_punctuation_map)
    tokens = tokenizer.tokenize(no_punctuation)
    filtered_tokens = [w for w in tokens if w not in stopwords.words('english')]
    stemmed_tokens = [stemmer.stem(w) for w in filtered_tokens]
    result = " ".join(stemmed_tokens)
    #print(result)
    return result


if __name__ == "__main__":
    print("Start to stem")
    #nltk.download('punkt')
    #nltk.download('stopwords')
    input_dir = os.sep.join(['.', 'Task6', 'Dataset', 'hygiene.dat'])
    output_dir = os.sep.join(['.', 'Task6', 'Cache', 'hygiene.dat'])
    s = "The baguettes and rolls are excellent, and although I haven't tried them yet I'm excited about the dozen-plus types of filled croissants on offer at ridiculously low prices. &#160;Cheese, with or without ham? &#160;Blueberry, with or without cream cheese? &#160;Chocolate, almond? &#160;This could be dangerous. &#160;I have a bad bakery habit, but at least at Q Bakery I won't go broke while I get fat. &#160;I've tried four different banh mi, and I'll agree with Matthew that the basic ones are somewhat Americanized. &#160;Mushroom was more interesting than chicken or BBQ pork, obviously. &#160;That made this a good place to get food for the in-laws that seemed exotic, but not too scary. &#160;(Note to self: don't publish this on Facebook, where the in-laws might see it.) &#160; Q Bakery's location on two divided streets makes it a slight pain to get to, but it's worth a stop if you want affordable variety. This used to be the location of my favorite Bahn Mi shop in Seattle, King Baguettes, so when I saw that, after one year as a Pho restaurant, that a new Bahn Mi joint had taken up residence. &#160;With dreams of King Baguettes' Chicken Bahn Mi dancing in my head I quickly rushed in.At first examination, Q Bakery is a lot more welcoming than the old King Baguette. &#160;There are a variety of baked goods in the cases, and they have both Bahn Mi and regular deli sandwiches available. &#160;I had both a pork and a teriyaki chicken bahn mi, and I found that they didn't quite hit the mark.  On the plus side, Q Bakery is not stingy with the meat, and the meat is both flavorful and juicy. &#160;The teriyaki chicken was especially interesting as I've never had a bahn mi like it before, and I quite enjoyed it. &#160;Also, Q Bakery is mercifully light on the mayonnaise. &#160;On the down side, both my sandwiches lacked much kick. &#160;They tasted like an Americanized bahn mi, with all the asian flavors toned way down. &#160;The baguette itself was also kind of disapointing, being more chewy than crusty.For a brand new place, however, I think Q Bakery has a lot of potential, and I look forward to trying them out again in the near future. YUM! I always, always look forward to visiting my family in Seattle, WA so I can get all types of baked goodies from Q's. They are known for their banh mi's. I usually order the banh mi cha lua.. The customer service, is getting better. English is obviously not their second language, but many establishments these days aren't anyways! Love this place. &#160;We mostly go there for the Vietnamese sandwiches. &#160;I usually go for the veggie ones - they're full of flavorful tofu and a great assortment of veggies. &#160;I don't feel like I've just had a sandwichful of bread after eating there - it actually feels like I've eaten my veggies. &#160;My husband gets the meat sandwiches. &#160;He says he likes Q's sandwiches because chicken is not shredded, the sandwich is \"bigger\" and the store is great because it's better lit, better arranged, and tidier than some.Having lived in France (and eaten my way though many-a-patisserie) I have to add that Q's pastry selection and taste are pretty awesome. I'm talking straight up delicious pains au chocolat and pains aux raisins. &#160;They also have all sorts of candies in jars, and sesame treats. &#160;They have one or 2 tables w/ 4 or 6 chairs for eating in. &#160;They're open til 7pm. &#160;Also, they take cards, which makes it handy if we don't have cash.One star off because it's been a little tough to communicate with the folks there since we don't speak Vietnamese. &#160;Wouldn't be a problem except we've ended up with the wrong food before. Overall, great little place. &#160;And I'll totally be bringing my parents there when they come to visit this weekend - thanks for the idea, Matthew!PS - Brought my mom there when she came for a visit and she loved it. &#160;Naturally, the 'rents had never had a Vietnamese sandwich before; great way to introduce them to the magic of banh mi."
    stemmer = SnowballStemmer(language="english")
    tokenizer = TreebankWordTokenizer()
    stem_sentence(stemmer, tokenizer, s)
    count = 0
    with open(input_dir, 'r', encoding='utf-8') as input_f, open(output_dir, 'w', encoding='utf-8') as output_f:
        for line in input_f:
            count+=1
            output_line = stem_paragraph(stemmer, tokenizer, line)
            output_f.write(output_line+'\n')
            print(count)
            print(output_line[0:min(100, len(output_line))])
        input_f.close()
        output_f.close()
