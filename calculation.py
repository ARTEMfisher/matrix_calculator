<<<<<<< HEAD
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
    return data.C

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

def slayer(b,j):
    a=[]
    for k in range(len(b)):
        a.append([])
        a[k]=b[k].copy()
    if len(a)>1:
        for i in range(0,len(a)):
            del a[i][j]
        del a[0]
        return a
    else:
        return a
def det(matrix):
    determinant = 0
    if len(matrix) >1:
        for i in range(len(matrix[0])):
            determinant +=matrix[0][i]*((-1)**(i+2))*(det(slayer(matrix,i)))
        return determinant
    else:
        return matrix[0][0]

def cofactoForInversedMatrix(matrix, row, col):
    sub_matrix = [row[:col] + row[col+1:] for row in (matrix[:row] + matrix[row+1:])]
    cofactor_value = ((-1) ** (row + col)) * det(sub_matrix)/det(matrix)
    return cofactor_value

def inverseMatrix(matrix):
    data.C=[]
    determinant = det(matrix)
    if determinant == 0:
        print("Обратной матрицы не существует")
        return

    for t in range(len(matrix)):
        data.C.append([])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            data.C[i].append(cofactoForInversedMatrix(matrix,i,j))
    showMatrix(*transposition(data.C))


def insertRow(matrix):
    position = int(input("Введите позицию, на которую хотите вставить строку: "))
    if position < 1 or position > len(matrix) + 1:
        print("Неверная позиция для вставки")
        return

    vectorC = []
    for i in range(len(matrix[0])):
        a = float(input(f"Введите элемент {i + 1}: "))
        vectorC.append(a)

    matrix.insert(position - 1, vectorC)
    showMatrix(*matrix)

def insertCol(matrix):
    position = int(input("Введите позицию, на которую хотите вставить столбец: "))
    if position < 1 or position > len(matrix[0]) + 1:
        print("Неверная позиция для вставки")
        return
    vectorC = []
    for i in range(len(matrix)):
        a = float(input(f"Введите элемент {i + 1}: "))
        vectorC.append(a)

    for j in range(len(vectorC)):
        matrix[j].insert(position-1, vectorC[j])
    showMatrix(*matrix)

def takeTrace(matrix):
    trace = 0
    for i in range(len(matrix)):
        trace += matrix[i][i]
    print(trace)

def diagonalElements(matrix):
    data.vectorC = []
    for i in range(len(matrix)):
        data.vectorC.append(matrix[i][i])
    showVector(*data.vectorC)

def changeRow(matrix):
    position = int(input("Введите позицию, на которую хотите заменить строку: "))
    if position < 1 or position > len(matrix) + 1:
        print("Неверная позиция для вставки")
        return

    vectorC = []
    for i in range(len(matrix[0])):
        a = float(input(f"Введите элемент {i + 1}: "))
        vectorC.append(a)

    matrix[position-1]=vectorC
    showMatrix(*matrix)

def changeCol(matrix):
    position = int(input("Введите позицию, на которую хотите вставить столбец: "))
    if position < 1 or position > len(matrix[0]) + 1:
        print("Неверная позиция для вставки")
        return
    vectorC = []
    for i in range(len(matrix)):
        a = float(input(f"Введите элемент {i + 1}: "))
        vectorC.append(a)

    for j in range(len(vectorC)):
        matrix[j][position-1]=vectorC[j]
    showMatrix(*matrix)


def insertMatrix(A, B, row, col):

    if row < 0 or col < 0 or row + len(B) > len(A) or col + len(B[0]) > len(A[0]):
        print("Невозможно выполнить вставку: неправильные размеры матриц или позиция")
        return

    for i in range(len(B)):
        for j in range(len(B[0])):
            A[row + i][col + j] = B[i][j]

    showMatrix(*A)

def gluingMatrix(matrix):
    data.vectorC=[]
    for i in range(len(matrix)):
        a = float(input(f"Введите {i+1} элемент вектора: "))
        data.vectorC.append(a)
    for j in range(len(matrix)):
        matrix[j].append(data.vectorC[j])

    showMatrix(*matrix)



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

def vectorInserting(firstVector,secondVector):
    data.vectorC=[]
    index = int(input("Введите позицию в которую нужно вставить вектор: "))
    if index<=len(firstVector):
        data.vectorC= firstVector[:index]+secondVector+firstVector[index:]
        showVector(data.vectorC)
    else:
        print("Введена неверная позиция")
=======
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


>>>>>>> e971cce98d26ac2d3e184dffb5cbf7d7d3c900ce
