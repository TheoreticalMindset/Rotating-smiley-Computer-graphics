import numpy as np
import matplotlib.pyplot as plt


# z, x, y, r, g, b
img = np.loadtxt('smiley.txt', delimiter=',')
img = img.T

fig = plt.figure()
ax = fig.add_subplot(projection='3d')



def visualize_3d(inp):
    ax.cla()
    ax.scatter(inp[1],inp[2],inp[0], c=np.transpose(inp[3:]))

    plt.xlim(-15, 15)
    plt.ylim(-15, 15)   
    ax.set_zlim(-15, 15)

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


def rotate_image_3d(img, angle, axis):

    angle = np.radians(angle)  
    matrix = rotate_matrix(angle, axis)

    for i in range(len(img[0])): 
        z = img[0][i] 
        x = img[1][i]
        y = img[2][i]

        vec = np.array([x, y, z])

        rotated = rotate_3d(matrix, vec)
    
        img[0][i] = rotated[2] # z
        img[1][i] = rotated[0] # x
        img[2][i] = rotated[1] # y
    
    return img



def task2(img):

    z = np.zeros((1, len(img[0]))) # add 0 as z coordinates
    img = np.row_stack((z, img))

    while True:
        print("_________________________")
        axis = str(input("Choose axis: "))
        angle = float(input("Choose angle: "))
        visualize_3d(rotate_image_3d(img, angle, axis))


task2(img)

