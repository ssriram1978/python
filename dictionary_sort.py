from operator import itemgetter, attrgetter, methodcaller, concat

class dictionary_sort :

    def __init__(self):
        self.dict={}
        self.sorted_dict=[]

    def getattribute(self,object):
        if(object==None):
            return 0
        else:
            return object

    def dictionary_sort_this_input(self,string1):
        index=0
        length=len(string1)
        for index in range(length) :
            character=string1[index]
            #print(character)
            occurance=self.dict.get(character)
            if occurance == None:
                self.dict[character] = 1
            else:
                occurance+=1
                self.dict[character]=occurance
        sorted_dict=sorted(self.dict.items(),key=itemgetter(1),reverse=True)
        return sorted_dict

    def print_dict_sorted_array(self,sorted_dict):
        count = sorted_dict[0][1]
        index = 0
        for index in range(count, 0, -1):
            concat_name = None
            for name, value in sorted_dict:
                if (value >= index and name != None):
                    if (concat_name == None):
                        concat_name = name
                    else:
                        concat_name = concat(concat_name, name)
            if (concat_name != None):
                print(concat_name)

    def return_object(self):
        return self.dict[0]


dict=dictionary_sort()
sorted_dict=[]
sorted_dict=dict.dictionary_sort_this_input("ecdcadcdcec")
print(sorted_dict)
dict.print_dict_sorted_array(sorted_dict)
