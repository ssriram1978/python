#Given a roman numeral, convert it to an integer.

#Input is guaranteed to be within the range from 1 to 3999.

#1. I - The easiest way to note down a number is to make that many marks - little I's.
# Thus I means 1, II means 2, III means 3. However, four strokes seemed like too many....
#2. V - So the Romans moved on to the symbol for 5 - V.
# Placing I in front of the V — or placing any smaller number in front of any larger number — indicates subtraction.
# So IV means 4. After V comes a series of additions - VI means 6, VII means 7, VIII means 8.
#3. X - X means 10. But wait — what about 9? Same deal.
# IX means to subtract I from X, leaving 9. Numbers in the teens, twenties and thirties
# follow the same form as the first set, only with X's indicating the number of tens. So XXXI is 31, and XXIV is 24.
#4. L - L means 50. Based on what you've learned, I bet you can figure out what 40 is.
# If you guessed XL, you're right = 10 subtracted from 50. And thus 60, 70, and 80 are LX, LXX and LXXX.
#5. C - C stands for centum, the Latin word for 100. A centurion led 100 men.
# We still use this in words like "century" and "cent." The subtraction rule means 90 is written as XC.
# Like the X's and L's, the C's are tacked on to the beginning of numbers to indicate how many hundreds there are: CCCLXIX is 369.
#6. D - D stands for 500. As you can probably guess by this time, CD means 400.
# So CDXLVIII is 448. (See why we switched systems?)
#7. M - M is 1,000. You see a lot of Ms because Roman numerals are used a lot to indicate dates.
# For instance, this page was written in the year of Nova Roma's founding,
# 1998 CE (Common Era; Christians use AD for Anno Domini, "year of our Lord"). That year is written as MCMXCVIII.
# But wait! Nova Roma counts years from the founding of Rome, ab urbe condita.
# By that reckoning Nova Roma was founded in 2751 a.u.c. or MMDCCLI.
#8. V - Larger numbers were indicated by putting a horizontal line over them,
# which meant to multiply the number by 1,000.
# Hence the V at left has a line over the top, which means 5,000.
# This usage is no longer current, because the largest numbers usually expressed in the Roman system are dates, as discussed above.

class Solution:
    def __init__(self):
        self.hash_table={}
        self.prepare_hash_table()

    def prepare_hash_table(self):
        self.hash_table['I']=1
        self.hash_table['V'] = 5
        self.hash_table['X'] = 10
        self.hash_table['L'] = 50
        self.hash_table['C'] = 100
        self.hash_table['D'] = 500
        self.hash_table['M'] = 1000

    def get_char_at_location(self,index,s):
        character=''
        character_val=0
        if index < len(s):
            character = s[index]
            try:
                character_val = self.hash_table[character]
            except:
                character_val = 0
        else:
            character_val = 0

        return character_val

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == None:
            return -1

        number=0
        index=0

        while index < len(s):
            first_char_val=self.get_char_at_location(index,s)
            second_char_val=self.get_char_at_location(index+1,s)

            print("first_char_val=(%d),second_char_val=(%d).\n" %(first_char_val,second_char_val))

            if first_char_val < second_char_val:
                #subtract first char val from second char val.
                number+=(second_char_val-first_char_val)
                index+=2
            else:
                #add the first char val to the number
                number += first_char_val
                index += 1

        return number

sol=Solution()
input="MMDCCLXIII"
print("converting %s to num=%d" %(input,sol.romanToInt(input)))