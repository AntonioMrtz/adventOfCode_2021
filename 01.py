'''
Created on 01 december 2021

@author: Antonio Martínez Fernández
'''

def lectura():

    archivo=open("input01.txt")
    #archivo=open("prueba.txt")
    return archivo

def main_v1():

    archivo=lectura()

    contador=0
    anterior=-1

    while True:

        linea=archivo.readline()

        if not linea:
        
            break

        linea=int(linea)

        if anterior==-1:

            anterior=linea
            
        
        else:

            actual=linea
            #print(f"anterior {anterior}" f"actual {actual}")

            if actual-anterior>0:
                
                contador+=1

            anterior=linea

    return contador



def addArray(array):

    total=0

    for i in range(3):

        total+=int(array[i])

    return total



def main_v2():
    
    archivo=lectura()
    contador=0
    
    # we supposed that the input cant have less than 3 lines

    array=[]

    for i in range(3):

        linea=archivo.readline()
        array.append(int(linea))


    last=addArray(array)

    while True:

        linea=archivo.readline()

        if not linea:

            break

        array.pop(0)
        array.append(int(linea))

        aux=addArray(array)

        print(aux)

        if(aux>last):

            contador+=1
        

        last=addArray(array)


    return contador








if __name__ == '__main__':
    print(f"part 1 : {main_v1()}" , f"part 2 : {main_v2()}")
    