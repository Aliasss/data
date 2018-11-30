f = open("C:/Users/seob/Desktop/test1.txt", "r")
lines = f.read()

from konlpy.tag import Okt
nlpy = Okt()
nouns = nlpy.nouns(lines)
print(nouns)

from collections import Counter

count = Counter(nouns)

tag_count = []
tags = []

for n, c in count.most_common(100):
    dics = {'tag': n, 'count': c}
    if len(dics['tag']) >= 2 and len(tags) <= 49:
        tag_count.append(dics)
        tags.append(dics['tag'])

for tag in tag_count:
    print(" {:<14}".format(tag['tag']), end='\t')
    print("{}".format(tag['count']))