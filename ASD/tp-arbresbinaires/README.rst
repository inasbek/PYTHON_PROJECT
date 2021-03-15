================================
Manipulation des arbres binaires
================================

L'objectif de ce TP est d'utiliser un module de création d'arbres
binaires (que vous avez écrit ou que vous écrirez lors du cours de
PdC) afin d'implanter les fonctions usuelles de manipulation des
arbres binaires puis des arbres binaires de recherche. Le dernier
travail consiste en l'implantation d'un petit jeu utilisant un arbre
binaire de recherche pour sa résolution.

Pour rappel voici les fonctions dont vous disposez dans le module d'arbres:
 - création d'un arbre 
 - ajouter/modifier un fils à gauche ou à droite en étant sur un nœud ou feuille
 - descendre à gauche, descendre à droite
 - obtenir la valeur associée à un nœud


#. Récupérez les `sources <./tp-arbresbinaires.zip>`__..

   Dans l'archive vous trouverez dans un répertoire
   :file:`src-c` : le module :mod:`ArbresBinaire` et un
   programme :mod:`Test_arbre.c` avec les entêtes des fonctions à
   écrire et le code pour des tests.

   Pour les étudiants en mathématiques (et pour eux-seuls) vous
   trouverez dans un répertoire :file:`src` le module
   :mod:`tree` et un programme :file:`test.py` vous
   permettant de réaliser le TP en Python.

--------------------------------
Vérification des arbres produits
--------------------------------

Réalisation en C
----------------

Le module *ArbreBinaire* permet de manipuler des arbres binaires. Afin
de vérifier que les arbres produits sont ceux auxquels vous vous
attendez, nous fournissons également une primitive qui prend un arbre,
le transforme en un fichier au format "gv" qui permet la visualisation
de l'arbre grâce au programme "dot".

Vous observerez attentivement la documentation dans *ArbreBinaire.h*
pour comprendre le fonctionnement des primitives.

Par exemple, le fichier :file:`exemple1_arbre.c` contient la construction d'un
arbre puis produit le fichier "gv" de cet arbre. Pour construire cet
arbre et le visualiser, il suffit d'exécuter les commandes suivantes :

::
   
   make exemple1_arbre.exec
   ./exemple1_arbre.exec # produit exemple1.gv
   make exemple1.pdf # produit exemple1.pdf si exemple1.gv existe

Vous pouvez alors visualiser le pdf produit avec l’outil de votre choix.

Pour compiler le programme de test :file:`Test_arbre.c` il suffira d'exécuter
:code:`make Test_arbre.exec`

et on pourra lancer ce programme grâce à
:code:`./Test_arbre.exec`


Réalisation en Python (uniquement pour les licence maths)
---------------------------------------------------------

Le module *tree* fournit les primitives pour manipuler les arbres
binaires. Afin de vérifier que les arbres produits sont ceux auxquels
vous vous attendez, nous fournissons également une primitive qui prend
un arbre, le transforme en un fichier au format "gv" qui permet la
visualisation de l'arbre grâce au programme "dot".

Par exemple, le fichier exemple.py contient la construction d'un
arbre puis produit le fichier "gv" de cet arbre. Pour construire cet
arbre et le visualiser, il suffit d'exécuter les commandes suivantes :

::
   
   python3 exemple.py
   dot -Tpdf -oexemple.pdf exemple.gv

---------------
Arbres binaires
---------------

Nous nous intéressons ici aux arbres binaires dans leur
généralité. Dans une seconde partie nous nous concentrerons sur les
arbres binaires de recherche.

Création d'arbres
-----------------

#. Écrire le code des trois fonctions :code:`arbre1`,
   :code:`arbre2` et :code:`arbre3` qui créent les arbres
   des figures ci-dessous.

.. tikz::
   
   [scale=0.5]
   \draw (0,1) node {arbre 1};
   \draw (0,0) node {12}
   child { 
   node {9} 
   }
   child { node {8} };
   \draw (10,1) node {arbre 2};
   \draw (10,0) node {12}
   child { 
      node {9} 
      child[color=white] { node {} }
      child { 
        node {5} 
        child {node {7}}
        child[color=white] {node {}}            
      }
    }
    child[color=white] { node {} };
   \draw (20,1) node {arbre 3};
   \draw (20,0) node {12}
   child { 
     node {9} 
     child { node {1} }
     child { node {5} }
   }
   child { 
     node {8}
     child[color=white] { node {} }
     child {
       node {4}
       child {node {7}}
       child {node {6}}            
     }
   };

Impression
----------

#.  Écrire le code de la fonction :code:`imprimer` qui écrit les valeurs d'un
    arbre binaire de manière infixée. Testez sur les trois arbres exemples.

Décomptes sur les arbres
------------------------

#.  Écrire le code de la fonction :code:`nbFeuilles` qui
    calcule le nombre de feuilles d'un arbre donné en paramètre.

