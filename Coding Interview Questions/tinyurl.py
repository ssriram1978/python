#TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl
# and it returns a short URL such as http://tinyurl.com/4e9iAk.
# Design the encode and decode methods for the TinyURL service.
# There is no restriction on how your encode/decode algorithm should work.
# You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

"""
Algorithm:
----------
The encode function should provide a tiny url that can be used as a key to index into a hash table to store the actual url.
The decode function should be able to use this tiny url as a key to fetch the actual url from the hash table.

Tiny url shall contain the following characters.
    'a' to 'z' - 26 elements
    'A' to 'Z' - 26 elements
    '0' to '9' - 10 elements
    Total of 62 elements

    If we were to have 6 place holders for these 62 elements,
    with repetitions, we can have a permutation of 62^6 = 56,800,235,584 or 56 Billion unique url's.

    Now how do we convert long url into tiny url of 6 characters?
    One Simple Solution could be Hashing.
    Use a hash function to convert long string to short string.
    In hashing, there may be collisions (2 long urls map to same short url)
    and we need a unique short url for every long url so that we can access long url back.

    A Better Solution is to use the integer id stored in database (mySQL which auto increments by 1)
     and convert the integer to character string that is at most 6 characters long.
    This problem can basically seen as a base conversion problem where we have a
    10 digit input number and we want to convert it into a 6 character long string.

"""

class Codec:
    def __init__(self):
        self.base_list = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.base = len(self.base_list)
        self.url_list=[]
        self.running_count_of_urls=0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        result = []

        current_index=self.running_count_of_urls

        #check for first entry into list
        if current_index == 0:
            result.append(self.base_list[0])

        while current_index > 0:
            #Get the reminder when dividing index by 62 and use this as the index to get the character from base_list
            result.append(self.base_list[current_index % self.base])
            #Right shift the number or get rid of the lsb
            current_index //= self.base

        #reverse the list and return it as a string
        shorturl="".join(reversed(result))

        #append the longurl to the urlist
        self.url_list.append(longUrl)

        #increment the running count of urls
        self.running_count_of_urls+=1

        return shorturl

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        num = 0
        #convert the short url into a list
        code_list = list(shortUrl)
        #multiply 64 to the power of index (0 to length of the shorturl) and
        # add it to the lsb of the index of the character found in the base_list
        for index, code in enumerate(reversed(code_list)):
            num += self.base_list.index(code) * self.base ** index

        url=""

        if num >=0 and num < self.running_count_of_urls:
            #return the url from the url_list found at this index.
            url = self.url_list[num]

        return url

        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.decode(codec.encode(url))


if __name__ == '__main__':
    sol=Codec()
    shorturl_list=[]
    for index in range(1000000):
        string="www.google"+str(index)+".com"
        shorturl=sol.encode(string)
        shorturl_list.append(shorturl)
        print("Encoded longurl(%s) to shorturl(%s)"%(string,shorturl))
    for index in range(1000000):
        shorturl=shorturl_list[index]
        longurl = sol.decode(shorturl)
        print("Decoded shorturl(%s) to longurl(%s)"%(shorturl, longurl))

