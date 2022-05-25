def AlphanumericStringSort(sentence):
    sorted_sentence = []
    tmplower = []
    tmpupper = []
    tmpnumber = []
    tmppair = []
    tmpodd = []
    for character in sentence:
        if character.isupper():
            tmpupper.append(character)
        elif character.islower():
            tmplower.append(character)
        elif character.isdigit():
            if int(character) % 2 == 0:
               tmppair.append(character)
            else:
                tmpodd.append(character)
        else:
            raise Exception("It's a not valid character")
    tmpnumber = tmppair + tmpodd    
    sorted_sentence =  tmplower + tmpupper + tmpnumber
    return "".join(sorted_sentence)

res = AlphanumericStringSort("2346asadfsGFAIKSM")
print(res)
