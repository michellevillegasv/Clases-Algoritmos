dictionary_translate = {}
x = " "
words = input("Enter the word and its translate (format: word:translate1 , word:translate1):  ")
words_pair=words.split(",")
for translation in words_pair:
    word_translate= translation.split(":")
    trans_key = word_translate[0]
    trans_value = word_translate [1]
    dictionary_translate[trans_key]= trans_value
print[dictionary_translate]
spanish = ("Enter your phrase in spanish: ")
separate = list(spanish.split(" "))
for spanish1 in separate:
        x+=dictionary_translate.get(spanish1, spanish1)
        x= " "
print(x)
        
    
