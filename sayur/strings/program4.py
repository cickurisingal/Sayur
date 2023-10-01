########## Program 4
#PigLatin - From the input string, for each word, remove the first chars until a vowek, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay nPythoay (in Python 'o' is the first vowel)

inputSentence = input("Enter the input string: ")
pigLatinKey = 'ay'
vowels = ['a','e','i','o','u']

for word in inputSentence.split(): #gets the word in a sentence
    #take the first chars until a vowel
    first_vowel_index = 0
    # check if the word has more than one char
    for index, char in enumerate(word):#returns both the index and the char in the word
        if char.lower() in vowels:
            first_vowel_index=index
            break
        
if first_vowel_index>0:
    word= word[first_vowel_index:]+word[:first_vowel_index]+pigLatinKey
else:
    word=word+pigLatinKey
    
print(word,end=" ")