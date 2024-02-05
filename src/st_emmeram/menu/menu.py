import pygame
from src.st_emmeram.menu.button import Button


class Menu:
  def __init__(self):
      resume_img = pygame.image.load("src/assets/menu/button_resume.png").convert_alpha()
      options_img = pygame.image.load("src/assets/menu/button_options.png").convert_alpha()
      quit_img = pygame.image.load("src/assets/menu/button_quit.png").convert_alpha()
      video_img = pygame.image.load('src/assets/menu/button_video.png').convert_alpha()
      audio_img = pygame.image.load('src/assets/menu/button_audio.png').convert_alpha()
      keys_img = pygame.image.load('src/assets/menu/button_keys.png').convert_alpha()
      back_img = pygame.image.load('src/assets/menu/button_back.png').convert_alpha()

      self.resume_button = Button(304, 125, resume_img, 1)
      self.options_button = Button(297, 250, options_img, 1)
      self.quit_button = Button(336, 375, quit_img, 1)
      self.video_button = Button(226, 75, video_img, 1)
      self.audio_button = Button(225, 200, audio_img, 1)
      self.keys_button = Button(246, 325, keys_img, 1)
      self.back_button = Button(332, 450, back_img, 1)
