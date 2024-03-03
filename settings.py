from numba import njit
import numpy as np
import glm
import math

# window resolution
WIN_RES = glm.vec2(1920, 1080)

# colors
BG_COLOR = glm.vec3(0.1, 0.16, 0.25)