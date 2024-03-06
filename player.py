import pygame as pg
from camera import Camera
from settings import *


class Player(Camera):
    def __init__(self, app, position=PLAYER_POS, yaw=-90, pitch=0):
        self.app = app
        self.velocity = glm.vec3(0.0, 0.0, 0.0) # initial velocity
        self.size = glm.vec3(PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_DEPTH)  # Define player's bounding box size
        super().__init__(position, yaw, pitch)

    def update(self):
        self.keyboard_control()
        self.apply_gravity() # method to apply gravity to player
        self.move() # method to move player based on velocity
        self.mouse_control()
        self.current_position()
        super().update()

    def current_position(self):
        print(self.position)

    def apply_gravity(self):
        if self.position.y > 0:
            self.velocity.y -= GRAVITY * self.app.delta_time

    # create a method to check for colision between player and a voxel
    def collision(self, voxel):
        # check for collision between player and voxel
        if self.position.x < voxel.position.x + 1 and self.position.x + 1 > voxel.position.x and self.position.y < voxel.position.y + 1 and self.position.y + 1 > voxel.position.y and self.position.z < voxel.position.z + 1 and self.position.z + 1 > voxel.position.z:
            print("collision")
            return True
        return False                    


        
    def move(self):
        self.position += self.velocity * self.app.delta_time
        if self.position.y <= 0:
            self.position.y = 0
            self.velocity.y = 0

    def handle_event(self, event):
        # adding and removing voxels with clicks
        if event.type == pg.MOUSEBUTTONDOWN:
            voxel_handler = self.app.scene.world.voxel_handler
            if event.button == 1:
                voxel_handler.set_voxel()
            if event.button == 3:
                voxel_handler.switch_mode()


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
        if key_state[pg.K_SPACE] and self.position.y == 0:
            # self.move_up(current_speed)
            self.velocity.y = JUMP_POWER * self.app.delta_time
        if key_state[pg.K_LCTRL]:
            self.move_down(current_speed)

    def render(self):
        pass
