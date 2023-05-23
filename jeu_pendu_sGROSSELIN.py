#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 16:14:25 2023

@author: salome
"""
    
    
import random
import string

# Fonction pour choisir un mot au hasard dans le fichier mots_pendu
def choisir_mot():
    #mots=[]
    with open("mots_pendu.txt", 'r') as f: 
        mots = f.readlines()
        choix_mot = random.choice(mots).strip()

        return choix_mot


#Une fonction qui permet d'initialiser la devinette en utilisant le mot choisi par la fonction précédente
def initial():
    #global mot_aleatoire
    mot_aleatoire = choisir_mot()  
    mystere=" "
    i=0
    
    while i<len(mot_aleatoire) :
       
        mystere+=" _ "
        i+=1
  
    return mystere

#Cette fonction choisi quel message afficher parmis plusieurs lorsqu'on ne trouve pas la bonne lettre, elle sera utilisé plus tard dans le jeu
def message_perdu():
    perdu=["Mince...cette lettre n'est pas dans le mot","Dommage cette lettre n'est pas dans le mot","C'est loupé pour cette fois, cette lettre n'est pas dans le mot"]
    message=random.choice(perdu)
    
    return message

# De la même façon que la fonction précédente, on affiche un message lorsqu'on trouve une lettre presente dans le mot
def message_gagne():
    gagne=["Bien joué !","Woow une de plus","Bravo","Super !!"]
    message=random.choice(gagne)
    return message

#La fonction qui permet de faire jouer l'utilisateur
def pendu ():
    #On initialise le jeu et on l'introduit à l'utilisateur
    print("\n  >>>>>>>>>>>>> BIENVENU DANS LE JEU DU PENDU <<<<<<<<<<<<<\n")
    print("vous avez 6 tentatives pour deviner le mot\n")
    vies =6
    mot_aleatoire = choisir_mot()
    lettres_trouvees=""
    lettre_essaye=""
    mot=initial()

    
    while vies>0: 
        print("\nLe mot à deviner est: ", mot)
        affichage=""
        lettre=input("Proposez une lettre : ")
        
        alphabet=string.ascii_lowercase+string.ascii_uppercase
        if lettre in alphabet: #on vérifie que l'entrée est bien une lettre
            
            if lettre in lettre_essaye : #On verifie que la lettre n'a pas déj) été essayé par l'utilisateur
                print("\n !! Vous avez déjà tenté cette lettre, essayez-en une autre !!")
                
            elif lettre in mot_aleatoire: #Si la lettre est bien dans le mot on modifie l'affichage en la plaçant aux bons emplacements
                print("\n>>>>>>>", message_gagne())
                lettres_trouvees+=lettre
                for x in mot_aleatoire:
                    if x in lettres_trouvees :
                        affichage +=  x
                    else :
                        affichage+=" _ "
                #print(affichage)
                mot=affichage  
                if "_" not in affichage : #Si on a trouvé toutes les lettres il faut mettre fin au jeu, c'est gagné
                    vies=0
                    print("\n C'est gagné !! Le mot est : ", mot_aleatoire)
                
            else: #Si la lettre n'est pas dans le mot, on décompte une vie du compteur et on indique le nombre de vie restante
                lettre_essaye+=lettre
                vies = vies -1
                print(affichage)
                print(">>>>>>>", message_perdu())
                print("\n Il vous reste ", vies, "tentatives")
                if vies==0: #S'il n'y a plus de vie, il faut mettre fin au jeu et le signaler à l'utilisateur
                    print ("\n   >>>>  Oh non... C'est perdu...  <<<<\n")
                    print("      =>  Le mot à deviner était : ", mot_aleatoire)
       
        else: #Si la saisie n'est pas une lettre, il faut l'indiquer à l'utilisateur et lui demander de recommencer
            print("\n >>>> Saisie incorrect. Veuillez entrer une lettre <<<<<< \n")
            
       
            
    return affichage
        
        










