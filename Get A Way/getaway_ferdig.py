# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 11:41:36 2018

@author: Eier
"""

#Importerer:
import pygame #pygame selve programmet
import pyganim #pyganim som brukes til animasjonen av figuren
import time #time som hånterer tiden
import random #random som velger tilfeldige tall

pygame.init() #Setter igang pygame

#Henter lyder
pygame.mixer.music.load("musikk.wav")
poeng_lyd = pygame.mixer.Sound("poeng.wav") 
levelup_lyd = pygame.mixer.Sound("levelup.wav")
tap_lyd = pygame.mixer.Sound("tap.wav")

#Bestemmer størrelsen på spillvinduet
vinduBredde = 800 
vinduHoyde = 600

#Definerer farger
svart = (0,0,0) 
hvit = (255,255,255)
rod=(255,0,0)
gronn=(0,255,0)
blaa=(0,0,255)

#Viser spillvinduet med tittel
spillVindu = pygame.display.set_mode((vinduBredde,vinduHoyde))
pygame.display.set_caption("Get a way") #tittelen til spillet som skrives øvers på vinduet

klokke = pygame.time.Clock() #klokken til spillet som tar tiden
      
#Henter bilder som skal vises på skjermen
figur1Bilde = pygame.image.load("figur1.png") #figuren når den står i ro
figur2Bilde = pygame.image.load("figur2.png") #figuren når den går
myntBilde = pygame.image.load("mynt.png")
steinBilde = pygame.image.load("stein.png")
bgIntroBilde = pygame.image.load("bg_intro.png")
bgBilde = pygame.image.load("bg.png")

animasjon = pyganim.PygAnimation([(figur1Bilde,80),(figur2Bilde,80)]) #beskrivelse av animasjonen til figuren
fig_gaar=0
krav = 0

#Definisjoner
def poengsum(count): 
    global krav
    font = pygame.font.SysFont(None, 25) #skrifttypen til teksten som viser poengsummen
    tekst = font.render("Mynter: " + str(count) + "/" + str(krav), True, svart) #teksten som viser poengsummen
    spillVindu.blit(tekst,(0, 0)) #viser teksten på skjermen

def figur(x,y,fig_gaar):
    if fig_gaar==1:
        animasjon.blit(spillVindu,(x,y)) #Viser figuren med animasjon (når den beveger seg)
    else:
        spillVindu.blit(figur1Bilde,(x,y)) #Viser figuren uten animasjon (når den står i ro)
    #Lager rektangler som brukes for kolisjon mellom objekter
    global fig_hode_rect
    global fig_kropp_rect
    fig_hode_rect=pygame.Rect((x+18,y),(30,40))
    fig_kropp_rect=pygame.Rect((x,y+40),(68,40))
    
def stein(steinx,steiny):
    spillVindu.blit(steinBilde,(steinx,steiny)) #viser steinen på skjermen
    #Lager et rektangl som brukes for kolisjon mellom objekter
    global steinrect
    steinrect=pygame.Rect((steinx,steiny),(100,50))

def mynt(myntx,mynty): 
    spillVindu.blit(myntBilde,(myntx,mynty)) #viser mynten på skjermen
    #Lager et rektangl som brukes for kolisjon mellom objekter
    global myntrect
    myntrect=pygame.Rect((myntx,mynty),(32,40))
    
def bakgrunnIntro(bakgrunnIntrox,bakgrunnIntroy): 
    spillVindu.blit(bgIntroBilde,(bakgrunnIntrox,bakgrunnIntroy)) #viser bakgrunnen på skjermen
    
def bakgrunn(bakgrunnx,bakgrunny): 
    spillVindu.blit(bgBilde,(bakgrunnx,bakgrunny)) #viser bakgrunnen på skjermen

#De fire neste definisjonene beskriver hvordan teksten skal se ut og hvor den skal plaseres
def tekstObjekt(tekst, font): 
    tekstOverflate = font.render(tekst, True, svart)
    return tekstOverflate, tekstOverflate.get_rect()
    
def melding(tekst):
    storTekst = pygame.font.Font("freesansbold.ttf",115)
    tekstOverflate, tekstBoks = tekstObjekt(tekst, storTekst)
    tekstBoks.center = ((vinduBredde/2),(vinduHoyde/3))
    spillVindu.blit(tekstOverflate, tekstBoks)
    
    pygame.display.update()  
    
def tekst1(tekst):
    storTekst = pygame.font.Font("freesansbold.ttf",30)
    tekstOverflate, tekstBoks = tekstObjekt(tekst, storTekst)
    tekstBoks.center = ((vinduBredde/2),(vinduHoyde-vinduHoyde/2))
    spillVindu.blit(tekstOverflate, tekstBoks)
    
    pygame.display.update()  

def tekst2(tekst):
    storTekst = pygame.font.Font("freesansbold.ttf",30)
    tekstOverflate, tekstBoks = tekstObjekt(tekst, storTekst)
    tekstBoks.center = ((vinduBredde/2),(vinduHoyde-(vinduHoyde/2-40)))
    spillVindu.blit(tekstOverflate, tekstBoks)
    
    pygame.display.update() 
    
def tap(): 
    melding("Game over!") #skriver ut "Game over!" på skjermen

def spill_intro(): #Det som skal vises i det man starter spillet
    intro = True 
    
    pygame.mixer.music.play(-1) #spiller av musikken i loop
    
    #Bestemmer koordinatene til figuren
    x = (vinduBredde * 0.45) 
    y = (vinduHoyde * 0.8)
    
    #Funksjon for knapper
    while intro == True: #så lenge intro er true skal dette skje
        for event in pygame.event.get(): #Henter event som skjer
            if event.type == pygame.QUIT: #Om spilleren krysser ut vinduet skal dette skje
                #Slutter programmet
                pygame.quit() 
                quit() 
            
            if event.type == pygame.KEYDOWN: #Om spilleren trykker ned en tast skal dette skje
                if event.key == pygame.K_w: #Om tast W er trykket skal dette skje
                    intro = False #Setter intro lik false for å hoppe ut av while løkken
                if event.key == pygame.K_q: #Om tasten Q et trykket skal dette skje
                    #Avslutter spillet
                    pygame.quit() 
                    quit() 
                if event.key == pygame.K_e: #Om tasten E er trykket skal dette skje
                    pause() #Starter pause funksjonen
                    intro = False #Setter intro lik false for å hoppe ut av while løkken
        
        #Plaserer bilder og tekst på skjermen
        bakgrunnIntro(0,0)
        figur(x,y,fig_gaar)
        melding("Get a way")
        
        #Oppdaterer hva som skjer på skjermen
        pygame.display.update()
        klokke.tick(15)
        
    spillLokke() #Setter igang spillLokke for å starte spillet
        
def pause(): #Det som skla vises når man har trykket på pauseknappen (lik spill_intro)
    pause = True 
    
    pygame.mixer.music.pause() #Stopper musikken
    
    #Registrering av knapper for å fortsette og avslutte spillet
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    pause = False
                    pygame.mixer.music.unpause()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        
        #Viser bilder og tekst på skjermen
        bakgrunn(0,0)
        tekst1("Press W to continue the game")
        tekst2("Press Q to quit the game")
        melding("Paused")
        pygame.display.update()
        klokke.tick(15)

def spillLokke(): #Løkken for selve spillet
    
    #Variabler
    x = (vinduBredde * 0.45)
    y = (vinduHoyde * 0.8)
    
    figurBredde = 68
    
    bakgrunnx = 0
    bakgrunny = 0
    
    stein_startx = random.randrange(0, vinduBredde)
    stein_starty = -600
    stein_fart = 20
    stein_bredde = 100
    stein_hoyde = 50
    
    mynt_startx = random.randrange(0, vinduBredde)
    mynt_starty = -600
    mynt_fart = 15
    mynt_bredde = 32
    mynt_hoyde = 40
    
    poeng = 0
    global krav
    niva = 1
       
    xForandring = 0
    fig_gaar=0 
    
    spillSlutt = False
    
    while not spillSlutt: #Så lenge spillslutt ikke er lik true skal dette skje
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                #Registrering av knapper som beveger figuren
                if event.key == pygame.K_LEFT and x > 20:
                    xForandring = -10 #Flytter figuren 10 piksler mot venstre
                    animasjon.play() #Starter animasjonen til figuren
                    fig_gaar=1 #Endrer variabelen til 1 for å starte animasjonen
                if event.key == pygame.K_RIGHT and x < vinduBredde-figurBredde:
                    xForandring = 10 #Flytter figuren 10 piksler til høyre
                    fig_gaar=1 #Endrer variabelen til 1 for å starte animasjonen
                
                #Registrering av knapper som pauser og slutter spillet
                if event.key == pygame.K_q:
                    pygame.quit() 
                    quit()
                if event.key == pygame.K_e:
                    pause()
                    
            if event.type == pygame.KEYUP: #Når spilleren slipper en knapp skal dette skje
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xForandring = 0 #Stopper figuren slik at den står i ro
                    fig_gaar=0 #Endrer variabelen til 0 for å stoppe animasjonen
                    

        x += xForandring #Endrer x med tanke på xForandring slik at figuren flytter seg
        
        #Viser bilder på skjermen
        bakgrunn(bakgrunnx,bakgrunny)
        stein(stein_startx, stein_starty)
        stein_starty += stein_fart
        mynt(mynt_startx,mynt_starty)
        mynt_starty += mynt_fart
        poengsum(poeng)
        
        #Viser figuren med eller uten animasjon
        figur(x,y,fig_gaar)
        
        if x <= 0 or x >= vinduBredde-figurBredde:
            xForandring = 0
        
        #Får steinen til å komme på nytt i det den kommer ut av spillvinduet
        if stein_starty > vinduHoyde:
            stein_starty = 0 - stein_hoyde #Starter rett over spillvinduet
            stein_startx = random.randrange(0, vinduBredde-stein_bredde) #En tilfeldig plass langs x-retningen
        
        #Når steinen treffer figuren
        if fig_hode_rect.colliderect(steinrect)==True or fig_kropp_rect.colliderect(steinrect)==True:
             pygame.mixer.music.pause() 
             pygame.mixer.Sound.play(tap_lyd) 
             krav = 0
             tap() #Viser en melding om at du har tapt
             spill_intro()

        
        #Får mynten til å komme på nytt i det den kommer ut av spillvinduet
        if mynt_starty > vinduHoyde:
            mynt_starty = 0 - mynt_hoyde
            mynt_startx = random.randrange(0, vinduBredde-mynt_bredde)
        
        #Når spilleren fanger en mynt
        if fig_hode_rect.colliderect(myntrect)==True or fig_kropp_rect.colliderect(myntrect)==True:
            pygame.mixer.music.pause() 
            pygame.mixer.Sound.play(poeng_lyd)
            pygame.mixer.music.unpause()
            poeng += 1 #Spilleren får et poeng
            mynt_starty = vinduHoyde
                
        #Øker level
        if poeng == krav:
            #Øker farten til mynten og steinen
            poeng += 1
            stein_fart += 1
            mynt_fart += 1
            krav += 10 #Øker kravet
            pygame.mixer.music.pause()
            pygame.mixer.Sound.play(levelup_lyd)
            melding("Level " + str(niva)) #Skriver hvilket level man er på
            time.sleep(1)
            niva += 1 
            poeng = 0 #Setter poengene tilbake til 0
            pygame.mixer.music.unpause()
        
        pygame.display.update() #Oppdaterer displayet
        klokke.tick(60) #Antall fps
 
spill_intro() #Starter spillIntro
#Slutter programmet
pygame.quit() 
quit() 