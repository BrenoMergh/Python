#Utilizando a biblioteca pygame(necessita instalar a biblioteca)
import pygame
#pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

#maneira mais simples e rápida de executar (necessita instalar a biblioteca)
'''from playsound import playsound
playsound('ex021.mp3')'''

#abre o reprodutor de som padrão do sistema
'''from webbrowser import open
open('ex021.mp3')'''