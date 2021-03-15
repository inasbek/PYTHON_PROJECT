# -*- coding: utf-8 -*-

"""
:mod:`sorting` module : sorting functions module for quicksort assignment

:author: `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_

:date: 2018, january
"""

import copy
import random
import numpy as np

def merge (t1,t2, cmp):
    """
    Given two sorted array, creates a fresh sorted array.
    
    :param t1: An array of objects
    :type t1: Array
    :param t2: An array of objects
    :type t1: Array
    :param cmp: A comparison function, returning 0 if a == b, -1 is a < b, 1 if a > b
    :type cmp: function
    :return: A fresh array, sorted.
    :rtype: array
    
    .. note::
    
       time complexity of merge is :math:`O(n_1+n_2)` with
       :math:`n_1` and :math:`n_2` resp. the length of *t1* and *t2*

    >>> import numpy
    >>> def cmp (x,y): 
    ...    if x == y:
    ...       return 0
    ...    elif x < y:
    ...       return -1
    ...    else:
    ...       return 1
    >>> t1 = numpy.array([0,2,5,6])
    >>> t2 = numpy.array([1,3,4])
    >>> merge(t1,t2,cmp)
    array([0, 1, 2, 3, 4, 5, 6])
    """
    n1 = len(t1)
    n2 = len(t2)
    t = np.zeros(n1+n2,dtype=type(t1[0]))
    i = j = k = 0
    while i < n1 and j < n2:
        if cmp(t1[i],t2[j]) < 0:
            t[k] = t1[i]
            i = i + 1
        else:
            t[k] = t2[j]
            j = j + 1
        k = k + 1
    while i < n1:
        t[k] = t1[i]
        i = i + 1
        k = k + 1
    while j < n2:
        t[k] = t2[j]
        j = j + 1
        k = k + 1
    return t


