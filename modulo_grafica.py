import pygame
from pygame.locals import *
from modulo_mastermind import *



def tabellone(conta_tentativi):

    global surf_tentativi, screen, surf_risposte, surf_statistiche, rr
    global red, yellow, green, blue, orange, purple
    rr=1
    color_pallino=(0,0,0)
    red=(255, 0, 0)
    green=(0,255, 0)
    yellow= (250,200,50)
    orange=(255,130,0)
    blue=(0,20,255)
    purple=(170,20,255)
    pink=(255, 209, 220)
    black=(45, 45, 255)
    white=(255,255,255)
    pygame.init()
    screen = pygame.display.set_mode((1000, 800+100*rr))
    screen.fill(pink)

    # SUPERFICIE titolo
    surf_gamename = pygame.Surface((550, 50))
    surf_gamename.fill((214, 204, 255))
    fnt = pygame.font.SysFont("Georgia Pro Black", 30)
    gamename= fnt.render("MASTERMIND - REVERSE", True, (100, 36, 255))
    surf_gamename.blit(gamename,(10,10))

    #SUPERFICIE  prova
    surf_prova = pygame.Surface((300, 50))
    surf_prova.fill((191, 235, 255))
    fnt = pygame.font.SysFont("Georgia Pro Black", 25)
    prova_txt0 = fnt.render("Codice=", True, (45, 45, 255))
    surf_prova.blit(prova_txt0, (10,10))

    #SUPERFICIE  prova_grafica
    surf_prova_g = pygame.Surface((300, 50))
    surf_prova_g.fill((191, 235, 255))
    
    



    #SUPERFICIE tentativi
    surf_tentativi = pygame.Surface((300, 500+100*rr))
    surf_tentativi.fill((255, 242, 178))
    surf_text_tentativo = fnt.render("Tentativi", True, (0, 0, 0))
    surf_tentativi.blit(surf_text_tentativo, (100,20))

    #SUPERFICIE risposte
    surf_risposte = pygame.Surface((300, 500+100*rr))
    surf_risposte.fill((155, 142, 78))
    surf_text_risposta = fnt.render("Risposte", True, (0, 0, 0))
    surf_risposte.blit(surf_text_risposta, (100,20))

    #SUPERFICIE statistiche
    surf_statistiche = pygame.Surface((100, 500+100*rr))
    surf_statistiche.fill((255, 242, 178))
    fnt_disp = pygame.font.SysFont("Georgia Pro Black", 15)
    surf_text_statistiche = fnt_disp.render("Disp.", True, (0, 0, 0))
    surf_statistiche.blit(surf_text_statistiche, (25,20))

   #SUPERFICIE pallini
    surf_pallini = pygame.Surface((50, 500+100*rr))
    surf_pallini.fill((255, 242, 178))
    pygame.draw.circle(surf_pallini, (255, 0, 0), (25, 40 ),  20)
    pygame.draw.circle(surf_pallini, (0, 255, 0), (25, 100+ 0),  20)
    pygame.draw.circle(surf_pallini, (0,20,255), (25, 160+ 0),  20)
    pygame.draw.circle(surf_pallini, (250,200,50), (25, 220+ 0),  20)
    pygame.draw.circle(surf_pallini, (255,130,0), (25, 280+ 0),  20)
    pygame.draw.circle(surf_pallini, (170,20,255), (25, 340+ 0),  20)
    lettera_r=fnt.render("r", True, (0, 0, 0))
    surf_pallini.blit(lettera_r, (20,20))
    lettera_g=fnt.render("v", True, (0, 0, 0))
    surf_pallini.blit(lettera_g, (20,80))
    lettera_b=fnt.render("b", True, (0, 0, 0))
    surf_pallini.blit(lettera_b, (20,140))
    lettera_y=fnt.render("g", True, (0, 0, 0))
    surf_pallini.blit(lettera_y, (20,200))
    lettera_o=fnt.render("a", True, (0, 0, 0))
    surf_pallini.blit(lettera_o, (20,260))
    lettera_p=fnt.render("l", True, (0, 0, 0))
    surf_pallini.blit(lettera_p, (20,320))

    #SUPERFICIE bottone gioca di nuovo
    surf_bottone = pygame.Surface((150, 50))
    surf_bottone.fill((191, 235, 255))
    fnt = pygame.font.SysFont("Georgia Pro Black", 15)
    bottone_txt0 = fnt.render("di nuovo?", True, (45, 45, 255))
    surf_bottone.blit(bottone_txt0, (10,10))

    # disegniamo surf sulla superficie principale
    screen.blit(surf_gamename, (50, 50))
    screen.blit(surf_prova, (650, 50))
    screen.blit(surf_prova_g, (650, 100))
    screen.blit(surf_pallini, (50, 150))
    screen.blit(surf_tentativi, (150, 150))
    screen.blit(surf_risposte, (500, 150))
    screen.blit(surf_statistiche, (850, 150))
    screen.blit(surf_bottone, (850, 650+100*rr))


    # aggiorniamo lo schermo
    pygame.display.flip()


    # inseriamo il testo da tastiera

    clk = pygame.time.Clock()


    # inizializziamo una stringa vuota e inseriamo il codice segreto da tastiera
    s = ""
    fnt = pygame.font.SysFont("Georgia Pro Black", 30)
    # ciclo principale
    done_txt = False
    K=conta_tentativi-1
    riga= 60*K + 100
    i=-1
    while not done_txt:
        # sottociclo degli eventi
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                done_txt = True
                screen.fill(white)
            else:
              if ev.type == pygame.K_BACKSPACE:           # se e' il backspace ...
                s = s[0:-1]            
              if ev.type == pygame.KEYDOWN:
                  if ev.key==pygame.K_RETURN:
                        done_txt=True
                    
                
                  else:
                      i+=1
                      s += ev.unicode
                                      
                      prova_txt= fnt.render(s, True, (0, 0, 0))
                      surf_prova.blit(prova_txt,(150,10))
                      screen.blit(surf_prova, (650, 50))
                      pygame.display.flip()
        
        list(s)
                      
    for i in range (0,4):
        print(i, s[i])
        if (s[i].upper()=="G"):
            color_pallino=yellow    
        if (s[i].upper()=="V"): 
            color_pallino=green   
        if (s[i].upper()=="B"):
            color_pallino=blue
        if (s[i].upper()=="A"):
            color_pallino=orange
        if (s[i].upper()=="L"):
            color_pallino=purple
        if (s[i].upper()=="R"):
            color_pallino=red
        pygame.draw.circle(surf_prova_g, color_pallino, (30+30*i, 10),  10)
    
    screen.blit(surf_prova_g,(650,100))
    pygame.display.flip()

    clk.tick(30)

    return s


