<<<<<<< HEAD
import calculation
# import time

import data

print('Добро пожаловать в калькулятор матриц!')
try:
    while True:

        print("""
    Выберите объекты взаимодействия:
    1.Матрицы
    2.Вектора
    0.Выход из приложенния
        """)

        mainOption = int(input('Выбор: '))

        match mainOption:
            case 0:
                break
            case 1:
                while True:
                    print("""
    Выберите операцию:
    1.Ввести матрицу A
    2.Ввести матрицу B
    3.Сложение матриц(A+B)
    4.Вычитание матриц(A-B)
    5.Транспонирование(А)
    6.Умножение матриц(A*B)
    7.Вертикальное соединение матриц
    8.Горизонтальное соединение матриц
    9.Найти определитель матрицы
    10.Найти обратную матрицу
    11.Вставка строки/столбца в матрицу
    12.Взятие следа матрицы
    13.Представление диагональных элементов вектором
    14.Замена строки/столбца матрицы
    15.Вставка матрицы в матрицу
    16.Склеивание матрицы и вектора
    0.Назад
        """)

                    option = int(input("Действие: "))

                    match option:
                        case 0:
                            break
                        case 1:
                            calculation.matrix_a()
                        case 2:
                            calculation.matrix_b()
                        case 3:
                            if data.A != [] and data.B != []:
                                if len(data.A[0]) == len(data.B[0]) and len(data.A) == len(data.B):
                                    calculation.summ()
                                else:
                                    print('Некорректные данные')
                            else:
                                print('Некорректные данные')
                        case 4:
                            if data.A!=[] and data.B!=[]:
                                if len(data.A[0]) == len(data.B[0]) and len(data.A) == len(data.B):
                                    calculation.diff()
                                else:
                                    print('Некорректные данные')
                            else:
                                print('Некорректные данные')
                        case 5:
                            while True:
                                print("""
    Выберите матрицу, которую хотите транспонировать:
    1.Матрица А
    2.Матрица B
    0.Назад
                            """)
                                option = int(input("Выбор: "))
                                match option:
                                    case 1:
                                        if data.A != []:
                                            calculation.showMatrix(calculation.transposition(data.A))
                                        else: print("Мартица А не введена")
                                    case 2:
                                        if data.B != []:
                                            calculation.showMatrix(calculation.transposition(data.A))
                                        else:
                                            print("Мартица B не введена")
                                    case 0:
                                        break
                        case 6:
                            if data.A!=[] and data.B!=[]:
                                if len(data.A[0]) == len(data.B):
                                    calculation.multiply()
                                else:
                                    print('Некорректные данные')
                            else:
                                print('Некорректные данные')
                        case 7:
                            if len(data.A[0]) == len(data.B[0]):
                                calculation.verticalAttaching()
                            else:
                                print('Некорректные данные')
                        case 8:
                            if len(data.A) == len(data.B):
                                calculation.horizontalAttaching()
                            else:
                                print('Некорректные данные')
                        case 9:
                            while True:
                                print("""
    1.Найти определитель матрицы A
    2.Найти определитель матрицы B
    0.Назад
                                """)
                                option = int(input("Действие: "))
                                match option:
                                    case 1:
                                        if data.A!=[] and len(data.A[0]) == len(data.A):
                                            print(calculation.det(data.A))
                                        else:
                                            print("Введены некорректные данные")
                                    case 2:
                                        if data.B != [] and len(data.B[0]) == len(data.B):
                                            print(calculation.det(data.B))
                                        else:
                                            print("Введены некорректные данные")
                                    case 0:
                                        break

                        case 10:
                            while True:
                                print("""
    1.Найти матрицу обратную A
    2.Найти матрицу обратную B
    0.Назад """)
                                option = int(input("Действие: "))
                                match option:
                                    case 1:
                                        if data.A!=[] and len(data.A[0]) == len(data.A):
                                            calculation.inverseMatrix(data.A)
                                        else:
                                            print("Введены некорректные данные")
                                    case 2:
                                        if data.B != [] and len(data.B[0]) == len(data.B):
                                            calculation.inverseMatrix(data.B)
                                        else:
                                            print("Введены некорректные данные")
                                    case 0:
                                        break

                        case 11:
                            while True:
                                print("""
    1.Вставка строки в матрицу
    2.Вставка столбца в матрицу
    0.Назад
                                """)
                                option = int(input("Действие: "))
                                match option:
                                    case 1:
                                        while True:
                                            print("""
    1.Вставка строки в матрицу А
    2.Вставка строки в матрицу B
    0.Назад
                                            """)
                                            option = int(input("Действие: "))
                                            match option:
                                                case 1:
                                                    if data.A!=[]:
                                                        calculation.insertRow(data.A)
                                                    else:print("Не введена матрица А")
                                                case 2:
                                                    if data.B!=[]:
                                                        calculation.insertRow(data.B)
                                                    else:
                                                        print("Не введена матрица B")
                                                case 0:
                                                    break
                                    case 2:
                                        while True:
                                            print("""
    1.Вставка столбца в матрицу А
    2.Вставка столбца в матрицу B
    0.Назад
                                            """)
                                            option = int(input("Действие: "))
                                            match option:
                                                case 1:
                                                    if data.A!=[]:
                                                        calculation.insertCol(data.A)
                                                    else:
                                                        print("Не введена матрица А")
                                                case 2:
                                                    if data.B != []:
                                                        calculation.insertCol(data.B)
                                                    else:
                                                        print("Не введена матрица B")
                                                case 0:
                                                    break

                        case 12:
                            while True:
                                print("""
    1.Взятие следа матрицы А
    2.Взятие следа матрицы B
    0.Назад
                                """)
                                option = int(input("Действие: "))
                                match option:
                                    case 1:
                                        if data.A!=[] and len(data.A)==len(data.A[0]):
                                            calculation.takeTrace(data.A)
                                        else:
                                            print("Матрица А не является квадратной или не введена")
                                    case 2:
                                        if data.B != [] and len(data.B) == len(data.B[0]):
                                            calculation.takeTrace(data.B)
                                        else:
                                            print("Матрица B не является квадратной или не введена")
                                    case 0:
                                        break
                        case 13:
                            while True:
                                print("""
    1.Представление виагональных элементов вектором матрицы А
    2.Представление виагональных элементов вектором матрицы B
    0.Назад
                                                    """)
                                option = int(input("Действие: "))
                                match option:
                                    case 1:
                                        if data.A != [] and len(data.A) == len(data.A[0]):
                                            calculation.diagonalElements(data.A)
                                        else:
                                            print("Матрица А не является квадратной или не введена")
                                    case 2:
                                        if data.B != [] and len(data.B) == len(data.B[0]):
                                            calculation.diagonalElements(data.B)
                                        else:
                                            print("Матрица B не является квадратной или не введена")
                                    case 0:
                                        break

                        case 14:
                            while True:
                                print("""
    1.Замена строки
    2.Замена столбца
    0.Назад
    
                                """)
                                option = int(input("Действие: "))
                                match option:
                                    case 1:
                                        while True:
                                            print("""
    1.Замена строки в матрице А
    2.Замена строки в матрице B
    0.Назад
    
                                            """)
                                            option = int(input("Действие: "))
                                            match option:
                                                case 1:
                                                    if data.A!=[]:
                                                        calculation.changeRow(data.A)
                                                    else:
                                                        print("Матрица A не введена")
                                                case 2:
                                                    if data.B != []:
                                                        calculation.changeRow(data.B)
                                                    else:
                                                        print("Матрица B не введена")
                                                case 0:
                                                    break
                                    case 2:
                                        while True:
                                            print("""
    1.Замена столбца в матрице А
    2.Замена столбца в матрице B
    0.Назад

                                                                            """)
                                            option = int(input("Действие: "))
                                            match option:
                                                case 1:
                                                    if data.A != []:
                                                        calculation.changeCol(data.A)
                                                    else:
                                                        print("Матрица A не введена")
                                                case 2:
                                                    if data.B != []:
                                                        calculation.changeCol(data.B)
                                                    else:
                                                        print("Матрица B не введена")
                                                case 0:
                                                    break
                                    case 0:
                                        break


                        case 15:
                            while True:
                                print("""
    1.Вставка матрицы B в матрицу A
    1.Вставка матрицы A в матрицу B
    0.Назад
                                """)
                                option = int(input("Действие: "))
                                match option:
                                    case 1:
                                        if data.A!=[] and data.B!=[]:
                                            i = int(input("Введите с какого элемента по вертикали начинать вставку: "))
                                            j = int(input("Введите с какого элемента по горизонтали начинать вставку: "))
                                            calculation.insertMatrix(data.A, data.B,i,j)
                                        else:
                                            print("Матрица A не введена")
                                    case 2:
                                        if data.A != [] and data.B != []:
                                            i = int(input("Введите с какого элемента по вертикали начинать вставку: "))
                                            j = int(
                                                input("Введите с какого элемента по горизонтали начинать вставку: "))
                                            calculation.insertMatrix(data.B, data.A, i-1, j-1)
                                        else:
                                            print("Матрица B не введена")
                                    case 0:
                                        break
                        case 16:
                            while True:
                                print("""
    1.Склеить матрицу A с вектором
    2.Склеить матрицу B с вектором
    0.Назад
                                """)
                                option = int(input("Действие: "))
                                match option:
                                    case 1:
                                        if data.A!=[]:
                                            calculation.gluingMatrix(data.A)
                                        else:
                                            print("Матрица A не введена")
                                    case 2:
                                        if data.B != []:
                                            calculation.gluingMatrix(data.B)
                                        else:
                                            print("Матрица B не введена")
                                    case 0:
                                        break


            case 2:
                while True:
                    print("""
    Выберите действия над векторами:
    1.Ввод вектора а
    2.Ввод вектора b
    3.Сложение векторов (a+b)
    4.Вычитание векторов (a-b)
    5.Вывод вектора
    6.Вывести значение элемента вектора
    7.Объединение векторов в один
    8.Объединение векторов в один
    9.Вычисление нормы вектора
    10.Взятие части вектора
    11.Вставка вектора в другой вектор
    0.Назад
                    """)
                    choice = int(input("Действие: "))

                    match choice:
                        case 0:
                            break
                        case 1:
                            calculation.vector('a')
                        case 2:
                            calculation.vector('b')
                        case 3:
                            if data.vectorA!=[] and data.vectorB!=[]:
                                calculation.vectorSumm()
                            else: print('Недостаточно данных')
                        case 4:
                            if data.vectorA != [] and data.vectorB != []:
                                calculation.vectorDiff()
                            else:
                                print('Недостаточно данных')
                        case 5:
                            while True:
                                print("""
                                Выберите вектор:
    1.Вектор a
    2.Вектор b
    0.Назад
             """)
                                option = int(input("Выберите действие: "))
                                match option:
                                    case 1:
                                        if data.vectorA!=[]:
                                            calculation.showVector(data.vectorA)
                                        else:
                                            print("Вектор a не введен")
                                    case 2:
                                        if data.vectorB != []:
                                            calculation.showVector(data.vectorB)
                                        else:
                                            print("Вектор b не введен")
                                    case 0:
                                        break
                        case 6:
                            while True:
                                print("""
    Выберите вектор:
    1.Вектор a
    2.Вектор b
    0.Назад
                        
                            """)
                                option = int(input("Выберите действие: "))
                                match option:
                                    case 1:
                                        if data.vectorA!=[]:
                                            calculation.showVectorElement(data.vectorA)
                                        else:
                                            print("Вектор a не введен")
                                    case 2:
                                        if data.vectorB != []:
                                            calculation.showVectorElement(data.vectorB)
                                        else:
                                            print("Вектор b не введен")
                                    case 0:
                                        break
                        case 7:
                            if data.vectorA != [] and data.vectorB != []:
                                calculation.vectorUnification()
                            else:
                                print('Недостаточно данных')
                        case 8:
                            if data.vectorA != [] and data.vectorB !=[] and len(data.vectorA) == len(data.vectorB):
                                calculation.vectorToMatrixUnification()
                            else:
                                print('Недостаточно данных или векторы разной размерности')
                        case 9:
                            while True:
                                print("""
    Выберите вектор, который нужно нормировать
    1.Нормировать вектор a
    2.Нормировать вектор b
    0.Назад
                                
                                """)
                                option = int(input("Выбор: "))
                                match option:
                                    case 1:
                                        if data.vectorA!=[]:
                                            calculation.norm(data.vectorA)
                                        else:
                                            print("Вектор a не введен")
                                    case 2:
                                        if data.vectorB != []:
                                            calculation.norm(data.vectorB)
                                        else:
                                            print("Вектор b не введен")
                                    case 0:
                                        break

                        case 10:
                            while True:
                                print("""
    Введите вектор от которого Вы хотите взять часть:
    1.Вектор a
    2.Вектор b
    0.Назад
                                
                                """)
                                option = int(input("Выбор: "))
                                match option:
                                    case 1:
                                        if data.vectorA!=[]:
                                            calculation.takePart(data.vectorA)
                                        else:
                                            print("Вектор a не введен")
                                    case 2:
                                        if data.vectorB != []:
                                            calculation.takePart(data.vectorB)
                                        else:
                                            print("Вектор b не введен")
                                    case 0:
                                        break
                        case 11:
                            while True:
                                print("""
    1.Вставка вектора а в вектор b
    2.Вставка вектора b в вектор а
    0.Назад                        
                                """)
                                option = int(input("Выбрать действие: "))
                                match option:
                                    case 0:
                                        break
                                    case 1:
                                        if data.vectorA != [] and data.vectorB != []:
                                            calculation.vectorInserting(data.vectorB, data.vectorA)

                                        else:
                                            print("Вектор a не введен")
                                    case 2:
                                        if data.vectorB != [] and data.vectorA != []:
                                            calculation.vectorInserting(data.vectorA, data.vectorB)
                                        else:
                                            print("Вектор b не введен")



            case 0:
                break




