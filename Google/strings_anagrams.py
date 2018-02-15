"""
Write a python module to return the number of unmatched characters between two input strings.
Example:
    string1 = abcdefgh
    string2 = abcghij
    unmatched count= 5 (def ij)

>>> unmatched_alphabet_count("abcdefgh","abcghij")
5
"""
def unmatched_alphabet_count(a, b):
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
    #print(dictionary_a)

    for index in range(len(b)):
        count = dictionary_b.get(b[index])
        if count == None:
            count = 1
        else:
            count += 1
        dictionary_b[b[index]] = count
    #print(dictionary_b)

    for key, value in dictionary_a.items():
        if dictionary_b.get(key) == None:
            total_unmatched_count += value

    for key, value in dictionary_b.items():
        if dictionary_a.get(key) == None:
            total_unmatched_count += value

    return total_unmatched_count


#a = input().strip().split(' ')
#b = input().strip().split(' ')

a = input().strip()
b = input().strip()

print(unmatched_alphabet_count(a, b))

if __name__ == "__main__":
    import doctest
    doctest.testmod()