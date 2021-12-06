'''
Created on 05 december 2021

@author: Antonio Martínez Fernández
'''

import re
from collections import defaultdict

PNUMBER = r'\b\d+\b'
re.compile(PNUMBER)


def not_marked_cells(matrix, num):

    counter = 0

    for line in matrix:

        for item in line:

            if item != "x":

                counter += int(item)

    return counter*int(num)


def is_accepted(matrix):

    # check rows

    control = 0

    for row in matrix:

        control = 0

        for num in row:

            if num != "x":
                control = 1
                break

        if control == 0:
            return True

    # check columns

    for i in range(5):

        control = 0

        for row in matrix:

            if row[i] != "x":
                control = 1
                break

        if control == 0:
            return True

    return False


def main_v1():

    archivo = open("input04.txt")
    # archivo=open("prueba.txt")

    # stores the sequence of numbers
    numbers = re.findall(PNUMBER, archivo.readline())
    archivo.readline()

    database = []
    matrix = []

    control = 0

    # we start to read from the first matrix

    while True:

        linea = archivo.readline()

        if not linea:
            database.append(matrix)
            break

        if(linea == "\n"):

            database.append(matrix)
            matrix = []

        elif linea != "\n":
            aux = re.findall(PNUMBER, linea)
            matrix.append(aux)

    # change x if its the number value

    # TODO SUGERENCIA : rentaria mas comprobar solo matrices modificadas!

    for numero in numbers:

        for j in range(len(database)):
            # for matrix in database:

            for k in range(len(database[j])):
                # for line in matrix:

                for y in range(len(database[j][k])):
                    # for cell in line:

                    if database[j][k][y] == numero:

                        database[j][k][y] = "x"

            if is_accepted(database[j]):
                #print(f"\n{database[j]} {numero}")
                return not_marked_cells(database[j], numero)


def main_v2():

    archivo = open("input04.txt")
    # archivo=open("prueba.txt")

    # stores the sequence of numbers
    numbers = re.findall(PNUMBER, archivo.readline())
    archivo.readline()

    database = []
    matrix = []

    control = 0

    # we start to read from the first matrix

    while True:

        linea = archivo.readline()

        if not linea:
            database.append(matrix)
            break

        if(linea == "\n"):

            database.append(matrix)
            matrix = []

        elif linea != "\n":
            aux = re.findall(PNUMBER, linea)
            matrix.append(aux)

    # change x if its the number value

    array = defaultdict(lambda: "0")
    counter = 0

    for numero in numbers:

        for j in range(len(database)):
            # for matrix in database:

            for k in range(len(database[j])):
                # for line in matrix:

                for y in range(len(database[j][k])):
                    # for cell in line:

                    if database[j][k][y] == numero:

                        database[j][k][y] = "x"

            if array[j] != 1 and is_accepted(database[j]):

                if(counter+1 == len(database)):

                    return not_marked_cells(database[j], numero)

                counter += 1
                array[j] = 1


if __name__ == '__main__':
    print(f"part 1 : {main_v1()} \npart 2 : {main_v2()}")
