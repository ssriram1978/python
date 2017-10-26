def number_needed(a, b):
    dictionary_a = {}
    dictionary_b = {}
    total_unmatched_count = 0
    for index in range(len(a)):
        count = dictionary_a.get(a[index])
        if count == None:
            count = 1
        else:
            count += 1
        dictionary_a[a[index]] = count

    for index in range(len(b)):
        count = dictionary_b.get(b[index])
        if count == None:
            count = 1
        else:
            count += 1
        dictionary_b[b[index]] = count

    for key, value in dictionary_a.items():
        if dictionary_b.get(key) == None:
            total_unmatched_count += value

    for key, value in dictionary_b.items():
        if dictionary_a.get(key) == None:
            total_unmatched_count += value

    return total_unmatched_count


a = input().strip()
b = input().strip()

print(number_needed(a, b))