#.  Écrire le code de la fonction :code:`taille` qui
    compte le nombre total de nœuds (nœuds internes et feuilles) d'un
    arbre.

#.  Écrire le code de la fonction :code:`hauteur` qui
    calcule la hauteur d'un arbre donné en paramètre (on rappelle que
    notre convention est qu'un arbre vide est de hauteur -1).


#. Etant donné une taille :math:`n` fixée, il est possible de construire des
    arbres binaires dont la topologie est différente. Le nombre de ces
    topologies différentes est donné par la récurrence :
    
    .. math::
      c_0 &= 1 \\
      c_{n+1} &= \sum_{k=0}^nc_k\cdot c_{n-k}


   Programmez la fonction :code:`nbArbres` avec un algorithme
   récursif s'appuyant sur ces équations de récurrence.


#. Calculez les valeurs de :math:`c_n` pour :math:`n` compris entre 0
   et 19. Que constatez-vous pour le calcul des dernières valeurs ?

#. Programmez une seconde version de la fonction :code:`nbArbres`
   nommée :code:`nbArbresEfficace` avec un algorithme itératif
   utilisant un tableau pour stocker les valeurs des nombres
   :math:`c_k` avec :math:`k \leq n`.

#. À l'aide de cette seconde version, calculez à nouveau les valeurs
   de :math:`c_n` pour `n` compris entre 0 et 19. Constatez
   l'amélioration des temps de calcul.

----------------------------
Arbres binaires de recherche
----------------------------

Nous considérons manipuler désormais des **arbres binaires de
recherche**. Nous vous rappelons leur propriété qui est que chaque
nœud :math:`x` de l'arbre binaire a une valeur telle que toutes les
valeurs des nœuds du sous-arbre gauche de :math:`x` sont inférieures
ou égales à la valeur du nœud :math:`x` et toutes les valeurs du
sous-arbre droit de :math:`x` sont strictement supérieures à la valeur
du nœud :math:`x`.

#.  Écrire une fonction :code:`abr1` permettant la création d'un
    arbre binaire de recherche dans lequel les valeurs sont insérées
    successivement en suivant l'ordre donné :

    ::
       
       arbre 1: 6, 4, 2, 7, 5, 1

#.  Comment s'assurer (simplement) que les arbres construits sont bien des
    arbres binaires de recherche ?

#.  Écrire une fonction :code:`ajouter` qui ajoute une
    valeur à un arbre binaire.

#.  Écrire les fonctions :code:`abr2` et :code:`abr3`
    permettant la création des arbres binaires de recherche en utilisant
    la fonction :code:`ajouter` dans lesquels les valeurs sont
    insérées successivement en suivant l'ordre donné :

    ::
       
       arbre 2: 5, 4, 2, 7, 6, 1
       arbre 3: 7, 1, 4, 5, 6, 2

#.  Écrire un prédicat :code:`appartient` qui teste si une
    valeur est présente dans l'arbre.

#.  Modifier cette fonction pour compter le nombre de
    comparaisons effectuées. Sur lequel des trois arbres donnés en exemple
    y a-t-il le moins de comparaisons pour la recherche de 0 ? Pourquoi
    ?

#.  Où se trouvent respectivement l'élément minimal et maximal
    d'un arbre binaire de recherche ? Écrire les deux fonctions qui retournent
    ces valeurs.

-------------------
L'entier mystérieux
-------------------

Le jeu de l'*entier mystérieux* n'est pas un jeu très
intelligent. Il se joue à deux joueurs : le premier choisit un entier
compris entre 1 et :math:`n`, 
et le second doit deviner cet entier en posant
des questions du style "5 ?", la réponse pouvant être "gagné", "trop
petit" ou "trop grand".  


La meilleure stratégie pour minimiser le nombre de questions à poser
est évidemment de procéder par dichotomie : on commence par tester
:math:`\frac{n}{2}`.  Si l'énigme à trouver est inférieure à
:math:`\frac{n}{2}`, on teste :math:`\frac{n}{4}`, etc.  Cette
dichotomie peut être représentée par un ABR contenant tous les
entiers de 1 à :math:`n` : la racine de l'ABR contient le premier coup à
jouer, puis suivant la réponse ("plus petit", "plus grand"), on joue
la racine du fils gauche ou celle du fils droit. Et ainsi de suite.
Le nombre de coups à jouer avant de gagner est la profondeur du
nœud de valeur celle de l'énigme dans cet ABR.

#. Écrire la fonction récursive
   :code:`contruireArbreEntierMysterieux` 
   qui construit l'ABR du jeu contenant les entiers de :math:`i` à :math:`j`, les
   deux paramètres de la fonction.

#. Écrire la procédure :code:`jouer` qui permet de faire jouer
   l'ordinateur à l'*entier mystérieux* en utilisant un ABR : vous
   choisissez un nombre et vous le faites deviner à l'ordinateur (sans
   tricher, bien sûr).

         
