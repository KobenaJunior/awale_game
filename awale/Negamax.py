# NEGAMAX######################################
# ALGORITHME NEGAMAX AVEC ELAGAGE ALPHA BETA
import copy

def negamax(moteur, plateau, tour, ptA, ptB, profondeur, alpha, beta, couleur):
    # Condition d'arrêt : profondeur atteinte ou fin de partie
    if profondeur == 0 or sum(plateau) == 0:
        # Score : (Points Joueur A - Points Joueur B) * couleur
        return (ptA - ptB) * couleur

    max_eval = float('-inf')
    
    # Intervalle de jeu selon le tour (0-5 pour A, 6-11 pour B)
    indices_possibles = range(0, 6) if tour % 2 == 0 else range(6, 12)
    
    for coup in indices_possibles:
        if plateau[coup] == 0: continue  # Trou vide
        
        # Simulation : On copie les données pour ne pas modifier l'original
        plat_sim = plateau[:]
        res_plat, res_A, res_B, _ = moteur.jeu(plat_sim, tour, ptA, ptB, coup)
        
        if res_plat is None: continue

        # Appel récursif (on inverse la couleur et on passe au tour suivant)
        eval = -negamax(moteur, res_plat, tour + 1, res_A, res_B, profondeur - 1, -beta, -alpha, -couleur)
        
        max_eval = max(max_eval, eval)
        alpha = max(alpha, eval)
        if alpha >= beta:
            break  # Élagage Alpha-Beta
            
    return max_eval

# MEILEUR COUP
def meilleur_coup(moteur, plateau, tour, ptA, ptB, profondeur):
    best_score = float('-inf')
    choix = -1
    indices = range(0, 6) if tour % 2 == 0 else range(6, 12)
    couleur = 1 if tour % 2 == 0 else -1
    
    for coup in indices:
        if plateau[coup] == 0: continue
        
        # Copie pour simulation
        plat_sim = plateau[:]
        res_plat, res_A, res_B, _ = moteur.jeu(plat_sim, tour, ptA, ptB, coup)
        
        # Evaluation du coup
        score = -negamax(moteur, res_plat, tour + 1, res_A, res_B, profondeur - 1, float('-inf'), float('inf'), -couleur)
        
        if score > best_score:
            best_score = score
            choix = coup
    if choix==-1:
        for coup in indices:
            if(plateau[coup]>0):
                return coup
    return choix

# coup=meilleur_coup(MoteurAwale(),)
