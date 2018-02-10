import re


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # declare a variable that stores the smallest string
        smallest_string = ""
        # declare a variable that stores the smallest string length
        smallest_string_len = 123456
        # declare a variable that stores the smallest string index
        smallest_string_index = 0
        # declare a string variable that stores longest common prefix
        longest_common_prefix = ""
        # declare a string variable that stores current common prefix
        current_common_prefix = ""

        # boundary check for input params
        if strs == None or len(strs) == 0:
            return longest_common_prefix

        # start a for loop to iterate all the elements to find the smallest string
        for index in range(len(strs)):
            # fetch the current string
            current_string = strs[index]
            # compare the string length with the smallest_string and update it.
            if len(current_string) < smallest_string_len:
                smallest_string_len = len(current_string)
                smallest_string = current_string
                smallest_string_index = index

        if len(strs)==1:
            #you just have one string, return this string.
            return strs[0]

        # declare a starting index for the smallest string as 0
        starting_index = 0
        for index in range(smallest_string_len):
            sub_string = smallest_string[starting_index:index + 1]
            #print("sub_string=%s" % (sub_string))
            # declare a boolean variable which is used to find out if the pattern match of the substring is found
            pattern_match = False
            # start another for loop to find the longest common prefix
            for index2 in range(len(strs)):
                # skip the smallest string index because that is the one that you are going to use as the search string
                if index2 == smallest_string_index:
                    continue
                if re.match(sub_string, strs[index2]):
                    # match found, move on to the next string to find a match
                    pattern_match = True
                    continue
                else:
                    # break from the for loop
                    pattern_match = False
                    break
            if pattern_match == True:
                # go to the next character and continue with the pattern match across all strings
                # update current_common_prefix with the current match
                current_common_prefix = sub_string
                # make sure to update the original longest_string if the length of the current prefix is larger.
                if len(current_common_prefix) > len(longest_common_prefix):
                    longest_common_prefix = current_common_prefix
            else:
                # change the starting index for the smallest string to the first non-common character
                # this is to ensure that you walk from the current non common character to the end of the substring.
                starting_index = index

        return longest_common_prefix

sol=Solution()
list=["abcdef","awfasfdef","asfafdefafagfagfeg","srgehytrjtktkdef"]
print(sol.longestCommonPrefix(list))