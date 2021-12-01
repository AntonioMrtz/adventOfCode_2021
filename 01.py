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


if __name__ == '__main__':
    print(main_v1())