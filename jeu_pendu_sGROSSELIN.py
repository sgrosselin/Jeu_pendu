#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 16:14:25 2023

@author: salome
"""
    
    
import random
import string

# Fonction pour choisir un mot au hasard
def choisir_mot():
    #mots=[]
    with open("mots_pendu.txt", 'r') as f: 
        mots = f.readlines()
        choix_mot = random.choice(mots).strip()

        return choix_mot



def initial():
    #global mot_aleatoire
    mot_aleatoire = choisir_mot()  
    mystere=" "
    i=0
    
    while i<len(mot_aleatoire) :
       
        mystere+=" _ "
        i+=1
    #print(mot_aleatoire)
    #print(len(mot_aleatoire))
   # print(mystere)
    return mystere

def message_perdu():
    perdu=["Mince...cette lettre n'est pas dans le mot","Dommage cette lettre n'est pas dans le mot","C'est loupé pour cette fois, cette lettre n'est pas dans le mot"]
    message=random.choice(perdu)
    
    return message

def message_gagne():
    gagne=["Bien joué !","Woow une de plus","Bravo","Super !!"]
    message=random.choice(gagne)
    return message

def pendu ():
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
        if lettre in alphabet:
            
            if lettre in lettre_essaye :
                print("\n !! Vous avez déjà tenté cette lettre, essayez-en une autre !!")
                
            elif lettre in mot_aleatoire:
                print("\n>>>>>>>", message_gagne())
                lettres_trouvees+=lettre
                for x in mot_aleatoire:
                    if x in lettres_trouvees :
                        affichage +=  x
                    else :
                        affichage+=" _ "
                #print(affichage)
                mot=affichage  
                if "_" not in affichage :
                    vies=0
                    print("\n C'est gagné !! Le mot est : ", mot_aleatoire)
                
            else:
                lettre_essaye+=lettre
                vies = vies -1
                print(affichage)
                print(">>>>>>>", message_perdu())
                print("\n Il vous reste ", vies, "tentatives")
                if vies==0:
                    print ("\n   >>>>  Oh non... C'est perdu...  <<<<\n")
                    print("      =>  Le mot à deviner était : ", mot_aleatoire)
       
        else:
            print("\n >>>> Saisie incorrect. Veuillez entrer une lettre <<<<<< \n")
            
       
            
    return affichage
        
        










