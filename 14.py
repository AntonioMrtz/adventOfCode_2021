import logging
import collections
import math

logging.basicConfig(level=logging.CRITICAL)


insertion_rules={}

pairs={}

current_polymer=""
initial_polymer=""


STEPS_P1=10
STEPS_P2=40


def read_insertion_rules():

    global current_polymer
    global initial_polymer

    file=open("input14.txt","r")
    #file=open("prueba.txt","r")

    line=file.readline()

    current_polymer=line.replace("\n","")
    initial_polymer=current_polymer

    while True:

        line=file.readline()


        if not line:

            break

        insertion_rules[line.split(" -> ")[0]]=line.split(" -> ")[1].replace("\n","")


def process_result()->int: # -> max occurrences - min occurrences 

    res = collections.Counter(current_polymer)
    max_occurrence = current_polymer.count(max(res, key = res.get))
    min_occurrence = current_polymer.count(min(res, key = res.get))

    return max_occurrence-min_occurrence

def insert_polymers():  # modifies global string current_polymer

    global current_polymer

    new_polymer=""

    for i in range(0,len(current_polymer)):

        current_character=current_polymer[i]

        if i!=len(current_polymer)-1: # not last character

            next_character=current_polymer[i+1]

            if insertion_rules[current_character+next_character]: 

                new_polymer+=(current_character+insertion_rules[current_character+next_character])

        else:
                
            new_polymer+=next_character

    
    current_polymer=new_polymer
    logging.debug(current_polymer)


def main_p1()->int:

    read_insertion_rules()

    for i in range(0,STEPS_P1):

        insert_polymers()
       
    return process_result()


def create_pairs_from_input(): # updates pairs from initial string

    global current_polymer
    global pairs

    for i in range(0,len(current_polymer)):

        if not i==len(current_polymer)-1:

            if not current_polymer[i]+current_polymer[i+1] in pairs.keys():

                pairs[current_polymer[i]+current_polymer[i+1]]=1

            else:

                pairs[current_polymer[i]+current_polymer[i+1]]+=1



def process_result_pairs()->int:

    occurrences={}

    max_occurrence_letter=0
    min_occurrence_letter=99999999999999999999999999999

    for pair in pairs.keys():

        for char in pair[0],pair[1]:

            if char in occurrences.keys():

                occurrences[char]+=pairs[pair]

            else:

                occurrences[char]=pairs[pair]

    for letter in occurrences.keys():

        occurrences[letter]=math.ceil(occurrences[letter]/2)

        
    for value in occurrences.values():

        if value>max_occurrence_letter:

            max_occurrence_letter=value

        if value<min_occurrence_letter:

            min_occurrence_letter=value
            

    logging.debug(occurrences)

    return max_occurrence_letter-min_occurrence_letter
        


def insert_polymers_pairs(): # updates dict "pairs" with new pairs

    global pairs
    global current_polymer

    new_pairs={}

    for pair in pairs.keys():

        if pair in insertion_rules.keys():

            if not pair[0]+insertion_rules[pair] in new_pairs.keys():

                new_pairs[pair[0]+insertion_rules[pair]] = pairs[pair]

            else:

                new_pairs[pair[0]+insertion_rules[pair]] += pairs[pair]

            if not insertion_rules[pair]+pair[1] in new_pairs.keys():

                new_pairs[insertion_rules[pair]+pair[1]] = pairs[pair]

            else:

                 new_pairs[insertion_rules[pair]+pair[1]] += pairs[pair]

            

    pairs=new_pairs
    logging.debug(pairs)


def main_p2()->int:

    global current_polymer
    global initial_polymer

    current_polymer=initial_polymer

    create_pairs_from_input()

    for i in range(0,STEPS_P2):

        logging.debug(i+1)
        insert_polymers_pairs()
    
    logging.debug(pairs)

    return process_result_pairs()

if __name__=="__main__":

    print(f"part 1 : {main_p1()}\n")
    print(f"part 2 : {main_p2()}\n")