'''

From a given passage extract unique words and print them.
Accept the passage as an input from the user

'''

import re
input_passage= "Without Dreams, life is like chasing an invisible shadow that has no substance or meaning. Even those who succeeded in life had to chase the Dreams that made them like today. Interestingly, such people do not give up their Dreams and set new standards in life one after another in order to reach the pinnacle of success."

words= input_passage.split()
print(len(words))
unique_words=set()
for word in words:
    word=word.strip(".,/?:{}[]()")
    word=word.lower()
    unique_words.add(word)
    
print(unique_words)
print(len(unique_words))
