import pygame as py

class Button(py.sprite.Sprite):
    def __init__(self, button_width, button_height, button_x, button_y, text_button, screen):
        super().__init__()
        # Определение размеров и положения кнопки
        self.button_width = button_width
        self.button_height = button_height
        self.button_x = button_x
        self.button_y = button_y
        self.text_button = text_button
        self.button_pressed = False
        self.screen = screen

    # Функция для отображения кнопки
    def update(self):
        red = (255, 0, 0)
        white = (255, 255, 255)

        if self.button_pressed:
            py.draw.rect(self.screen, red, (self.button_x, self.button_y,
                                            self.button_width, self.button_height))
        else:
            py.draw.rect(self.screen, white, (self.button_x, self.button_y,
                                              self.button_width, self.button_height))

        font = py.font.Font(None, 36)
        text = font.render(self.text_button, True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.button_x + self.button_width // 2, 
                                          self.button_y + self.button_height // 2))
        self.screen.blit(text, text_rect)