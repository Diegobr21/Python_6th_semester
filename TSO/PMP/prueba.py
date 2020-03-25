from collections import Counter
import time
import random
import os
from os.path import dirname

def merge(list1, list2):
    merged_list=tuple(zip(list1, list2))
    return merged_list

def random_start(m,p,n):
    x=0
    dist_ij=[]
    for e in data[1:]:        
        x=x+1
        dist_ij.append(data[x])
   
    dij=[]
    for e in dist_ij:
        dij.append(tuple(map(int, e.split())))

    list_facilities=[]
    for i in range(m):
        list_facilities.append(i)
    F=random.sample(list_facilities, p)
    print('Objective function with random start',calculate_distance(m,n,dij,F))
    return F


def greedy_start(m,n,p):
    x=0
    dist_ij=[]
    for e in data[1:]:        
        x=x+1
        dist_ij.append(data[x])
   
    dij=[]
    for e in dist_ij:
        dij.append(tuple(map(int, e.split())))
    #print(dij)
    listmin=[]
    listmax=[]
    for i in range(len(dij)):
        listmin.append(min(dij[i][1:]))
        listmax.append(max(dij[i][1:]))
    vmin=min(listmin)
    vmax=max(listmax)
    radius = (vmax + vmin)/2 #Greedy Start radius
    #---------------------Initial Selection----------------------------
    inside_radius=[]
    for i in range(len(dij)):
        inside_radius.append(0)
    for i in range(len(dij)):
        for j in range(n):
            if dij[i][j] <= radius:
                inside_radius[i]+=1
    #print(inside_radius)
    list_index_facilities=[]
    for i in range(m):
        list_index_facilities.append(i)
    ir = merge(list_index_facilities, inside_radius)
    irsorted=sorted(ir, key=lambda i: i[1], reverse=True)
    #print(irsorted)
    F=[]
    for i in range(p):
        F.append(irsorted[i][0])
    print('Objective function with Greedy start', calculate_distance(m,n,dij,F))
    return F

def calculate_distance(m,n,dij,F):
    new_dij=[]
    for e in dij:
        new_dij.append(e[1:])
    V = [[] for i in range(n)]
    
    for j in range(n):#through customers
        for i in range(m):#through facilities
            V[j].append(dij[i][j+1])
    #V[0]=distances from customer 0 to every facility 
    list_index_in_F_closest=[]
    liFc=[]
    #!For the ones on F which one is closer to you
    V2=[[] for i in range(n)]
    for i in range(len(V)):
        for j in F:
            menor=V[i][j]
            if V[i][j] < menor:
                menor =V[i][j]
            else:
                V2[i].append(menor)
          
                
    for e in V2:
        list_index_in_F_closest.append(e.index(min(e)))

    for e in list_index_in_F_closest:
        liFc.append(F[e]) #List per customer to which facility they'd go of the opened ones
    #print(list_index_in_F_closest,'\n')
    #print(liFc)
    #print('****************************************************',V2)
    #print(dij)
    #print(list_index_closest_facility)
    added = [] 
    for i in range(len(liFc)):
        #print(dij[liFc[i]][i])
        added.append(new_dij[liFc[i]][i])
    totdist=sum(added)
    #print(totdist)

    return totdist

#*-------------------------------------------------------------------------------------------------------------*#
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

F=greedy_start(m,n,p)
Fr= random_start(m,p,n)
print('GS',F)
print('RS',Fr)
    