except ValueError:
    print("Произошла непредвиденная ошибка")
    print(ValueError)

=======
import calculation
# import time

import data

print('Добро пожаловать в калькулятор матриц!')
while True:

    print("""
    Выберите объекты взаимодействия:
    1.Матрицы
    2.Вектора
    0.Выход из приложенния
    """)

    mainOption = int(input('Выбор: '))

    match mainOption:
        case 0:
            break
        case 1:
            while True:
                print("""
    Выберите операцию:
    1.Ввести матрицу A
    2.Ввести матрицу B
    3.Сложение матриц(A+B)
    4.Вычитание матриц(A-B)
    5.Транспонирование(А)
    6.Умножение матриц(A*B)
    7.Вертикальное соединение матриц
    8.Горизонтальное соединение матриц
    0.Назад
    """)

                option = int(input("Действие: "))

                match option:
                    case 0:
                        break
                    case 1:
                        calculation.matrix_a()
                    case 2:
                        calculation.matrix_b()
                    case 3:
                        if data.A != [] and data.B != []:
                            if len(data.A[0]) == len(data.B[0]) and len(data.A) == len(data.B):
                                calculation.summ()
                            else:
                                print('Некорректные данные')
                        else:
                            print('Некорректные данные')
                    case 4:
                        if data.A!=[] and data.B!=[]:
                            if len(data.A[0]) == len(data.B[0]) and len(data.A) == len(data.B):
                                calculation.diff()
                            else:
                                print('Некорректные данные')
                        else:
                            print('Некорректные данные')
                    case 5:
                        while True:
                            print("""
    Выберите матрицу, которую хотите транспонировать:
    1.Матрица А
    2.Матрица B
    0.Назад
                        """)
                            option = int(input("Выбор: "))
                            match option:
                                case 1:
                                    if data.A != []:
                                        calculation.transposition(data.A)
                                    else: print("Мартица А не введена")
                                case 2:
                                    if data.B != []:
                                        calculation.transposition(data.B)
                                    else:
                                        print("Мартица B не введена")
                                case 0:
                                    break


                    case 6:
                        if data.A!=[] and data.B!=[]:
                            if len(data.A[0]) == len(data.B):
                                calculation.multiply()
                            else:
                                print('Некорректные данные')
                        else:
                            print('Некорректные данные')
                    case 7:
                        if len(data.A[0]) == len(data.B[0]):
                            calculation.verticalAttaching()
                        else:
                            print('Некорректные данные')
                    case 8:
                        if len(data.A) == len(data.B):
                            calculation.horizontalAttaching()
                        else:
                            print('Некорректные данные')

            else:
                print("Произошла непредвиденная ошибка")

        case 2:
            while True:
                print("""
        Выберите действия над векторами:
        1.Ввод вектора а
        2.Ввод вектора b
        3.Сложение векторов (a+b)
        4.Вычитание векторов (a-b)
        5.Вывод вектора
        6.Вывести значение элемента вектора
        7.Объединение векторов в один
        8.Объединение векторов в один
        9.Вычисление нормы вектора
        0.Назад
                """)
                choice = int(input("Действие: "))

                match choice:
                    case 0:
                        break
                    case 1:
                        calculation.vector('a')
                    case 2:
                        calculation.vector('b')
                    case 3:
                        if data.vectorA!=[] and data.vectorB!=[]:
                            calculation.vectorSumm()
                        else: print('Недостаточно данных')
                    case 4:
                        if data.vectorA != [] and data.vectorB != []:
                            calculation.vectorDiff()
                        else:
                            print('Недостаточно данных')
                    case 5:
                        while True:
                            print("""
    1.Вывод вектора a
    2.Вывод вектора b
    0.Назад
                            """)
                            option = int(input("Выберите действие: "))
                            match option:
                                case 1:
                                    if data.vectorA!=[]:
                                        calculation.showVector(data.vectorA)
                                    else:
                                        print("Вектор a не введен")
                                case 2:
                                    if data.vectorB != []:
                                        calculation.showVector(data.vectorB)
                                    else:
                                        print("Вектор b не введен")
                                case 0:
                                    break
                    case 6:
                        while True:
                            print("""
    Выберите вектор:
    1.Вектор a
    2.Вектор b
    0.Назад
                        
                        """)
                            option = int(input("Выберите действие: "))
                            match option:
                                case 1:
                                    if data.vectorA!=[]:
                                        calculation.showVectorElement(data.vectorA)
                                    else:
                                        print("Вектор a не введен")
                                case 2:
                                    if data.vectorB != []:
                                        calculation.showVectorElement(data.vectorB)
                                    else:
                                        print("Вектор b не введен")
                                case 0:
                                    break
                    case 7:
                        if data.vectorA != [] and data.vectorB != []:
                            calculation.vectorUnification()
                        else:
                            print('Недостаточно данных')
                    case 8:
                        if data.vectorA != [] and data.vectorB !=[] and len(data.vectorA) == len(data.vectorB):
                            calculation.vectorToMatrixUnification()
                        else:
                            print('Недостаточно данных или векторы разной размерности')
                    case 9:
                        while True:
                            print("""
    Выберите вектор, который нужно нормировать
    1.Нормировать вектор a
    2.Нормировать вектор b
    0.Назад
                            
                            """)
                            option = int(input("Выбор: "))
                            match option:
                                case 1:
                                    if data.vectorA!=[]:
                                        calculation.norm(data.vectorA)
                                    else:
                                        print("Вектор a не введен")
                                case 2:
                                    if data.vectorB != []:
                                        calculation.norm(data.vectorB)
                                    else:
                                        print("Вектор b не введен")
                                case 0:
                                    break

                    case 10:
                        while True:
                            print("""
    Введите вектор от которого Вы хотите взять часть:
    1.Вектор a
    2.Вектор b
    0.Назад
                            
                            """)
                            option = int(input("Выбор: "))
                            match option:
                                case 1:
                                    if data.vectorA!=[]:
                                        calculation.takePart(data.vectorA)
                                    else:
                                        print("Вектор a не введен")
                                case 2:
                                    if data.vectorB != []:
                                        calculation.takePart(data.vectorB)
                                    else:
                                        print("Вектор b не введен")
                                case 0:
                                    break






>>>>>>> e971cce98d26ac2d3e184dffb5cbf7d7d3c900ce
print('Досвидания')