import data


def showMatrix(*matrix):
    for i in matrix:
        for i2 in i:
            print(i2, end=' ')
        print()


def matrix_a():
    data.A=[]
    height = int(input("Введите количество строк : "))
    width = int(input("Введите количество столбцов : "))

    data.heightA=height
    data.widthA=width

    for t in range(height):
        data.A.append([])

    for i in range(0, height):
        for j in range(0, width):
            a = float(input("Введите значение а"+str(i + 1)+str(j + 1) + ': '))
            data.A[i].append(a)

    showMatrix(*data.A)


def matrix_b():
    data.B = []
    height = int(input("Введите количество строк : "))
    width = int(input("Введите количество столбцов : "))

    data.heightB = height
    data.widthB = width

    for t in range(height):
        data.B.append([])

    for i in range(0, height):
        for j in range(0, width):
            b = float(input("Введите значение b" + str(i + 1) + str(j + 1) + ': '))
            data.B[i].append(b)

    showMatrix(*data.B)

def summ():
    data.C=[]
    for t in range(data.heightA):
        data.C.append([])
    for i in range(0, data.heightA):
        for j in range(0, data.widthA):

            data.C[i].append(data.A[i][j] + data.B[i][j])
    showMatrix(*data.C)

def diff():
    data.C=[]
    for t in range(data.heightA):
        data.C.append([])
    for i in range(0, data.heightA):
        for j in range(0, data.widthA):

            data.C[i].append(data.A[i][j] - data.B[i][j])
    showMatrix(*data.C)

def transposition():
    data.C=[]
    for t in range(data.widthA):
        data.C.append([])
    for i in range(0, data.heightA):
        for j in range(0, data.widthA):
            data.C[j].append(data.A[i][j])
    showMatrix(*data.C)

def multiply():
    data.C=[]
    c=0
    for t in range(data.heightA):
        data.C.append([])
    for i in range(len(data.A)):
        for j in range(len(data.B[0])):
            for k in range(len(data.B)):
                c+=data.A[i][k]*data.B[k][j]
            data.C[i].append(c)
            c=0
    showMatrix(*data.C)