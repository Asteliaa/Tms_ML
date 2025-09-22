from collections import Counter

def top_3(s):
    s = s.replace(" ", "")
    counter = Counter(s)
    return counter.most_common(3)

text = "Кошка ходит далеко"
print( top_3(text))
