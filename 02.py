'''
Created on 01 december 2021

@author: Antonio Martínez Fernández
'''


def lectura():

    archivo=open("input02.txt")
    # archivo=open("prueba.txt")
    return archivo

def main_v1():

    archivo=lectura()
    
    x=0     #horizontal
    y=0     #vertical


    while True:

        linea=archivo.readline()

        if not linea:
            break

        #implementacion
        
        steps=int(linea.split()[1])

        if linea.startswith("f"):
            #forward

            x+=steps

        elif linea.startswith("u"):
            #up

            y-=steps


        elif linea.startswith("d"):
            #down

            y+=steps



    return x*y



def main_v2():
    pass
    
if __name__ == '__main__':
    print(f" part 1: {main_v1()}")


