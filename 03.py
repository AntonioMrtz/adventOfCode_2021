'''
Created on 03 december 2021

@author: Antonio Martínez Fernández
'''

def lectura():

    archivo=open("input03.txt")
    # archivo=open("prueba.txt")
    return archivo

def main_v1():

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
            gamma+="0"

        elif bit_1>bit_0:
            gamma+="1"


    

    epsilon=gamma.replace("1","2")
    epsilon=epsilon.replace("0","1")
    epsilon=epsilon.replace("2","0")

    
    epsilon=int(epsilon,2)
    gamma=int(gamma,2)

    print(f"gamma = {gamma}")
    print(f"epsilon = {epsilon}")

    return int(epsilon)*int(gamma)
    

def main_v2():
    pass

if __name__ == '__main__':
    print(f"part 1 : {main_v1()}" , f"\npart 2 : {main_v2()}")