'''

From a given passage find the longest and shortest word 
and print the same. Accept the passage as an input from user.

'''

import re
#giving input passage
passage="Without Dreams, life is like chasing an invisible shadow that has no substance or meaning. Even those who succeeded in life had to chase the Dreams that made them like today. Interestingly, such people do not give up their Dreams and set new standards in life one after another in order to reach the pinnacle of success."

words=passage.split()
shortest_words=set()

shortest_words= words.findall(min(words, key=len))

print("Shortest words:", shortest_words)
