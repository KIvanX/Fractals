import pygame as pg
import math
from time import sleep
from random import random, choice
import random


def randintN(a, b):
    return random.triangular(-a, b, random.gauss((a+b)//2, min(a, b)))

def randomN():
    return random.triangular(-1, 1, random.gauss(0, 1))

def make_tacts(axiom, rules, tacts):
    s = axiom
    for t in range(tacts):
        for r in rules:
            if type(r[1]) == list:
                while s.find(r[0]) >= 0:
                    s = s[:s.find(r[0])] + choice(r[1]).title() + s[s.find(r[0])+len(r[0]):]
            else:
                s = s.replace(r[0], r[1].title())
        s = s.lower()
    return s


class My_Turtle:
    def __init__(self, n=600, m=600):
        pg.init()
        self.angle = 90
        self.speed = 1
        self.width_pen = 1
        self.color_pen = (0, 0, 0)
        self.x, self.y = n//2, m//2
        self.n, self.m = n, m
        self.window = pg.display.set_mode((n, m))
        self.window.fill((10, 120, 10))
        pg.display.set_caption('L-системы')

    def update(self, point=True):
        if point:
            pg.draw.circle(self.window, self.color_pen, (self.x, self.y), self.width_pen)
        pg.display.flip()

    def leaf(self, r, color):
        pg.draw.circle(self.window, color, (self.x, self.y), r)
        pg.draw.circle(self.window, color, (self.x, self.y+3), r)
        pg.display.flip()

    def forward(self, n):
        if self.speed:
            for i in range(1, int(n)+1):
                self.x += math.cos(math.radians(self.angle))
                self.y -= math.sin(math.radians(self.angle))
                self.update()
                sleep(1/self.speed/100)
        else:
            x1 = self.x + math.cos(math.radians(self.angle)) * n
            y1 = self.y - math.sin(math.radians(self.angle)) * n
            pg.draw.line(self.window, self.color_pen, (self.x, self.y), (x1, y1), self.width_pen)
            self.x, self.y = x1, y1
            self.update(False)


    def left(self, ang):
        self.angle = (self.angle + ang) % 360

    def right(self, ang):
        self.angle = (self.angle - ang) % 360

    def done(self):
        wait = True
        while wait:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    wait = False
