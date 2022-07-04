import logging

logging.basicConfig(level=logging.INFO)


input=[]
folds=[]

dots={} # keys could be x or y depending or the first fold

size_paper_y=0
size_paper_x=0


# coordenates (x,y) 
# x -> positions right
# y -> positions down


def read_input():

    file = open("input13.txt")
    #file = open("prueba.txt")

    while True:

        line = file.readline()
        line = line.replace("\n", "")

        if not line:

            break

        elif line.startswith("fold"):

            folds.append(line)

        else:
            input.append(line)


def organize_dots(first_fold):     # the keys  are x or y values depending of the first fold

    global size_paper_y
    global size_paper_x

    if first_fold[0]=="y":

        for dot in input:

            if(int(dot.split(",")[1]!=first_fold[1])):

                x=dot.split(",")[0]
                y=dot.split(",")[1]

                if int(x)>size_paper_x:

                    size_paper_x=int(x)

                
                if int(y)>size_paper_y:

                    size_paper_y=int(y)



                if y in dots:

                    dots[y].append(x)

                else:

                    dots[y]=[]
                    dots[y].append(x)


    elif first_fold[0]=="x":

        for dot in input:

            if(int(dot.split(",")[0]!=first_fold[1])):

                x=dot.split(",")[0]
                y=dot.split(",")[1]

                if int(x)>size_paper_x:

                    size_paper_x=int(x)


                if int(y)>size_paper_y:

                    size_paper_y=int(y)


                if x in dots:

                    dots[x].append(y)

                else:

                    dots[x]=[]
                    dots[x].append(y)

    logging.debug(f" dots : {dots}")




def make_fold(first_fold):


    dots_set=set()

    split_number = first_fold[1]


    if "y" in first_fold[0]:

        if split_number<=(size_paper_y/2): 
        
            for row in dots.keys():


                if int(row)>split_number:

                    # convert coordenates of y

                    for x in dots[row]: #! CHECKEAR

                        dots_set.add(str(x)+","+str(split_number-(int(row)-split_number))) 
                    


                elif int(row)<split_number:
                    
                    for x in dots[row]:

                        dots_set.add(str(x)+","+str(row))                
        

        else:

            for row in dots.keys():


                if int(row)>split_number:

                    for x in dots[row]:

                        dots_set.add(str(x)+","+str(row))  


                elif int(row)<split_number:
                    
                    # convert coordenates of y
                       
                    for x in dots[row]:

                        dots_set.add(str(x)+","+str(split_number-int(row)+split_number))


    ### ------

    elif "x" in first_fold:
       
            if split_number<=(size_paper_x/2): 
            
                for column in dots.keys():


                    if int(column)>split_number:

                        # convert coordenates of x

                        for y in dots[column]: 

                            dots_set.add(str(split_number-(int(column)-split_number))+","+str(y))
                        


                    elif int(column)<split_number:
                        
                        for y in dots[column]:

                            dots_set.add(str(column)+","+str(y))                
            

            else:

                for column in dots.keys():


                    if int(column)>split_number:

                        for y in dots[column]:

                            dots_set.add(str(column)+","+str(y))  


                    elif int(column)<split_number:
                        
                        # convert coordenates of x
                        
                        for y in dots[column]:

                            dots_set.add(str(split_number-int(column)+split_number)+","+str(y))


    logging.debug(dots_set)

    return len(dots_set)


def main_p1():


    read_input()

    first_fold=folds[0] # we only need the first fold in part1

    if "x" in first_fold:

        first_fold=["x",int(first_fold.split("=")[1])]

    elif "y" in first_fold:

        first_fold=["y",int(first_fold.split("=")[1])]

    organize_dots(first_fold)  # first_fold=["x",5] -> fold along x=5
    

    return make_fold(first_fold)


if __name__ == "__main__":
  
    print(f"part 1 : {main_p1()}\n")
    #print(f"part 2 : {main_p2()}\n")  