import pygame
import sys

#Pygame setup
pygame.init()
screenWidth = 1000
screenHight = 1000
screen = pygame.display.set_mode((screenWidth, screenHight))
clock = pygame.time.Clock()
icon = pygame.image.load("Matriels/GameIcon.png")
pygame.display.set_caption("Wordle")
pygame.display.set_icon(icon)
screenIsRunning = True

#Global variables
textFont = pygame.font.SysFont("Matriels/TiltWarp.ttf", 100)
xCordinates = 300
yCordinates = [i for i in range(50, 50 + (100 * 6), 100)]
yIndex = 0
userTexts = []
userText = ''

#Functions
def is_valid_char(key):
    return pygame.K_a <= key <= pygame.K_z

def draw_text(text, font, textColor, x, y):
    img = font.render(text, True, textColor)
    screen.blit(img, (x, y))


#Main function

##Main game loop
while screenIsRunning:
    ###Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            screenIsRunning = False
        
        elif event.type == pygame.KEYDOWN:
            if is_valid_char(event.key) and len(userText) < 5:
                userText += chr(event.key)

            elif event.key == pygame.K_BACKSPACE:
                userText = userText[:-1]
                
            elif event.key == pygame.K_RETURN:
                userTexts.append(userText)
                userText = userText[: 0]
                yIndex += 1
                yIndex %= 6

    
    screen.fill((255, 255, 255))
    
    

    for i, line in enumerate(userTexts):
        draw_text(line.upper(), textFont, (0, 0, 0), xCordinates, yCordinates[i])
    draw_text(userText.upper(), textFont, (0, 0, 0), xCordinates, yCordinates[yIndex])

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()