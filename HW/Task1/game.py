# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

import random
from random import randint

message = 'Ваш ход'


def play_game(n, m, players, message):
    count = 0
    while n > 0:
        print(f'{players[count%2]}, {message}')
        move = int(input())
        if move > n or move > m:
            print(f'Конфет можно взять не более {m}')
            while True:
                if n >= move <= m:
                    break
                print(f'Выберите количество конфет еще раз')
                move = int(input())
        n = n - move
        if n > 0: print(f'Осталось {n} конфет(а)')
        else: print('Все конфеты разобраны.')
        count +=1
    return players[not count%2]


n = 2021   # количество конфет
m = 28     # максимальное количество конфет за ход

print(f'На столе лежит {n} конфет(а). Играют два игрока делая ход друг после друга.' 
f'Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем {m} конфет(у).' 
'Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,' 
'чтобы забрать все конфеты у своего конкурента?')


a = random.randint(1, 2)   # (определяем случайным образом кто ходит первый Игрок 1 или 2)
b = 0
if a == 1: b == 2
else: b == 1


player1 = f'Игрок {a}'
player2 = f'Игрок {b}'
players = [player1, player2]

winer = play_game(n, m, players, message)
if not winer:
    print('Ничья')
else: print(f'Победил {winer}!')