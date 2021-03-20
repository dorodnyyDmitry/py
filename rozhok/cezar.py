alphabet = [x for x in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя']
rank = list(range(33))

rankedAlphabet = {alphabet[i] : rank[i] for i in range(33)}
reversedRankedAlphabet = {rank[i] : alphabet[i] for i in range(33)}
opentext = [x for x in 'мягкихбулок']

print(*opentext, sep = ',')
print(*list(map(lambda x: (rankedAlphabet[x])%33, opentext)), sep = ',')
print(*list(map(lambda x: (rankedAlphabet[x] + 6)%33, opentext)), sep = ',')
print(*[reversedRankedAlphabet[list(map(lambda x: (rankedAlphabet[x] + 6)%33, opentext))[i]] for i in range(len(opentext))], sep = ',')
print()
