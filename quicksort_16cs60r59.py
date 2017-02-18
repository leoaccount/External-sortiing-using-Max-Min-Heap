# refer from https://gist.github.com/gnarmis/4647645#file-minmaxheap-py-L23
#refer max-min heap algorithm from http://www.akira.ruc.dk/~keld/teaching/algoritmedesign_f08/Artikler/02/Atkinson86.pdf #refer max-min heap algorithm from http://www.akira.ruc.dk/~keld/teaching/algoritmedesign_f08/Artikler/02/Atkinson86.pdf 
#!usr/bin/python2.7 -tt
from math import log, floor, pow
array=list()
import sys
flag=0
#data=sorted(data)
"""f_sort=open("temp","w")
def has_child(position):
    if len(heap)>2*position:
        return True
    else:
        return False
def has_grandchild(position):
    if has_child(2*position):
        return True
    else:
        return False

def is_grand_child(m,position):
    c_parent=int(m/2)
    c_parent=int(c_parent/2)
    if position==c_parent:
        return True
    else:
        return False  """                  
        
def leftchild(parent):
	size=len(heap)
	if 2*parent < size:
		return 2*parent;
	else:
		 return 0;
def rightchild(parent):
	size=len(heap)
	if (2*parent+1)<size:
		return 2*parent+1;
	else:
		return 0;
def grandparent(node):
	return int(int(node/2)/2);
def TrickleDown_Min(position):
	global heap
	a=list();
#creating list of childrens and its grandchildrens
	if (len(heap)>2*position):
		lc=2*position
		a.append(lc);
		if (len(heap)>4*position):
			gc=4*position
			a.append(gc);
		if (len(heap)>4*position+1):
			gc2=4*position+1
			a.append(gc2);
	if(len(heap)>2*position+1):
		rc=2*position+1
		a.append(rc)
		if (len(heap)>4*position+2):
			gc=4*position+2
			a.append(gc);
		if (len(heap)>4*position+3):
			gc2=4*position+3
			a.append(gc2)
#list creation completed
#finding minimum of the child grandchild and node
	if len(a) !=0:
		ind=position
		for childs in a:
			if heap[childs]<heap[ind]:	
				ind=childs
#if minimum is grandchild
		if(grandparent(ind)==position):
			if (heap[ind]<heap[position]):
				heap[ind],heap[position]=heap[position],heap[ind]
				if (heap[ind] > heap[int(ind/2)]):
					heap[ind],heap[int(ind/2)]=heap[int(ind/2)],heap[ind]
				TrickleDown_Min(ind);
#if ind is not a grandchild it must be child
		else:
			if heap[ind] < heap[position]:
				heap[ind],heap[position]=heap[position],heap[ind]

	else:
		pass					

#to move down the max i.e. equivalent to calling max heapify top to bottom
def TrickleDown_Max(position):
	global heap;
	a=list();
#creating list of childrens and its grandchildrens
	if (len(heap)>2*position):
		lc=2*position
		a.append(lc);
		if (len(heap)>4*position):
			gc=4*position
			a.append(gc);
		if (len(heap)>4*position+1):
			gc2=4*position+1
			a.append(gc2);
	if(len(heap)>2*position+1):
		rc=2*position+1
		a.append(rc)
		if (len(heap)>4*position+2):
			gc=4*position+2
			a.append(gc);
		if (len(heap)>4*position+3):
			gc2=4*position+3
			a.append(gc2)
#list creation completed
#finding minimum of the child grandchild and node
	if len(a) !=0:
		ind=position
		for childs in a:
			if heap[childs]>heap[ind]:	
				ind=childs
#if minimum is grandchild
		if(grandparent(ind)==position):
			if (heap[ind]>heap[position]):
				heap[ind],heap[position]=heap[position],heap[ind]
				if (heap[ind] < heap[int(ind/2)]):
					heap[ind],heap[int(ind/2)]=heap[int(ind/2)],heap[ind]
				TrickleDown_Max(ind);
#if ind is not a grandchild it must be child
		else:
			if heap[ind] > heap[position]:
				heap[ind],heap[position]=heap[position],heap[ind]
	else:
		pass       
               
        
def TrickleDown(position):
    if on_min_level(position):
        TrickleDown_Min(position)
    else:
        TrickleDown_Max(position)   
def remove_min():
    global heap
    if len(heap)==1:
        #print "no more word in heap"
        return
    #print heap
    c=list()
    size=len(heap)
    if size>1:
        c.append(heap[1])
        if size>2:
            c.append(heap[2])
            if size>3:
                c.append(heap[3])
    #minimum=min(c)
    Index=c.index(min(c))
    #print c
    val=c[Index]
    #print Index
    #print heap[Index]
    heap[Index+1]=heap[-1]     
    del(heap[-1])
    TrickleDown(Index+1)
    return val
    
    
    
def remove_max():
    global heap
    if len(heap)==1:
        #print "no more word in heap"
        return
    size=len(heap)
    #print size
    if size<=1:
        print "error:empty queue"
    else:    
        if size==2:
            print "only one word in queue, which is:%s"%(heap[1])
            del(heap[1])
        else:
            #print "in remove_max"
            val=heap[1]
            heap[1]=heap[-1]   #heap[-1]=last element of queue
            del(heap[-1])
            TrickleDown(1)
            return val
              	    
    	
    