def merge_sort (t,cmp):
    """
    A sorting function implementing the merge sort algorithm
    
    :param t: A array of integers
    :type t: array
    :param cmp: A comparison function, returning 0 if a == b, -1 is a < b, 1 if a > b
    :type cmp: function
    :return: A fresh array, sorted.
    :rtype: array

    .. note::
    
       time complexity of merge is :math:`O(n_1+n_2)` with
       :math:`n_1` and :math:`n_2` resp. the length of *t1* and *t2*

    >>> import generate
    >>> def cmp_element (x,y): 
    ...    return x.cmp(y)
    >>> t = generate.random_array(10)
    >>> merge_sort(t,cmp_element)
    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=object)
    """
    n = len(t)
    if n <= 1:
        # cas de base
        return copy.deepcopy(t)
    else:
        # cas general
        t1 = merge_sort((t[0:((n-1)//2+1)]),cmp)
        t2 = merge_sort((t[((n-1)//2+1):n]),cmp)
        return merge(t1,t2,cmp)
    

def quicksort (t,cmp):
    """
    A sorting function implementing the quicksort algorithm
    
    :param t: An array of Element
    :type t: NumPy array
    :param cmp: A comparison function, returning 0 if a == b, -1 is a < b, 1 if a > b
    :type cmp: function
    :return: Nothing

    .. note::
       *t* is modified during the sort process

    >>> import generate
    >>> import numpy
    >>> def cmp (x,y):
    ...    if x == y:
    ...       return 0
    ...    elif x < y:
    ...       return -1
    ...    else:
    ...       return 1
    >>> t = numpy.array([Element(i) for i in [5, 6, 1, 3, 4, 9, 8, 2, 7]])
    >>> quicksort(t, cmp)
    >>> t == numpy.array([Element(i) for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]])
    array([ True,  True,  True,  True,  True,  True,  True,  True,  True])
    """
    p={'left':0,'right':len(t)-1,'data':t}
    quicksort_slice (p, cmp)


def quicksort_slice (s, cmp):
    """
    A sorting function implementing the quicksort algorithm
    
    :param s: A slice of an array, that is a dictionary with 3 fields :
              data, left, right representing resp. an array of objects and left
              and right bounds of the slice.
    :type s: dict
    :param cmp: A comparison function, returning 0 if a == b, -1 is a < b, 1 if a > b
    :type cmp: function
    :return: Nothing

    >>> import generate
    >>> import numpy
    >>> def cmp (x,y):
    ...    if x == y:
    ...       return 0
    ...    elif x < y:
    ...       return -1
    ...    else:
    ...       return 1
    >>> t = numpy.array([Element(i) for i in [5, 6, 1, 3, 4, 9, 8, 2, 7]])
    >>> p = {'left':0,'right':len(t)-1,'data':t}
    >>> quicksort_slice(p, cmp)
    >>> p['data'] == numpy.array([Element(i) for i in [1,2,3,4,5,6,7,8,9]])
    array([ True,  True,  True,  True,  True,  True,  True,  True,  True])
    
    """
    
    if (s['left'] < s['right']):  # tant que la tranche est non vide, on la trie
        s1,s2 = partition(s,find_median(s, cmp),cmp)
        quicksort_slice(s1, cmp)
        quicksort_slice(s2, cmp)
    


def partition (s,i,cmp):
    """
    Creates two slices from *s* by selecting in the first slice all
    elements being less than the pivot and in the second one all other
    elements.

    :param s: A slice of is a dictionary with 3 fields :
              - data: the array of objects,
              - left: left bound of the slide (a position in the array),
              - right: right bound of the slice.
    :type s: dict
    :param cmp: A comparison function, returning 0 if a == b, -1 is a < b, 1 if a > b
    :type cmp: function
    :return: A couple of slices, the first slice contains all elements that are 
             less than the pivot, the second one contains all elements that are 
             greater than the pivot, the pivot does not belong to any slice.
    :rtype: tuple

    >>> import generate
    >>> import element
    >>> import numpy
    >>> def cmp (x,y): 
    ...    if x == y:
    ...       return 0
    ...    elif x < y:
    ...       return -1
    ...    else:
    ...       return 1
    >>> t = numpy.array([element.Element(i) for i in [5, 6, 1, 3, 4, 9, 8, 2, 7]])
    >>> p = {'left':0,'right':len(t)-1,'data':t}
    >>> p1,p2 = partition(p,0,cmp)
    
    >>> p1['data'][p1['left']:p1['right']+1]
    array([1, 2, 3, 4], dtype=object)
    >>> p2['data'][p2['left']:p2['right']+1]
    array([6,7 ,8 ,9 ], dtype=object)
    """
    
    
     # on échange le pivot choisi avec le premier élément de la tranche considérée
    tmp = s['data'][s['left']]
    s['data'][s['left']] = s['data'][i]
    s['data'][i] = tmp
    pivot = s['data'][s['left']]
    # on  compte le nombre d'éléments inférieurs au pivot
    cptinf = 0
    for i in range(len(s['data'])):
        if (cmp(pivot,s['data'][i])==1):
            cptinf += 1
    # on place le pivot à sa bonne position
    s['data'][s['left']],s['data'][cptinf]=s['data'][cptinf],s['data'][s['left']]
    j = cptinf+1
    # on parcourt la première partie du tableau (avant le pivot) pour trouver les éléments supérieurs au pivot
    for i in range(cptinf):
        # si l'élément considéré est plus grand que le pivot
        if cmp(s['data'][i], pivot)==1 :
            continuer = True
            # on parcourt la seconde partie du tableau pour trouver l'élément mal positionné
            while (continuer and j<len(s['data'])):
                if cmp(s['data'][j], pivot)==-1:
                    s['data'][j],s['data'][i] = s['data'][i],s['data'][j]
                    continuer = False
                j += 1
    return ({'left':s['left'], 'right': cptinf-1, 'data': s['data']}, {'left':cptinf+1, 'right': s['right'], 'data': s['data']})


def random_pivot(s):
    '''
    retourne un indice aléatoire de la tranche du tableau.
    :param s: une tranche de tableau
    :return : un indice aléatoir
    :exemple
    >>> t = numpy.array([element.Element(i) for i in [5, 6, 1, 3, 4, 9, 8, 2, 7]])
    >>> p = {'left':0,'right':len(t)-1,'data':t}
    
    '''
    return random.randint(s['left'], s['right'])
    

def optimal_pivot(s, cmp):
    """
    Returns the index of an optimal pivot for the slice given.

    :param s:: A slice of is a dictionary with 3 fields :
    
              - data: the array of objects,
              
              - left: left bound of the slide (a position in the array),
              
              - right: right bound of the slice.
              
    :type s: dict
    
    :return : an index for an optimal pivot
    
    :rtype: int

    >>> import generate
    >>> import numpy
    >>> import element
    >>> def cmp (x,y):
    ...    if x == y:
    ...       return 0
    ...    elif x < y:
    ...       return -1
    ...    else:
    ...       return 1
    
    >>> t = np.array([i for i in [5, 6, 1, 3, 4, 9, 8, 2, 7]])
    >>> p = {'left':0,'right':len(t)-1,'data':t}
    >>> optimal_pivot(p, cmp)
    0
    """
    t = merge_sort(s['data'][s['left']:s['right']+1], cmp)
    med = t[len(t)//2]
    i = s['left']
    while (i <= s['right']):
        if med == s['data'][i]:
            return i            
        i += 1



# choix du pivot optimal (mediane) sans trier le tableau
def find_median_aux(s, cmp):
    n = s['right'] - s['left'] + 1
    # si le tableau contient 1 element, cet element est la mediane
    if (n==1):
        return s['data'][s['left']]
    # on divise le tableau en paquets de 5
    k = n//5 # nombre de paquets de 5
    t = []
    j = 0
    l = []
    for i in range(n):
        if (i//5 != j):
            t.append(np.array(l))
            l = []
            j += 1
        l.append(s['data'][s['left'] + i])
    if len(l)!=0:
        t.append(np.array(l))
    # on trouve le milieu de chaque paquet
    mil_tab = []
    for i in range(len(t)):
        t[i] = merge_sort(t[i], cmp)
        mil_tab.append(t[i][len(t[i])//2])
    p = {'left':0, 'right':len(mil_tab)-1, 'data':np.array(mil_tab)}
    return find_median_aux(p, cmp)

def find_median(s, cmp):
    """
    Returns the index of the median of the slice given.

    :param s:: A slice of is a dictionary with 3 fields :
    
              - data: the array of objects,
              
              - left: left bound of the slide (a position in the array),
              
              - right: right bound of the slice.
              
    :type s: dict
    
    :return : an index for the median
    
    :rtype: int

    >>> import generate
    >>> import numpy
    >>> import element
    >>> def cmp (x,y):
    ...    if x == y:
    ...       return 0
    ...    elif x < y:
    ...       return -1
    ...    else:
    ...       return 1
    
    >>> t = numpy.array([Element(i) for i in [5, 6, 1, 3, 9, 4, 8, 2, 7]])
    >>> p = {'left':0,'right':len(t)-1,'data':t}
    """
    med = find_median_aux(s, cmp)
    for i in range(s['left'], s['right']+1):
        if (med == s['data'][i]) :
            return i

    

    

        
def cmp (x,y):
    global cpt
    cpt=cpt+1
    
    if x == y:
        return 0
    elif x < y:
       return -1
    else:
       return 1    
cpt=0
t = np.array([i for i in [5, 6, 1, 3, 4, 9, 8, 2, 7]])
p = {'left':0,'right':len(t)-1,'data':t}
p1,p2 = partition(p,0,cmp)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

