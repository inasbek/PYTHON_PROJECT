# -*- coding: utf-8 -*-

"""
:mod:`test` module : test module for experiences assignment

:author: `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_

:date: 2018, january
"""

import sys
import experience
import marker
import numpy as np
import sorting

def compare (m1,m2):
    global cpt
    cpt=cpt+1
    return m1.cmp(m2)

# STRATEGY 1
def negative_markers1(markers,positive):
    """
    Computes the list of negative markers from the list of markers and
    the list of positive markers.

    :param markers: The list of markers 
    :type markers: Numpy array of String
    :param positive: The list of positive markers
    :type positive: Numpy array of String
    :return: The list of negative markers
    :rtype: Numpy array of String
    """
    negative = np.array([])
    for mrkr in markers :
        trouve=False
        i=0
        while  not trouve and i<len(positive):
            if compare(mrkr,positive[i])==0:
                
                trouve=True
            i=i+1
        if  not trouve:
            negative =np.append(negative,mrkr)
    return negative


# STRATEGY 2
def recherche_dichotomique( element, liste):
    a = 0
    b = len(liste)-1
    
    while a < b :
        m=(a+b)//2
        if compare(liste[m] ,element) < 0:
            a=m+1
        else :
            b = m
    if compare(liste[a] ,element)==0:
        return True
    else:
        return False
        
def negative_markers2(markers,positive):
    negative = np.array([])
    positive_sorted=sorting.merge_sort(positive,compare)
    
    for m in range(len(markers)):
        
        if  not recherche_dichotomique(markers[m],positive_sorted):
            negative=np.append(negative,markers[m])
    return negative
                    

# STRATEGY 3
def negative_markers3(markers,positive) :
    negative=np.array([])
    ms=sorting.merge_sort(markers,compare)
    ps=sorting.merge_sort(positive,compare)
    i=0
    m=0
    while i<=len(ps)-1:
        if compare(ms[m],ps[i])==0:
            i=i+1
        else:
            negative = np.append(negative,ms[m])
        m=m+1
    while m<len(ms):
        negative = np.append(negative,ms[m])
        m=m+1
    return negative
        
        
    
<<<<<<< HEAD
    

    
"""       
##if __name__ == "__main__":
##    p = int(sys.argv[1])
##    m = int(sys.argv[2])
"""
p=5

m=10
    
assert (m > 0), "The number of markers must be greater than 0"
assert (p <= m), "The number of positive markers must be less or equal to the number of markers"

exp = experience.Experience(p,m)
markers = exp.get_markers()
positive = exp.get_positive_markers()

print("Markers: %s" % (markers))
print("Positive markers: %s" % (positive))

# test stategy 1
cpt = 0
print("Negative markers: %s" % (negative_markers1(markers,positive)))
print("Nb. comparisons: %d" % (cpt))

# test stategy 2
cpt = 0
print("Negative markers: %s" % (negative_markers2(markers,positive)))
print("Nb. comparisons: %d" % (cpt))

# test stategy 3
cpt = 0
print("Negative markers: %s" % (negative_markers3(markers,positive)))
print("Nb. comparisons: %d" % (cpt))
=======
     
      
if __name__ == "__main__":
   p= int(sys.argv[1])
   m= int(sys.argv[2])



    
assert (m > 0), "The number of markers must be greater than 0"
assert (p <= m), "The number of positive markers must be less or equal to the number of markers"
for i in range(1,m+1):
    p=i
    exp = experience.Experience(p,m)
    markers = exp.get_markers()
    positive = exp.get_positive_markers()
    
    print(m,end=' ')
    print(i,end=' ')
    cpt=0
    s=negative_markers1(markers,positive)
    print( " %d"  % (cpt),end=' ')
    cpt=0
    l=negative_markers2(markers,positive)
    print( " %d"  % (cpt),end=' ')
    cpt=0
    x=negative_markers3(markers,positive)
    print( " %d"  % (cpt))
    

##print("Markers: %s" % (markers))
##print("Positive markers: %s" % (positive))
##
### test stategy 1
##cpt = 0
##print("Negative markers: %s" % (negative_markers1(markers,positive)))
##print("Nb. comparisons: %d"  % (cpt))
##
### test stategy 2
##cpt = 0
##print("Negative markers: %s" % (negative_markers2(markers,positive)))
##print("Nb. comparisons: %d" % (cpt))
##
### test stategy 3
##cpt = 0
##print("Negative markers: %s" % (negative_markers3(markers,positive)))
##print("Nb. comparisons: %d" % (cpt))
>>>>>>> c45e3466b19eabd1739b355d3d6d3a84a6920d75
