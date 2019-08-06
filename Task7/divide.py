import os
import json

categories_dir = os.sep.join(['.', 'Task7', 'categories.csv'])
category_review_root = os.sep.join(['.', 'Task7', 'Categories'])
business_id_dir = os.sep.join(['.', 'Task7', 'business_ids.json'])
reviews_dir = os.sep.join(['.', 'yelp_dataset_challenge_academic_dataset', 'yelp_academic_dataset_review.json'])

categories = set()
business_info = {}

with open(categories_dir, 'r') as f:
    for line in f.readlines():
        category = line.split(',')[0]
        categories.add(category)

print(len(categories))

with open(business_id_dir, 'r') as f:
    content = json.loads(f.read())
    business_info = content

#print(business_info)


with open(reviews_dir, 'r') as f:
    count = 0
    for line in f.readlines():
        count += 1
        print(count)
        content = json.loads(line)
        id = content["business_id"]
        if (id not in business_info.keys()):
            continue
        review = content["text"]
        cats = business_info[id]
        print(id)
        for cat in cats:
            if (cat not in categories):
                continue
            try:
                with open(category_review_root + os.sep + cat + '.txt', 'a') as review_f:
                    review_f.write(review + '\n')
                    review_f.close()
            except:
                continue
    f.close()
    
       




