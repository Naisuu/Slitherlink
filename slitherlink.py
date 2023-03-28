from fltk import *
import sys
import math
import time

etat = {"trace" : (), "interdit": ()}

indices = [[2,2],
            [2,2]]


def est_trace(etat,segment):
    '''
    Permet de vérifier qu'un segment est considéré comme tracé.
    Il renverra True si il est dans le dictionnaire et dans la clé "trace" sinon renverra False

    >>> etat = {"trace" : (((1,1),(2,1)), ((2,3),(2,4)), ((2,4),(3,4))), "interdit": (((0,1),(1,1)), ((2,1),(3,1)), ((1,4),(2,4)), ((2,4),(2,5)))}
    >>> est_trace(etat,((1,1),(2,1)))
    True

    >>> etat = {"trace" : (((1,1),(2,1)), ((2,3),(2,4)), ((2,4),(3,4))), "interdit": (((0,1),(1,1)), ((2,1),(3,1)), ((1,4),(2,4)), ((2,4),(2,5)))} 
    >>> est_trace(etat,((0,1),(1,1)))
    False

    '''
    segment = tri(segment)
    if segment in etat.get('trace'):
        return True
    return False

def est_interdit(etat,segment):
    '''
    Permet de vérifier qu'un segment est considéré comme tracé.
    Il renverra True si il est dans le dictionnaire et dans la clé "trace" sinon renverra False

    >>> etat = {"trace" : (((1,1),(2,1)), ((2,3),(2,4)), ((2,4),(3,4))), "interdit": (((0,1),(1,1)), ((2,1),(3,1)), ((1,4),(2,4)), ((2,4),(2,5)))}
    >>> est_interdit(etat,((0,1),(1,1)))
    True

    >>> etat = {"trace" : (((1,1),(2,1)), ((2,3),(2,4)), ((2,4),(3,4))), "interdit": (((0,1),(1,1)), ((2,1),(3,1)), ((1,4),(2,4)), ((2,4),(2,5)))}
    >>> est_interdit(etat,((2,4),(3,4)))
    False

    '''
    segment = tri(segment)
    if segment in etat.get('interdit'):
        return True
    return False

def est_vierge(etat,segment):
    '''
    Permet de vérifier qu'un segment est considéré comme tracé.
    Il renverra True si il est dans le dictionnaire et dans la clé "trace" sinon renverra False

    >>> etat = {"trace" : (((1,1),(2,1)), ((2,3),(2,4)), ((2,4),(3,4))), "interdit": (((0,1),(1,1)), ((2,1),(3,1)), ((1,4),(2,4)), ((2,4),(2,5)))}
    >>> est_vierge(etat,((0,0),(0,1)))
    True

    >>> etat = {"trace" : (((1,1),(2,1)), ((2,3),(2,4)), ((2,4),(3,4))), "interdit": (((0,1),(1,1)), ((2,1),(3,1)), ((1,4),(2,4)), ((2,4),(2,5)))}
    >>> est_vierge(etat,((1,1),(2,1)))
    False

    >>> etat = {"trace" : (((1,1),(2,1)), ((2,3),(2,4)), ((2,4),(3,4))), "interdit": (((0,1),(1,1)), ((2,1),(3,1)), ((1,4),(2,4)), ((2,4),(2,5)))}
    >>> est_vierge(etat,((0,1),(1,1)))
    False

    '''
    segment = tri(segment)
    if ((segment not in etat.get('trace')) and (segment not in etat.get('interdit'))):
        return True
    return False

