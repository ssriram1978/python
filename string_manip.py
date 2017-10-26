def ransom_note(magazine, ransom):
    dictionary_magazine={}
    match_found=1

    for index in range(len(magazine)):
        count=dictionary_magazine.get(magazine[index])
        if count == None:
            count=1
        else:
            count+=1
        dictionary_magazine[magazine[index]]=count

    for index in range(len(ransom)):
        if dictionary_magazine.get(ransom[index]) == None:
            match_found=0
            break

    return match_found

#m, n = map(int, input().strip().split(' '))
magazine_name="hello this is sriram from westford"
ransom_name="sriram westford"

#magazine = input().strip().split(' ')
#ransom = input().strip().split(' ')
magazine = magazine_name.strip().split(' ')
ransom = ransom_name.strip().split(' ')
answer = ransom_note(magazine, ransom)
if (answer):
    print("Yes")
else:
    print("No")
