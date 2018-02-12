#'.' Matches any single character.
#'*' Matches zero or more of the preceding element.
#The matching should cover the entire input string (not partial).
#The function prototype should be:
#bool isMatch(const char *s, const char *p)
#
#Some examples:
#isMatch("aa","a") → false
#isMatch("aa","aa") → true
#isMatch("aaa","aa") → false
#isMatch("aa", "a*") → true
#isMatch("aa", ".*") → true
#isMatch("ab", ".*") → true
#isMatch("aab", "c*a*b") → true
"""
The idea is to slide the input string over the pattern.
If you find that the content of the indexes of input string and pattern do not match,
move the index of the pattern by 1 and retry sliding the input string over the pattern.
If the input string matches with the pattern, return true.
If the input string does not match with the pattern, return false.
"""
class Solution:

    def match_string_with_pattern(self,s,p,p_start):
        isMatch=False
        #set the p and s indexes
        p_index=p_start
        s_index=0
        matched_characters=0
        matched_char_array=[]
        # start a loop which iterates over all the characters of p
        while p_index < len(p):
            if p[p_index] == "*":
                if p_index >0 and p[p_index-1]==".":
                    #this means that you can match any character
                    #therefore relax this check and allow any character not necessarily the preceding element
                    matched_char_array.append(s[s_index])
                    matched_characters += 1
                    p_index += 1
                    s_index += 1
                else:
                    if s_index == 0:
                        #special case, allow any character
                        matched_char_array.append(s[s_index])
                        matched_characters += 1
                        p_index += 1
                        s_index += 1
                    else:
                        #print("Going to match "+ s[s_index] + " "+ s[s_index-1])
                        if s[s_index] == s[s_index - 1]:
                            # match zero or more of the preceding element
                            matched_char_array.append(s[s_index])
                            matched_characters+=1
                            p_index+=1
                            s_index+=1
                        else:
                            #no match
                            break
            elif p[p_index] == ".":
                # match any single character
                matched_char_array.append(s[s_index])
                matched_characters+=1
                p_index+=1
                s_index+=1
            elif s[s_index] == p[p_index]:
                # match exact character
                matched_char_array.append(s[s_index])
                matched_characters+=1
                p_index+=1
                s_index+=1
            else:
                break

        #print(matched_char_array)
        if matched_characters == len(s):
            #complete match
            isMatch=True
        else:
            #print("No match found for "+ s[s_index] + " " + s[p_index])
            isMatch=False

        return isMatch

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        isCompleteMatch = False

        if s == None or len(s) == 0 or p == None or len(p) == 0:
            return False
        #start a loop that iterates over all the characters in p.
        for index in range(len(p)):
            isCompleteMatch = self.match_string_with_pattern(s,p,index)
            if isCompleteMatch == True:
                break
        return isCompleteMatch

sol=Solution()
print("sol.isMatch(aa,a) returned %s" %(str(sol.isMatch("aa","a"))))
print("sol.isMatch(aa,aa) returned %s" %(str(sol.isMatch("aa","aa"))))
print("sol.isMatch(aaa,aa) returned %s" %(str(sol.isMatch("aaa","aa"))))
print("sol.isMatch(aa,a*) returned %s" %(str(sol.isMatch("aa","a*"))))
print("sol.isMatch(aa,.*) returned %s" %(str(sol.isMatch("aa",".*"))))
print("sol.isMatch(ab,.*) returned %s" %(str(sol.isMatch("ab",".*"))))
print("sol.isMatch(aab,c*a*b) returned %s" %(str(sol.isMatch("aab","c*a*b"))))