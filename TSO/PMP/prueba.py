from collections import Counter
import time
import random
import os
from os.path import dirname

def merge(list1, list2):
    merged_list=tuple(zip(list1, list2))
    return merged_list

def random_start():
    list_facilities=[]
    for i in range(m):
        list_facilities.append(i)
    F=random.sample(list_facilities, p)
    print('Objective function with random start',calculate_distance(F))
    return F


def greedy_start():
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
    print('Objective function with Greedy start', calculate_distance(F))
    return F

def calculate_distance(F):
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

def vertex_substitution():
    Facilities = greedy_start()
    res_actual=calculate_distance(Facilities)
    print(Facilities)
    #1)Encontrar el nodo que mas distancia añada dentro de F y tratar de cambiarlo por uno mejor 
    #1)Puede hacer suma de distancias por facility y el que más tenga dentro de F cambiarlo por uno mejor, evaluar objective function y substituirlo en F si si
    #2)Cambiar los peores nodos de F, por facilities mejores en suma de distancias y que no estén incluidas ya,
    #2) evaluar si es mejor resultado(obj function), si no, repetir hasta que no sea mejor o hasta que haya dado m iteraciones 
    
    list_sum_dij=[]
    
    #Sum for each to facility to all customers
    for i in range(len(dij)):
        list_sum_dij.append( sum(dij[i])-i )

    ind=[i for i in range(m)]
    #List of sums with index
    listsumindex= merge(ind, list_sum_dij)
    #From smallest to greatest sum
    lsum=sorted(listsumindex, key=lambda i: i[1], reverse=False)
    distances_F=[]
    for i in range(len(listsumindex)):
        if listsumindex[i][0] in Facilities:
            distances_F.append(listsumindex[i])
    dist_F_sorted=sorted(distances_F, key=lambda i: i[1], reverse=True)
    """
    dist_F_noindex=[]
    for e in distances_F:
        dist_F_noindex.append(e[1])

    print('No index',dist_F_noindex)
    """

    pseudo_F=[]
    for e in Facilities:
        pseudo_F.append(e)
    F2=list(Facilities)
  
    #?Vertex Substitution 
    """
    for i in range(len(dist_F_sorted)):
        for j in range(len(lsum)):
            if lsum[j][0] not in pseudo_F:
                if lsum[j][1] < dist_F_sorted[i][1]:
                    index=Facilities.index(dist_F_sorted[i][0])
                    pseudo_F.pop(index)
                    pseudo_F.insert(index, lsum[j][0])
                    if calculate_distance(pseudo_F) > res_actual:
                        pseudo_F.pop(index)
                        pseudo_F.insert(index, dist_F_sorted[i][0])
    """
    #?------------------------
    #!2nd VS----------------------
    keep=True
    
    print(pseudo_F)
    #print(lsum)
    #print(dist_F_sorted)
    Neighbors=[]
    evaluation_Neighbors=[]
    while keep:
        #pseudo_F=list(F2)
        Neighbors.clear()
        evaluation_Neighbors.clear()
        #changes=0
        for i in range(len(lsum)):
            if lsum[i][0] not in pseudo_F and lsum[i][1] < dist_F_sorted[0][1]:
                print('cumplido, dFs[0][1]: ', dist_F_sorted[0][1])
                index = pseudo_F.index(dist_F_sorted[0][0])
                pseudo_F.pop(index)
                pseudo_F.insert(index, lsum[i][0])                
                print(f'{i} pseudoF:' , pseudo_F)
                Neighbors.append(list(pseudo_F))
                print('N(X)',Neighbors)
                #changes+=1
                distances_F.clear()
                dist_F_sorted.clear()
                for i in range(len(listsumindex)):
                    if listsumindex[i][0] in pseudo_F:
                        distances_F.append(listsumindex[i])
                dist_F_sorted=sorted(distances_F, key=lambda i: i[1], reverse=True)
                #print(dist_F_sorted)
            #If no changes were made, a random change will be made
            """
            if changes < 1:
                ir = random.randint(0,p-1)
                pseudo_F.pop(ir)
                for i in range(len(lsum)):
                    if lsum[i][0] not in pseudo_F:
                        pseudo_F.insert(ir, lsum[i][0])
                        Neighbors.append(pseudo_F)
                changes+=1
            """
                #print(dist_F_sorted)
                #pseudo_F=list(F2)
        if len(Neighbors) > 0:    
            for e in Neighbors:
                evaluation_Neighbors.append(calculate_distance(e))
            indexmin = evaluation_Neighbors.index(min(evaluation_Neighbors))
            if evaluation_Neighbors[indexmin] < res_actual:
                F2=list(Neighbors[indexmin])
                pseudo_F=list(F2)
                #print('New F:             \n\n', F2)

            else:
                keep=False
        else:
            keep=False
    print('Final F2', F2)
    res_f2=calculate_distance(F2)
    print('Test ObFun F2', res_f2)

    #!------------------------------
    """
    res_nuevo=calculate_distance(pseudo_F)   
    #print('Res: ', res_nuevo) 
    if len(set(pseudo_F)) == len(Facilities) and res_nuevo < res_actual:
        print('Objective Function After VS: ', res_nuevo) 
        print('After VS',pseudo_F) 
        return pseudo_F
    else:
        print('Could not be improved: ', res_actual)
        print('The same facilities opened after trying VS: ',Facilities)  
        return Facilities
    """
    #print('All facilities: ', lsum)
    #print(distances_F)
    #print(dist_F_sorted)


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

x=0
dist_ij=[]
for e in data[1:]:        
    x=x+1
    dist_ij.append(data[x])
   
dij=[]
for e in dist_ij:
    dij.append(tuple(map(int, e.split())))


print(random_start())

vertex_substitution()
    