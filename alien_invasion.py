import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = self.settings.bg_color
        self.ship = Ship(self)

    def run_game(self):
        #게임의 메인루프 시작
        while True:
            self._check_evnets()
            self._update_screen()


    def _check_evnets(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("exit")
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()