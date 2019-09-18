import pygame, random, time
pygame.init(); screen = pygame.display.set_mode((885, 350)); centres = [None, (440, 175), (440, 175)]
while True:
    colour = random.choice(list(pygame.colordict.THECOLORS.values()))
    # centres = [centres[2]] + [(colour[0] * 2 + random.randint(0, 360), colour[1] + random.randint(0, 80)) for _ in range(2)]
    centres = centres[1:] + [(random.randint(0, 885), random.randint(0, 350))]
    pygame.draw.polygon(screen, random.choice(list(pygame.colordict.THECOLORS.values())), centres, 4)
    # for centre in centres:
    pygame.draw.circle(screen, colour, centres[0], 10)
    pygame.display.flip()
    time.sleep(1)
    screen.fill((25, 25, 25), None, pygame.BLEND_SUB)
