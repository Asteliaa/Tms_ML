temp_list = [1, 3, 4, 8, 2]

def useless(numbers):
    if not numbers:
        return None
    min_num = min(numbers)
    length = len(numbers)
    return min_num / length

print(useless(temp_list))
