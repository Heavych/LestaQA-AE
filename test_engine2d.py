import unittest
import pygame
import sys

# Импорт классов из вашего исходного кода
from engine2d import Engine2D, Circle, Triangle, Rectangle

class TestEngine2D(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.engine = Engine2D(800, 600)

    def test_change_color(self):
        self.engine.change_color((255, 0, 0))
        self.assertEqual(self.engine.color, (255, 0, 0))

    def test_add_figure(self):
        circle = Circle(200, 100, 50)
        self.engine.add_figure(circle)
        self.assertIn(circle, self.engine.figures)

    def test_draw(self):
        circle = Circle(200, 100, 50)
        triangle = Triangle([(400, 50), (450, 150), (350, 150)])
        rectangle = Rectangle(550, 50, 100, 100)
        self.engine.add_figure(circle)
        self.engine.add_figure(triangle)
        self.engine.add_figure(rectangle)

        self.engine.draw()
        self.assertEqual(self.engine.figures, [])

class TestCircle(unittest.TestCase):
    def setUp(self):
        self.circle = Circle(200, 100, 50)

    def test_draw(self):
        mock_canvas = pygame.Surface((800, 600))
        color = (255, 255, 255)
        self.circle.draw(mock_canvas, color)  # Проверка, что метод не выбрасывает ошибку

class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.triangle = Triangle([(400, 50), (450, 150), (350, 150)])

    def test_draw(self):
        mock_canvas = pygame.Surface((800, 600))
        color = (255, 255, 255)
        self.triangle.draw(mock_canvas, color)  # Проверка, что метод не выбрасывает ошибку

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(550, 50, 100, 100)

    def test_draw(self):
        mock_canvas = pygame.Surface((800, 600))
        color = (255, 255, 255)
        self.rectangle.draw(mock_canvas, color)  # Проверка, что метод не выбрасывает ошибку

if __name__ == '__main__':
    main(run_game=False)  # Запуск без запуска игрового цикла
    unittest.main()  # Запуск тестов
