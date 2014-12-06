#Coded by Anmol Raina 
#Shows the closure of given functional dependencies and performs a lossless 
#decomposition into BCNF

def reflexivity(fd):
    ourFplus = fd
    for i in fd:
        count = 0
        temp = i[0]
        tempList1 = [(temp, temp)]
        ourFplus = ourFplus + tempList1
        if len(temp) > 1:
            for x in temp:
                tempList2 = [(temp,[x])]
                ourFplus = ourFplus + tempList2
    #the next function gets rid of repeats(courtesy of stackoverflow)
    ourFplus = list(eval(x) for x in set([str(x) for x in ourFplus]))
    return ourFplus

def augmentation(attributes, ourFplus):
    for i in ourFplus:
        for j in attributes:
            temp = list(set(i[0] + [j]))
            temp2 = list(set(i[1] + [j]))
            ourFplus = ourFplus + [(temp,temp2)]
    #the next function gets rid of repeats(courtesy of stackoverflow)
    ourFplus = list(eval(x) for x in set([str(x) for x in ourFplus]))
    return ourFplus
   
def transitivity(newFplus):
    for i in newFplus:
        for j in newFplus:
            if i != j:
                if i[1] == j[0]:
                    tempList = [(i[0],j[1])]
                    newFplus = newFplus + tempList
                    #the next function gets rid of repeats(courtesy of stackoverflow)
                    newFplus = list(eval(x) for x in set([str(x) for x in newFplus]))
   
    return newFplus
#the attribute closure function
#Algorithm used from the textbook
def closure(attributes, fd):
    test1 = 0
    check = 0
    while(check!= 1):
            test2 = len(fd)
            Fplus = reflexivity(fd)
            newFplus = augmentation(attributes, Fplus)
            finalFplus = transitivity(newFplus)  
            test1 = len(finalFplus)
            finalFplus = list(eval(x) for x in set((str(x) for x in finalFplus)))
            fd = finalFplus
            if(test2 == test1):
                check = 1
    return fd

#the bcnf function which tries to decompose using a functional dependency at a time    
'''
Algorithm used from stackOverflow:
Initialize S = {R}
While S has a relation R' that is not in BCNF do:   
   Pick a FD: X->Y that holds in R' and violates BCNF
   Add the relation XY to S
   Update R' = R'-Y
Return S
'''


def bcnf(relation,fds):    
    listRelation = ""
    check = 0
    for i in fds:
        for j in i:
                if j[0] in relation:
                    check = 1
                else:
                    check = 0
                    print ("\nCannot be decomposed using dependency: "+ str(i))
                    break
        if check == 1:
            newRelation = i[0] + i[1]
            print("\nFunctional dependency used: " + str(i))
            print ("New Relation Added: " + str(newRelation))
            listRelation = listRelation + str(newRelation) + ","
            temp = 0
            while temp < len(i[1]):
                relation.remove(i[1][temp])
                temp = temp +1
            print ("Original Relation Modified: " + str(relation))
    print("\nAll final relations: " + listRelation + str(relation))  
    
def main():
    fd1 = ([1],[2])
    fd2 = ([2,3],[4,5])
    fds = [fd1,fd2]
    tempfd = closure([1,2,3,4,5], fds)
    
    #closure takes a while (about 2 min) to output
    
    print(tempfd)
    counter = 0
    for i in tempfd:
        counter = counter + 1
    print ("\nNumber of functional dependencies: " + str(counter))
    bcnf([1,2,3,4,5], fds)

main()

