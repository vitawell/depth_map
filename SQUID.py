import cv2
import numpy as np
import scipy.io as scio
from PIL import Image
import matplotlib.pyplot as plt

dataFile = r'd.mat' # 单个的mat文件
data = scio.loadmat(dataFile)
# print(type(data))
# (class 'dict')
# print(data.keys())
# dict_keys(['__header__', '__version__', '__globals__', 'dist_map_l', 'dist_map_r'])
a=data['dist_map_r']
# 取出需要的数据矩阵（numpy数组类型ndarry），里面有nan值
print(a)
# print(np.nan_to_num(a))
# 用0替换nan，若copy=Ture不会改变a的nan值
print(np.nan_to_num(a, copy=False))
print(a.max()) #最大值为39.9

# 数据矩阵转图片的函数
def MatrixToImage(data):
    new_im = Image.fromarray(data)
    new_im = new_im.convert('RGB')
    return new_im

new_im = MatrixToImage(a/40*255) #把a范围放到0～255
print(new_im)
#plt.imshow(a, cmap=plt.cm.gray, interpolation='nearest')
new_im.show()
new_im.save("d.png")



# img = cv2.imread("4336.tif",-1)
# #第二个参数是通道数和位深的参数，
# #IMREAD_UNCHANGED = -1#不进行转化，比如保存为了16位的图片，读取出来仍然为16位。
# #IMREAD_GRAYSCALE = 0#进行转化为灰度图，比如保存为了16位的图片，读取出来为8位，类型为CV_8UC1。
# #IMREAD_COLOR = 1#进行转化为RGB三通道图像，图像深度转为8位
# #IMREAD_ANYDEPTH = 2#保持图像深度不变，进行转化为灰度图。
# #IMREAD_ANYCOLOR = 4#若图像通道数小于等于3，则保持原通道数不变；若通道数大于3则只取取前三个通道。图像深度转为8位
#
# #print (img)
# print (img.shape)
# print (img.dtype)
# print (img.min())
# print (img.max())
#
# d=img[:,:,0]
# cv2.namedWindow("d",0)
# cv2.imshow('d',d)
# # SQUID的tif图是三通道，没有深度信息？
#
# #创建窗口并显示图像,第二个参数默认为1不能缩放
# cv2.namedWindow("Image",0)
# cv2.imshow("Image",img)
# cv2.waitKey(0)
# #释放窗口
# cv2.destroyAllWindows()
