#!/usr/bin/env python
# -*- coding: utf-8 -*-



def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def main():
    theBoard = {
        'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
        'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
        'low-L': ' ', 'low-M': ' ', 'low-R': ' '
    }
    # printBoard(theBoard)
    turn = 'X'
    for i in range(9):
        printBoard(theBoard)
        print('Turn for ' + turn + '. Move on which space?')
        flag = False
        move = input()
        if theBoard[move] == ' ':
            flag = True
        else:
            flag = False
        while not flag:
            print('Turn for ' + turn + '. Move on which space?')
            move = input()
            if theBoard[move] == ' ':
                flag = True
            else:
                flag = False
        theBoard[move] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'



if __name__ == '__main__':
    main()