def Bubble_up(position):
    global array
    global heap
    if on_min_level(position):
        if has_parent(position):
                if heap[position] > heap[parent(position)]:
                    swap(position, parent(position))
                    Bubble_up_max(parent(position))
                else:
                    Bubble_up_min(position)
    else:
        if has_parent(position):
            if heap[position] < heap[parent(position)]:
                swap(position, parent(position))
                Bubble_up_min(parent(position))
            else:
                Bubble_up_max(position)
                    
def Bubble_up_min(position):
        global array
        global heap
        grand_parent = parent(parent(position))
        if has_grand_parent(position):
            if heap[position] < heap[grand_parent]:
                swap(position, grand_parent)
                Bubble_up_min(grand_parent)

def Bubble_up_max(position):
        global array
        global heap
        if has_grand_parent(position):
            grand_parent = parent(parent(position))
            if heap[position] > heap[grand_parent]:
                swap(position, grand_parent)
                Bubble_up_max(grand_parent)
                
def parent(child):
    """return child's parent"""
    return int(child)/2                
                
def swap(a, b):
    """swap values between a and b"""
    global array
    global heap
    a_val = heap[a]
    b_val = heap[b]
    heap[a] = b_val
    heap[b] = a_val
    
def has_parent(position):
        p = parent(position)
        if p is not 0:
            return True
        else:
            return False

def has_grand_parent( position):
        gp = parent(parent(position))
        if gp is not 0:
            return True
        else:
            return False
                
def on_min_level(position):
    """returns bool - is it on a min level?"""
    test = on_level(position) % 2
    if test == 0:
        return False
    else:
        return True

def on_max_level(position):
    """returns bool - is it on a max level?"""
    test = on_level(position) % 2
    if test == 0:
        return True
    else:
        return False

def on_level(position):
        """returns what level the key at position is on"""
        return floor(log(int(position), 2))
heap=list()
#file_name=sys.argv[1]

def GetMin():
    if len(heap)==1:
        print "no more  element in heap"
        return
    if len(heap)==2:
        return heap[1]
    else:
        if heap[2]<heap[3]:
            return heap[2]
        else:
            return heap[3]
def GetMax():
    if len(heap)==1:
        print "no more element in heap"
        return
    return heap[1]
heap=[0]        #global array heap
def insert(word):
    global array
    global heap
    heap.append(word)
    Bubble_up(len(heap) - 1) #call Bubble_up for heapify
#myfile=open (sys.argv[1], "r")
count=0 
#l_file=open("left_file","w")
#r_file=open("right_file","w")
#l_file=open("left_file","r+")
#r_file=open("right_file","r+")
with open (sys.argv[1], "r+") as myfile:
    for line in myfile:
        count=count+1
        #print count

myfile.close()
#myfile=open(sys.argv[1],"r+")


"""quick sort start"""

def quicksort(start,end):
    print "start:%d"%start
    print "end:%d"%end
    if(end<start):
        return;
    if end-start+1<=100:
        myfile=open(sys.argv[1],"r")
        for i in range(1,start):
            myfile.readline()
            #print "skip"
        for i in range(start,end+1):
            word=myfile.readline()
            insert(word)
        myfile.close()
                #print word
        #create temp file then skip start no. of lines
        f_sort=open(sys.argv[1], "r+")
        for k in range(1,start):
            parmar=f_sort.readline()
        for j in range(start,end+1):
            p=remove_min()
            print p
            f_sort.write(p)
        f_sort.close()
        return
    myfile=open(sys.argv[1], "r+")
    #print  "hi"
    #with open (sys.argv[1], "r+") as myfile:
    for k in range(1,start):
        parmar=myfile.readline()

    for i in range(start,start+100):
        word=(myfile.readline())
        insert(word)
    #print heap
    l_file=open("left_file","w+")
    r_file=open("right_file","w+")
    #l_file=open("left_file","r+")
    #r_file=open("right_file","r+")
    l_count=0
    r_count=0
    #i=1
    for i in range(start+100,end+1):
        word=(myfile.readline())
        if word<=GetMin():
            l_file.write(word)   #put into left file
            #l_file.write("\n")   #for new line in file
            #print heap
            #print "l_file:%s",word
            l_count=l_count+1            #no of line in left file
        else:
            if word>=GetMax():
                r_file.write(word)    #put into right file
                #r_file.write("\n")    #for new line in file
                #print "r_file:%s",word
                #print heap
                r_count=r_count+1             #no of line in right file
            else:
                #if i%2==0:
                p=remove_min()  #Remove_Min() and put into left file
                l_file.write(p)
                insert(word)  #insert word
                l_count=l_count+1
                """else:
                    #p=remove_max() #Remove_Max() and put into right file
                    r_file.write(remove_max())
                    #r_file.write("\n")
                    #print "r_file:%s",word
                    #print heap
                    insert(word)   #insert word
                    r_count=r_count+1 """   
    myfile.close()
    l_file.close()
    r_file.close()
    myfile=open(sys.argv[1],"r+")
    #skip start lines
    for k in range(1,start):
        parmar=myfile.readline()
    with open("left_file","r") as l_file:
        i=0
        for i in range(l_count):
            line=l_file.readline()
            myfile.write(line)
    for i in range(0,100):
        #i=0
        x=remove_min()
        print x
        myfile.write(x)
    with open("right_file","r") as r_file:
        i=0
        for i in range(r_count):
            line=r_file.readline()
            myfile.write(line)
    myfile.close()
    l_file.close()
    r_file.close()
    quicksort(start,start+l_count-1)            
    quicksort(start+l_count+100-1,start+l_count+r_count+100-1)
    
    """end of quiksort"""
quicksort(1,count)
