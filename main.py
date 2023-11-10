import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("The best game ever")

x_coordinate = 400
y_coordinate = 400

running = True
while running == True:
    for event in pygame.event.get():
        pygame.draw.rect(screen, (255, 255, 255), (x_coordinate, y_coordinate, 50, 50))

    button = pygame.key.get_pressed()

    print(x_coordinate, y_coordinate)
    if button[pygame.K_LEFT]:
        x_coordinate -= 0.5

    if button[pygame.K_RIGHT]:
        x_coordinate += 0.5

    if button[pygame.K_UP]:
        y_coordinate -= 0.5

    if button[pygame.K_DOWN]:
        y_coordinate += 0.5

    pygame.display.flip()
