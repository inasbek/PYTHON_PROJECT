# -*- coding: utf-8 -*-

"""
:mod:`test` module : test module for quicksort assignment

:author: `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_

:date: 2016, january
"""

import sorting
import generate
import copy
from element import Element
import random

global cpt

def cmp(a,b):
    """
    A comparison function

    :param a: First element    
    :param b: Second element
    :return: 0 if a == b, 1 if a > b, -1 if a < b
    :rtype: int

    >>> from element import Element
    >>> cpt = 0
    >>> cmp(Element(10),Element(5))
    1
    >>> cmp(Element(5),Element(5))
    0
    >>> cmp(Element(5),Element(10))
    -1
    """
    global cpt
    cpt = cpt + 1
    return Element.cmp(a,b)

if __name__ == "__main__":
    cpt = 0

    import doctest
    doctest.testmod()

##    t = generate.random_array(30)
##    tt = sorting.merge_sort(t,cmp)
##   
##    print (tt)
##    if generate.is_sorted (tt):
##        print("Yes !!") 
##    else:
##        raise Exception("Array has not been correctly sorted by merge sort")

    #print (t)
    
    
    
    t = generate.random_array(30)
    for n in range(1, 101): # affichage des moyennes (sur 100 tirages) du nombre
        moy = 0             # de comparaisons effectuées lors du tri d'un
        for j in range(100):    # tableau de taille n
            cpt = 0
            t = generate.random_array(n)
            sorting.quicksort(t, cmp)
            moy += cpt
        moy = moy//100
        print("{:d} {:d}".format(n, moy))
