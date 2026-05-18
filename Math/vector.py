import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class StaticObject:
    def __init__(self, vertices, color = "blue"):
        """
        vertices: Nx2 numpy array of points
        color: object color
        
        """
        self.vertices = np.array(vertices)
        self.color = color
    def transform(self, matrix):
        """
        Apply a transformation matrix to the object
        """
        return np.dot(self.vertices, matrix.T)
    
    def rotate(self, angle_deg):
        """
        Rotation matrix
        """

        theta = np.radians(angle_deg)

        rotation_matrix = np.array([
            [np.cos(theta), -np.sin(theta)],
            [np.sin(theta), np.cos(theta)]

        ])

        return self.transform(rotation_matrix)
    
    def translate(self, tx, ty):
        """ 
        Translation using homogenous coordinates
        """
        homogenous_vertices = np.hstack(
            (self.vertices, np.ones((len(self.vertices), 1)))
        )

        translation_matrix = np.array([
            [1, 0, tx],
            [0, 1, ty],
            [0, 0, 1]
        ])

        translated = np.dot(homogenous_vertices, translation_matrix.T)

        return translated[:, :2]
    
    #Definition of a square object
square = StaticObject([
        [-1, -1],
        [1, -1],
        [1, 1],
        [-1, 1],
        [-1, -1]

    ], color = "red")

#Plot Setup
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')

line, = ax.plot([], [], color = square.color, linewidth = 2)

def update(frame):
    ax.clear()

    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal')
    ax.grid(True)

#Rotation
    rotated = square.rotate(frame * 5)

#Move object in a circular path

    tx = 4 * np.cos(np.radians(frame * 3))
    ty = 4 * np.sin(np.radians(frame * 3))

#Apply translation
    homogenous = np.hstack((rotated, np.ones((len(rotated), 1))))

    translation_matrix = np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])
    
    transformed = np.dot(homogenous, translation_matrix.T)

#Draw transformed object
    ax.plot(
        transformed[:, 0],
        transformed[:, 1],
        color = square.color,
        linewidth = 2
    )

    ax.set_title("Matrix Transformation: Rotation + Transformation")

#animation

ani = FuncAnimation(fig, update, frames = 120, interval = 50)

plt.show()

        


