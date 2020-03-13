from collections import Counter
import time
import os
from os.path import dirname

def merge(list1, list2):
    merged_list=tuple(zip(list1, list2))
    return merged_list

def greedy_p(p):
    x=0
    dist_ij=[]
    for e in data[1:]:        
        x=x+1
        dist_ij.append(data[x])
   
    dij=[]
    for e in dist_ij:
        dij.append(tuple(map(int, e.split())))
    #List of distances_ij already integer values
    list_sum_dij=[]
    
    #Sum for each to facility to all customers
    for i in range(len(dij)):
        list_sum_dij.append( sum(dij[i])-i )

    ind=[i for i in range(m)]
    #List of sums with index
    listsumindex= merge(ind, list_sum_dij)
    #From smallest to greatest sum
    lsum=sorted(listsumindex, key=lambda i: i[1], reverse=False)

    #Append the facility which which most reduces total cost/distance until the p criteria is met
    F=[] 
    x=0
    totdist=0
    while p!=0:
        F.append(lsum[x][0])
        totdist+=lsum[x][1]
        x+=1
        p-=1
    print('Facilities to be opened: ')
    print(F)
    print('Total distance/cost covered: ',totdist)

def greedy_ls(p):
    x=0
    dist_ij=[]
    for e in data[1:]:        
        x=x+1
        dist_ij.append(data[x])
   
    dij=[]
    for e in dist_ij:
        dij.append(tuple(map(int, e.split())))
    #List of distances_ij already integer values
    #List of distances_ij already integer values
    list_sum_dij=[]
    
    #*Sum for each facility to all customers
    for i in range(len(dij)):
        list_sum_dij.append( sum(dij[i])-i )

    ind=[i for i in range(m)]
    #List of sums with index
    listsumindex= merge(ind, list_sum_dij)
    #From smallest to greatest sum
    lsum=sorted(listsumindex, key=lambda i: i[1], reverse=False)

    #Append the facility which which most reduces total cost/distance until the p criteria is met
    
    #Count how many customers each facility has
    #*Create as many subsets of Vi as there are customers
    V = [[] for i in range(n)]
    
    for j in range(n):#through customers
        for i in range(m):#through facilities
            V[j].append(dij[i][j+1])
    #V[0]=distances from customer 0 to every facility 
    F=[] 
    totdist=0
    F.append(lsum[0][0])
    totdist+=lsum[0][1]#Add the distance covered
    dij.pop(lsum[0][0])
    V.pop(lsum[0][0])#Don´t consider the already assigned facility
    p = p - 1
    
    #*Assign the customers to their closest facility
    closest_f=[]     #List of which facility is closest to each customer
    for subset in V:
        closest_f.append(subset.index(min(subset)))
    
    result = [item for items, c in Counter(closest_f).most_common() #Ordered list with facilities repeating many times they were chosen as the closest
                                      for item in [items] * c] 
    lcust=[]
    l_times=[]
    c=0
    k=result[0]
    for i in range(len(result)):
        if k == result[i]:
            c+=1
        else:
            lcust.append(k)
            l_times.append(c)
            k=result[i]
            c=1
            if k==result[-1]:
                lcust.append(k)
                l_times.append(1)

    assign_f=merge(lcust,l_times) #Ordered list with facilities and how many times they were chosen as the closest
    #print("Facilities, and how many customers were assigned to them as they chose the closest one:\n", assign_f)       

    #*Select the following facilities with most customers, without considering the already selected facility
    
    for i in range(len(assign_f)):
        if assign_f[i][0] != F[0]:
            F.append(assign_f[i][0])
            p = p - 1
            if p==0:
                break      
    print(F)
    
    for e in F[1:]:
        for i in range(len(lsum)):
            if e ==lsum[i][0]:
                totdist+=lsum[i][1]


    print('Total distance/cost covered: ',totdist)




print('.txt files in directory\n')
for file in os.listdir(dirname(os.path.realpath(__file__))):#os.path.realpath(__file__)
    if file.endswith(".txt"):
        print(f"* {file} ")
print('\n')
try:
    filename=input('Enter a filename or press Enter to leave it as instancia: ')
    if len(filename) != 0:
        filename+='.txt'
except:
    filename=' '

if len(filename) == 0:    
    with open('instancia.txt', 'r') as f:
        data = f.read().splitlines()
        f.close()   

elif filename != ' ':
    try:
        with open(filename, 'r') as f:
            data = f.read().splitlines()
            f.close()
    except:
        print('Instance not received')

try:      
    list_elements=[]
    for e in data:
        list_elements.append(tuple(e.split())) #.split()= each space represents another element of the tuple
    #list of tuples
    m=list_elements[0][0]
    n=list_elements[0][1] 
    p=list_elements[0][2]

    print('Instance received')
    print("The instance received contains "+ m + " facilities and "+ n + " customers \nThe amount of facilities to be opened is:", p)
    print('\n')
    m=int(m)
    n=int(n)
    p=int(p)

    try:
        choice=int(input('Enter 1 for Local search or 2 for doing it without ls: '))
        if choice==1:
            greedy_ls(p)
        else:
            greedy_p(p)
    except:
        print("Running it without local search then")
        greedy_p(p)
        
except:
    print('data not processed')
