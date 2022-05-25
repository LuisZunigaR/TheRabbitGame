def AlphanumericStringSort(sentence):
    sorted_sentence = []
    tmplower = []
    tmpupper = []
    tmpnumber = []
    tmppair = []
    tmpodd = []
    for i in range(0,len(sentence)):
        if sentence[i].isupper():
            tmpupper.append(sentence[i])
        elif sentence[i].islower():
            tmplower.append(sentence[i])
        else:
            # TODO validate if is a number to avoid issues
            if int(sentence[i]) % 2 == 0:
               tmppair.append(sentence[i])
            else:
                tmpodd.append(sentence[i])

    tmpnumber = tmppair + tmpodd    
    sorted_sentence =  tmplower + tmpupper + tmpnumber
    return "".join(sorted_sentence)

res = AlphanumericStringSort("2346asadfsGFAIKSM")
print(res)
