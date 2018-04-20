import pygame
from controller import Controller
import constants

if __name__ == "__main__":
    pygame.init()

    pygame.mixer.music.load('muz.mp3')
    pygame.mixer.music.play()

    controller = Controller()
    screen_width = 672
    screen_height = 672
    black = 255, 0, 255
    screen = pygame.display.set_mode([ screen_width , screen_height ])


    running = 1

    while running:
        time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                controller.handle_mouseclick()

        screen.fill(black)
        controller.draw(screen)
        pygame.display.flip()
        pygame.display.set_caption("Добро пожаловать в мир шахмат")

        elapsed_time = pygame.time.get_ticks() - time
        if elapsed_time < 1000/30:
            pygame.time.wait(int(1000/30-elapsed_time))