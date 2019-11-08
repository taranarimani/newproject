from hazm import *
import re
import io


def query_process(query):
    str = normalizer.normalize(query)
    str = str.translate(str.maketrans(';،=$&@-/:<>+.()«»؟', '                  ', '\u200c'))
    words = word_tokenize(str)
    words = list(dict.fromkeys(words))
    i = 0
    added_words = []
    while i < len(words):
        while True:
            if i >= len(words): break
            repeat = False
            word = words[i]
            for group in samewords:
                if word == group[0]:
                    added_words = added_words + group[1:]

            lem_word = lemmatizer.lemmatize(word).split('#')[0]
            if lem_word == '':
                lem_word = 'است'
            if word in stopwords or lem_word in stopwords:
                words.remove(word)
                repeat = True
            if repeat == False:
                break
        words[i] = lem_word
        i = i + 1
    #return str_from_words #####################################################
    return words, added_words #####################################################


stopwords_f = open('stop_words.txt', 'r', encoding='utf-8')
stopwords = stopwords_f.readlines()
for i in range(len(stopwords)):
    stopwords[i] = stopwords[i].replace("\n", "")
samewords_f = open('same_words.txt', 'r', encoding='utf-8')
samewords = samewords_f.readlines()
#samewords_tokens = word_tokenize(samewords_f.read(),"\n")
for i in range(len(samewords)):
    samewords[i] = samewords[i].replace("\n", "")
    samewords[i] = word_tokenize(samewords[i])
print('same=' + str(samewords))
samewords_f.close()
stopwords_f.close()
print('stop='+str(stopwords))

lemmatizer = Lemmatizer()
normalizer = Normalizer()
print(query_process("ما تو را بچه کتابهای به برای دوست داریم خودرو را هنوز"))