# CES-22: Programação Orientada à Objeto
# Professor: Yano
# Código utilizado para Questão 3 da Lista 2 de Python
# Escrito por Lucas do Vale Bezerra, COMP-22

import sys   

def test(did_pass): # Printa o resultado do teste
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Teste na linha {0} deu certo.".format(linenum)
    else:
        msg = "Teste na linha {0} deu ERRADO.".format(linenum)
    print(msg)

def cleanword(word):
    cleanword = ""
    for caractere in word:
        if caractere.isalpha():
            cleanword += caractere
    return cleanword

def has_dashdash(word):
    for i in range(len(word) - 1):
        if (word[i] == "-") and (word[i+1] == "-"):
            return 1
    return 0

def extract_words(phrase):
    phrase = phrase.lower()
    for caractere in phrase:
        if not caractere.isalpha():
            phrase = phrase.replace(caractere," ")
    wds = phrase.split()
    return wds

def wordcount(word, phrase):
    cont = phrase.count(word)
    return cont

def wordset(list):
    wordset = []
    for i in list:
        if i not in wordset:
            wordset.append(i)
    wordset.sort()
    return wordset

def longestword(list):
    maior = 0
    for i in range(len(list)):
        if len(list[i]) > maior:
            maior = len(list[i])
    return maior

def test_suite():
    # Testes função cleanword
    test(cleanword("what?") == "what")
    test(cleanword("'now!'") == "now")
    test(cleanword("?+='w-o-r-d!,@$()'") == "word")

    # Testes função has_dashdash
    test(has_dashdash("distance--but"))
    test(not has_dashdash("several"))
    test(has_dashdash("spoke--"))
    test(has_dashdash("distance--but"))
    test(not has_dashdash("-yo-yo-"))

    # Testes função extract_words
    test(extract_words("Now is the time! 'Now', is the time? Yes, now.") == ['now','is','the','time','now','is','the','time','yes','now'])
    test(extract_words("she tried to curtsey as she spoke--fancy") == ['she','tried','to','curtsey','as','she','spoke','fancy'])

    # Testes função wordcount
    test(wordcount("now", ["now","is","time","is","now","is","is"]) == 2)
    test(wordcount("is", ["now","is","time","is","now","the","is"]) == 3)
    test(wordcount("time", ["now","is","time","is","now","is","is"]) == 1)
    test(wordcount("frog", ["now","is","time","is","now","is","is"]) == 0)

    # Testes função wordset
    test(wordset(["now", "is", "time", "is", "now", "is", "is"]) == ["is", "now", "time"])
    test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) == ["I", "a", "am", "is"])
    test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) == ["a", "am", "are", "be", "but", "is", "or"])

    # Testes função longestword
    test(longestword(["a", "apple", "pear", "grape"]) == 5)
    test(longestword(["a", "am", "I", "be"]) == 2)
    test(longestword(["this","supercalifragilisticexpialidocious"]) == 34)
    test(longestword([ ]) == 0)

test_suite()