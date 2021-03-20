alphabet = [x for x in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя']
rank = list(range(33))

k = 6
gamma = rank



rankedAlphabet = {alphabet[i] : rank[i] for i in range(33)}
reversedRankedAlphabet = {rank[i] : alphabet[i] for i in range(33)}

def cipher(opentext, gammaRow):
    return [reversedRankedAlphabet[list(map(lambda x, y: (rankedAlphabet[x] + y)%33, opentext, gammaRow))[i]] for i in range(len(opentext))]

def rankText(text, gammaRow):
    return list(map(lambda x, y: (rankedAlphabet[x] + y)%33, text, gammaRow))

def decipher(cipherText, gammaRow):
    return [reversedRankedAlphabet[list(map(lambda x, y: (rankedAlphabet[x] - y)%33, cipherText, gammaRow))[i]] for i in range(len(cipherText))]

opentext1 = [x for x in 'щъевйегмзаинчхбсакыыпяъп']

sample1 = [x for x in 'дремлешь']

sampGamma = [21,20,2,29,18,31,29,19]

for i in range(len(opentext1) - len(sample1)):
    print(*decipher(opentext1[i:i+len(sampGamma)], sampGamma), sep = '')
