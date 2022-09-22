# Крестики-нолики

import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Матрица игрового поля
hodSave=[' ',' ',' ',
         ' ',' ',' ',
         ' ',' ',' ',]
id=2

# Вывод игрового поля
def board():
    print('Номера ячеек слева направо сверху вниз:\n7 8 9\n4 5 6\n1 2 3\nДля хода укажите номер ячейки')
    for i in range(7):
        if i in [0,2,4,6]: print('-------------')
        if i==1: print(f'| {hodSave[6]} | {hodSave[7]} | {hodSave[8]} |')
        if i==3: print(f'| {hodSave[3]} | {hodSave[4]} | {hodSave[5]} |')
        if i==5: print(f'| {hodSave[0]} | {hodSave[1]} | {hodSave[2]} |')


# Заполняем матрицу hodSave ходами игроков (X или 0)
def schet(h):
    while True:
        if h in [0,1,2,3,4,5,6,7,8]:
            if id==1: hodSave[h]='X'
            else: hodSave[h]='0'
            break
        else: h=int(input(f'Введите номер ячейки (от 1 до 9) -> '))-1


# Проверка на победителя
def winControl():
    FlagWin=False

    for i in range(1,5):
        if (hodSave[4] == hodSave[4-i] == hodSave[4+i]) and hodSave[4]!=' ': FlagWin=True
    for i in range(0,7,6): 
        if (hodSave[i] == hodSave[i+1] == hodSave[i+2]) and hodSave[i]!=' ': FlagWin=True
    for i in range(0,3,2): 
        if (hodSave[i] == hodSave[i+3] == hodSave[i+6]) and hodSave[i]!=' ': FlagWin=True
    if FlagWin:
        print(f'Gamer №{id} YOU WIN!')
        z=input('Чтобы начать заново нажмите ENTER\nЧтобы закончить игру введите любой символ и нажмите ENTER-> ')
        if z: exit()
        for i in range(len(hodSave)):
            hodSave[i]=' '
        return False
    return True


# Запускаем игру

while True:
    cls()
    board()
    if winControl():
        if id==1: id=2
        else: id=1
        schet(int(input(f'Ход игрока №{id} -> '))-1)
    else: id=2
