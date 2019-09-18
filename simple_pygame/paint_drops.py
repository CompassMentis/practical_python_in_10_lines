import pygame, random, time
pygame.init()
screen = pygame.display.set_mode((768, 512))
while True:
    colour = random.choice(list(pygame.colordict.THECOLORS.values()))
    for _ in range(15):
        centre = colour[0] * 3 + random.randint(-150, 150), colour[1] + random.randint(-100, 100)
        pygame.draw.circle(screen, colour, centre, random.randint(5, 20))
        pygame.display.flip()
        time.sleep(0.1)
