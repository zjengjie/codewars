#Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known for almost always capitalizing every word.

#Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

def toJadenCase(string):
	return ' '.join([w[:1].upper()+w[1:] for w in string.split(' ')])

#other solutions
def toJadenCase2(string):
	return ' '.join(w.capitalize() for w in string.split(' '))

import string
toJadenCase3 = string.capwords

' '.join(map(lambda x: x.capitalize(), string.split(' ')
