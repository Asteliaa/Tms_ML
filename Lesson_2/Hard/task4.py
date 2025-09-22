
import collections 

def count_it(seq):

    if not seq.isdigit():
        return {}
    
    lst = [int(num) for num in seq]
    cnt = collections.Counter(lst)
    return dict(cnt.most_common(3))

st = input('Введите строки чисел:\n')

print(count_it(st))