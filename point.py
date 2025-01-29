from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window_height = 300
window_width = 300
window_title = b"Renderizar ponto com OpenGL"

teto = [
    [0,0.9],
    [0.7,0.3],
    [-0.7,0.3],
    ]
base = [
    [0.7, 0.3],
    [0.7,-0.6],
    [-0.7, -0.6],
    [-0.7,0.3],
    ]
porta = [
    [-0.5, -0.6],
    [-0.5, 0],
    [-0.1, 0],
    [-0.1, -0.6],
    ]
janela = [
    [0.1, -0.3],
    [0.1, 0],
    [0.5, 0],
    [0.5, -0.3],
    [0.1, -0.3],
    [0.3, -0.3],
    [0.3, 0],
    [0.1, 0],
    ]


def init():
    glClearColor(0, 0, 0, 1)
    glPointSize(5)

def render():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.0, 0.9)
    
    
    glBegin(GL_LINE_LOOP)
    for v in teto:
        glVertex2fv(v)
    glEnd()

    glBegin(GL_LINE_LOOP)
    for v in base:
        glVertex2fv(v)
    glEnd()

    glBegin(GL_LINE_LOOP)
    for v in porta:
        glVertex2fv(v)
    glEnd()

    glBegin(GL_LINE_LOOP)
    for v in janela:
        glVertex2fv(v)
    glEnd()


    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(window_width, window_height)
    glutCreateWindow(window_title)
    init()
    glutDisplayFunc(render)
    glutMainLoop()

main()