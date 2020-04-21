from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

start_time = time.time()


def init():
   glClearColor (0.0, 0.0, 0.0, 0.0)
   glShadeModel (GL_FLAT)


def display():
    sphere = gluNewQuadric
    t = time.time() - start_time
    year_period = 15.0                  # 15 seconds for simulating one year
    year = (t / year_period)
    day = 365 * year
    moon_sid = (365 / 27.3) * year

    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    glEnable( GL_DEPTH_TEST )

    glColor4f (1.0, 1.0, 0, 1)

    glPushMatrix()

    glPushMatrix()
    glRotatef(day + 360.0, 0.0, 0.1, 0.0)          # sun sidereal
    glRotatef(90, 1.0, 0.0, 0.0)
    glColor4f(1, 0.7, 0.1, 1)
    glutWireSphere(1.5, 60, 60)
    glPopMatrix()


    glRotatef(year*360.0, 0.0, 1.0, 0.0)     # earth rotation around the sun
    glTranslatef(3.0, 0.0, 0.0)              # earth location

    glPushMatrix()                           # push earth system
    glRotatef(day*360.0, 0.0, 1.0, 0.0)      # earth spinn
    glRotatef(90-23.4, 1.0, 0.0, 0.0)        # earth axis
    glColor4f(0, 0, 1, 1)                    # blue
    glutWireSphere(0.5, 30, 30)
    #gluSphere(sphere, 0.3, 10, 8)            # earth
    glPopMatrix()

    glPushMatrix()
    glRotatef(moon_sid*360.0, 0.0, 1.0, 0.0) # moon sidereal
    glTranslatef(1.0, 0.0, 0.0)              # distance moon to earth
    glRotatef(0, 1.0, 0.0, 0.0)
    glColor3f (1, 1, 1)
    glutWireSphere(0.1, 20, 10)
    #gluSphere(sphere, 0.1, 10, 8)               # moon
    glPopMatrix()

    glPushMatrix()
    glRotatef(moon_sid*360.0, 0.0, 1.0, 0.0)
    glRotatef(90, 0.0, 10.0, 0.0)
    glColor3f(0, 1, 0)
    glutSolidCylinder(0.01, 1.0, 32, 32)
    glPopMatrix()

    glPushMatrix()
    glRotatef(90, 0.0, -10.0, 0.0)
    glColor3f(1, 0, 0)
    glutSolidCylinder(0.01, 3.0, 32, 32)
    glPopMatrix()

    glPopMatrix()                            # pop earth system
    glutSwapBuffers()


def reshape(w, h):
   glViewport (0, 0, w, h)
   glMatrixMode (GL_PROJECTION)
   glLoadIdentity ()
   gluPerspective(70.0, w/h, 1.0, 20.0)
   glMatrixMode(GL_MODELVIEW)
   glLoadIdentity()
   gluLookAt (0.0, 4.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(1200, 1000)
glutInitWindowPosition (100, 100)
glutCreateWindow("Solar System")
init ()
glutDisplayFunc(display)
glutIdleFunc(display)
glutReshapeFunc(reshape)
glutMainLoop()
