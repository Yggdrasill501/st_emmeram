# -*- conding: utf-8 -*-
"""Module for the music player."""
import pygame


class MusicPlayer:
    """Class for the music player."""

    def __init__(self, music_file):
        """Initialize the music player."""
        self.music_file = music_file
        self.is_playing = False
        pygame.mixer.init()
        pygame.mixer.music.load(self.music_file)

    def toggle_music(self):
        if self.is_playing:
          pygame.mixer.music.pause()
        else:
            pygame.mixer.music.play(-1)
        self.is_playing = not self.is_playing