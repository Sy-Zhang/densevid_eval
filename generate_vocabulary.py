import re
import json

def word_tokenize(s):
    sent = s.lower()
    sent = re.sub('[^A-Za-z0-9\s]+',' ', sent)
    return sent.split()

if __name__ == '__main__':

    glove_dim = 300
    glove_path = '/localdisk/szhang83/Developer/LocalizingMoments/data/glove.6B.%dd.txt' % glove_dim
    glove_txt = open(glove_path).readlines()
    glove_txt = [g.strip() for g in glove_txt]
    glove_vector = [g.split(' ') for g in glove_txt]
    glove_words = [g[0] for g in glove_vector]

    txt_path = 'data/vocab_glove_complete.txt'
    vocab_file = open(txt_path, 'w')
    words = []
    for split in ['train','val_1', 'val_2']:
        anno_list = json.load(open('data/{}.json'.format(split)))

        for info in anno_list.values():
            for sentence in info['sentences']:
                sentence = sentence.split('.')[0]
                words.extend(word_tokenize(sentence))
    valid_words = list(filter(lambda w: w in glove_words, set(words)))
    vocab_file.write('\n'.join(set(valid_words)))