def tracer_segment(etat,segment): 
    '''
    Permet de considerer qu'un segment est tracé.
    Il renverra etat avec le nouveau segment tracé

    >>> etat = {"trace" : (((1,1),(2,1)), ((2,3),(2,4)), ((2,4),(3,4))), "interdit": (((0,1),(1,1)), ((2,1),(3,1)), ((1,4),(2,4)), ((2,4),(2,5)))}
    >>> tracer_segment(etat,((0,0),(1,0)))
    {'trace': (((1, 1), (2, 1)), ((2, 3), (2, 4)), ((2, 4), (3, 4)), ((0, 0), (1, 0))), 'interdit': (((0, 1), (1, 1)), ((2, 1), (3, 1)), ((1, 4), (2, 4)), ((2, 4), (2, 5)))}

    >>> etat = {"trace" : (((1,1),(2,1)), ((2,3),(2,4)), ((2,4),(3,4))), "interdit": (((0,1),(1,1)), ((2,1),(3,1)), ((1,4),(2,4)), ((2,4),(2,5)))} 
    >>> tracer_segment(etat,((0,1),(1,1)))
    {'trace': (((1, 1), (2, 1)), ((2, 3), (2, 4)), ((2, 4), (3, 4))), 'interdit': (((0, 1), (1, 1)), ((2, 1), (3, 1)), ((1, 4), (2, 4)), ((2, 4), (2, 5)))}

    ''' 
    if est_vierge(etat,segment) == False :
        return etat
    etat["trace"] = list(etat["trace"])
    etat["trace"].append(tri(segment))
    etat["trace"] = tuple(etat["trace"])
    return etat

def interdire_segment(etat,segment):
    '''
    Permet d'interdire un segment.
    Il renverra etat avec le nouveau segment interdit.

    >>> etat = {"trace" : (((1,1),(2,1)), ((2,3),(2,4)), ((2,4),(3,4))), "interdit": (((0,1),(1,1)), ((2,1),(3,1)), ((1,4),(2,4)), ((2,4),(2,5)))}
    >>> interdire_segment(etat,((0,0),(1,0)))
    {'trace': (((1, 1), (2, 1)), ((2, 3), (2, 4)), ((2, 4), (3, 4))), 'interdit': (((0, 1), (1, 1)), ((2, 1), (3, 1)), ((1, 4), (2, 4)), ((2, 4), (2, 5)), ((0, 0), (1, 0)))}

    >>> etat = {"trace" : (((1,1),(2,1)), ((2,3),(2,4)), ((2,4),(3,4))), "interdit": (((0,1),(1,1)), ((2,1),(3,1)), ((1,4),(2,4)), ((2,4),(2,5)))}
    >>> interdire_segment(etat,((0,1),(1,1)))
    {'trace': (((1, 1), (2, 1)), ((2, 3), (2, 4)), ((2, 4), (3, 4))), 'interdit': (((0, 1), (1, 1)), ((2, 1), (3, 1)), ((1, 4), (2, 4)), ((2, 4), (2, 5)))}

    ''' 
    if est_trace(etat,segment) == True :
        etat["trace"] = list(etat["trace"])
        etat["trace"].remove(segment)
        etat["trace"] = tuple(etat["trace"])
    if est_interdit(etat,segment) == True :
        return etat
    etat["interdit"] = list(etat["interdit"])
    etat["interdit"].append(segment)
    etat["interdit"] = tuple(etat["interdit"])
    return etat

def effacer_segment(etat,segment):
    '''
    Permet d'effacer les informations d'un segment.
    Il renverra etat en retirant les informations du segment.

    >>> etat = {"trace" : (((1,1),(2,1)), ((2,3),(2,4)), ((2,4),(3,4))), "interdit": (((0,1),(1,1)), ((2,1),(3,1)), ((1,4),(2,4)), ((2,4),(2,5)))}
    >>> effacer_segment(etat,((1,1),(2,1)))
    {'trace': (((2, 3), (2, 4)), ((2, 4), (3, 4))), 'interdit': (((0, 1), (1, 1)), ((2, 1), (3, 1)), ((1, 4), (2, 4)), ((2, 4), (2, 5)))}

    >>> etat = {"trace" : (((1,1),(2,1)), ((2,3),(2,4)), ((2,4),(3,4))), "interdit": (((0,1),(1,1)), ((2,1),(3,1)), ((1,4),(2,4)), ((2,4),(2,5)))} 
    >>> effacer_segment(etat,((0,1),(1,1)))
    {'trace': (((1, 1), (2, 1)), ((2, 3), (2, 4)), ((2, 4), (3, 4))), 'interdit': (((2, 1), (3, 1)), ((1, 4), (2, 4)), ((2, 4), (2, 5)))}

    >>> etat = {"trace" : (((1,1),(2,1)), ((2,3),(2,4)), ((2,4),(3,4))), "interdit": (((0,1),(1,1)), ((2,1),(3,1)), ((1,4),(2,4)), ((2,4),(2,5)))} 
    >>> effacer_segment(etat,((0,0),(0,1)))
    {'trace': (((1, 1), (2, 1)), ((2, 3), (2, 4)), ((2, 4), (3, 4))), 'interdit': (((0, 1), (1, 1)), ((2, 1), (3, 1)), ((1, 4), (2, 4)), ((2, 4), (2, 5)))}
    ''' 
    if est_trace(etat,tri(segment)) == True :
        etat["trace"] = list(etat["trace"])
        etat["trace"].remove(tri(segment))
        etat["trace"] = tuple(etat["trace"])   
    if est_interdit(etat,tri(segment)) == True :
        etat["interdit"] = list(etat["interdit"])
        etat["interdit"].remove(tri(segment))
        etat["interdit"] = tuple(etat["interdit"]) 
    return etat


