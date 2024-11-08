import pygame

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

white = (255, 255, 255)
screen.fill(white)
    
rect_width = 100
rect_height = 50

rect_x = screen_width // 2 - rect_width // 2
rect_y = screen_height // 2 - rect_height // 2

rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

color = (255, 0, 0)
pygame.draw.rect(screen, color, rect)

text = pygame.font.Font(None, 36).render('Welcome ;)', True, pygame.Color('black'))
text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 + 110))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False    
 
    screen.blit(text, text_rect)   
    pygame.display.flip()
    
pygame.quit()