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
    business_id_mapping = dict()
    with open(path2buisness, 'r') as business, open (cuisine_restaurants, 'w+') as restaurants:
        for line in business.readlines():
            business_json = json.loads(line)
            bjc = business_json['categories']
            if (cuisine in bjc):
                restaurants.write(line)
                business_id_mapping[business_json['business_id']] = business_json['name']
        business.close()
        restaurants.close()
    return business_id_mapping

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

def count(dish_name: str):
    cuisine_reviews = os.sep.join(['.', 'Task4', 'Chinese_reviews.txt'])
    dish_ratings = {}
    with open(cuisine_reviews, 'r') as reviews:
        count = 0
        for line in reviews.readlines():
            review_json = json.loads(line)
            review = review_json['text'].lower()
            print(count)
            count += 1
            rating = review_json['stars']
            restaurant_id = review_json['business_id']
            if (restaurant_id in dish_ratings.keys()):
                dish_ratings[restaurant_id]['amount'] += rating
                dish_ratings[restaurant_id]['count'] += 1
            else:
                dish_ratings[restaurant_id] = {'amount':rating, 'count':1}
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


if __name__ == "__main__":
    cuisine = "Chinese"
    restaurants = extract_cuisine(cuisine)
    #ids = extract_cuisine_business_id(cuisine)
    #extract_cuisine_reviews(cuisine, ids)
    
    ratings = count('chicken')
    with open(os.sep.join(['.', 'Task4', 'restaurant_ratings.csv']), 'w') as f:
        f.write(','.join(['restaurant_name', 'amount', 'count', 'average'])+'\n')
        for key in ratings.keys():
            f.write(','.join([restaurants[key], str(ratings[key]['amount']), str(ratings[key]['count']), str(0 if ratings[key]['count']==0 else ratings[key]['amount']/ratings[key]['count'])])+'\n')
    print(ratings)
    """
    with open(os.sep.join(['.', 'Task4', 'ratings.json']), 'w') as f:
        json.dump(ratings, f, ensure_ascii=False)
    """
    #sort()
    #tf_idf()
    print("Done")
    
