import numpy as np
import matplotlib.pyplot as plt


# z, x, y, r, g, b
img = np.loadtxt(r'C:\Users\eriks\OneDrive\Desktop\Quantum Physics\Case studies\Computer graphics\Code\smiley.txt', delimiter=',')
img = img.T

images = [img.copy() for i in range(6)]

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

r = 10

def visualize_3d(faces):
    ax.cla()
    for face in faces:
        ax.scatter(face[1],face[2],face[0], c=np.transpose(face[3:]))

    plt.xlim(-15, 15)
    plt.ylim(-15, 15)   
    ax.set_zlim(-15, 15)

    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')

    plt.show(block=False)


def rotate_matrix(angle, axis): 

    if axis == 'z':
        rot = np.array([[np.cos(angle), -np.sin(angle), 0],
                        [np.sin(angle), np.cos(angle), 0],
                        [0, 0, 1]])
    elif axis == 'x':
        rot = np.array([[1, 0 ,0],
                        [0, np.cos(angle), -np.sin(angle)],
                        [0, np.sin(angle), np.cos(angle)]])

    else:
        rot = np.array([[np.cos(angle), 0, np.sin(angle)],
                        [0, 1, 0],
                        [-np.sin(angle), 0, np.cos(angle)]])
        
    return rot



def rotate_3d(matrix, vector):
    return matrix @ vector




def rotate_image_3d(face, theta, phi): # first time is the onlöy time we have to use gradient, go to

    theta = np.radians(theta+90) # to meassure correctly
    phi = np.radians(phi) 

    matrix_x = rotate_matrix(phi, 'x') # in negative phi direction. first around x
    matrix_z = rotate_matrix(theta, 'z') # then around z

    for i in range(len(face[0])): 
        z = face[0][i] 
        x = face[1][i]
        y = face[2][i]

        vec = np.array([x, y, z])

        rotated = rotate_3d(matrix_z,  rotate_3d(matrix_x, vec))
    
        face[0][i] = rotated[2] # z
        face[1][i] = rotated[0] # x
        face[2][i] = rotated[1] # y
    
    return face



def create_cube(faces):
    rotations = [[0,0], [90,90], [0,180], [-90, 90], [180, 90], [0, 90]] # rotations theta (x-axis), phi (z-axis) for every face

    for i in range(6): # 6 faces
        faces[i] = rotate_image_3d(faces[i], rotations[i][0], rotations[i][1]) # theta, phi

    return faces



def rotate_cube(face, a, b, c): # x --> y --> z

    a, b, c = np.radians(a), np.radians(b), np.radians(c)

    matrix_x = rotate_matrix(a, 'x') 
    matrix_y = rotate_matrix(b, 'y')
    matrix_z = rotate_matrix(c, 'z') 

    for i in range(len(face[0])): 
        z = face[0][i] 
        x = face[1][i]
        y = face[2][i]

        vec = np.array([x, y, z])

        rotated = rotate_3d(matrix_z, rotate_3d(matrix_y,  rotate_3d(matrix_x, vec)))
    
        face[0][i] = rotated[2] # z
        face[1][i] = rotated[0] # x
        face[2][i] = rotated[1] # y
    
    return face


def task4(faces):
    
    z = np.ones((1, len(faces[0][0])))*r # add 0 as z coordinates
    for i in range(6):
        faces[i] = np.row_stack((z, faces[i]))

    faces = create_cube(faces)
    visualize_3d(faces)

    while True:
        print("___________________")
        a = float(input("Choose x: "))
        b = float(input("Choose y: "))
        c = float(input("Choose z: "))
        
        face_copys = []

        for face in faces:
            face_copy = face.copy() # to absolute position
            face_copys.append(rotate_cube(face_copy, a, b, c))
        
        visualize_3d(face_copys)


task4(images) # input all faces

