import numpy as np
import matplotlib.pyplot as plt


# z, x, y, r, g, b
img = np.loadtxt('smiley.txt', delimiter=',')
img = img.T

def visualize(inp):
    plt.clf()
    plt.scatter(inp[0],inp[1], c=np.transpose(inp[2:])) #  z, x, y

    plt.xlim(-20, 20)
    plt.ylim(-20, 20)
    plt.show(block=False)



def rotate_matrix(angle):
    return np.array([[np.cos(angle), -np.sin(angle)],
                    [np.sin(angle), np.cos(angle)]])


def rotate(matrix, vector):
    return matrix @ vector



def rotate_image(img, angle):

    angle = np.radians(angle) 
    matrix = rotate_matrix(angle) 
    new_img = img.copy()

    for i in range(len(new_img[0])): 
        x = new_img[0][i]
        y = new_img[1][i]

        vec = np.array([x, y])

        rotated = rotate(matrix, vec)
    
        new_img[0][i] = rotated[0] # x
        new_img[1][i] = rotated[1] # y
    
    return new_img


def task1(img):
    
    while True:
        print("_____________________")
        angle = float(input("Choose angle: "))
        visualize(rotate_image(img, angle))



task1(img)