def segment_trace(etat,sommet):
    '''
    Renvoi la liste des segments tracés adjacents à un sommet donné.

    >>> etat = {"trace" : (((1,1),(2,1)), ((2,3),(2,4)), ((2,4),(3,4))), "interdit": (((0,1),(1,1)), ((2,1),(3,1)), ((1,4),(2,4)), ((2,4),(2,5)))}
    >>> segment_trace(etat,(1,1))
    [((1, 1), (2, 1))]

    >>> etat = {"trace" : (((1,1),(2,1)), ((2,3),(2,4)), ((2,4),(3,4))), "interdit": (((0,1),(1,1)), ((2,1),(3,1)), ((1,4),(2,4)), ((2,4),(2,5)))} 
    >>> segment_trace(etat,(0,0))
    []

    '''
    x = sommet[0]
    y = sommet[1]
    lst = []
    if y != len(indices) :
        if est_trace(etat,((x,y),(x,y+1))) == True :
            lst.append(((x,y),(x,y+1)))
    if x != len(indices) :
        if est_trace(etat,((x,y),(x+1,y))) == True :
            lst.append(((x,y),(x+1,y)))
    if y != 0 :
        if est_trace(etat,((x,y),(x,y-1))) == True :
            lst.append(((x,y),(x,y-1)))
    if x != 0 :
        if est_trace(etat,((x,y),(x-1,y))) == True :
            lst.append(((x,y),(x-1,y)))
    return lst


def segment_interdit(etat,sommet):
    '''
    Renvoi la liste des segments tracés adjacents à un sommet donné.

    >>> etat = {"trace" : (((1,1),(2,1)), ((2,3),(2,4)), ((2,4),(3,4))), "interdit": (((0,1),(1,1)), ((2,1),(3,1)), ((1,4),(2,4)), ((2,4),(2,5)))}
    >>> segment_interdit(etat,(1,1))
    [((1, 1), (0, 1))]

    >>> etat = {"trace" : (((1,1),(2,1)), ((2,3),(2,4)), ((2,4),(3,4))), "interdit": (((0,1),(1,1)), ((2,1),(3,1)), ((1,4),(2,4)), ((2,4),(2,5)))} 
    >>> segment_interdit(etat,(0,0))
    []

    '''
    x = sommet[0]
    y = sommet[1]
    lst = []
    if y != len(indices) :
        if est_interdit(etat,((x,y),(x,y+1))) == True :
            lst.append(((x,y),(x,y+1)))
    if x != len(indices) :
        if est_interdit(etat,((x,y),(x+1,y))) == True :
            lst.append(((x,y),(x+1,y)))
    if y != 0 :
        if est_interdit(etat,((x,y),(x,y+1))) == True :
            lst.append(((x,y),(x,y+1)))
    if x != 0 :
        if est_interdit(etat,((x,y),(x-1,y))) == True :
            lst.append(((x,y),(x-1,y)))
    return lst

