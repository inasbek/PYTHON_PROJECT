====================
Autour du tri rapide
====================

L'objectif de ce TP est de programmer le tri rapide et d'évaluer
l'incidence du choix du pivot. Vous avez déjà vu en cours d'AP2
(semaine 3) le fonctionnement et l'implantation du tri rapide sur des
listes. L'implantation présentée ne se précoccupait pas de l'espace
mémoire utilisé et ne tirait pas parti que le tri rapide est un tri
qui peut être implémenté en utilisant un espace mémoire en
:math:`O(1)`.

Ici on va le faire sur des tableaux NumPy tout en mettant en
œuvre une structure de donnée pour éviter les recopies de
tableaux.

----------------------
Préparation au travail
----------------------
   
#. Récupérez les `sources <./tp-rapide.zip>`__.

   Vous trouverez un module de génération de tableaux d'entiers, un
   module de tris avec le tri fusion déjà implémenté et un programme de
   test minimal nommé :file:`test.py`. 

#. Vous répondrez aux questions dans le fichier :file:`index.rst`.
   
#. Générez la documentation des modules fournis.
   
-------------------------
Rappels sur le tri rapide
-------------------------

Le principe du tri rapide consiste à partitionner le tableau à trier
autour d'un pivot, les éléments inférieurs à ce pivot étant placés au
début du tableau, à gauche du pivot, et les éléments supérieurs sont
placés à droite du pivot, en fin de tableau. Puis on appelle
récursivement ce tri sur chaque sous-tableau : la tranche contenant
les éléments à gauche du pivot (*t1* ci-dessous), puis la
tranche contenant les éléments à droite du pivot (*t2*
ci-dessous). Le principe de l'algorithme peut être décrit ainsi :

   .. code:: text

      tri_rapide t
         soit t1,t2 = partitionner t
         tri_rapide t1
         tri_rapide t2


Un exemple de partionnement est donné ci-dessous, où le pivot est le
premier élément du tableau (ici 3) :

   **3** 8 9 6 2 1 5 7 4 devient 2 1 **3** 4 7 5 6 9 8 

La propriété du partitionnement est que **tous** les éléments plus petits
que le pivot sont à gauche, et que **tous** les éléments les plus
grands sont à droite. On remarque alors que le pivot est
nécessairement à la position
qu'il occupera lorsque le tableau aura été trié. Ainsi, après chaque
partition un élément du tableau est correctement mis en place. 

Avec le tri rapide il n'est pas nécessaire de copier le tableau à chaque
étape, contrairement au tri fusion, puisque le pivot est directement
mis à sa place définitive dans le tableau trié à chaque étape. 

On appelle ces tris qui ne nécessitent pas de recopie de tableau des
**tris sur place** (ou en place).


