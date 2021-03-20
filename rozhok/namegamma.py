from random import choice

alphabet = [x for x in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя']
rank = list(range(33))


rankedAlphabet = {alphabet[i] : rank[i] for i in range(33)}
reversedRankedAlphabet = {rank[i] : alphabet[i] for i in range(33)}

def cipher(opentext, gammaRow):
    return [reversedRankedAlphabet[list(map(lambda x, y: (rankedAlphabet[x] + y)%33, opentext, gammaRow))[i]] for i in range(len(opentext))]

def rankText(text, gammaRow):
    #print(gammaRow)
    return list(map(lambda x, y: (rankedAlphabet[x] + y)%33, text, gammaRow))

def genGamma(opentext, gammatext):
    return (rankText(gammatext, [0 for i in range(len(gammatext))])*len(opentext))[:len(opentext)]



opentext1 = [x for x in 'двадцатоемарта']

gammatext1 = [x for x in 'октябрь']

gammaRow = genGamma(opentext1, gammatext1)

sumgamma = [(gammaRow[i] + rankText(opentext1, [0 for i in range(len(opentext1))])[i])%33 for i in range(len(opentext1))]

cipherText1 = [reversedRankedAlphabet[x] for x in sumgamma]


print(*opentext1, sep = ',')
print(*rankText(opentext1, [0 for i in range(len(opentext1))]), sep = ',')

print(*((gammatext1*len(opentext1))[:len(opentext1)]), sep = ',')
print(*gammaRow, sep = ',')


print(*sumgamma, sep = ',')

print(*cipherText1, sep = ',')

print()