def segment_vierge(etat,sommet):
    '''
    Renvoi la liste des segments tracés adjacents à un sommet donné.

    >>> etat = {"trace" : (((1,1),(2,1)), ((2,3),(2,4)), ((2,4),(3,4))), "interdit": (((0,1),(1,1)), ((2,1),(3,1)), ((1,4),(2,4)), ((2,4),(2,5)))}
    >>> segment_vierge(etat,(1,1))
    [((1, 1), (1, 2)), ((1, 1), (1, 0))]

    >>> etat = {"trace" : (((1,1),(2,1)), ((2,3),(2,4)), ((2,4),(3,4))), "interdit": (((0,1),(1,1)), ((2,1),(3,1)), ((1,4),(2,4)), ((2,4),(2,5)))} 
    >>> segment_vierge(etat,(2,4))
    []

    '''
    x = sommet[0]
    y = sommet[1]
    lst = []
    if y != len(indices) :
        if est_vierge(etat,((x,y),(x,y+1))) == True :
            lst.append(((x,y),(x,y+1)))
    if x != len(indices) :
        if est_vierge(etat,((x,y),(x+1,y))) == True :
            lst.append(((x,y),(x+1,y)))
    if y != 0 :
        if est_vierge(etat,((x,y),(x,y-1))) == True :
            lst.append(((x,y),(x,y-1)))
    if x != 0 :
        if est_vierge(etat,((x,y),(x-1,y))) == True :
            lst.append(((x,y),(x-1,y)))
    return lst


def statut_case(indices,etat,case):
    '''
    Permet de comparer le nombre segments autour d'une cases avec l'indice donné.
    Il renverra None si il n'y a pas d'indices, renverra 0 si le nombre de segments corresponds à l'indice,
    reverra un nombre positif coreespondant au nombre de segments manquant autour de la case 
    ou renverra un nombre négatif correspondant au nombre de segments en trop autour de la case.

    >>> etat = {"trace" : (((1,1),(2,1)),((2,3),(2,4)),((2,4),(3,4))), "interdit": ((0,1),(1,1),((2,1),(3,1)),((1,4),(2,4)),((2,4),(2,5))) } 
    >>> statut_case(indices, etat, (1,0))
    2

    '''
    x = case[0]
    y = case[1]
    c = 0
    if (indices[x][y] == None):
        return None
    if est_trace(etat,((x,y),(x,y+1))) == True :
        c+=1
    if est_trace(etat,((x,y),(x+1,y))) == True :
        c+=1
    if est_trace(etat,((x,y+1),(x+1,y+1))) == True :
        c+=1
    if est_trace(etat,((x+1,y),(x+1,y+1))) == True :
        c+=1
    return (indices[x][y] - c)

def tri(segment):
    '''
    Permet de trier les segment pour ne pas avoir de problème avec l'inversabilité des sommets

    >>> tri(((0,0),(1,1)))
    ((0, 0), (1, 1))

    >>> tri(((1,1),(0,0)))
    ((0, 0), (1, 1))
    '''
    if segment[0][0] < segment[1][0] :
        return segment
    if segment[0][0] == segment[1][0] :
        if segment[0][1] < segment[1][1] :
            return segment
    return ((segment[1]),(segment[0]))

def victoire1(indices, etat):
    for i in range (len(indices)):
        for y in range (len(indices)):
            if indices[i][y] != None :
                if statut_case(indices, etat, (i, y)) != 0 :
                    return False
    return True

def longueur_boucle(etat, segment):
    '''
    Fonction nqui vérifie si tous les segments appartiennent à une seule boucle
    et qui renvoie la longueur de celle-ci si elle st fermée
    '''
    c = 1
    depart = (segment[0][0], segment[0][1])
    precedent = depart
    courant = (segment[1][0], segment[1][1])
    while courant != depart :
        adj = segment_trace(etat, courant)
        if len(adj) != 2:
            return None
        if adj[0][1] == precedent :
            precedent = courant
            courant = adj[1][1]
        else:
            precedent = courant
            courant = adj[0][1]
        c+=1
    return c

