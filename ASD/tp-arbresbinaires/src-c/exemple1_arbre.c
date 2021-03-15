#include "ArbreBinaire.h"
#include "Affichage.h"

int
main
(void)
{
  Noeud_t arbre,tmp,tmp2  ;

	arbre = CreerNoeud(1) ;
	tmp = CreerNoeud(2) ;
	AjouterFilsGauche(arbre,tmp);
	tmp = CreerNoeud(3) ;
	AjouterFilsDroit(arbre,tmp);
  tmp2 = CreerNoeud(4) ;
	AjouterFilsDroit(tmp,tmp2);
	
	SauverArbreDansFichier(arbre,"exemple1");
	
	return 0 ;
}
