def hi(): # функция приветсвия (правил игры)
    print('--------------------------------------------')
    print('Привет! Добро пожаловать к Крестики-Нолики')
    print('Пусть победит сильнейший!')
    print('Ход писать через пробел')
    print('Сначала вертикаль потом горизонталь')
    print('Удачи!!!')
    print('--------------------------------------------')

def ask(): #функция получения хода пользователя, и проверка правильности ввода хода
    while True:
        pozition = input('Ходи:').split()
        if len(pozition) !=2:
            print('Введите две кооринаты!!!')
            continue
        x, y = pozition

        if not (x.isdigit()) or not (y.isdigit()):
            print('Ввод только чисел')
            continue
        x, y = int(x), int(y)
        if 0>x or 2<x or 0>y or 2<y:
            print('Числа вышли за пределы поля!')
            continue
        if field[x][y]!=' ':
            print('Клетка уже занята!')
            continue
        return x, y


def win():  #функция проверки выигрыша
    for i in range(3):
        sym = []
        for j in range(3):
            sym.append(field[i][j])
        if sym == ['X','X','X'] or sym == ['0','0','0']:
            return True

    for i in range(3):
        sym = []
        for j in range(3):
            sym.append(field[j][i])
        if sym == ['X', 'X', 'X'] or sym == ['0', '0', '0']:
             return True

    sym=[]
    for i in range(3):
        sym.append(field[i][i])
        if sym == ['X','X','X'] or sym == ['0','0','0']:
            return True

    sym=[]
    for i in range(3):
        sym.append(field[i][i-2])
        if sym == ['X','X','X'] or sym == ['0','0','0']:
            return True
    return False

def table(): #функция создания поля для игры
    print()
    print("    | 0 | 1 | 2 | ")
    print("  -- --- --- --- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  -- --- --- --- ")
    print()

hi()
field = [[' ']*3 for i in range(3)]
count = 0
while True:
    count += 1
    table()
    if count % 2 == 1:
        print('Ходит крестик')
    else:
        print('Ходит нолик')

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = '0'

    if win():
        break

    if count == 9:
        print('Ничья')
        break