def interface(indices, etat):
    '''
    Permet de créer l'interface du jeu en fonction de la taille de la grille
    '''
    for i in range (taille+1) :
        for y in range (taille+1) :
            cercle(100*i + 100, 100*y + 100, 3, remplissage="black")
    for i in range (taille) :
        for y in range (taille) :
            if statut_case(indices, etat, (y, i)) == None :
               color = "black" 
            elif statut_case(indices, etat, (y, i)) > 0 :
                color = "black"
            elif statut_case(indices, etat, (y, i)) == 0 :
                color = "blue"
            elif statut_case(indices, etat, (y, i)) < 0 :
                color = "red"
            texte(100*i + 140, 100*y + 133, indices[y][i], couleur = color)
    for i in range (len(etat["trace"])) :
        ligne(etat["trace"][i][0][1]*100 + 100, etat["trace"][i][0][0]*100 + 100, etat["trace"][i][1][1]*100 + 100, etat["trace"][i][1][0]*100 + 100, epaisseur=3)
    for i in range (len(etat["interdit"])) :
        ligne(etat["interdit"][i][0][1]*100 + 100, etat["interdit"][i][0][0]*100 + 100, etat["interdit"][i][1][1]*100 + 100, etat["interdit"][i][1][0]*100 + 100, epaisseur=3, couleur = "red")
    
def maj(indices, etat):
    '''
    Fonction qui permet de jouer sur la grille : de tracer un segment, de supprimer
    un segment, d'interdire un segment en fonction du clic effectuer et de sa position 
    dans la fenêtre
    '''
    while True :
        ev = donne_ev()
        tev = type_ev(ev)
        if tev == "Quitte":
            ferme_fenetre()
            break
        elif tev == "ClicGauche" or tev == "ClicDroit" :
            y = abscisse(ev)
            x = ordonnee(ev)
            dx = (x - 100) / 100
            dy = (y - 100) / 100
            if dx < 0 or dy < 0 :
                break
            if dx > len(indices) or dy > len(indices):
                break
            if -0.2 < dy - round(dy) < 0.2:
                if 0 <= dy - round(dy):
                    if est_vierge(etat, (((math.floor(dx), math.floor(dy)), ((math.floor(dx)+1),(math.floor(dy)))))) == True:
                        if tev == "ClicDroit":
                            interdire_segment(etat, (((math.floor(dx), math.floor(dy)), ((math.floor(dx)+1),(math.floor(dy))))))
                        elif tev == "ClicGauche":
                            tracer_segment(etat, (((math.floor(dx), math.floor(dy)), ((math.floor(dx)+1),(math.floor(dy))))))
                    else :
                        effacer_segment(etat, (((math.floor(dx), math.floor(dy)), ((math.floor(dx)+1),(math.floor(dy))))))
                if 0 > dy - round(dy):
                    if est_vierge(etat, (((math.floor(dx), math.floor(dy)+1), ((math.floor(dx)+1),(math.floor(dy)+1))))) == True:
                        if tev == "ClicDroit":
                            interdire_segment(etat, (((math.floor(dx), math.floor(dy)+1), ((math.floor(dx)+1),(math.floor(dy)+1)))))
                        elif tev == "ClicGauche": 
                            tracer_segment(etat, (((math.floor(dx), math.floor(dy)+1), ((math.floor(dx)+1),(math.floor(dy)+1)))))
                    else:
                        effacer_segment(etat, (((math.floor(dx), math.floor(dy)+1), ((math.floor(dx)+1),(math.floor(dy)+1)))))
                efface_tout()
            elif -0.2 < dx - round(dx) < 0.2:
                if 0 <= dx - round(dx):
                    if est_vierge(etat, (((math.floor(dx), math.floor(dy)), ((math.floor(dx)),(math.floor(dy)+1))))) == True:
                        if tev == "ClicDroit":
                            interdire_segment(etat, (((math.floor(dx), math.floor(dy)), ((math.floor(dx)),(math.floor(dy)+1)))))
                        elif tev == "ClicGauche":
                            tracer_segment(etat, (((math.floor(dx), math.floor(dy)), ((math.floor(dx)),(math.floor(dy)+1)))))
                    else :
                        effacer_segment(etat, (((math.floor(dx), math.floor(dy)), ((math.floor(dx)),(math.floor(dy)+1)))))
                if 0 > dx - round(dx):
                    if est_vierge(etat, (((math.floor(dx)+1, math.floor(dy)), ((math.floor(dx)+1),(math.floor(dy)+1))))) == True:
                        if tev == "ClicDroit":
                            interdire_segment(etat, (((math.floor(dx)+1, math.floor(dy)), ((math.floor(dx)+1),(math.floor(dy)+1)))))
                        elif tev == "ClicGauche": 
                            tracer_segment(etat, (((math.floor(dx)+1, math.floor(dy)), ((math.floor(dx)+1),(math.floor(dy)+1)))))
                    else:
                        effacer_segment(etat, (((math.floor(dx)+1, math.floor(dy)), ((math.floor(dx)+1),(math.floor(dy)+1)))))
                efface_tout()
            return True
        mise_a_jour()

