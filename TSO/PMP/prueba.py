from collections import Counter
#import pandas as pd
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
    rsF = calculate_distance(F)
    print('Objective function with random start',rsF)
    return F, rsF

def sort_by_sum(F):
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
    dist=[]
    for i in range(len(listsumindex)):
        if listsumindex[i][0] in F:
            distances_F.append(listsumindex[i])
    dist_F_sorted=sorted(distances_F, key=lambda i: i[1], reverse=True)

    sorted_facilities = []
    for t in dist_F_sorted:
        sorted_facilities.append(t[0])
        dist.append(t[1])

    return dist_F_sorted, dist, sorted_facilities


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
    start_time = time.time()  #*---Start timer---
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
    irsorted=sorted(ir, key=lambda i: i[1], reverse=True) #The ones with more customers closer to them at the beggining
    #print(irsorted)
    F=[]
    for i in range(p):
        F.append(irsorted[i][0])
    timeGS = time.time() - start_time  #*---end timer----
    gsF = calculate_distance(F)
    print('Objective function with Greedy start', gsF )
    return F, gsF, timeGS

def calculate_distance(F):
    new_dij=[]
    for e in dij:
        new_dij.append(e[1:])
    V = [[] for i in range(n)] #list of empty list for each user
    
    for j in range(n):#through customers
        for i in range(m):#through facilities
            V[j].append(dij[i][j+1])
    #V[i]=distances from customer i to every facility // columns
    list_index_in_F_closest=[]
    liFc=[]
    #!For the ones on F which one is closer to you(customer)
    V2=[[] for i in range(n)]

    for i in range(len(V)):
        for j in F:
            
            menor=V[i][j]
            if V[i][j] < menor:
                menor =V[i][j]
            else:
                V2[i].append(menor)
            
            #V2[i].append(min(V[j]))
          
                
    for e in V2:
        list_index_in_F_closest.append(e.index(min(e)))

    for e in list_index_in_F_closest:
        liFc.append(F[e]) #List per customer to which facility they'd go of the opened ones
    
    added = [] 
    for i in range(len(liFc)):
        #print(dij[liFc[i]][i])
        added.append(new_dij[liFc[i]][i])
    totdist=sum(added)
    #print(totdist)

    return totdist

def vertex_substitutionBF(F, resultado_actual):
    #f = greedy_start()
    Facilities = F
    res_actual= resultado_actual
    print(Facilities)
    
    
    list_sum_dij=[]
    
    #Sum for each to facility to all customers
    for i in range(len(dij)):
        list_sum_dij.append( sum(dij[i])-i )

    ind=[i for i in range(m)]
    #List of sums with index
    listsumindex= merge(ind, list_sum_dij)
    #From smallest to greatest sum
    lsum=sorted(listsumindex, key=lambda i: i[1], reverse=False) #[(facility, sum of its row),(),()] sorted
  
    pseudo_F=[]
    for e in Facilities:
        pseudo_F.append(e)
    #F2=list(Facilities)
    
   
    
    #! Vertex Substitution----------------------

    Facilities_sorted = sort_by_sum(Facilities)
    dist_F_sorted = Facilities_sorted[0] # (facility, distance)
    distances_F = Facilities_sorted[1] #distances from largest to smallest
    sorted_facilities = Facilities_sorted[2].copy() #facilities
    worst_facility = dist_F_sorted[0][0]
    #print(sorted_facilities)
    keep=True
    start_time = time.time()  #*---Start timer---
    
    
    
    Neighbors=[]
    evaluation_Neighbors=[]
    while keep:
        Neighbors.clear()
        evaluation_Neighbors.clear()
        x=0
        #print('(ordered) lsum:', lsum)
        for i in range(len(lsum)):
            try:
                if lsum[i][0] not in sorted_facilities and lsum[i][1] < distances_F[x]:

                    sorted_facilities.pop(x)
                    sorted_facilities.insert(x, lsum[i][0])
                    Neighbors.append(list(sorted_facilities)) 
                   
                    if x < p-1:
                        x+=1
                    else:
                        break
                    #index = pseudo_F.index(worst_facility)
                    #pseudo_F.pop(index)
                    #pseudo_F.insert(index, lsum[i][0])                
                    #Neighbors.append(list(map(lambda x: x if x != sorted_facilities[0] else lsum[i][0], 
                    # sorted_facilities)))##pseudo_F [index] = lsum[i][0]
                    #dist_F_sorted.pop(0)
                    #dist_F_sorted.insert(0, lsum[i])
                     
            except ValueError:
                pass
                
        if len(Neighbors) > 0:    
            for e in Neighbors:
                evaluation_Neighbors.append(calculate_distance(e))
            indexmin = evaluation_Neighbors.index(min(evaluation_Neighbors))

            if evaluation_Neighbors[indexmin] < res_actual:
                res_actual= evaluation_Neighbors[indexmin]
                #F2=list(Neighbors[indexmin])
                pseudo_F=list(Neighbors[indexmin]) 
                distances_F.clear()
                dist_F_sorted.clear()                   
                Facilities_sorted = sort_by_sum(pseudo_F)
                dist_F_sorted = Facilities_sorted[0]
                distances_F = Facilities_sorted[1]
                sorted_facilities = Facilities_sorted[2].copy()
                    
            else:#?random changes could be implemented here as well?
                 
                keep=False

        elif len(Neighbors) == 0: #If no changes were made, a random change could be made...
            """ 
            ir = random.randint(0,p-1) #index that´ll change
            for i in range(p):
                if listsumindex[i][0] not in pseudo_F:
                    pseudo_F.pop(ir)
                    pseudo_F.insert(ir, listsumindex[i][0])
                    Neighbors.append(list(pseudo_F))
                    
            #print('N(X2)',Neighbors)
            for e in Neighbors:
                evaluation_Neighbors.append(calculate_distance(e))
            indexmin = evaluation_Neighbors.index(min(evaluation_Neighbors))
            if evaluation_Neighbors[indexmin] < res_actual:
                res_actual= evaluation_Neighbors[indexmin]
                F2=list(Neighbors[indexmin])            
            """   
            keep=False
           
    timeBF = time.time() - start_time  #*---end timer----
    print('Final F2', pseudo_F)

    res_f2=calculate_distance(pseudo_F)
    
    print('ObFun After VS with BF', res_f2)

    return pseudo_F, res_f2, timeBF 


    #!------------------------------


    
