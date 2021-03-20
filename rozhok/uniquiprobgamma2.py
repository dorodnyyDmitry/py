from random import choice

alphabet = [x for x in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя']
rank = list(range(33))

k = 6
gamma = [k, k+3, k+4]



rankedAlphabet = {alphabet[i] : rank[i] for i in range(33)}
reversedRankedAlphabet = {rank[i] : alphabet[i] for i in range(33)}

opentext = [x for x in 'основныепонятиякриптографии']

gammaRow = [choice(gamma) for i in range(len(opentext))]


cipherText = [reversedRankedAlphabet[list(map(lambda x, y: (rankedAlphabet[x] + y)%33, opentext, gammaRow))[i]] for i in range(len(opentext))]
rankedCipherText = list(map(lambda x, y: (rankedAlphabet[x] + y)%33, opentext, gammaRow))

print(*cipherText, sep = ',')
print(*rankedCipherText, sep = ',')


print(*list(map(lambda x: reversedRankedAlphabet[(x  - gamma[0])%33], rankedCipherText)), sep = ',')
print(*list(map(lambda x: reversedRankedAlphabet[(x  - gamma[1])%33], rankedCipherText)), sep = ',')
print(*list(map(lambda x: reversedRankedAlphabet[(x  - gamma[2])%33], rankedCipherText)), sep = ',')

#print(*[reversedRankedAlphabet[list(map(lambda x, y: (rankedAlphabet[x] + gammaRow[0])%33, opentext))[i]] for i in range(len(opentext))], sep = ',')
#print(*[reversedRankedAlphabet[list(map(lambda x, y: (rankedAlphabet[x] + gammaRow[1])%33, opentext))[i]] for i in range(len(opentext))], sep = ',')
print(*gammaRow, sep = ',')


print(*list(map(lambda x: (rankedAlphabet[x])%33, opentext)), sep = ',')




print(*opentext, sep = ',')
print()
