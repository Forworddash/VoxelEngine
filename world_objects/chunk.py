from settings import *
from meshes.chunk_mesh import ChunkMesh
import random
from terrain_gen import *


class Chunk:
    def __init__(self, world, position):
        self.app = world.app
        self.world = world
        self.position = position
        self.m_model = self.get_model_matrix()
        self.voxels: np.array = None
        self.mesh: ChunkMesh = None
        self.is_empty = True
        self.center = (glm.vec3(self.position) + 0.5) * CHUNK_SIZE
        self.is_on_frustum = self.app.player.frustum.is_on_frustum

    def get_model_matrix(self):
        m_model = glm.translate(glm.mat4(), glm.vec3(self.position) * CHUNK_SIZE)
        return m_model

    def check_collision(self, player):
        # Get the boundaries of the chunk
        chunk_min = glm.vec3(self.position) * CHUNK_SIZE
        chunk_max = chunk_min + glm.vec3(CHUNK_SIZE)


        # Get the boundaries of the player
        player_min = player.position - player.size / 2
        player_max = player.position + player.size / 2

     

        # Check for collision
        if (chunk_min.x < player_max.x and chunk_max.x > player_min.x and
            chunk_min.y < player_max.y and chunk_max.y > player_min.y and
            chunk_min.z < player_max.z and chunk_max.z > player_min.z):
            print("Collision detected")
            return True
        return False

    def set_uniform(self):
        self.mesh.program['m_model'].write(self.m_model)

    def build_mesh(self):
        self.mesh = ChunkMesh(self)

    def render(self):
        if not self.is_empty and self.is_on_frustum(self):
            self.set_uniform()
            self.mesh.render()

    def build_voxels(self):
        voxels = np.zeros(CHUNK_VOL, dtype='uint8')

        cx, cy, cz = glm.ivec3(self.position) * CHUNK_SIZE
        self.generate_terrain(voxels, cx, cy, cz)

        if np.any(voxels):
            self.is_empty = False
        return voxels

    @staticmethod
    @njit
    def generate_terrain(voxels, cx, cy, cz):
        for x in range(CHUNK_SIZE):
            wx = x + cx
            for z in range(CHUNK_SIZE):
                wz = z + cz
                world_height = get_height(wx, wz)
                local_height = min(world_height - cy, CHUNK_SIZE)

                for y in range(local_height):
                    wy = y + cy
                    set_voxel_id(voxels, x, y, z, wx, wy, wz, world_height)
