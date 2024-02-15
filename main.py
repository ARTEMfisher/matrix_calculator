import calculation
import time

import data

print('Добро пожаловать в калькулятор матриц!')
while True:
    print("""
    Выберите операцию:
    1.Ввести матрицу A
    2.Ввести матрицу B
    3.Сложение матриц(A+B)
    4.Вычитание матриц(A-B)
    5.Транспонирование(А)
    6.Умножение матриц(A*B)
    """)

    option = int(input("Действие: "))

    match option:
        case 1:
            calculation.matrix_a()
        case 2:
            calculation.matrix_b()
        case 3:
            if data.widthA == data.widthB & data.heightA == data.heightB:
                calculation.summ()
            else:
                print('Некорректные данные')
        case 4:
            if data.widthA == data.widthB & data.heightA == data.heightB:
                calculation.diff()
            else:
                print('Некорректные данные')
        case 5:
            calculation.transposition()
        case 6:
            calculation.multiply()

    # time.sleep(3)