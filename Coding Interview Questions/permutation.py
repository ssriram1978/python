#permutation of a string

class Solution:

    def permuted_recurse(self, input_string):
        permuted_string_list = []

        #base case, return an empty list.
        if input_string == None or input_string=="" or type(input_string) != str:
            return ""

        #base case, return a list with just one character
        if len(input_string)==1:
            return input_string

        #recurse and find the permutations of the string with no repetitions.
        for index in range(len(input_string)):
            #create a string without the current character.
            split_string=input_string[:index] + input_string[index+1:]
            #send this split string recursively to get the list of recursive strings
            recursive_output_of_strings=self.permuted_recurse(split_string)

            if type(recursive_output_of_strings) == str:
                #just prepend the current character to it
                recursive_output_of_strings=input_string[index]+recursive_output_of_strings
                #append the current string to the list.
                permuted_string_list.append(recursive_output_of_strings)
            else:
                #it is a list
                #walk through the list and append the current character to all the elements in the list
                for index2 in range(len(recursive_output_of_strings)):
                    recursive_output_of_strings[index2]=input_string[index]+recursive_output_of_strings[index2]
                #now append this list to the original permuted string list
                permuted_string_list+=recursive_output_of_strings

            #print(permuted_string_list)

        return permuted_string_list

    def permutation(self,input_string):
        return self.permuted_recurse(input_string)

sol=Solution()
print(sol.permutation("sriram"))
