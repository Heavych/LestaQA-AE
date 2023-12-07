import pygame
import sys
import pytest
from engine2d import Engine2D, Circle, Triangle, Rectangle

@pytest.fixture
def engine():
    pygame.init()
    engine = Engine2D(800, 600)
    yield engine
    pygame.quit()

def test_add_figure(engine):
    assert len(engine.figures) == 0

    circle = Circle(100, 100, 50)
    engine.add_figure(circle)
    assert len(engine.figures) == 1
    assert engine.figures[0] == circle

def test_change_color(engine):
    initial_color = engine.color

    engine.change_color((255, 0, 0))  # Красный цвет
    assert engine.color != initial_color
    assert engine.color == (255, 255, 0)

def test_draw(engine):
    circle = Circle(100, 100, 50)
    triangle = Triangle([(200, 200), (300, 300), (400, 200)])
    rectangle = Rectangle(400, 400, 100, 50)

    engine.add_figure(circle)
    engine.add_figure(triangle)
    engine.add_figure(rectangle)


def test_circle_draw():
    canvas = pygame.Surface((800, 600))
    circle = Circle(100, 100, 50)
    circle.draw(canvas, (255, 0, 0))


def test_triangle_draw():
    canvas = pygame.Surface((800, 600))
    triangle = Triangle([(200, 200), (300, 300), (400, 200)])
    triangle.draw(canvas, (0, 255, 0))


def test_rectangle_draw():
    canvas = pygame.Surface((800, 600))
    rectangle = Rectangle(400, 400, 100, 50)
    rectangle.draw(canvas, (0, 0, 255))

