import data
import math


# Матрицы
def showMatrix(*matrix):
    for i in matrix:
        for i2 in i:
            print(i2, end=' ')
        print()


def matrix_a():
    data.A=[]
    height = int(input("Введите количество строк : "))
    width = int(input("Введите количество столбцов : "))


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

    for t in range(height):
        data.B.append([])

    for i in range(0, height):
        for j in range(0, width):
            b = float(input("Введите значение b" + str(i + 1) + str(j + 1) + ': '))
            data.B[i].append(b)

    showMatrix(*data.B)

def summ():
    data.C=[]
    for t in range(len(data.A)):
        data.C.append([])
    for i in range(0, len(data.A)):
        for j in range(0, len(data.A[0])):

            data.C[i].append(data.A[i][j] + data.B[i][j])
    showMatrix(*data.C)

def diff():
    data.C=[]
    for t in range(len(data.A)):
        data.C.append([])
    for i in range(0, len(data.A)):
        for j in range(0, len(data.A[0])):

            data.C[i].append(data.A[i][j] - data.B[i][j])
    showMatrix(*data.C)

def transposition(matrix):
    data.C=[]
    for t in range(len(matrix)):
        data.C.append([])
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            data.C[j].append(matrix[i][j])
    showMatrix(*data.C)

def multiply():
    data.C=[]
    c=0
    for t in range(len(data.A)):
        data.C.append([])
    for i in range(len(data.A)):
        for j in range(len(data.B[0])):
            for k in range(len(data.B)):
                c+=data.A[i][k]*data.B[k][j]
            data.C[i].append(c)
            c=0
    showMatrix(*data.C)

def verticalAttaching():
    data.C=[]
    data.C=data.A+data.B
    showMatrix(*data.C)

def horizontalAttaching():
    data.C=[]
    data.C=data.A
    for i in range(len(data.A)):
        for j in range(len(data.B[i])):
            data.C[i].append(data.B[i][j])
    showMatrix(*data.C)



# Векторы

def showVector(*vector):
    for i in range(len(vector)):
        print(vector[i], end=' ')

def showVectorElement(vector):
    number = int(input("Введите номер координаты, которую хотите вывести: "))-1
    if 0 <= number < len(vector):
        print(vector[number])
        return 0
    print("Данной координаты не существует")


def vector(name):
    data.vectorC=[]

    dim = int(input('Введите меру вектора '+name+': '))
    for i in range(0,dim):
        coordinate=float(input('Введите значение координаты '+name+str(i+1)+': '))
        data.vectorC.append(coordinate)
    match name:
        case 'a':
            if data.vectorA!=[]:
                data.vectorA = []
            data.vectorA = data.vectorC
            showVector(*data.vectorA)
        case 'b':
            if data.vectorB != []:
                data.vectorB = []
            data.vectorB=data.vectorC
            showVector(*data.vectorB)

def vectorSumm():
    data.vectorC=[]
    dim = min(len(data.vectorA),len(data.vectorB))
    for i in range(dim):
        data.vectorC.append(data.vectorA[i]+data.vectorB[i])

    if len(data.vectorA)>len(data.vectorB):
        data.vectorC.extend(data.vectorA[dim:])
    elif len(data.vectorB)>len(data.vectorA):
        data.vectorC.extend(data.vectorB[dim:])

    showVector(data.vectorC)


def vectorDiff():
    data.vectorC = []

    dim = min(len(data.vectorA), len(data.vectorB))
    for i in range(dim):
        data.vectorC.append(data.vectorA[i] - data.vectorB[i])

    if len(data.vectorA) > len(data.vectorB):
        data.vectorC.extend(data.vectorA[dim:])
    elif len(data.vectorB) > len(data.vectorA):
        data.vectorC.extend(data.vectorB[dim:])

    showVector(data.vectorC)


def vectorUnification():
    data.vectorC = []
    data.vectorC = data.vectorA+data.vectorB
    showVector(data.vectorC)

def vectorToMatrixUnification():
    data.C = []
    data.C.append(data.vectorA)
    data.C.append(data.vectorB)
    for i in data.C:
        for i2 in i:
            print(i2, end=' ')
        print()

def norm(vector):
    norm = 0
    for i in vector:
        norm += i**2
    print(math.sqrt(norm))


def takePart(vector):
    firstPart=int(input("Ввведите первую часть вектора: "))-1
    secondPart=int(input("Введите вторую чать вектора: "))
    if firstPart<secondPart and firstPart>0 and secondPart>0 and secondPart<=len(vector):
        print(vector[firstPart:secondPart])
        return 0
    print("Введены некорректные значения")


