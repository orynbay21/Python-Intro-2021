#Write a function that accepts string from user, return a sentence with the words reversed. 
#We are ready -> ready are We
def reversed_sentence(sentence):
    sentence1=sentence.split(' ')
    sentence1.reverse()
    print(*sentence1)
reversed_sentence("We Are Ready")