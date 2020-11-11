# Bataille navale
> Implémentation du projet BATAILLE NAVALE dans le cadre du cours de Développement informatique II (Python).

## Objectif
L’objectif à travers de ce projet est de réaliser le jeu de la bataille navale afin de montrer nos compétences en matière de programmation Python. Mais également de divertir les potentiels joueurs.

## MVP
**__Voici la déscription du MVP.__**

### Description MVP
* Notre MVP fonctionnera en ligne de commande où la grille sera affichée en console. 

* L'utilisateur commencera par introduire son prénom / pseudo.

* L'utilisateur aura un nombre limité de bateaux à placer, les bateaux de l'ordinateur (contre qui l'utilisateur joue) seront placés de façon aléatoire.

* Pour le MVP, l'utilisateur aura un nombre limité de tour, afin de ne pas éterniser la partie et la rendre plus chouette. La partie finira donc après x tours, le gagnant sera celui qui a touché le plus de bateaux, si aucun des joueurs n'a touché de bateaux, alors ce sera une égalité.

* Quand le joueur choisi une case et qu'il "touche" un bateau ennemi, il peut alors rejouer un autre tour. Ce sera de même dans le cas contraire.

* La grille ira de A à x pour les colonnes et de 1 à x pour les lignes, il sera donc demandé à l'utilisateur de placer les bateaux selon des coordonnées.

* En ligne de commande, il sera demandé à l'utilisateur de donner une coordonnée. Si l'utilisateur insère une mauvaise coordonnée, il devra alors en réintroduire une valide.

* La taille des bateaux fera une « case », il y en aura 3 à placer. Au cours du développement du programme, la taille des bateaux changera (1 sur 4 cases, ...) .

* Quand une partie de bateau est touchée, un "X" apparaitra dans la grille qui se trouve en console.

* Selon le gagnant de la partie, un message apparaitra disant " nomUtilisateur a gagné contre l'ordinateur" ou inversement.

* A la fin de la partie, une fois le résultat affiché, il sera proposé au joueur de rejouer une partie ou de quitter le jeu.
## Besoins fonctionnels du projet
Les besoins fonctionnels de ce projet sont:
* Une interface graphique et une interface console sur lesquelles l’utilisateurpeut jouer. C’est-à-dire que les grilles s’affichent également en interface console.
* Dans l’interface graphique, il y aura un bouton « help » qui permettra de décrire le fonctionnement du jeu si l’utilisateur en a besoin.
* Une légende sera présente en interface console, au début du jeu, afin d’indiquer au joueur la signification des symboles.
* La taille de la grille de jeu qui varie selon le niveau de difficulté choisi par le joueur.
* Le joueur ne peut placer un bateau en dehors des limites de la grille, sinon un message d’erreur s’affichera.
* Les bateaux ne peuvent ni se toucher, ni être superpositionnés sinon un message d’erreur apparaitra.
* Le programme doit permettre au joueur de rejouer lorsqu’il a touché un bateau ennemi.
* L’utilisateur aura sa grille affichée avec ses bateaux placés ainsi que la grille de son adversaire afin d’attaquer les bateaux.
* Les attaques de l’ordinateur seront visibles sur la grille du joueur.
* Un nombre de tours est définit au préalable afin de ne pas éterniser la partie.
* Si un des joueurs parvient à couler un navire, un message s’affiche indiquant « J’ai coulé ton navire en x tirs ! ».
* Si un tir est raté, un message sera affiché en console.

## Navires disponibles
Le client aura à sa disposition plusieurs navires qu'il devra placer.
Chaque navire possède une longueur déterminé et innchangable, voici la description:
* The Dying Gull :
    * Longueur de 2 cases.
* HMS Intercepteur :
    * Longueur de 3 cases.
* Silent Mary :
    * Longueur de 3 cases.
* Queen Anne’s Revenge :
    * Longueur de 2 cases.
* Black Pearl :
    * Longueur de 2 cases.

#### Fonctionnalité supplémentaire
Le client aura droit à choisir le niveaux dans lequel il préfère jouer. Chaque niveau est limité par un nombre de tours (pas modificable !).

#### Mode d'emploi

Le client doit se rendre dans le dossier dans lequel il y a:
 * **__Les fichiers contenant le MVP en question__** 

Après la recherche des fichiers, le client doit simplement saisir dans l'invité de commandes :
 > **_python fichierMVP.py_**



## Interface
L’interface sera simple d’utilisation, ergonomique. Il sera également possible de jouer en console.


## Déroulement d’une partie

1. Le joueur rentre son prénom afin de l’identifier.
2. Il choisit le niveau de difficulté du jeu (facile, normal, difficile)
3. Selon le niveau choisi, le joueur place le nombre de bateau qu’il a sur la grille (sans qu’ils se touchent) qu’il a à sa disposition en respectant les limites de la grille.
4. La grille de l’adversaire (l’ordinateur) est générée aléatoirement.
5. Une fois les bateaux placés, la partie peut commencer, le joueur choisit les coordonnées de la grille là où il souhaite attaquer.
6. S’il touche un bateau adversaire, il peut rejouer, sinon c’est au tour de l’adversaire (l’ordinateur) de jouer.
7. La partie se termine quand tous les bateaux sont coulés, ou quand les 10 tours définit par le programmeur sont écoulés. Un message est affiché indiquant qui a gagné la partie.
8. Il sera ensuite demandé au joueur s’il souhaite rejouer ou non. Selon sa réponse, une partie est relancée ou non.
9. Si le joueur a réalisé plusieurs parties, à la fin, quand il souhaite ne plus jouer, un message indiquera combien de partie le joueur a gagné contre l’ordinateur et inversement.
