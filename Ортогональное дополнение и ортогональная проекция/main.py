import numpy
np = numpy
#Сверху вниз линейное пространство
arr = [[-2, 2, -6, 2, -10], [-2, 6, -14, 4, -24], [2, 0, 0, 2, -2], [-2, 8, -20, 8, -38]]

#вектор
y = [-2, -2, 4, -4, 10]


a = []
for i in range(len(arr)):
    pra = []
    for j in range(len(arr)):
        pra.append(np.dot(arr[i], arr[j]))
    pra.append(np.dot(arr[i], y))
    a.append(pra)
print(a)

