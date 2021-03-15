# -*- coding: utf-8 -*-

""":mod:`test` module : Test module for bloomfilter analysis

:author: `FIL - Univ. Lille <http://portail.fil.univ-lille1.fr>`_

:date: 2016, january

"""
import random
import bloomfilter

nb_hash_functions = 8
random_tab = [ 0 for i in range(128 * nb_hash_functions)]

def init_random_tab ():
    """
    Creates the hash functions.
    """
    global random_tab
    for i in range(128):
        for j in range(nb_hash_functions):
            random_tab[j * 128 + i] = random.randint(1,32000)

def code_of_string (str,n):
    """
    For a given string, returns the hash code for the n-th hashing function.
    
    :param str: The string to be hashed.
    :type str: string
    :param n: The function number.
    :type n: int
    :return: A hash code
    :rtype: int

    .. note:: 
       1 <= n <= nb_hash_functions
    """
    global random_tab
    h = 0
    for c in str:
        hashcode_c=random_tab[ord(c)+(128*n)] #position of the char c in the hash function n
        h+= hashcode_c #sum of all characters's hashcode (= word) 
    return h

def random_word ():
    """
    Returns a word with random letters whose length is between 4 and 7.

    :rtype: string
    """
    letters = [ chr(i) for i in range(ord('a'),ord('z')+1) ] + [ chr(i) for i in range(ord('A'),ord('Z')+1) ]
    length = 4 + random.randint(0,4)
    str = ""
    for i in range(length):
        str = str + random.choice(letters)
    return str

def analyse_faux_positif():
    """
    Algorithme de la Question 4.3
    """
    file=open('res.txt','w') 
    mots_testes=0
    faux_positifs=0
    liste_mots_aleatoires=[]
    for mot_a_inserer in range (2**10+1):
        liste_mots_aleatoires += [random_word()] 
        
    for n in range (1,9):
        for t in range (10,21):
            bf= bloomfilter.create(t,code_of_string,n)
            for mot in liste_mots_aleatoires: #
                bloomfilter.add(bf,mot)
            for mot_test in range (1,(2**14)+1): 
                mot = random_word()
                if mot not in liste_mots_aleatoires:
                    mots_testes+=1
                    if bloomfilter.contains(bf,mot) == True:
                        faux_positifs+=1
            file.write(str(t )+ " " + str(n) + " " + str(mots_testes) + " " + str(faux_positifs) + " " + str(round((faux_positifs/mots_testes),6))+ "\n") #écriture de la ligne
            mots_testes=0
            faux_positifs=0 #réinitialisation des valeurs
        file.write("\n\n") #séparation avant ajout d'une fonction de hachage
            


if __name__ == "__main__":
    init_random_tab()
    analyse_faux_positif()
    bf = bloomfilter.create(6,code_of_string,8)
    w = random_word()
    bloomfilter.add(bf,"timoleon")
    if bloomfilter.contains(bf,"timoleon"):
        print("%s est present" % ("timoleon"))
    if bloomfilter.contains(bf,w):
        print("%s est present" % (w))
    
    
    

    
