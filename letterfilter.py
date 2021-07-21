class LetterFilter:

    def __init__(self, s):
        self.s = s

def filter_vowels(self):
#create a list of vowels   
    vowels=['a','e','i','o','u']

    string=''

    for ch in self:

       #every consonant in given string i.e self is concatinated to string

       if ch not in vowels:

           string=string+ch

    self=string

    return self


def filter_consonants(self):
#create a list of vowels

    vowels=['a','e','i','o','u']

    string=''

    for ch in self:
        
       #every vowel in given string i.e self is concatinated to string

       if ch in vowels:

           string=string+ch
             
    self=string

    return self  
s = input("Please enter the message:\n")
f = LetterFilter(s)
print(f'processing out consonants from input\n', filter_consonants(s))
print(f'processing out vowels from input\n', filter_vowels(s))
