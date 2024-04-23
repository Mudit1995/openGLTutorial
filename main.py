import pygame as pg
import moderngl as mgl
import sys
from model import *
from Camera import Camera 
from light import Light

class GraphicsEngine:
    def __init__(self, win_size=(1600, 900)):
        # init pygame modules
        pg.init()
        # window size
        self.WIN_SIZE = win_size
        # set opengl attr
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        # create opengl context
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
       
         # detect and use existing opengl context
        self.ctx = mgl.create_context()
         #  set the dept test flag 
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)
        # mouse settings
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)

        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)
        # self.ctx.front_face = 'cw'
        # self.ctx.wireframe = True
        # create an object to help track time
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0
        # light
        self.light = Light()
        # camera
        self.camera = Camera(self)
        # # mesh
        # self.mesh = Mesh(self)
        # # scene
        self.scene = Cube(self)
        self.scene1 = Cube1(self, pos =(-2.5,0,0), rot=(45,0,0) )
        self.scene.m_model = glm.translate(self.scene.m_model, glm.vec3(-3.8, 0.0, 0.0))  # Move the first cube to the left
        self.scene1.m_model = glm.translate(self.scene1.m_model, glm.vec3(2.0, 0.0, 0.0))  # Move the second cube to the rig

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.scene.destroy()
                pg.quit()
                sys.exit()

    def render(self):
        # while True:
        # clear framebuffer
        self.ctx.clear(color=(0.08, 0.16, 0.18))
        # render scene
        self.scene.render()
        self.scene1.render()
        # swap buffers
        pg.display.flip()

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.camera.update()
            self.render()
            self.delta_time = self.clock.tick(60)
        


if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()






























