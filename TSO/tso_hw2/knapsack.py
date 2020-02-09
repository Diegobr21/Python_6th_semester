
def select_heuristic():
    try:    
        select=int(input('Your choice: '))        
        if select < 4 and select > 0:
            print('Your choice was made:', select)    
            #if 1 if 2 if 3 function()
        else:
            print('Your choice wasn´t inside the parameters')

    except:
        print('Your choice wasn´t understood')
    if select==1:
        pick_greatest_value(list_elements,w)
    elif select==2:
        pick_lower_weight(list_elements,w)
    elif select==3:
        pick_biggest_ratio(list_elements,w)    
    

def merge(list1, list2):
    merged_list=tuple(zip(list1, list2))
    return merged_list

def pick_greatest_value(elements,w):
    n=0
    lv=[]
    lw=[]
    le=[]
    
    w=float(w)
           
    for e in elements[1:]:        
        n=n+1
        lv.append(elements[n][1])
        lw.append(elements[n][2])       

        
    set_v=[]
    for i in range(len(lv)):
        lv[i]=int(lv[i])
        lw[i]=int(lw[i])

    le=merge(lv,lw)

    lvsorted=lv
    lvsorted.sort()
    #print('Both:', lvsorted)
    sumvalues=0
    for j in range(n):
        for i in range(n):
            if le[i][0]==lvsorted[-1] and le[i][1] <= w: # and i not in set_v:
                set_v.append(i)
                sumvalues+=le[i][0]
                lvsorted.pop()
                
                w = w - (le[i][1])
            elif le[i][1] > w:
                #print('Capacity left:',w)
                w=0     
                break    

    #print('index of values chosen',set_v)
    print('sum of values chosen',sumvalues) 
    return sumvalues  

def pick_lower_weight(elements, w):
    n=0
    lv=[]
    lw=[]
    le=[]
    
    w=float(w)
           
    for e in elements[1:]:
        n=n+1
        lv.append(elements[n][1])
        lw.append(elements[n][2])       

    set_v= []
    for i in range(len(lv)):
        lv[i]=int(lv[i])
        lw[i]=int(lw[i])

    le=merge(lv,lw)

    lwsorted=lw
    lwsorted.sort(reverse=True)
    #print('sorted list:', lwsorted)
    #print(le)
    
    sumvalues=0
    
    for j in range(n):
        for i in range(len(lwsorted)):
            if le[i][1]==lwsorted[-1] and lwsorted[-1] <= w: #and i not in set_v:            
                set_v.append(i)
                sumvalues+=le[i][0]
                w = w - (lwsorted[-1])
                lwsorted.pop()
                
            elif lwsorted[-1] > w:
                #print('Capacity left:',w)
                w=0
                break

    #print('index of values chosen',set_v)
    print('sum of values chosen',sumvalues)
    return sumvalues     

def pick_biggest_ratio(elements,w):
    n=0
    lv=[]
    lw=[]
    le=[]
    lr=[]
    lrsorted=[]
    set_v= set()
    
    w=float(w)
           
    for e in elements[1:]:        
        n=n+1
        lv.append(elements[n][1])
        lw.append(elements[n][2])   

        
    for i in range(len(lv)):
        lv[i]=int(lv[i])
        lw[i]=int(lw[i])

    le=merge(lv,lw)

    for i in range(len(lw)):        
        lr.append((lv[i])/(lw[i]))
        lrsorted.append((lv[i])/(lw[i]))
    
    #lrsorted.sort()
    lrsorted = sorted(lr)
    
    #print(lr)
    
    sumvalues=0
    
    for j in range(n):
        for i in range(len(lr)):            
            if lr[i] == lrsorted[-1] and le[i][1] <= w and i not in set_v:            
                set_v.add(i)
                sumvalues+=le[i][0]
                w = w - (le[i][1])
                lrsorted.pop()
                
            elif le[i][1] > w:
                #print('Capacity left:',w)
                w=0
                break

    #print('index of values chosen',set_v)
    #print('sorted list:', lrsorted)
    print('sum of values chosen',sumvalues) 
    return sumvalues

    #################################################################



def select_from_gui(select):
    if select==1:
        result= pick_greatest_value(list_elements,w)
    elif select==2:
        result= pick_lower_weight(list_elements,w)
    elif select==3:
        result= pick_biggest_ratio(list_elements,w)
    return result

try:
    with open('instancia.txt', 'r') as f:
        data = f.read().splitlines()
    list_elements=[]
    for e in data:
        list_elements.append(tuple(e.split()))
    #list of tuples
    n=list_elements[0][0]
    w=list_elements[0][1]
    print('Instance received')
    print("The instance received contains "+ n + " elements \nThe capacity of the knapsack is:", w)
    print('\n')
    print('Enter 1, 2 or 3 to pick the corresponding heuristic\n1)Pick greatest value\n2)Pick lower weight\n3)Pick biggest ratio(Vi/Wi)\n')
    try:
        choice=int(input('Are you trying to use the GUI?\n1)YES 2)NO(any other character will keep you at the cmd)\n'))
    except:
        choice=2
    if choice ==1:
        print('got it, bye')
    elif choice==2:       
        select_heuristic()
    else:
        print('option not recognized')
       
except:
    print('Instance not received')

#pick_biggest_ratio(list_elements,w)