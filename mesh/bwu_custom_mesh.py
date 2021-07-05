import bpy
from random import randint


class createOcean():
    bpy.ops.mesh.primitive_cube_add()
    count = 1
    for c in range(0,count):
       x = randint(-10,10)
       y = randint(-10,10)
       z = randint(-10,10)
       bpy.ops.mesh.primitive_cube_add(location=(x,y,z))