def creer_indices(grille):
    '''
    Permet de creer la tableu d'indices depuis un fichier texte externe
    et renvoie ce tableau
    '''
    with open(grille, 'r') as content:
        lignes = content.readlines()
        indices = []
        temp = []
        for ligne in lignes:
            temp.append(ligne.split())
     
        for i in range(len(temp)):
            temp2 = list(temp[i][0])
            for j in range(len(temp)):
                if temp2[j] == '_':
                    temp2[j] = None
                else:
                    temp2[j] = int(temp2[j])
            indices.append(temp2)
    return indices

def choix_grille():
    '''
    Creer une fenêtre qui permet de sélectionner une grille pour jouer et 
    renvoie le numéro de la grille choisie
    '''
    cree_fenetre(325, 325)
    g = 1
    for i in range(3):
        for y in range(3):
            rectangle(25 + 100*y, 25 + 100*i, 100 + 100*y, 100+ 100*i, epaisseur = 3)
            texte(52+ 100*y, 45 + 100*i, g)
            g+=1
    while True:
        ev = donne_ev()
        tev = type_ev(ev)
        if tev == "Quitte":
            ferme_fenetre()
            break
        elif tev == "ClicGauche":
            y = abscisse(ev)
            x = ordonnee(ev)
            dx = math.floor(x/100)
            dy = math.floor(y/100)
            c = 1
            a = 0
            for i in range(3):
                for j in range(3):
                    if dx == i and dy == j:
                        a = c
                    c+=1
            break
        mise_a_jour()
    ferme_fenetre()
    return (a)
    
def jeu(etat, indices):
    '''
    Fonction qui permet de jouer eu jeu manuellement 
    '''
    taille = len(indices)
    cree_fenetre(100 * taille + 200, 100 * taille + 200)
    interface(indices, etat)
    while longueur_boucle(etat, etat["trace"][0]) != len(etat["trace"]) or victoire1(indices, etat) != True:
        while True :
            maj(indices, etat)
            interface(indices, etat)
            if etat["trace"] != () :
                break
            
def rejouer():
    '''
    Créer une fenêtre lorsqu'une partie est fini et permet de rejouer ou de quitter
    le jeu
    '''
    cree_fenetre(325, 325)
    texte(100, 75, "Rejouer ?", couleur="blue")
    rectangle(50,150, 125, 225, couleur ="green", epaisseur = 3, remplissage="green")
    rectangle(200,150, 275, 225, couleur ="red",epaisseur = 3, remplissage="red")
    while True:
        ev = donne_ev()
        tev = type_ev(ev)
        if tev == "Quitte":
            ferme_fenetre()
            break
        elif tev == "ClicGauche":
            y = abscisse(ev)
            x = ordonnee(ev)
            if 50 < y < 125 and 150 < x < 225:
                rejouer = True
                break
            elif 200 < y < 275 and 150 < x < 225:
                rejouer = False
                break
        mise_a_jour()
    ferme_fenetre()       
    return rejouer

def choix_jeu():
    '''
    Créer une fenêtre qui donne le choix entre jouer manuellment
    ou utiliser le solveur
    '''
    cree_fenetre(325, 325)
    texte(100, 75, "Solveur ?", couleur="blue")
    rectangle(50,150, 125, 225, couleur ="green", epaisseur = 3, remplissage="green")
    rectangle(200,150, 275, 225, couleur ="red",epaisseur = 3, remplissage="red")
    while True:
        ev = donne_ev()
        tev = type_ev(ev)
        if tev == "Quitte":
            ferme_fenetre()
            break
        elif tev == "ClicGauche":
            y = abscisse(ev)
            x = ordonnee(ev)
            if 50 < y < 125 and 150 < x < 225:
                rejouer = True
                break
            elif 200 < y < 275 and 150 < x < 225:
                rejouer = False
                break
        mise_a_jour()
    ferme_fenetre()       
    return rejouer

