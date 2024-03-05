from settings import *
from world import World
from player import Player

class Scene:
    def __init__(self, app):
        self.app = app
        self.world = World(self.app)
        self.player = Player(self.app, position=STARTING_POSITION)

    def update(self):
        self.world.update()
        self.player.update()
    def render(self):
        self.world.render()
        self.player.render()










































