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


def main(run_game=True):
    pygame.init()  # Инициализация Pygame для работы с графикой
    clock = pygame.time.Clock()  # Создание объекта часов для управления FPS (кадры в секунду)

    engine = Engine2D(800, 600)  # Создание объекта движка с размерами холста 800x600
    circle = Circle(200, 100, 50)  # Создание объекта круга с координатами (200, 100) и радиусом 50
    triangle = Triangle([(400, 50), (450, 150), (350, 150)])  # Создание объекта треугольника с заданными координатами точек
    rectangle = Rectangle(550, 50, 100, 100)  # Создание объекта прямоугольника с заданными координатами и размерами

    engine.add_figure(circle)  # Добавление круга на холст движка
    engine.add_figure(triangle)  # Добавление треугольника на холст движка
    engine.add_figure(rectangle)  # Добавление прямоугольника на холст движка

    engine.change_color((26, 115, 232))  # Изменение цвета отрисовки фигур на холсте

    engine.draw()  # Отрисовка всех добавленных фигур на холсте

    if run_game:  # Если run_game=True (по умолчанию), запускается игровой цикл Pygame
        running = True
        while running:  # Цикл игры, ожидает события выхода из игры
            for event in pygame.event.get():  # Проверка событий Pygame
                if event.type == pygame.QUIT:  # Если происходит событие выхода из игры
                    running = False  # Установка флага для выхода из цикла

            pygame.display.flip()  # Обновление экрана
            clock.tick(60)  # Установка FPS (60 кадров в секунду)

        pygame.quit()  # Закрытие Pygame
        sys.exit()  # Выход из программы
    else:
        # Если run_game=False (исполняется тестирование), завершаем инициализацию Pygame
        pygame.quit()  # Закрытие Pygame (в случае тестирования)

if __name__ == "__main__":
    main()