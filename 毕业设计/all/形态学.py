import cv2
import numpy as np

imagePath = '../houghTest5.png'
img = cv2.imread(imagePath)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# sobel边缘检测得到二值图
sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, ksize=3)

# 二值化
ret, binary = cv2.threshold(sobel, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)

# 膨胀腐蚀
element1 = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 9))
element2 = cv2.getStructuringElement(cv2.MORPH_RECT, (24, 6))

# 膨胀一次，使轮廓突出
dilation = cv2.dilate(binary, element2, iterations=1)

# 腐蚀一次，去掉细节
erosion = cv2.erode(dilation, element1, iterations=1)

# 再次膨胀，使轮廓明显
dilation2 = cv2.dilate(erosion, element2, iterations=2)

# 查找轮廓和筛选
region = []

contours, hierarchy = cv2.findContours(dilation2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    cnt = contours[i]
    area = cv2.contourArea(cnt)
    if (area < 1000):
        continue
    
    # 找到最小矩形
    rect = cv2.minAreaRect(cnt)
    print("rect is:")
    print(rect)
    
    # box四个点的坐标
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    
    # 计算高和宽
    height = abs(box[0][1] - box[2][1])
    width = abs(box[0][0] - box[2][0])
    
    # 根据文字特征，筛选那些太细的矩形，留下扁的
    if (height > width * 1.3):
        continue
        
    region.append(box)    
    
for box in region:
    cv2.drawContours(img, [box], 0, (0, 255, 0), 2)

cv2.imshow("img", img)
# cv2.imshow("gray", gray)
# cv2.imshow("sobel", sobel)
# cv2.imshow("binary", binary)
# cv2.imshow("d1", dilation)
# cv2.imshow("e1", erosion)
# cv2.imshow("d2", dilation2)
cv2.waitKey(0)