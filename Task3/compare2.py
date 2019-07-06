removed = []
update = []

with open('Task3/unified.csv') as result, open('Task3/update_labels.label', 'w') as label_file:
    result_content = result.readlines()
    for line in result_content:
        token = line.split(',')[0]
        words = token.split('_')
        label_file.write(' '.join(words)+'\n')
result.close()
label_file.close()
        
        