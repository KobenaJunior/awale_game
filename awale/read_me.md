<!-- Par Kobena Junior Koffi: koffikobenajunior@gmail.com -->

<!-- IMPLEMENTATION DU JEU DE PLATEAU AWALE VIE L'ALGORITHME MINIMAX AVEC ELAGAGE ALPHA BET -->

# Installation
````bash
pip install -r requirements.txt
```

prérequis:
- Python 3.8+

# Fichiers R
- awale_main.py : le colde principale
- kv_file.py : l'interface graphique du programme
- moteur.py: contient la logique du jeu
-Negamax.py contient l'algorithme Negamax

# A noter:
	Dans un  jeu d'awale classique lorsqu'un joueur est affamé(n'as plus de pions alors que c'est son tour), l'autre joueur a l'obligation de le ressourcer(lui apporter d'autre pion lorsque celui ci le peux, il peut ainsi sse retrouver a jouer plusieur fois de suite pour ressourcer son adversaire) J'ai retirer cette contrainte de sorte que lorsqu'un joueur se retrouve a court de pions alors que c'est à son tour de jouer le jeu s'achève et il est juger perdant, 

	Les points se calcule en faisant la somme des pions capturée et des pions present dans notre partie du plateau.