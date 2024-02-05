import pygame
import src.st_emmeram.inventory.inventory
import src.st_emmeram.health_bar.health_bar
from src.st_emmeram.menu.menu import Menu
import sys


class GameLoop(Menu):

    def __init__(self):
        pygame.init()

        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)

        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Saint Emmeram's Dungeon")

        # game variables
        self.game_paused = False
        self.menu_state = "main"
        self.font = pygame.font.SysFont("arialblack", 40)
        self.TEXT_COL = (255, 255, 255)
        super().__init__()

    def draw_text(self,text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    def game_loop(self):
        running = True
        while running:
            # check if game is paused
            if self.game_paused:
                # check menu state
                if self.menu_state == "main":
                    # draw pause screen buttons
                    if self.resume_button.draw():
                        game_paused = False
                    if self.options_button.draw():
                        menu_state = "options"
                    if self.quit_button.draw():
                        run = False
                # check if the options menu is open
                if self.menu_state == "options":
                    # draw the different options buttons
                    if self.video_button.draw():
                        print("Video Settings")
                    if self.audio_button.draw():
                        print("Audio Settings")
                    if self.keys_button.draw():
                        print("Change Key Bindings")
                    if self.back_button.draw():
                        menu_state = "main"
            else:
                self.draw_text("Press SPACE to pause",self.font, self.TEXT_COL, 160, 250)

                # Render health bar
                # Render Inventory

                # Render Map

                # Render Player

                # if player enters room,
                    # render monster
                    # Combat

            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_paused = True
                if event.type == pygame.QUIT:
                    running = False

        pygame.display.update()

        pygame.quit()
        sys.exit()
