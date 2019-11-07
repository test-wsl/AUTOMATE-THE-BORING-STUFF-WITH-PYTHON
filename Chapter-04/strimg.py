#!/usr/bin/env python
# -*- coding: utf-8 -*-



def prin(list):
    for y in range(len(list[len(list) - 1])):
        for x in range(len(list)):
            print(list[x][y], end='')
        print()


def main():
    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]
    prin(grid)


if __name__ == '__main__':
    main()