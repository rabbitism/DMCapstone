import os
import json

business_dir = os.sep.join(['.', 'yelp_dataset_challenge_academic_dataset', 'yelp_academic_dataset_business.json'])
categories_dir = os.sep.join(['.', 'Task7', 'categories.csv'])
business_id_dir = os.sep.join(['.', 'Task7', 'business_ids.json'])


categories = set()

with open(business_dir, 'r') as f:
    for i in f.readlines():
        content = json.loads(i)
        cats = content["categories"]
        for cat in cats:
            categories.add(cat)
            print(len(categories))

with open(categories_dir, 'a') as f:
    for i in categories:
        f.write(i+'\n')


categories = dict()

with open(business_dir, 'r') as f:
    for i in f.readlines():
        content = json.loads(i)
        cats = content["categories"]
        if ('Restaurants' not in cats):
            #print(cats)
            continue
        else:
            for cat in cats:
                if (cat in categories.keys()):
                    categories[cat] += 1
                else:
                    categories[cat] = 1

sorted_items = sorted(categories.items(), key = lambda x:x[1], reverse=True)

with open(categories_dir, 'w') as f:
    for i in sorted_items:
        if (i[1] < 100):
            continue
        if (i[0] == 'Restaurants'):
            continue
        f.writelines(i[0]+','+str(i[1])+'\n')


categories = set()

business_info = {}

with open(categories_dir, 'r') as f:
    for line in f.readlines():
        category = line.split(',')[0]
        categories.add(category)

with open(business_dir, 'r') as f:
    for line in f.readlines():
        content = json.loads(line)
        business_id = content["business_id"]
        cats = content["categories"]
        flag = False
        for cat in cats:
            if (cat in categories):
                flag = True
        if flag:
            business_info[business_id] = cats

with open(business_id_dir, 'w') as f:
    content = json.dumps(business_info)
    f.write(content)

