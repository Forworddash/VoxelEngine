import pygame as pg
from camera import Camera
from settings import *


class Player(Camera):
    def __init__(self, app, position=PLAYER_POS, yaw=-90, pitch=0):
        self.app = app
        super().__init__(position, yaw, pitch)

    def update(self):
        self.keyboard_control()
        self.mouse_control()
        super().update()

    def mouse_control(self):
        mouse_dx, mouse_dy = pg.mouse.get_rel()
        if mouse_dx:
            self.rotate_yaw(delta_x=mouse_dx * MOUSE_SENSITIVITY)
        if mouse_dy:
            self.rotate_pitch(delta_y=mouse_dy * MOUSE_SENSITIVITY)

    def keyboard_control(self):
        key_state = pg.key.get_pressed()
        vel = PLAYER_SPEED * self.app.delta_time
        runningVel = PLAYER_RUN_SPEED * self.app.delta_time
        current_speed = runningVel if key_state[pg.K_LSHIFT] else vel

        if key_state[pg.K_w]:
            self.move_forward(current_speed)
        if key_state[pg.K_s]:
            self.move_back(current_speed)
        if key_state[pg.K_d]:
            self.move_right(current_speed)
        if key_state[pg.K_a]:
            self.move_left(current_speed)
        if key_state[pg.K_q]:
            self.move_up(current_speed)
        if key_state[pg.K_e]:
            self.move_down(current_speed)
        if key_state[pg.K_SPACE]:
            self.move_up(current_speed)
        if key_state[pg.K_LCTRL]:
            self.move_down(current_speed)



        # if key_state[pg.K_LSHIFT]:
            # self.current_speed = runningVel
















































