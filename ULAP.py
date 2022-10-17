#基于水下光衰减先验(ULAP)，即水下图像的像素RGB关系预测场景深度
import cv2
import numpy as np
img = cv2.imread("175.jpg") #openCV读取图片
B,G,R = cv2.split(img) #得到的数组是按照 B，G，R 的顺序返回
width = img.shape[0]
length = img.shape[1]
D = np.empty(shape=(width,length))
for i in range(width):
    for j in range(length):
        b = B[i,j]
        g = G[i,j]
        r = R[i,j]
        m = max(b,g)
        v = r
        d = 0.53214829 + 0.51309827*m - 0.91066194*v
        D[i,j] = d

cv2.imwrite("/Users/Vita/PycharmProjects/py36/D.jpg", D)#保存图片
