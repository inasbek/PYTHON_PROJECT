---------------
 tp-iterateurs
---------------


.. toctree::
   :maxdepth: 1

   listiterator.rst

TP réalisé par ait ali belkacem azzedine et bekkouche inas du G5.
---------------
BUT DU TP :
--------------
* Le but du TP est l’implémentation de listes doublement chaînées avec itérateurs.

Reponses aux Questions:
-----------------------

Question 3.2.1.1
----------------

Les dictionnaires semblent être une réponse appropriée au problème car mutables et facilité de parcours (Et  parce que c'est déjà marqué dans le rtype des doctests).

Question 3.2.3.4
----------------

Tout dépend de comment la fonction add a été pensée initialement. Cependant, il faut prendre en compte que l'ajout à la fin, tout comme au début, ne modifie pas la tête et la queue de Liste avec laquelle l'itérateur a été créé, entraînant des problèmes lors de l'exécution des tests (les fonctions d'impression ont pour paramètre l, qui n'est du coup plus à jour). Pour palier à ce problème, une fonction annexe, nommée set_head_tail, a été créée, et permet de mettre à jour la liste lorsqu'un élément est ajouté en début ou fin de liste.

Question 3.2.4.1
----------------

Oui, cela est compatible. Mais cette fonction n'est pas la réelle réciproque de la fonction add (add puis remove ne revient pas à la situation initiale), et donc par conséquent supprimer l'élement qui a été retourné par l'appel à next. L'itérateur ne change pas de position, il renvoie toujours le même précédent, mais désormais il pointe aussi vers le suivant du suivant supprimé (Ou None lorsque l'élement en queue est supprimé)

Question 3.2.4.3
----------------

Lors d'appels successifs à la fonction remove, tous les éléments situés à la position next de l'itérateur sont supprimés successivement. L'itérateur ne bouge pas.
