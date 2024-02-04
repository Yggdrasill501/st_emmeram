# -*- coding: utf-8 -*-
"""Module for the menu."""
import pygame


class Menu:
    """Class with the menu."""

    def __init__(self, screen, music_player):
        """Initialize the menu."""
        self.screen = screen
        self.running = True

        button_size = (200, 100)

        self.start_button_image = pygame.transform.scale(pygame.image.load('assets/menu/start_logo.png'), button_size)
        self.start_button_rect = self.start_button_image.get_rect()

        self.start_button_rect.center = (screen.get_width() // 2, screen.get_height() // 2)

        self.music_player = music_player
        self.music_toggle_button = pygame.Rect(100, 200, 200, 50)

    def draw(self):
        """Draw the menu."""
        self.screen.blit(self.start_button_image, self.start_button_rect)

        pygame.draw.rect(self.screen, (0, 0, 128), self.music_toggle_button)  # Draw a blue button
        font = pygame.font.Font(None, 36)
        text = font.render('Toggle Music', True, (255, 255, 255))
        text_rect = text.get_rect(center=self.music_toggle_button.center)
        self.screen.blit(text, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_button_rect.collidepoint(event.pos):
                self.running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.music_toggle_button.collidepoint(event.pos):
                self.music_player.toggle_music()

    def is_running(self):
        return self.running
