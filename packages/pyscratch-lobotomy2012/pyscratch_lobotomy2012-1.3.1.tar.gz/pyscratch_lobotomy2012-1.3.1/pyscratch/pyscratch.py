from .run import run
from .Sprite.sprite import Sprite
from .Sprite.code import Code

def init():
    import pygame

    pygame.init()

    print()
    print("\033[96mHello from PyScratch")
    print("\033[94mPyScratch 1.3.1")
    print("\033[90mGithub: https://github.com/Lobotomy2012/PyScratch\033[0m")