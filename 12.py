import logging

logging.basicConfig(level=logging.WARNING)


routes = {}

ways=0

all_paths=[]


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

        if  src!="start" and dst!="end"  :


            if not dst in routes :

                routes[dst]=[]
                routes[dst].append(src)

            else:

                routes[dst].append(src)


    logging.debug(routes)


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


def get_small_caves():

    small_caves=[]

    for cave in routes:

        if cave!="start" and cave!="end" and cave.islower():

            small_caves.append(cave)


    return small_caves


def recursive_finding_repeated_cave(src,visited,small_cave,flag,path):   

    global ways

    path.append(src)

    if src=="end" and path not in all_paths:
        
        all_paths.append(path)

        #logging.debug("part2: "+path)
        
        ways +=1
        return


    if src in routes:

        if src==small_cave and flag==1:

            visited.append(src)
            flag=2

        elif src==small_cave and flag==0:

            flag=1

        elif src.islower():

            visited.append(src)

        for dst in routes[src]:

            if dst not in visited:

                recursive_finding_repeated_cave(dst, visited[:],small_cave,flag,path[:]) 


def compute_paths_p2():

    global ways

    small_caves=get_small_caves()

    for small_cave in small_caves:

        for dst in routes["start"]:

            recursive_finding_repeated_cave(dst,[],small_cave,0,[]) 

    return ways


def main_p2():

    global ways

    ways=0

    return compute_paths_p2()
    

if __name__ == "__main__":
  
    print(f"part 1 : {main_p1()}\n")
    print(f"part 2 : {main_p2()}\n")  
  