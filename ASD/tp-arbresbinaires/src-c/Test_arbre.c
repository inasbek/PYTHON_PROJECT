#include <stdio.h>

#include "ArbreBinaire.h"

#define max(a,b) ((a)>(b)?(a):(b))

/* Manipulation d'arbres binaires */

Noeud_t arbre1 (void) {
   return NULL;
}

Noeud_t arbre2 (void) {
   return NULL;
}

Noeud_t arbre3 (void) {
   return NULL;
}

void imprimer (Noeud_t a) {
   ;
}

int taille (Noeud_t a) {
   return -1;
}

int hauteur (Noeud_t a) {
   return -1;
}

int nbFeuilles(Noeud_t a) {
   return -1;
}


/* Comptage d'arbres */

int nbArbres(int n) {
   return 0;
}
    
/* Manipulation d'arbres binaires de recherche */

Noeud_t abr1 (void) {
   return NULL;
}

Noeud_t ajouter (value_t v, Noeud_t a) {
   return NULL;
}

Noeud_t abr2 (void) {
   return NULL;
}

Noeud_t abr3 (void) {
   return NULL;
}

int appartient (value_t v, Noeud_t a) {
   return 0;
}

int valeur_minimale (Noeud_t abr) {
   return -1;
}

int valeur_maximale (Noeud_t abr) {
   return -1;
}

/* Entier mysterieux */

Noeud_t construitArbreEntierMysterieux (value_t i, value_t j) { 
   return NULL;
}

void jouer (int n) {
   ;
}

/* Tests sur les arbres binaires */

void testArbreBinaire(Noeud_t a) {
   imprimer(a); printf("\n");
   printf("Taille     = %d\n",(taille(a)));
   printf("Hauteur    = %d\n",(hauteur(a)));
   printf("nbFeuilles = %d\n",(nbFeuilles(a)));
}

/* Tests sur les arbres binaires de recherche */
void testABR (Noeud_t a) {
   int i;
   imprimer(a); printf("\n");
   printf("Taille     = %d\n",(taille(a)));
   printf("Hauteur    = %d\n",(hauteur(a)));
   printf("nbFeuilles = %d\n",(nbFeuilles(a)));
   printf("Valeurs présentes dans l'arbre : ");
   for (i = 1; i <= 10; i++) {
      if (appartient(i,a)) {
         printf("%d ",i);
      }
   }
   printf("\n");
}
  
/* Programme principal */
int main (int argc, char **argv) {

   int i;
   
   testArbreBinaire(arbre1());
   testArbreBinaire(arbre2());
   testArbreBinaire(arbre3());

   for (i = 0; i <= 19; i++) {
      printf("Le nombre d'arbres à %d noeuds est %d\n",i,(nbArbres(i)));
   }
  
   testABR(abr1());
   testABR(abr2());
   testABR(abr3());

   printf("Arbre mysterieux entre 12 et 24:\n");
   imprimer(construitArbreEntierMysterieux(12,24));
   printf("\n");
  
   jouer(100);

   return 0;
   
}
