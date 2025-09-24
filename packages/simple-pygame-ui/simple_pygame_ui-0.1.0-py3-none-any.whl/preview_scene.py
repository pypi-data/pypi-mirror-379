import pygame

import scene_handler
from better_math import Vector2i
from elements.py_button import Button, ToggleButton
from pygame_scene import PyGameScene
from elements.text import Text, TextEdit, UnderlinedTextEdit
from elements.texture import Texture


class PreviewScene(PyGameScene):
    def update(self):
        super().update()
        self.drawables.append(Text("This is a Text","arial",pygame.Rect(scene_handler.camera_size.x // 2,60,0,40)))
        button_rect = pygame.Rect(0,120,250,50)
        button_rect.centerx = scene_handler.camera_size.x // 2
        self.drawables.append(Button("This is a Button",(scene_handler.camera_size.x // 2, 130),(250,40),pygame.font.SysFont("arial",16),lambda: print("You Clicked A Button")))
        self.drawables.append(ToggleButton("Test",(scene_handler.camera_size.x // 2, 130),(0,0),pygame.font.SysFont("arial",16),lambda new_value: print("You Toggled A Button"),text_color=(0,0,0)))
        self.drawables.append(TextEdit("","Enter Text:","arial",pygame.Rect(scene_handler.camera_size.x // 2 - 125,200,250,40)))
        self.drawables.append(UnderlinedTextEdit("",6,"arial",Vector2i(scene_handler.camera_size.x // 2,260), centered=True,skip=[2]))
        self.drawables.append(Texture("textures/test.png",pygame.Rect(0,0,128,128),texture_size=Vector2i(16,16)))

    def render(self, screen, events) -> bool:
        pygame.draw.rect(screen,(255,255,255),(0,0,scene_handler.camera_size.x,scene_handler.camera_size.y))
        super().render(screen,events)
        return True