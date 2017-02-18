# refer from insertion from https://gist.github.com/gnarmis/4647645#file-minmaxheap-py-L23
#refer max-min heap algorithm from http://www.akira.ruc.dk/~keld/teaching/algoritmedesign_f08/Artikler/02/Atkinson86.pdf  
#!usr/bin/python2.7 -tt
from math import log, floor, pow
array=list()
import sys

#data=sorted(data)
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
	

#decide whether to move down or up based on level
"""def TrickleDown(position):
	if (math.floor(math.log(position,2))%2 == 0):
		TrickleDownMax(position)
	else:
		TrickleDownMin(position)"""



        
def TrickleDown(position):
    if on_min_level(position):
        TrickleDown_Min(position)
    else:
        TrickleDown_Max(position)   
def remove_min():
    global heap
    if len(heap)==1:
        print "no more word in heap"
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
    print val
    #print heap
    TrickleDown(Index+1)
    
def remove_max():
    global heap
    if len(heap)==1:
        print "no more word in heap"
        return
    size=len(heap)
    #print size
    if size<=1:
        print "error:empty heap"
    else:    
        if size==2:
            print "only one word in heap, which is:%s"%(heap[1])
            del(heap[1])
        else:
            print "in remove_max"
            val=heap[1]
            heap[1]=heap[-1]   #heap[-1]=last element of heap
            del(heap[-1])
            print val
            TrickleDown(1)  	    
    	
    
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

heap=[0]
def insert(word):
    global array
    global heap
    heap.append(word)
    Bubble_up(len(heap) - 1)

def BuiltDEPQ(file_name):
    global array
    global heap
    i=0
    #file_name = sys.argv[1]
    with open (file_name, "r") as myfile:
        array=myfile.readlines()
    for i in array:
        insert(i)
   

def is_empty():
    if len(heap)==1:
        return True 
    else:
        return False
        
def GetMin():
    if len(heap)==1:
        print "no more  element in heap"
        return
    if len(heap)==2:
        return heap[1]
    else:
        if heap[2]<=heap[3]:
            return heap[2]
        else:
            return heap[3]
def GetMax():
    if len(heap)==1:
        print "no more element in heap"
        return
    return heap[1]
"""def is_contain(word):
    print word
    global heap
    if ('xg\n' in heap):
        return True
    else:
        return False"""
print "enter choice:\n"
print "1.is_empty\n"
print "2.size\n"
print "3.Get_min\n"
print "4.get_max\n"
print "5.put(x)\n"
print "6.builddepq\n"
print "7.remove_min\n"
print "8.remove_max\n"
print "9.is_contain(x)\n"

while 1:
    #i=i-1;
    print "enter choice"
    choice=input('choice')
    if choice==1:
        print "is_empty:%s"%is_empty()
    else:
        if choice==2:
            print "size:%d"%(len(heap)-1)
        else:
            if choice==3:
                print "min:%s"%GetMin()
            else:  
                if choice==4:
                    print "max:%s"%GetMax()
                else:
                    if choice==5:
                        print "enter word do you want to put"
                        w=raw_input()
                        insert(w)
                        for i in range(1,len(heap)):
                                print(heap[i])
                                i+=1
                    else:
                        if choice==6:
                            print "enter file name"
                            FileName=raw_input()
                            BuiltDEPQ(FileName)
                            for i in range(1,len(heap)):
                                print(heap[i])
                                i+=1
                        else:
                            if choice==7:
                                print "remove min:"
                                remove_min()
                            else:
                                if choice==8:
                                    print "remove max"
                                    remove_max()
                                else:
                                    if choice==9:
                                        print "enter x"
                                        x=input()
                                        if x in heap:
                                            print "contains"
                                        else:
                                            print "not contains"
                                    else:
                                        if choice==10:
                                            print heap

        



