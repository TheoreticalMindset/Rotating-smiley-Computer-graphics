import numpy as np
import matplotlib.pyplot as plt


# z, x, y, r, g, b
img = np.loadtxt(r'C:\Users\eriks\OneDrive\Desktop\Quantum Physics\Case studies\Computer graphics\Code\smiley.txt', delimiter=',')
img = img.T


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

r = 10

def visualize_3d(inp):
    ax.cla()
    ax.scatter(inp[1],inp[2],inp[0], c=np.transpose(inp[3:]))

    plt.xlim(-15, 15)
    plt.ylim(-15, 15)   
    ax.set_zlim(-15, 15)

    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')

    plt.show(block=False)


def draw_sphere():
    phi, theta = np.mgrid[0.0:2.0*np.pi:100j, 0.0:np.pi:50j]
    x, y, z = get_coordinate(theta, phi)
    ax.plot_surface(x, y, z, color='c', alpha=0.3)
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



def get_coordinate(theta, phi):

    x = r * np.sin(phi) * np.cos(theta)
    y = r * np.sin(phi) * np.sin(theta)
    z = r * np.cos(phi)

    return x, y, z


def get_grad_matrix(gradient, theta, phi, psi):
    """
    rotation around vector x,y,z is R=I+sin(θ)⋅K+(1-cos(θ))⋅K^2
    """
    x,y,z = gradient[0], gradient[1], gradient[2]

    I = np.eye(3)
    K = np.array([[0, -z, y],
                  [z, 0, -x],
                  [-y, x, 0]])
                  
    return (I + np.sin(psi)*K + (1-np.cos(psi))*(K@K))



def rotate_image_3d(img, theta, phi, psi): # first time is the only time we have to use gradient, go to

    theta, phi, psi = np.radians(theta), np.radians(phi), np.radians(psi) 

    gradient = np.array([0,0,1])
    xy_matrix = rotate_matrix(theta, 'z') @ rotate_matrix(phi, 'x')

    gradient = xy_matrix @ gradient

    comb = get_grad_matrix(gradient, theta, phi, psi) @ xy_matrix


    for i in range(len(img[0])): 
        z = img[0][i] 
        x = img[1][i]
        y = img[2][i]

        vec = np.array([x, y, z])

        rotated = rotate_3d(comb, vec)

        img[0][i] = rotated[2] # z
        img[1][i] = rotated[0] # x
        img[2][i] = rotated[1] # y
    
    return img


def task3(img):

    z = np.ones((1, len(img[0])))*r # add 0 as z coordinates
    img = np.row_stack((z, img))

    ########### initialize
    img = rotate_image_3d(img, 0, 0, 0)
    visualize_3d(img)
    draw_sphere()
    ##############

    while True:
        img_copy = img.copy() # to absolute position
        print("____________________")
        theta = float(input("Choose theta: "))
        phi = float(input("Choose phi: "))
        psi = float(input("Choose psi: "))
        visualize_3d(rotate_image_3d(img_copy, theta, phi, psi))
        draw_sphere()


task3(img)

