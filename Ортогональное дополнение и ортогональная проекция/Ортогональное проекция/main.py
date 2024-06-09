import numpy
np = numpy
#Сверху вниз линейное пространство
arr = [[6, -6, 0], [3, 0, 3]]

#вектор
y = [-3, 3, -3]

#Если не задана матрица Грамма, то оставить пустой
g = []


a = []
for i in range(len(arr)):
    pra = []
    for j in range(len(arr)):
        if (len(g) >= 1):
            pra.append(np.dot(np.dot(arr[i], g) , arr[j]))
        else:
            pra.append(np.dot(arr[i], arr[j]))

    if len(g) >= 1:
        pra.append(np.dot(np.dot(arr[i], g), y))
    else:
        pra.append(np.dot(arr[i], y))
    a.append(pra)

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print('')