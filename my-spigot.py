import numpy as np
import sys

# calculate one column of the table
def cCo ( col): 
    a[3][col]=a[2][col]*10
    #a[4][col]=?
    a[5][col]=a[4][col]+a[3][col]

    if col==1:
        a[6][col]=a[5][col]%10
        a[5][col-1]=int(a[5][col]/10)
    else:
	    a[6][col]=a[5][col]%a[1][col]
	    a[4][col-1]=int(a[5][col]/a[1][col])*a[0][col]#return an int?

def init(dcs,ind):
    
    ## table with three lines of headers/redetermined values, then each 4 rows 
    ## for values to be filled as algorithm progresses
    ##to get width "desired digits" multiplied 3.32

    w=int(dcs*cmpm)+1+1
    h = 3 + (dcs*4)
    ## table headers

    a = []

    fl=["pi","r"]
    for x in range(1,w-2+1):
        fl.append(x)

    sl=["=",None]
    for x in range(1,w-2+1):
        sl.append((x*2)+1)

    tl=ind
    ##tl=[None]
    ##for x in range(w-1):
    ##    tl.append(2)

    a.append(fl)
    a.append(sl)
    a.append(tl)

    ##each calc digit is done in 4 rows
    ##for k in range(1,dcs+1):

    ## now add the rows for a single digit calc (4 rows or * 10, co, sum, rem
    for x in range(1,5):
        r = []

        if x==2:
            r.append(None)
            for y in range(w-1):
                r.append(0)     
        else:
            for y in range(w):
                r.append(None)

        a.append(r)

    return a

pi=[] ##counting of pi, the answer
dgs = 50  ##how many digits to compute for
cmpm = 3.32 ## times by number of digits for array size required

if len(sys.argv) >1:
    dgs = int(sys.argv[-1])

# this is how a calculation matrix would be initialised for calucalting pi to 4 digits
#a = [["pi", "r", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], ["=", None,3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25], [None,2,2,2,2,2,2,2,2,2,2,2,2,2],[None,None,None,None,None,None,None,None,None,None,None,None,None,None],[None,0,0,0,0,0,0,0,0,0,0,0,0,0],[None,None,None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None,None,None]]

b=[None]
for x in range(int(dgs*cmpm)+1):
    b.append(2)

a=init(dgs,b)

for x in range(dgs):

    for x in range(int(dgs*cmpm)+1,0,-1):
        cCo(x)

    ##bodge for when the cal value is >99
    if a[5][0]>9:
        pi[-1]=pi[-1]+1
        a[5][0]=0

    pi.append(a[5][0])

    #print pi
    #print(np.matrix(a))

    a=init(dgs,a[6])

#print(np.matrix(a))
print(pi)

