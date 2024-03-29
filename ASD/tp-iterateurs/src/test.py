# -*- coding: utf-8 -*-

import listiterator as list

def print_with_iterator (l):
    """
    Print elements of a list using an iterator.
    
    :param l: The list to be printed
    :type l: dict
    """
    l_iterator=list.get_listiterator(l)
    while list.hasNext(l_iterator):
        print(list.next(l_iterator))
    return None
            
    
def print_with_iterator_reverse(l):
    """
    Print elements of a list using an iterator in reverse order.
    
    :param l: The list to be printed
    :type l: dict
    """
    l_iterator=list.get_listiterator(l)
    while list.hasNext(l_iterator):
        list.next(l_iterator)
    while list.hasPrevious(l_iterator):
         print(list.previous(l_iterator))
    return None
     
def print_with_iterator_reverse_bis (l):
    """
    Print elements of a list using an iterator in reverse order.
    
    :param l: The list to be printed
    :type l: dict
    """
    l_iterator=list.get_listiterator(l,default = True)
    while list.hasPrevious(l_iterator):
        print(list.previous(l_iterator))
    return None

def ordering_insert (l, v):
    """
    Add *v* to list *l* such that *l* is kept ordered.
    
    :param l: An ordered list.
    :type l: dict
    :param v: The value to be inserted.
    :type v: same as elements of *l*
    """
    if list.is_empty(l):
        cons(l,v)
        Found = True
    else:
        Found = False
        it=list.get_listiterator(l)
        while list.hasNext(it) and not Found:
            if v<=list.next(it):
               list.previous(it)
               list.add(it,v)
               Found = True
    if not Found:
        list.add(it,v)
    return None

def get (l, i):
    """
    Get the i-th element of *l*. Raise Exception if *i* is not valid.

    :param l: An ordered list .
    :type l: dict
    :return: the i-th element    
    :rtype: Type of the elements of the list

    Throws NoSuchElementException if *i* is out of bounds.
    """
    pass

if __name__ == "__main__":
    l = list.empty_list ()
    for i in reversed(range(1,5)):
        list.cons(l,i)
        
    list.print_list(l);

     #test 0 : impression renversee
    list.print_list(l,reverse=True)

     #test 1 : impression avec iterateurs
    print ('--- test 1 ---')
    print_with_iterator(l)
    print_with_iterator_reverse(l)

     #test 2 : verification des exceptions
    print ('--- test 2 ---')
    try:
        it = list.get_listiterator(l)
        while True:
            list.next(it)
    except list.NoSuchElementException:
        print("Exception levee avec next")
    try:
        it = list.get_listiterator(l)
        while True:
            list.previous(it) 
    except list.NoSuchElementException:
        print("Exception levee avec previous")
      
    
    # test 3 : insertion avant le 3eme element
    print ('--- test 3 ---')
    it = list.get_listiterator (l)
    print(it)
    print(list.next(it)) 
    print(list.next(it))
    list.add(it,23)
    assert(list.previous(it) == 23)
    print_with_iterator(l)
    print_with_iterator_reverse(l)

    # test 4 : insertion apres le dernier element
    print ('--- test 4 ---')
    
    it = list.get_listiterator (l)
    while (list.hasNext(it)):
        list.next(it)
    list.add(it,45)
    assert(list.previous(it) == 45)
    print_with_iterator(l)
    print_with_iterator_reverse(l)

    # test 5 : insertion avant le premier element
    print ('--- test 5 ---')
    l = list.empty_list ()
    for i in reversed(range(1,5)):
        list.cons(l,i)
    it = list.get_listiterator (l)
    list.add(it,0)
    assert(list.previous(it) == 0)
    print_with_iterator(l)
    print_with_iterator_reverse(l)

    # test 6 : insertion avant le dernier element avec l'iterateur placé en fin
    print ('--- test 6 ---')
    it = list.get_listiterator (l,True)
    list.previous(it)
    list.add(it,445)
    assert(list.previous(it) == 445)
    print_with_iterator(l)
    print_with_iterator_reverse(l)

    # test 7 : affichage à l'envers avec l'itérateur placé en fin
    print ('--- test 7 ---')
    print_with_iterator_reverse_bis(l)

#    # test 8 : ajout après le dernier élément
    print ('--- test 8 ---')
    it = list.get_listiterator (l,True)
    list.add(it,5)
    assert(list.previous(it) == 5)
    print_with_iterator(l)
    print_with_iterator_reverse(l)
#        
#    # test 9 : inserer trié, à vous d'écrire ce test
    print ('--- test 9 ---')
    l = list.empty_list ()
    for i in reversed(range(2,10,2)):
        list.cons(l,i)
    it = list.get_listiterator (l)
    ordering_insert(l,5)
    ordering_insert(l,9)
    ordering_insert(l,1)
    l=list.set_head_tail(it)    
    print_with_iterator(l)
    print_with_iterator_reverse(l)
#
#    # test 10 : suppression en tete
    print ('--- test 10 ---')
    l = list.empty_list ()
    for i in reversed(range(1,5)):
        list.cons(l,i)
    it = list.get_listiterator (l)
    list.remove(it)
    l=list.set_head_tail(it)  
    print_with_iterator(l)
    print_with_iterator_reverse(l)
#
#    # test 11 : suppression en queue
    print ('--- test 11 ---')
    l = list.empty_list ()
    for i in reversed(range(1,5)):
        list.cons(l,i)
    it = list.get_listiterator (l,True)
    list.previous(it)
    list.remove(it)
    l=list.set_head_tail(it)  
    print_with_iterator(l)
    print_with_iterator_reverse(l)
    # test 12 : (non-)efficacite de get
    print ('--- test 12 ---')
        #terminer l'ecriture
