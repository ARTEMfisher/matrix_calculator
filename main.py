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






print('Досвидания')