def vertex_substitutionFF(F, resultado_actual):
    #f = greedy_start()
    Facilities = F
    res_actual= resultado_actual
    print(Facilities)
    
    list_sum_dij=[]
    
    #Sum for each to facility to all customers
    for i in range(len(dij)):
        list_sum_dij.append( sum(dij[i])-i )

    ind=[i for i in range(m)]
    #List of sums with index
    listsumindex= merge(ind, list_sum_dij)
    #From smallest to greatest sum
    lsum=sorted(listsumindex, key=lambda i: i[1], reverse=False)
    
    Facilities_sorted = sort_by_sum(Facilities)
    dist_F_sorted = Facilities_sorted[0]
    #distances_F = Facilities_sorted[1]

    pseudo_F=[]
    for e in Facilities:
        pseudo_F.append(e)
  
    #?Vertex Substitution 
    start_time = time.time()
    new_r = res_actual
    iterations = 0
    noimprov = 0
    continueFF = True
    while continueFF:
        for j in range(len(lsum)):
            if lsum[j][0] not in pseudo_F and lsum[j][1] < dist_F_sorted[0][1]:
                iterations += 1
                #print(iterations)
                index=pseudo_F.index(dist_F_sorted[0][0])
                pseudo_F.pop(index)
                pseudo_F.insert(index, lsum[j][0])
                result = calculate_distance(pseudo_F)
                
                if  result < new_r:
                    new_r = result
                    #distances_F.clear()
                    dist_F_sorted.clear()
                    Facilities_sorted = sort_by_sum(pseudo_F)
                    dist_F_sorted = Facilities_sorted[0]
                    #distances_F = Facilities_sorted[1]
                    break                   
                    
                else:
                    pseudo_F.pop(index)
                    pseudo_F.insert(index, dist_F_sorted[0][0])
                    noimprov +=1
                    
            else:
                iterations+=1
            #if iterations > 20:
                #break;
                #print(iterations)
        if noimprov >= len(lsum) or result >= new_r:
            continueFF = False      
        
                
            #if iterations > 20:
                #break;
                #print(iterations)
         
                   
    
    res_nuevo=new_r  
    #print('Res: ', res_nuevo) 
    if len(set(pseudo_F)) == len(Facilities) and res_nuevo < res_actual:
        print('Obj. Function After VS with FF strategy: ', res_nuevo) 
        print('After VS with FF strategy',pseudo_F) 
        timeFF = time.time() - start_time
        return pseudo_F, res_nuevo, timeFF
    else:
        print(f'Could not be improved in {iterations}: ', res_actual)
        print('The same facilities opened after trying VS: ',Facilities)  
        timeFF = time.time() - start_time
        return Facilities, res_actual, timeFF
    
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
        #datapd= pd.read_csv('instancia.txt')
        f.close()   

elif filename != ' ':
    try:
        with open(filename, 'r') as f:
            data = f.read().splitlines()
            #datapd= pd.read_csv(filename)
            f.close()
    except:
        print('Instance not received')
        

     
list_elements=[]
i=0
for e in data:
    i+=1
    #print(i)
    list_elements.append(tuple(e.split())) #.split()= each space represents another element of the tuple
#print(list_elements)
#list of tuples
m=list_elements[0][0]
n=list_elements[0][1] 
p=list_elements[0][2]
mu=list_elements[0][3]

print('Instance received')
print("The instance received contains "+ m + " facilities and "+ n + " customers \nThe amount of facilities to be opened is:", p)
print('\n')
m=int(m)
n=int(n)
p=int(p)
mu=int(mu)

x=0
dist_ij=[]
for e in data[1:]:        
    x=x+1
    dist_ij.append(data[x])

dij=[]
for e in dist_ij:
    dij.append(tuple(map(float, e.split())))
#print(dij)


#*------------------------------------------Calls---------------------------------------
RS = random_start()

GS = greedy_start()

RBF = vertex_substitutionBF(RS[0], RS[1]) #random start
GBF = vertex_substitutionBF(GS[0], GS[1]) #greedy start

RFF = vertex_substitutionFF(RS[0], RS[1])#random start
GFF = vertex_substitutionFF(GS[0], GS[1])#greedy start
print('Time GS+BF: ',GBF[2])
print('Time GS+FF: ',GFF[2])

#print('RS+FF = ', RFF[1])

filepath = 'resultados/results.txt'
f=open(filepath, "a+")
f.write('\n')
#f.write('%r, %r' % (GS[1], GS[2]))
f.write('%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r' % (p, m, n, mu, RS[1], GS[1], RBF[1], RBF[2], GBF[1], GBF[2], RFF[1], RFF[2], GFF[1], GFF[2] ))

#m15 last one