###################################################################################

def mostra_tentativo (tentativo, conta_tentativi):
    
    K=conta_tentativi-1
    riga= 60*K + 100
    for i in range(0,4):
       cerchietti=tentativo[i]
       colonna= 100 + 50*i
       if cerchietti== "V":
            pygame.draw.circle(surf_tentativi, (0,225,0), (colonna, riga),  20)
       if cerchietti== "B":
            pygame.draw.circle(surf_tentativi, (0,20,255), (colonna, riga),  20)
       if cerchietti== "G":
            pygame.draw.circle(surf_tentativi, (250,200,50), (colonna, riga),  20)
       if cerchietti== "A":
            pygame.draw.circle(surf_tentativi, (255,130,0), (colonna, riga),  20)
       if cerchietti== "R":
            pygame.draw.circle(surf_tentativi, (255,0,0), (colonna, riga),  20)
       if cerchietti== "L":
            pygame.draw.circle(surf_tentativi, (170,20,255), (colonna, riga),  20)
    screen.blit(surf_tentativi, (150, 150))
    pygame.display.flip()
    return

##########################################################################################

    
def mostra_risposte (n_neri, n_bianchi, conta_tentativi):
    K=conta_tentativi-1
    riga= 60*K + 100
    colonna=100
    for i in range(0,n_neri):
            pygame.draw.circle(surf_risposte, (0,0,0), (colonna+ 20*i, riga),  10)
    for i in range(0, n_bianchi):
            pygame.draw.circle(surf_risposte, (255,255,255), (colonna+ 20*i+50, riga),  10)
    screen.blit(surf_risposte, (500, 150))
    pygame.display.flip()

    return
                
#################################################################################

def mostra_disp(rimanenti, conta_tentativi):
    K=conta_tentativi-1
    riga= 60*K + 100
    colonna=10
    fnt_disp = pygame.font.SysFont("Georgia Pro Black", 15)
    surf_text_disp = fnt_disp.render(str(rimanenti), True, (0, 0, 0))
    surf_statistiche.blit(surf_text_disp, (colonna ,riga))
        
    screen.blit(surf_statistiche, (850, 150))
    pygame.display.flip()

    return

##################################################################

def ancora():
    done_ancora=False
    clk = pygame.time.Clock()
    play=0
    #print("Play dentro ancora=", play)
    #conta_tentativi=1
    while not done_ancora:
        for ev in pygame.event.get(): 
                if pygame.mouse.get_pressed()[0]:
                    mx, my=pygame.mouse.get_pos()
                #print("******************", mx, my)
                    if ((mx > 850 and mx < 900+100*rr) and (my > 750 and my < 800)):
                        play=1
                        print("play dentro ancora", play)
                        conta_tentativi=1
                        done_ancora=1
        clk.tick(30)
    
    return play, conta_tentativi





