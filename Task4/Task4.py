import os
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

path2files = "yelp_dataset_challenge_academic_dataset/"
path2buisness=path2files+"yelp_academic_dataset_business.json"
path2reviews = path2files + "yelp_academic_dataset_review.json"
path2dishname = os.sep.join(['.', 'Task4', 'student_dn_annotations.txt'])



def extract_cuisine(cuisine: str):
    cuisine_restaurants = os.sep.join(['.', 'Task4', cuisine + ".txt"])
    print("Start to extract cuisine", cuisine, "restaurants to", cuisine_restaurants)
    with open(path2buisness, 'r') as business, open (cuisine_restaurants, 'w+') as restaurants:
        for line in business.readlines():
            business_json = json.loads(line)
            bjc = business_json['categories']
            if (cuisine in bjc):
                restaurants.write(line)
        business.close()
        restaurants.close()

def extract_cuisine_business_id(cuisine:str):
    cuisine_restaurants = os.sep.join(['.', 'Task4', cuisine + ".txt"])
    business_id = set()
    with open(cuisine_restaurants, 'r') as f:
        for line in f.readlines():
            business_json = json.loads(line)
            print(business_json['categories'])
            business_id.add(business_json['business_id'])
        f.close()
    print("Loaded", len(business_id), "restaurants.")
    return business_id

def extract_cuisine_reviews(cuisine: str, ids: set):
    cuisine_reviews = os.sep.join(['.', 'Task4', cuisine+'_reviews.txt'])
    with open(path2reviews, 'r') as reviews, open(cuisine_reviews, 'w') as creviews:
        print("Start to extract reviews...")
        for line in reviews.readlines():
            review_json = json.loads(line)
            if (review_json['business_id'] in ids):
                creviews.write(line)
        creviews.close()
        reviews.close()

def count(cuisine: str):
    cuisine_reviews = os.sep.join(['.', 'Task4', cuisine+'_reviews.txt'])
    dish_ratings = {}
    with open(path2dishname, 'r') as f:
        for line in f.readlines():
            dish_name = line.strip()
            print(dish_name)
            dish_ratings[dish_name] = {'amount': 0, 'count': 0}
    with open(cuisine_reviews, 'r') as reviews:
        count = 0
        for line in reviews.readlines():
            review_json = json.loads(line)
            review = review_json['text'].lower()
            print(count)
            count += 1
            rating = review_json['stars']
            for key in dish_ratings.keys():
                if (key in review):
                    dish_ratings[key]['amount'] += rating
                    dish_ratings[key]['count'] += 1
    return dish_ratings

def sort():
    ratings = {}
    with open(os.sep.join(['.', 'Task4', 'ratings.json']), 'r') as f:
        content = f.read()
        ratings = json.loads(content)
    print(ratings)
    amount = {}
    count = {}
    average = {}
    for key in ratings.keys():
        amount[key] = ratings[key]['amount']
        count[key] = ratings[key]['count']
        average[key] = 0 if ratings[key]['amount'] == 0 else ratings[key]['amount'] / ratings[key]['count']
    with open(os.sep.join(['.', 'Task4', 'summary.csv']), 'w') as f:
        f.write(','.join(['dish_name', 'amount', 'count', 'average'])+'\n')
        for key in ratings.keys():
            f.write(','.join([key, str(ratings[key]['amount']), str(ratings[key]['count']), str(0 if ratings[key]['amount'] == 0 else ratings[key]['amount'] / ratings[key]['count'])])+'\n')

    sorted_amount = sorted(amount.items(), key=lambda d: d[1], reverse=True)
    sorted_count = sorted(count.items(), key=lambda d: d[1], reverse=True)
    sorted_average = sorted(average.items(), key=lambda d: d[1], reverse=True)
    print(sorted_amount)
    with open(os.sep.join(['.', 'Task4', 'amount.csv']), 'w') as f:
        for i in sorted_amount:
            f.write(i[0] + ',' + str(i[1]) + '\n')
    with open(os.sep.join(['.', 'Task4', 'count.csv']), 'w') as f:
        for i in sorted_count:
            f.write(i[0] + ',' + str(i[1]) + '\n')
    with open(os.sep.join(['.', 'Task4', 'average.csv']), 'w') as f:
        for i in sorted_average:
            f.write(i[0]+','+str(i[1])+'\n')

def tf_idf():
    vectorizor = TfidfVectorizer()
    reviews = []
    cuisine_reviews = os.sep.join(['.', 'Task4', 'Chinese_reviews.txt'])
    stemmer = PorterStemmer()
    with open(cuisine_reviews, 'r') as f:
        for line in f.readlines():
            review_json = json.loads(line)
            text = word_tokenize(review_json['text'])
            stemmed_text = [stemmer.stem(word) for word in text]
            reviews.append(' '.join(stemmed_text))
    
    print('test')

if __name__ == "__main__":
    cuisine = "Chinese"
    #extract_cuisine(cuisine)
    #ids = extract_cuisine_business_id(cuisine)
    #extract_cuisine_reviews(cuisine, ids)
    """
    ratings = count(cuisine)
    
    with open(os.sep.join(['.', 'Task4', 'ratings.json']), 'w') as f:
        json.dump(ratings, f, ensure_ascii=False)
    """
    #sort()
    #tf_idf()
    print("Done")
    
