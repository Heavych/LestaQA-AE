import pygame  # Импорт библиотеки Pygame для работы с графикой
import sys  # Импорт модуля sys для выхода из программы

class Engine2D:  # Определение класса для движка 2D
    def __init__(self, width, height):  # Инициализация холста
        # Инициализация свойств: ширина, высота и создание холста с заданными параметрами
        self.width = width
        self.height = height
        self.canvas = pygame.display.set_mode((self.width, self.height))
        self.figures = []  # Список для хранения фигур
        self.color = (255, 255, 255)  # Начальный цвет для отрисовки (белый)

    def change_color(self, color):  # Метод для изменения цвета отрисовки
        self.color = color

    def add_figure(self, figure):  # Метод для добавления фигуры на холст
        self.figures.append(figure)

    def draw(self):  # Метод для отрисовки фигур на холсте
        for figure in self.figures:
            figure.draw(self.canvas, self.color)  # Отрисовка всех фигур
        self.figures = []  # Очистка списка фигур после отрисовки

class Circle:  # Определение класса для круга
    def __init__(self, x, y, radius):
        self.x = x  # Установка координаты x центра круга
        self.y = y  # Установка координаты y центра круга
        self.radius = radius  # Установка радиуса круга

    def draw(self, canvas, color):
        pygame.draw.circle(canvas, color, (self.x, self.y), self.radius)  # Рисование круга на заданном холсте Pygame
        print(f"Drawing Circle at ({self.x}, {self.y}) with radius {self.radius} in color {color}")  # Вывод информации о круге

class Triangle: # Определение класса для треугольника
    def __init__(self, points):
        self.points = points  # Инициализация атрибута, содержащего координаты точек треугольника

    def draw(self, canvas, color):
        pygame.draw.polygon(canvas, color, self.points)  # Отрисовка треугольника на холсте
        print(f"Drawing Triangle with points {self.points} in color {color}")  # Вывод информации о треугольнике

class Rectangle: # Определение класса для прямоугольника
    def __init__(self, x, y, width, height):
        self.x = x  # Установка координаты x верхнего левого угла прямоугольника
        self.y = y  # Установка координаты y верхнего левого угла прямоугольника
        self.width = width  # Установка ширины прямоугольника
        self.height = height  # Установка высоты прямоугольника

    def draw(self, canvas, color):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)  # Создание объекта прямоугольника
        pygame.draw.rect(canvas, color, rect)  # Отрисовка прямоугольника на холсте
        print(f"Drawing Rectangle at ({self.x}, {self.y}) with width {self.width}, height {self.height} in color {color}")  # Вывод информации о прямоугольнике


# Инициализация Pygame
pygame.init()
clock = pygame.time.Clock()

# Создание объекта движка с заданными размерами холста
engine = Engine2D(800, 600)

# Создание фигур (круга, треугольника и прямоугольника) с заданными параметрами
circle = Circle(200, 100, 50)
triangle = Triangle([(400, 50), (450, 150), (350, 150)])
rectangle = Rectangle(550, 50, 100, 100)

# Добавление фигур на холст движка
engine.add_figure(circle)
engine.add_figure(triangle)
engine.add_figure(rectangle)

# Изменение цвета отрисовки на голубой
engine.change_color((26, 115, 232))

# Отрисовка фигур на холсте и очистка списка фигур
engine.draw()

# Основной игровой цикл Pygame
running = True
while running:
    for event in pygame.event.get():  # Проверка событий Pygame
        if event.type == pygame.QUIT:  # Если нажата кнопка закрытия окна
            running = False  # Устанавливаем флаг для выхода из цикла

    pygame.display.flip()  # Обновление экрана
    clock.tick(60)  # Установка FPS (60 кадров в секунду)

pygame.quit()  # Выход из Pygame
sys.exit()  # Выход из программы
