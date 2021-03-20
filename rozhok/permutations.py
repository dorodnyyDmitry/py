import itertools

list1 = ['о','е', 'р']
list2 = ['л','в', 'н']
list3 = ['к','м', 'б']

#res = [x for x in itertools.product(list1, list2)]

#print(*res, sep = '\n')

list12 = [[list1[i], list2[i], list3[i]] for i in range(3)]

for element in itertools.product(*list12):
    print(*element, sep = '')
