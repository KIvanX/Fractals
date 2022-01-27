
import L_systems
from random import choice
from L_systems import randomN, randintN

t = L_systems.My_Turtle()
t.color_pen, t.speed = (80, 40 ,0), 0

for k1 in range(3):
    for k2 in range(3):
        t.x, t.y, t.angle = 120+k2*180, 200+k1*180, 90

        axiom = choice(['a[+f][-f]', 'a[+f][f][-f]', 'a[++f][+f][-f][--f'])
        rules = [('a', 'a_'), ('f', ['a[+f][-f]', 'a[+f][f][-f]', 'a[++f][+f][-f][--f]'])]
        delta_angle = 20
        coef_len = 1.45
        tacts = 5
        length = 10

        instr = L_systems.make_tacts(axiom, rules, tacts)

        stack = []
        for i in range(len(instr)):
            if instr[i] == '[':
                stack.append((t.x, t.y, t.angle))
            if instr[i]  == ']':
                t.x, t.y, t.angle = stack.pop()
            if instr[i]  == 'f':
                t.width_pen = 1
                t.forward(length)
                if len(stack) == tacts+1:
                    color = choice([(0, 130, 0), (0, 140, 0), (0, 150, 0), (0, 160, 0)])
                    t.leaf(2, color)
            if instr[i]  == 'a':
                i1 = i+1
                while instr[i1] == '_':
                    i1 += 1
                i1 += randomN()
                t.width_pen = max(1, int(i1-i))
                t.forward(length*coef_len**(i1-1-i))
            if instr[i]  == '-':
                t.right(randintN(-delta_angle, delta_angle))
            if instr[i]  == '+':
                t.left(randintN(-delta_angle, delta_angle))

t.done()