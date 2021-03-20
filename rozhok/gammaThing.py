


from random import choice

alphabet = [x for x in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя']
rank = list(range(33))

k = 6
gamma = rank



rankedAlphabet = {alphabet[i] : rank[i] for i in range(33)}
reversedRankedAlphabet = {rank[i] : alphabet[i] for i in range(33)}


opentext1 = [x for x in 'имитостойкостьшифра']
opentext2 = [x for x in 'ккриптографическому']

gammaRow = [choice(gamma) for i in range(len(opentext1))]


#cipherText = [reversedRankedAlphabet[list(map(lambda x, y: (rankedAlphabet[x] + y)%33, opentext, gammaRow))[i]] for i in range(len(opentext))]
#rankedCipherText = list(map(lambda x, y: (rankedAlphabet[x] + y)%33, opentext, gammaRow))

def cipher(opentext, gammaRow):
    return [reversedRankedAlphabet[list(map(lambda x, y: (rankedAlphabet[x] + y)%33, opentext, gammaRow))[i]] for i in range(len(opentext))]

def rankText(text, gammaRow):
    return list(map(lambda x, y: (rankedAlphabet[x] + y)%33, text, gammaRow))

cipherText1 = cipher(opentext1, gammaRow)
cipherText2 = cipher(opentext2, gammaRow)

print(*opentext1, sep = ',')
print(*rankText(opentext1, [0 for i in range(len(opentext1))]), sep = ',')

print(*opentext2, sep = ',')
print(*rankText(opentext2, [0 for i in range(len(opentext2))]), sep = ',')

print(*gammaRow, sep = ',')


print(*rankText(cipherText1, [0 for i in range(len(opentext1))]), sep = ',')
print(*cipherText1, sep = ',')


print(*rankText(cipherText2, [0 for i in range(len(opentext1))]), sep = ',')
print(*cipherText2, sep = ',')



#print(*list(map(lambda x: reversedRankedAlphabet[(x  - gamma[0])%33], rankedCipherText)), sep = ',')
#print(*list(map(lambda x: reversedRankedAlphabet[(x  - gamma[1])%33], rankedCipherText)), sep = ',')

#print(*[reversedRankedAlphabet[list(map(lambda x, y: (rankedAlphabet[x] + gammaRow[0])%33, opentext))[i]] for i in range(len(opentext))], sep = ',')
#print(*[reversedRankedAlphabet[list(map(lambda x, y: (rankedAlphabet[x] + gammaRow[1])%33, opentext))[i]] for i in range(len(opentext))], sep = ',')



#print(*list(map(lambda x: (rankedAlphabet[x])%33, opentext)), sep = ',')



#print(*opentext, sep = ',')
print()