Si on ne recopie pas le tableau, il faut passer en paramètre à la
fonction de tri le tableau ainsi que les positions entre lesquelles on
souhaite trier (même technique que celle montrée en cours pour la v4
de la recherche d'un élément dans un tableau).

Plutôt que de passer le tableau et les indices définissant la tranche
de tableau à traiter, nous allons utiliser une structure de données qui
permettra de représenter cela (bien entendu, on ne créera pas de
tranche de tableau par une copie). La structure de donnée sera donc un
dictionnaire qui contient une référence sur le tableau ainsi que
deux entiers permettant de définir les positions gauche et droite de
la tranche qui nous intéresse. Une tranche représentant tout le tableau
``t`` sera donc en Python le dictionnaire :

   .. code:: Python

      { "data" : t, "left" : 0, "right" : len(t) - 1}
       
Ainsi, les définitions :

   .. code:: Python
      
      mon_tableau = numpy.array([ 1 , 2 , 3 , 4 , 5 ])
      ma_tranche_1 = { "data" : mon_tableau, "left" : 2, "right" : 3 }
      ma_tranche_2 = { "data" : mon_tableau, "left" : 0, "right" : 0 }

permettent de définir la tranche qui contient les éléments ``3; 4`` du
tableau ``mon_tableau`` puis la tranche qui contient l'unique élément
``1``.

#. Citez d'autres exemples de tris sur place.

#. Réfléchissez sur la façon de partitionner un tableau sans disposer
   d'un espace mémoire supplémentaire proportionnel à la taille du tableau. Puis programmez dans le module
   :mod:`sorting` la fonction :code:`partition` qui réalise la
   partition d'une tranche en deux tranches. On choisira comme pivot
   l'élément situé en première position de la tranche passée en
   paramètre.

#. Quelle(s) propriété(s) peut-on donner qui garantisse que le
   partionnement est correctement réalisé ? Utilisez celle(s)-ci pour
   compléter le doctest de la fonction :code:`partition`, en plus de
   remplacer les 'None' par la valeur attendue.
   
#. Testez (vraiment).

#. Programmez l'algorithme du tri rapide sur une tranche dans le
   module :mod:`sorting`.

#. Enfin, programmez l'algorithme de tri rapide qui s'applique cette
   fois sur un tableau (et non une tranche) et qui utilise la fonction
   de la question précédente.

#. Testez.

#. Quel est exactement l'espace mémoire supplémentaire utilisé lors
   d'un tri rapide d'un tableau de longueur :math:`n` ?


------------------
Sélection du pivot
------------------

Le choix du pivot dans le tri rapide est primordial. Un pivot mal
choisi (le minimum ou le maximum) par exemple, et le tri ne sera pas
plus rapide qu'un tri bulle.

~~~~~~~~~~~~~~~
Pivot aléatoire
~~~~~~~~~~~~~~~

#. Dans le modules :mod:`sorting`, écrivez la fonction :code:`random_pivot`
   qui retourne un indice aléatoire de la tranche du tableau.

#. Ajoutez un paramètre qui donnera l'indice dans le tableau
   correspondant au pivot à utiliser à la fonction :code:`partition`.

#. Modifiez vos codes pour compter le nombre de comparaisons
   effectuées par le tri rapide. 

#. Pour chacune des deux versions du tri rapide (pivot en première
   position, pivot aléatoire), calculez et stockez ces décomptes pour des
   tableaux de taille 1 à 100 tirés aléatoirement (on effectuera la
   moyenne sur 100 tirages). Concluez.

#. Pour quelle valeur du pivot est-on dans le pire des cas
   pour le tri rapide ? Donnez l'équation de récurrence et déduisez-en la
   complexité en temps dans le pire des cas.

~~~~~~~~~~~~~
Pivot optimal
~~~~~~~~~~~~~

#. Quelle est théoriquement la meilleure valeur à choisir
   pour le pivot ?

#. Dans le module :mod:`sorting`, programmez une fonction
   :code:`optimal_pivot` qui prend en entrée une tranche de tableau et
   retourne l'/indice/ du pivot choisi (**sans vous soucier de
   l'efficacité de ce calcul**). Testez.

#. En utilisant ce choix de pivot, calculez et stockez le
   nombre de comparaisons pour des tableaux de taille 1 à 100 tirés
   aléatoirement (on effectuera la moyenne sur 100 tirages). 

#. Réalisez une courbe compilant les chiffres produits au
   questions précédentes et permettant de voir l'évolution du nombre de
   comparaisons dans les trois versions. Concluez.

#. Établissez l'équation de récurrence du tri rapide avec
   ce choix du pivot et déduisez-en la complexité en temps dans le
   meilleur des cas.

Pivot réellement optimal ?
__________________________

#. Ajoutez aux comparaisons comptées celles de la fonction
   calculant le pivot. La tri rapide avec choix du pivot optimal est-il
   toujours le meilleur ?

#. *Défi !* Sinon, trouvez un algorithme efficace du
   calcul du pivot optimal (vous pouvez bien sûr utiliser toute ressource qui
   vous permettra d'avancer dans votre quête). 


