alphabet = [x for x in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя']
rank = list(range(33))

a = 7;
b = 6;

rankedAlphabet = {alphabet[i] : rank[i] for i in range(33)}
reversedRankedAlphabet = {rank[i] : alphabet[i] for i in range(33)}
opentext = [x for x in 'создатьновыйдокумент']

print(*opentext, sep = ',')
print(*list(map(lambda x: (rankedAlphabet[x])%33, opentext)), sep = ',')
print(*list(map(lambda x: (rankedAlphabet[x]*a + b)%33, opentext)), sep = ',')
print(*[reversedRankedAlphabet[list(map(lambda x: (rankedAlphabet[x]*a + b)%33, opentext))[i]] for i in range(len(opentext))], sep = ',')
print()
