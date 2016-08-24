import pyglet
import numpy as np
from doredo import Shader, Entity, Window, cumclock



window = Window(bgColor=(.3, .7, .4, 1.), vsync=False)


triangle_verts = (-1., -1.,
                  1., -1.,
                  0., 1.)

player = Entity(triangle_verts)


vert = """
#version 330 core
layout(location = 0) in vec3 vertexPosition_modelspace;
void main(){
    gl_Position.xyz = vertexPosition_modelspace;
    gl_Position.w = 1.0;
}
"""

frag = """
#version 330 core
out vec3 color;
void main(){
  color = vec3(1,0,0);
}
"""

shader = Shader(vert=vert, frag=frag)

@window.event
def on_draw():
    window.clear()
    with shader:
        player.draw()



def update(dt):
    player.update(dt)
    new_verts = [np.sin(cumclock.cumtime) * v for v in triangle_verts]
    player.vertices = new_verts
pyglet.clock.schedule(update)

pyglet.app.run()
