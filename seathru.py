import cv2
import numpy as np
img = cv2.imread("3416.tif",-1)
#第二个参数是通道数和位深的参数，
#IMREAD_UNCHANGED = -1#不进行转化，比如保存为了16位的图片，读取出来仍然为16位。
#IMREAD_GRAYSCALE = 0#进行转化为灰度图，比如保存为了16位的图片，读取出来为8位，类型为CV_8UC1。
#IMREAD_COLOR = 1#进行转化为RGB三通道图像，图像深度转为8位
#IMREAD_ANYDEPTH = 2#保持图像深度不变，进行转化为灰度图。
#IMREAD_ANYCOLOR = 4#若图像通道数小于等于3，则保持原通道数不变；若通道数大于3则只取取前三个通道。图像深度转为8位

#print (img)
print (img.shape)
print (img.dtype)
print (img.min())
print (img.max())

img = img/img.max()
img =img*255-0.001#减去0.001防止变成负整型
img =img.astype(np.uint8)
# sea-thru的tiif深度图直接看距离氛围为0～3区别太小，加上上面三行后可以看出距离变化，还能显示指针处数值


#创建窗口并显示图像,第二个参数默认为1不能缩放
cv2.namedWindow("Image",0)
cv2.imshow("Image",img)
cv2.imwrite("/Users/Vita/PycharmProjects/py36/1.jpg", img)#保存图片
cv2.waitKey(0)
#释放窗口
cv2.destroyAllWindows()
