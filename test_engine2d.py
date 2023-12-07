# Импорт необходимых модулей и классов
import unittest  # Импорт модуля unittest для написания и запуска тестов
import pygame  # Импорт библиотеки Pygame для работы с графикой
import sys  # Импорт модуля sys для работы с системными функциями

# Импорт классов из исходного кода для тестирования
from engine2d import Engine2D, Circle, Triangle, Rectangle, main


# Определение класса TestEngine2D, который будет содержать юнит-тесты для класса Engine2D
class TestEngine2D(unittest.TestCase):
    # Метод setUp() инициализирует объект перед выполнением каждого теста
    def setUp(self):
        pygame.init()  # Инициализация Pygame для работы с графикой
        self.engine = Engine2D(800, 600)  # Создание объекта движка с заданными размерами холста

    # Проверка метода изменения цвета отрисовки
    def test_change_color(self):
        self.engine.change_color((255, 0, 0))
        self.assertEqual(self.engine.color, (255, 0, 0))

    # Проверка метода добавления фигуры на холст
    def test_add_figure(self):
        circle = Circle(200, 100, 50)  # Создание объекта круга
        self.engine.add_figure(circle)
        self.assertIn(circle, self.engine.figures)

    # Проверка метода отрисовки фигур на холсте
    def test_draw(self):
        circle = Circle(200, 100, 50)  # Создание объекта круга
        triangle = Triangle([(400, 50), (450, 150), (350, 150)])  # Создание объекта треугольника
        rectangle = Rectangle(550, 50, 100, 100)  # Создание объекта прямоугольника

        self.engine.add_figure(circle)
        self.engine.add_figure(triangle)
        self.engine.add_figure(rectangle)

        self.engine.draw()  # Вызов метода отрисовки фигур на холсте
        self.assertEqual(self.engine.figures, [])  # Проверка очистки списка фигур после отрисовки


# Определение класса TestCircle, который тестирует класс Circle
class TestCircle(unittest.TestCase):
    # Метод setUp() инициализирует объект перед выполнением каждого теста
    def setUp(self):
        self.circle = Circle(200, 100, 50)  # Создание объекта круга

    # Проверка метода отрисовки круга на холсте
    def test_draw(self):
        mock_canvas = pygame.Surface((800, 600))  # Создание поверхности для имитации холста
        color = (255, 255, 255)  # Задание цвета для отрисовки
        self.circle.draw(mock_canvas, color)  # Проверка, что метод не выбрасывает ошибку


# Определение класса TestTriangle, который тестирует класс Triangle
class TestTriangle(unittest.TestCase):
    # Метод setUp() инициализирует объект перед выполнением каждого теста
    def setUp(self):
        self.triangle = Triangle([(400, 50), (450, 150), (350, 150)])  # Создание объекта треугольника

    # Проверка метода отрисовки треугольника на холсте
    def test_draw(self):
        mock_canvas = pygame.Surface((800, 600))  # Создание поверхности для имитации холста
        color = (255, 255, 255)  # Задание цвета для отрисовки
        self.triangle.draw(mock_canvas, color)  # Проверка, что метод не выбрасывает ошибку


# Определение класса TestRectangle, который тестирует класс Rectangle
class TestRectangle(unittest.TestCase):
    # Метод setUp() инициализирует объект перед выполнением каждого теста
    def setUp(self):
        self.rectangle = Rectangle(550, 50, 100, 100)  # Создание объекта прямоугольника

    # Проверка метода отрисовки прямоугольника на холсте
    def test_draw(self):
        mock_canvas = pygame.Surface((800, 600))  # Создание поверхности для имитации холста
        color = (255, 255, 255)  # Задание цвета для отрисовки
        self.rectangle.draw(mock_canvas, color)  # Проверка, что метод не выбрасывает ошибку


if __name__ == '__main__':
    main(run_game=False)  # Запуск без запуска игрового цикла
    unittest.main()  # Запуск тестов
