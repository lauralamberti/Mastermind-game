from random import choice
from modulo_mastermind import *
from modulo_grafica import *
import pygame
from pygame.locals import *




# apertura del file di output
scrivo=("master_out.txt",'w')
#inizializzazione delle variabili
n_neri=0
n_bianchi=0
play=1
elimino=[]
prova=[0]*1296
N_colours=6
colours = ["V","R","G","B","A","L"]   
# costruisco la lista con tutte le disposizioni
#costruisci(N_colours)
#risposte=[[0 for i in range(10)] for k in range(10)]
conta_tentativi=1



#inizio del gioco del computer
################################################


while( play==1):
   
    win=False

    
    # costruisco la lista con tutte le disposizioni
    prova=costruisci(N_colours)        #prova[] è la lista di tutte le disposizioni possibili: sono N_colours^4
    #richiesta di inserimento del codice segreto nostro
    #inserisco tramite l'interfaccia grafica il codice che il pc deve indovinare 
    codice=tabellone(conta_tentativi)   
    codice=codice.upper()
    codice=list(codice)                 #codice[] è il codice segreto
    while not win :
        if (conta_tentativi==1):
            #la strategia migliore sembrerebbe essere quella di partire con due colori
            # primo tentativo:
            tentativo=["V", "V", "R", "R"] 
        else: 
            tentativo=choice(prova)

        # il tentativo viene stampato sul tabellone insieme alle risposte e alla riduzione delle disposizioni possibili
    
        mostra_tentativo(tentativo, conta_tentativi)
        n_neri=confronta(tentativo, codice)[0]
        n_bianchi=confronta(tentativo, codice)[1]
        mostra_risposte(n_neri, n_bianchi, conta_tentativi)
        pulisci(prova, tentativo, codice)
        mostra_disp(len(prova), conta_tentativi)
       #domanda=input("che cosa vuoi fare adesso?")
        # controllo se ha indovinato
        win=verifica(n_neri)    
                        # if ( conta_tentativi>10) :
                        #     print("Hai superato il numero di tentativi consentivi", conta_tentativi)
                        #     win=True
        conta_tentativi+=1
        
    play=ancora()[0]
    #print("play=",play)
    if play==1:
        conta_tentativi=ancora()[1]
        win=False
        
                
    else:
        win=True
        print("fine")   

pygame.quit()
         
    
 
