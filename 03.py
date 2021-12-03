'''
Created on 03 december 2021

@author: Antonio Martínez Fernández
'''


def lectura():

    archivo=open("input03.txt")
    #archivo = open("prueba.txt")
    return archivo


def main_v1():

    archivo = lectura()
    table = []

    gamma = ""
    # epsilon is the opposite

    linea = archivo.readline()
    length = len(linea)
    table.append(linea)

    while True:

        linea = archivo.readline()

        if not linea:
            break

        table.append(linea)

    # algorithm

    for i in range(length):

        bit_0 = 0
        bit_1 = 0

        for j in range(len(table)):

            if table[j][i] == "0":

                bit_0 += 1

            elif table[j][i] == "1":

                bit_1 += 1

        if bit_0 > bit_1:
            gamma += "0"

        elif bit_1 > bit_0:
            gamma += "1"

    epsilon = gamma.replace("1", "2")
    epsilon = epsilon.replace("0", "1")
    epsilon = epsilon.replace("2", "0")

    return int(epsilon, 2)*int(gamma, 2)


def del_rows(array, i,pos):

    # for j in range(len(array)):

    #     if array[j][0]==str(i):

    #         array.remove(array[j])

    # return array

    aux=array[:]

    for linea in array:

       #if linea.startswith(str(i)):
       if linea[pos]==str(i):

           aux.remove(linea)

    return aux



def main_v2():
    
    archivo=lectura()
    table=[]

    gamma=""
    # epsilon is the opposite
    
    linea=archivo.readline()
    length=len(linea)
    table.append(linea)

    while True:

        linea=archivo.readline()

        if not linea:
            break


        table.append(linea)

    table_epsilon=table[:]

    # algorithm


    for i in range(length):

        bit_0=0
        bit_1=0

        for j in range(len(table)):

            if table[j][i]=="0":

                bit_0+=1

            elif table[j][i]=="1":

                bit_1+=1

        if bit_0>bit_1:
            table=del_rows(table,1,i)

        elif bit_1>=bit_0:
            table=del_rows(table,0,i)


    #print(table)


    for i in range(length):

        if(len(table_epsilon)==1):
            break

        bit_0=0
        bit_1=0

        for j in range(len(table_epsilon)):

            if table_epsilon[j][i]=="0":

                bit_0+=1

            elif table_epsilon[j][i]=="1":

                bit_1+=1

        if bit_0>bit_1:
            table_epsilon=del_rows(table_epsilon,0,i)

        elif bit_1>=bit_0:
            table_epsilon=del_rows(table_epsilon,1,i)


    #print(table_epsilon)


    return int(table[0],2)*int(table_epsilon[0],2)
        



if __name__ == '__main__':
    print(f"part 1 : {main_v1()}" , f"\npart 2 : {main_v2()}")
