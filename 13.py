import logging

logging.basicConfig(level=logging.WARNING)


input=[]
folds=[]

dots={} # keys could be x or y depending or the first fold

size_paper_y=0
size_paper_x=0

fold_result_set=None # -> stores set of dots given by doing the folds


# coordenates (x,y) 
# x -> positions right
# y -> positions down


def read_input()->None:

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


def organize_dots(first_fold:list)->None:     # the keys  are x or y values depending of the first fold

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





def make_fold(fold:list)->list:  # returns [ number of dots , set of dots] | gets fold[x,159]

    global dots
    global fold_result_set

    dots_set=set()

    split_number = fold[1]


    if "y" in fold[0]:

        if split_number<=(size_paper_y/2): 
        
            for row in dots.keys():


                if int(row)>split_number:

                    # convert coordenates of y

                    for x in dots[row]: 

                        dots_set.add(str(x)+","+str(split_number-(int(row)-split_number))) 
                    


                elif int(row)<split_number:
                    
                    for x in dots[row]:

                        dots_set.add(str(x)+","+str(row))                
        

        else:

            for row in dots.keys():


                if int(row)<split_number:

                    for x in dots[row]:

                        dots_set.add(str(x)+","+str(row))  


                elif int(row)>split_number:
                    
                    # convert coordenates of y
                       
                    for x in dots[row]:

                        dots_set.add(str(x)+","+str(split_number-int(row)+split_number))


    ### ------

    elif "x" in fold:
       
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

    fold_result_set=dots_set
    return len(dots_set),dots_set


def main_p1():

    global fold_result_set

    read_input()

    first_fold=folds[0] # we only need the first fold in part1

    if "x" in first_fold:

        first_fold=["x",int(first_fold.split("=")[1])]

    elif "y" in first_fold:

        first_fold=["y",int(first_fold.split("=")[1])]

    organize_dots(first_fold)  # first_fold=["x",5] -> fold along x=5
    
    first_fold_result_set=make_fold(first_fold)

    fold_result_set=first_fold_result_set[1]

    return first_fold_result_set[0], first_fold_result_set[1]



def print_folds_result(dots_set:list,last_fold:list)->str: # it uses dots_set to print the final fold

    global size_paper_x
    global size_paper_y
   
    line="\n"

    for i in range(0, size_paper_y+1):

        for j in range(0, size_paper_x+1):

            found_flag = 0

            for dot in dots_set:

                x = dot.split(",")[0]
                y = dot.split(",")[1]

                if int(x) == j and int(y) == i:

                    found_flag = 1

            if found_flag == 1:

                    line += "#"

            else:

                line += " "

        line+="\n"

    return line

def organize_dots_by_set(dots_set:set,fold_data:list)->None: # updates dots{} by using set of dots ( instead of file) and fold data
    
    global size_paper_y
    global size_paper_x
    global dots

    dots={}

    size_paper_x=0
    size_paper_y=0

    if fold_data[0]=="y":

        for dot in dots_set:

            if(int(dot.split(",")[1]!=fold_data[1])):

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


    elif fold_data[0]=="x":

        for dot in dots_set:

            if(int(dot.split(",")[0]!=fold_data[1])):

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



def main_p2():

    global fold_result_set

    folds.pop(0) # get rid of first pop ( we did it in p1 )

    for fold in folds:

        if "x" in fold:

            fold_data=["x",int(fold.split("=")[1])]

        elif "y" in fold:

            fold_data=["y",int(fold.split("=")[1])]

        organize_dots_by_set(fold_result_set,fold_data)          # use set of dots to update dots{} 
        make_fold(fold_data)

    organize_dots_by_set(fold_result_set,fold_data)

    logging.debug(fold_result_set)

    return print_folds_result(fold_result_set,fold_data)



if __name__ == "__main__":
  
    print(f"part 1 : {main_p1()[0]}\n")
    print(f"part 2 : {main_p2()}\n")  