import json
import numpy as np

if __name__ == '__main__':

    for split in ['train','val_1','val_2']:
        anno_list = json.load(open('data/{}.json'.format(split)))
        json_path = 'data/new_{}.json'.format(split)

        data = []
        for vid, info in anno_list.items():
            for (start, end), sentence in zip(info['timestamps'],info['sentences']):
                row = {'video':vid, 'description': sentence, 'times':[[float(start), float(end)]], 'duration':info['duration']}
                data.append(row)
        with open(json_path, 'w') as json_file:
            json.dump(data, json_file)