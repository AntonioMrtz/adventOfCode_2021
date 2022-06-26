import logging

logging.basicConfig(level=logging.DEBUG)


routes = {}

ways=0

def read_routes():

    file = open("input12.txt")
    #file = open("prueba.txt")


    while True:

        line = file.readline()

        if not line:

            break

        # they can go back , bidirectional relationships

        src = line.split("-")[0]
        dst = line.split("-")[1].replace("\n","")

        if dst!="start" and src!="end":

            if not src in routes:

                routes[src]=[]
                routes[src].append(dst)

            else:

                routes[src].append(dst)

        #if src != "end" and src!="start" and dst!="end"  :
        if  src!="start" and dst!="end"  :


            if not dst in routes :

                routes[dst]=[]
                routes[dst].append(src)

            else:

                routes[dst].append(src)


    logging.debug(routes)
  




# solo pilla

# start,A,b,end | start,A,end | start,b,end

def recursive_finding(src,visited):   

    global ways


    if src=="end":
        
        logging.debug(visited)

        ways +=1
        return


    if src in routes:

        if src.islower():

            visited.append(src)

        for dst in routes[src]:

            if dst not in visited:

                recursive_finding(dst, visited[:]) 

def compute_paths():

    global ways

    for dst in routes["start"]:

        recursive_finding(dst,[]) 

    return ways


def main_p1():

    read_routes()
    return compute_paths()
    

if __name__ == "__main__":
  
    print(f"part 1 : {main_p1()}\n")
    #print(f"part 2 : {main_p2()}\n")  
  