import pygame

BACKGROUND = 'game/images/ramin.jpg'
BOARD_SIZE = (820, 820)
BLACK = (0, 0, 0)


def get_rbg(color):
    if color == 'WHITE':
        return 255, 255, 255
    elif color == 'BLACK':
        return 0, 0, 0
    else:
        return 0, 133, 211


def coords(point):
   
    return 5 + point[0] * 40, 5 + point[1] * 40


def leftup_corner(point):
    return -15 + point[0] * 40, -15 + point[1] * 40


class UI:
    def __init__(self):
       
        self.outline = pygame.Rect(45, 45, 720, 720)
        self.screen = None
        self.background = None

    def initialize(self):
        
      
        pygame.init()
        pygame.display.set_caption('Goban')
        self.screen = pygame.display.set_mode(BOARD_SIZE, 0, 32)
        self.background = pygame.image.load(BACKGROUND).convert()

        pygame.draw.rect(self.background, BLACK, self.outline, 3)
       
        self.outline.inflate_ip(20, 20)
        for i in range(18):
            for j in range(18):
                rect = pygame.Rect(45 + (40 * i), 45 + (40 * j), 40, 40)
                pygame.draw.rect(self.background, BLACK, rect, 1)
        for i in range(3):
            for j in range(3):
                coords = (165 + (240 * i), 165 + (240 * j))
                pygame.draw.circle(self.background, BLACK, coords, 5, 0)
        self.screen.blit(self.background, (0, 0))
        pygame.display.update()

    def draw(self, point, color, size=20):
        color = get_rbg(color)
        pygame.draw.circle(self.screen, color, coords(point), size, 0)
        pygame.display.update()

    def remove(self, point):
        blit_coords = leftup_corner(point)
        area_rect = pygame.Rect(blit_coords, (40, 40))
        self.screen.blit(self.background, blit_coords, area_rect)
        pygame.display.update()

    def save_image(self, path_to_save):
        pygame.image.save(self.screen, path_to_save)
