import pygame
import sys

class Engine2D: # Класс для движка 2D
    def __init__(self, width, height): # Инициализация холста
        self.width = width
        self.height = height
        self.canvas = pygame.display.set_mode((self.width, self.height))
        self.figures = []  # Список для хранения фигур
        self.color = (255, 255, 255)  # Начальный цвет для отрисовки (белый)

    def change_color(self, color):
        self.color = color  # Метод для изменения цвета отрисовки

    def add_figure(self, figure):
        self.figures.append(figure)  # Метод для добавления фигуры на холст

    def draw(self):
        for figure in self.figures:
            figure.draw(self.canvas, self.color)  # Отрисовка всех фигур
        self.figures = []  # Очистка списка фигур после отрисовки

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, canvas, color):
        pygame.draw.circle(canvas, color, (self.x, self.y), self.radius)
        print(f"Drawing Circle at ({self.x}, {self.y}) with radius {self.radius} in color {color}")

class Triangle:
    def __init__(self, points):
        self.points = points  # Предполагается, что points содержит координаты точек треугольника

    def draw(self, canvas, color):
        pygame.draw.polygon(canvas, color, self.points)
        print(f"Drawing Triangle with points {self.points} in color {color}")

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, canvas, color):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(canvas, color, rect)
        print(f"Drawing Rectangle at ({self.x}, {self.y}) with width {self.width}, height {self.height} in color {color}")

# Инициализация Pygame
pygame.init()
clock = pygame.time.Clock()

# Создание объекта движка
engine = Engine2D(800, 600)

# Добавление фигур на холст
circle = Circle(200, 100, 50)
triangle = Triangle([(400, 50), (450, 150), (350, 150)])
rectangle = Rectangle(550, 50, 100, 100)

engine.add_figure(circle)
engine.add_figure(triangle)
engine.add_figure(rectangle)

# Изменение цвета отрисовки
engine.change_color((26, 115, 232))  # Голубой цвет

# Отрисовка фигур на холсте и очистка списка фигур
engine.draw()

# Основной игровой цикл Pygame
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
