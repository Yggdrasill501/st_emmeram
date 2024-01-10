# -*- coding: utf-8 -*-
"""Module for the menu."""
import pygame


class Menu:
    """Class with the menu."""

    def __init__(self, screen):
        """Initialize the menu."""
        self.screen = screen
        self.running = True

        button_size = (200, 100)

        self.start_button_image = pygame.transform.scale(pygame.image.load('assets/menu/start_logo.png'), button_size)
        self.start_button_rect = self.start_button_image.get_rect()

        self.start_button_rect.center = (screen.get_width() // 2, screen.get_height() // 2)

    def draw(self):
        """Draw the menu."""
        self.screen.blit(self.start_button_image, self.start_button_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_button_rect.collidepoint(event.pos):
                self.running = False

    def is_running(self):
        return self.running