def case_adj(indices, segment):
    '''
    Vérifie si les indices des cases adjacentes à un segment sont superieurs
    à 0 revoie True si c'est le cas et False sinon
    '''
    segment = tri(segment)
    x = segment[0][0]
    y = segment[0][1]
    x1 = segment[1][0]
    y1 = segment[1][1]
    if y == y1:
        if y == 0:
            c = 5
        else :
            c = statut_case(indices, etat, (x,y-1))
            if c == None:
                c = 6
        if y1 == len(indices):
            c1 = 5
        else: 
            c1 = statut_case(indices, etat, (x,y))
            if c1 == None:
                c1 = 6
    else:
        if x == 0:
            c = 5
        else :
            c = statut_case(indices, etat, (x-1,y))
            if c == None:
                c = 6
        if x1 == len(indices):
            c1 = 5
        else:
            c1 = statut_case(indices, etat, (x,y))
            if c1 == None:
                c1 = 6
    if (c > 0 and c1 > 0):
        return True
    return False

def solveur(indices,etat,sommet):
    '''
    Permet de resoudre une grille de facon recursiveen remplissant au 
    fur et à mesure celle-ci en fonction des indices des cases adjacentes
    '''
    interface(indices, etat)
    adj_trace = segment_trace(etat,sommet)
    adj = segment_vierge(etat,sommet)
    if len(segment_trace(etat,sommet)) == 2:
        if victoire1(indices, etat) != True:
            for i in range (len(adj)):
                effacer_segment(etat,adj[i])
                efface_tout()
                mise_a_jour()
            return False
        return True
    elif len(segment_trace(etat,sommet)) > 2:
        for i in range (len(adj)):
            effacer_segment(etat,adj[i])
            efface_tout()
            mise_a_jour()
        return False
    elif len(adj_trace) <= 1:
        for i in range (len(adj)):
            if case_adj(indices,adj[i]) == True:
                tracer_segment(etat,adj[i])
                mise_a_jour()
                res = solveur(indices,etat,adj[i][1])
                if res == True:
                    return True
                else:
                    effacer_segment(etat,adj[i])
                    efface_tout()
                    mise_a_jour()
            else:
                effacer_segment(etat,adj[i])
                efface_tout()
                mise_a_jour()

def start(indices,c):
    '''
    Sélectionne un point pour debuter le solveur en fonction des 
    indices de la grille
    '''
    for i in range (len(indices)):
        for y in range (len(indices)):
            if indices[i][y] == 3:
                return(i, y)
    for i in range (len(indices)):
        for y in range (len(indices)):
            if indices[i][y] == 2:
                if c == 1 :
                    return(i+1, y)
                return(i, y)
    for i in range (len(indices)):
        for y in range (len(indices)):
            if indices[i][y] == 1:
                if c == 1:
                    return (i+1, y)
                if c == 2 :
                    return (i+1, y+1)
                return(i, y)
    return False

while True:
    grille = choix_grille()
    indices = creer_indices("grille"+ str(grille) +".txt")
    taille = len(indices)
    c = 0
    if choix_jeu() == True:
        tps1 = time.perf_counter()
        while True:
            etat = {"trace" : (), "interdit": ()}
            cree_fenetre(100 * taille + 200, 100 * taille + 200)
            interface(indices, etat)
            debut = start(indices,c)
            if solveur(indices,etat, debut) == True:
                break
            c+=1

    else :
        tps1 = time.perf_counter()
        etat = {"trace" : (((0,0),(0,1)),), "interdit": ()}
        jeu(etat, indices)
    tps2 = time.perf_counter()
    print("Temps de la partie :" , round(tps2 - tps1, 2))
    texte(25,25, "Victoire", couleur="green")
    attend_clic_gauche()
    efface_tout()
    ferme_fenetre()
    if rejouer() == False:
        break
