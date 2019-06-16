removed = []
update = []

with open('Task3/Labels/indian.label') as orignal, open('Task3/Labels/indian_update.label') as updated:
    orignal_labels = orignal.readlines()
    orignal_dict = {}
    update_dict = {}
    for line in orignal_labels:
        info = line.split('\t')
        #print(info[0])
        orignal_dict[info[0]] = info[1].replace('\n','')
    #print(orignal_dict)
    updated_labels = updated.readlines()
    for line in updated_labels:
        #print(line)
        info = line.split('\t')
        update_dict[info[0]] = info[1].replace('\n', '')
    for key in orignal_dict.keys():
        if (key not in update_dict.keys()):
            removed.append(key)
    for key in update_dict.keys():
        if (update_dict[key] != orignal_dict[key]):
            update.append(key)
orignal.close()
updated.close()

print(removed)
print(update)
with open('Task3/removed.txt', 'w') as removed_file:
    removed_file.writelines('\n'.join(removed))
removed_file.close()
with open('Task3/update.txt', 'w') as update_file:
    update_file.writelines('\n'.join(update))
update_file.close() 
        
        