import random
import pylatex

def gen_rand_roots():
    root1 = random.randint(-15,15)
    root2 = random.randint(-15,15)
    if abs(root1) != abs(root2) and abs(root1*root2) <= 75:
        return (root1,root2)
    else:
        gen_rand_roots()

def gen_basic_quadratic(root1,root2):
    