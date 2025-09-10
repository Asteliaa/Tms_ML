words = ['крот', 'белка', 'выхухоль']

def all_eq(lst):
    maxlen = max(len(word) for word in lst)
    return [word + '_' * (maxlen - len(word)) for word in lst]

after_words = all_eq(words)
print(after_words)
