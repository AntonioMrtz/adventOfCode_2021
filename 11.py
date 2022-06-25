import logging

logging.basicConfig(level=logging.WARNING)


flashes=0


def read_file():
     
    file = open("input11.txt")
    #file = open("prueba.txt")

    input_matrix=[]
    output = []

    while True:

        line = file.readline()

        if not line:

            break

        input_matrix.append(list(map(int,line.replace("\n",""))))    

    return input_matrix


def manage_adjacent(i,j,input_matrix,flashed_cells):

    # check adjacents

    # add extra value if mod 9 != 0 

    #mod = input_matrix[i][j] % 9

    #logging.debug(mod)

    if i-1>=0 and j-1>=0 and [i-1,j-1] not in flashed_cells: # up left

        input_matrix[i-1][j-1]+=1

    if i-1>=0 and j+1 < len(input_matrix[i]) and [i-1,j+1] not in flashed_cells: #up right

        input_matrix[i-1][j+1]+=1

    if i+1 < len(input_matrix) and j-1>=0 and [i+1,j-1] not in flashed_cells: #down left

        input_matrix[i+1][j-1]+=1

    if i+1 < len(input_matrix) and j+1 < len(input_matrix[i]) and [i+1,j+1] not in flashed_cells : # down right

        input_matrix[i+1][j+1]+=1



    if i-1>=0 and [i-1,j] not in flashed_cells: # up

        input_matrix[i-1][j]+=1

    if j-1>=0 and [i,j-1] not in flashed_cells: # left

        input_matrix[i][j-1]+=1

    if j+1 < len(input_matrix[i]) and [i,j+1] not in flashed_cells: # right

        input_matrix[i][j+1]+=1    

    if i+1 < len(input_matrix) and [i+1,j] not in flashed_cells: # down

        input_matrix[i+1][j]+=1





def manage_flashes(input_matrix):

    global flashes

    flashed_cells = [] 

    # iterate while there are changes , if not return 
    # consider adding a list to store cells that flashed if theres needed

    while True:

        has_changed=0 # updates when theres a change

        for i in range(0,len(input_matrix)):

                for j in range(0,len(input_matrix[0])):

                    if input_matrix[i][j]>=10: #flashes -> manage adjacents
                        
                        flashes+=1
                        #input_matrix[i][j]=0 + input_matrix[i][j] % 9
                        input_matrix[i][j]=0
                        manage_adjacent(i,j,input_matrix,flashed_cells)
                        flashed_cells.append([i,j])
                        has_changed=1


        if has_changed==0:
            break




def update_matrix(input_matrix):

    for i in range(0,len(input_matrix)):

        for j in range(0,len(input_matrix[0])):

            input_matrix[i][j]=input_matrix[i][j]+1


    manage_flashes(input_matrix)


def main_p1():
    
    input_matrix=read_file()

    logging.debug(f" p1 : start matrix = {input_matrix}")

    has_changed=0


    for i in range(100):

        update_matrix(input_matrix)
        

    logging.debug(f" p1 :end matrix = {input_matrix}")

    return flashes



def check_all_flashed(input_matrix):

    for i in range(0,len(input_matrix)):

        for j in range(0,len(input_matrix[0])):

            if input_matrix[i][j]!=0:

                return False

    return True
 

def main_p2():

    input_matrix=read_file()

    steps=1

    while True:

        update_matrix(input_matrix)
        
        if check_all_flashed(input_matrix):
            break

        steps+=1

    return steps


if __name__ == "__main__":
    
    read_file()

    
    print(f"part 1 : {main_p1()}\n")
    print(f"part 2 : {main_p2()}\n")