# -*- coding: utf-8 -*-

""":mod:`listiterator` module : list implementation with iterator interaction

Provides constructor, selectors and modifiers for mutable lists.
Lists of this module must be traversed via iterators. 

An iterator for lists allows the programmer to traverse the list in
either direction and adding elements to the list during iteration.  

An iterator has no current element; its cursor position always lies
between the element that would be returned by a call to :code:`previous` and
the element that would be returned by a call to `next`. 

An iterator for a list of length n has n+1 possible cursor positions,
as illustrated by the carets (^) below:

.. code::

                      Element(0)   Element(1)   Element(2)   ... Element(n-1)
 cursor positions:  ^            ^            ^            ^                  ^

:author: `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_

:date: 2016, january

"""

class EmptyList (Exception):
    """
    Exception for empty lists
    """
    def __init__ (self,msg):
        self.message = msg

class NoSuchElementException (Exception):
    """
    Exception for iterators not positionned
    """
    def __init__ (self,msg):
        self.message = msg
        
def __new_cell (v,next_cell,prev_cell):
    return { "value" : v, "next" : next_cell, "prev" : prev_cell }

def __empty_cell (c):
    return c == None

def empty_list ():
    """
    Creates a new empty list.

    :return: A frest list
    :rtype: dict
    """    
    return { "head" : None, "tail" : None }

def is_empty (l):
    """
    Returns true if the list is empty, false else.
    
    :param l: The list
    :type l: dict
    :rtype: boolean
    """
    return l == { "head" : None, "tail" : None }#tail est le dernier element

def cons (l,v):
    """
    Add the value :code:`v` at the begining of the list :code:`l`.

    :param l: The list, possibly empty.
    :type l: dict
    :param v: The value to be added.
    :type v: Any

    UC: not compatible with iterators
    """
    if l["head"] == None:
        l["head"] = l["tail"] = __new_cell (v, None, None)
    else:
        l["head"] = __new_cell (v, l["head"], None)
        l["head"]["next"]["prev"] = l["head"]

def __print_without_iterator_forward (c):
    """
    :param c: A cell
    :type c: dict
    """
    if __empty_cell(c):
        print()
    else:
        print(c["value"],end=' ')
        __print_without_iterator_forward (c["next"])

def __print_without_iterator_reversed (c):
    """
    :param c: A cell
    :type c: dict
    """
    if __empty_cell(c):
        print()
    else:
        print(c["value"])
        __print_without_iterator_reversed (c["prev"])

def print_list (l,reverse=False):
    """
    :param l: The list, possibly empty.
    :type l: dict
    :param reverse: True if the the list *l* must be printed from the end to the begining
    :type reverse: boolean
    """
    if is_empty(l):
        raise EmptyList("The list has no elements")
    if reverse:
        __print_without_iterator_reversed (l["tail"])
    else:
        __print_without_iterator_forward (l["head"])


def get_listiterator (l,default=False):
    """
    Creates a new iterator for list *l*.

    :param l: The list
    :type l: dict
    :return: An iterator at the begining of the list
    :rtype: dict
    """
    if is_empty(l):
        raise EmptyList("The list has no elements")
    if default:
        return {"prev" : l["tail"] , "next" : None}
    else:
        return {"prev" : None , "next" : l["head"]}


def hasNext (it):
    """
    Returns :code:`True` if this list iterator has more elements when
    traversing the list in the forward direction. (In other words,
    returns :code:`True` if :code:`next(it)` would return an element rather than
    throwing an exception.)

    :param it: The iterator
    :type it: dict
    :rtype: boolean
    """
    return  it["next"] != None


def next (it):
    """
    Returns the next element in the list and advances the cursor
    position. This method may be called repeatedly to iterate through
    the list, or intermixed with calls to :code:`previous(it)` to go back and
    forth. (Note that alternating calls to next and previous will
    return the same element repeatedly.)

    Throws NoSuchElementException if theere is no such element.

    :param it: The iterator
    :type it: dict
    :rtype: Type of the elements of the list
    """
    if not hasNext(it):
        raise NoSuchElementException ("End of the list")
    else:
        it["prev"]=it["next"]
        it["next"]=it["next"]["next"]
    return it["prev"]["value"]



def hasPrevious (it):
    """
    Returns :code:`True` if this list iterator has more elements when
    traversing the list in the reverse direction. (In other words,
    returns :code:`True` if :code:`previous(it)` would return an
    element rather than throwing an exception.)

    :param it: The iterator
    :type it: dict
    :rtype: boolean
    """
    return it["prev"] != None


def previous (it):
    """
    Returns the previous element in the list and moves the cursor
    position backwards. This method may be called repeatedly to
    iterate through the list backwards, or intermixed with calls to
    :code:`next(it)` to go back and forth. (Note that alternating calls to next
    and previous will return the same element repeatedly.)

    Throws NoSuchElementException if there is no such element.

    :param it: The iterator
    :type it: dict
    :rtype: Type of the elements of the list
    """
    if not hasPrevious(it):
        raise NoSuchElementException ("Begin of the list")
    else:
        it["next"]=it["prev"]
        it["prev"]=it["prev"]["prev"]
    return it["next"]["value"]

def add (it,v):
    """Inserts the specified element into the list. The element is
    inserted immediately before the element that would be returned by
    next(), if any, and after the element that would be returned by
    previous(), if any. (If the list contains no elements, the new
    element becomes the sole element on the list.) The new element is
    inserted before the implicit cursor: a subsequent call to next
    would be unaffected, and a subsequent call to previous would
    return the new element.

    :param it: The iterator
    :type it: dict
    :param v: The element
    :type v: Any
    """
    new_cell = __new_cell(v,it["next"],it["prev"])
    if hasNext(it):
        it["next"]["prev"]= new_cell
    if hasPrevious(it):
        it["prev"]["next"]= new_cell
    it["prev"] = new_cell
    return None
            

def remove (it):
    """Removes from the list the last element that was returned by
    next(). This call can only be made once per call to next.

    :param it: The iterator
    :type it: dict
    """
    if hasPrevious(it):
        next(it)
        if hasNext(it): #Cas où l'élement à supprimer n'est ni en queue ni en tête 
            previous(it)
            it["prev"]["next"]=it["next"]["next"]
            it["next"]["next"]["prev"]=it["prev"]
            it["next"]=it["next"]["next"]
        else: #Cas où l'élement à supprimer est en queue
            previous(it)
            it["next"]=None
            it["prev"]["next"]=it["next"]
    else: #Cas où l'élement à supprimer est en tête
        next(it)
        if hasNext(it):
            previous(it)            
            it["next"]=it["next"]["next"]
            it["next"]["prev"]=it["prev"] #Ou None c'est pareil.
        else: #Cas où un seul élément
            previous(it)   
            it["prev"] = None
            it["next"] = None
            
    return None

def set_head_tail(it):
    """
    returns a list setted with the head and the tail of the list
    Because when we use add's function before the head, the list associated to the iterator is not up    
    to date, same for the tail
    So it's cause complications for the tests
    :param it: the iterator who'll use for create the list
    :type it: dict
    :return: a list setted with the head and the tail of the list
    :rtype: dict (head,tail)
    
    """
    l=empty_list ()
    while hasPrevious(it):
        previous(it)
    l["head"]=it["next"]
    while hasNext(it):
        next(it)
    l["tail"]=it["prev"]
    return l
l = empty_list ()
for i in reversed(range(1,5)):
    cons(l,i)
it=get_listiterator (l)
c=__new_cell (45, None, None)

