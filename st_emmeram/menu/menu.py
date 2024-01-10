# -*- coding: utf-8 -*-
"""Module for the menu."""
import pygame


class Menu:
    """Class with the menu."""

    def __init__(self, screen):
        """Initialize the menu."""
        self.screen = screen
        self.running = True
        self.start_button = pygame.Rect(100, 100, 200, 50)

    def draw(self):
        """Draw the menu."""
        pygame.draw.rect(self.screen, (0, 128, 0), self.start_button)  # Draw a green button
        font = pygame.font.Font(None, 36)
        text = font.render('Start Game', True, (255, 255, 255))
        text_rect = text.get_rect(center=self.start_button.center)
        self.screen.blit(text, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_button.collidepoint(event.pos):
                self.running = False

    def is_running(self):
        return self.running
