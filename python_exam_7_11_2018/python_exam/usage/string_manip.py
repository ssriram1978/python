word = 'Python'
list1=[ord(char) for char in word]
print(list1)
list2=[ chr(x) for x in list1]
word2=''.join(list2)
print(word2)
print( word2[:2] + word2[2:])
print(''.join([word2[x] for x in range(len(word2)-1,-1,-1)]))
print(word2[::-1])
print(word2[::2])
print(word2[-6:])
