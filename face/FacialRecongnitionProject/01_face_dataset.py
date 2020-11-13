import cv2
import os
 
cam = cv2.VideoCapture(0)
cam.set(3, 640) # 设置摄像头宽
cam.set(4, 480) # 设置摄像头高
 
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # 调用opencv识别器及其参数
 
# 每个人对应一个id
face_id = input('\n 请输入你的id并按下回车 <return> ==>  ')
 
print("\n [INFO] 初始化摄像头中，请将正脸对准摄像头并等待数秒...")
# 统计录入的照片数量
count = 0
 
while(True):
    ret, img = cam.read()
    img = cv2.flip(img, -1) # 反转摄像头
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 将采集的彩色图像转换为灰度图像
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
 
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2) # 框出识别到的人脸
        count += 1
 
        # 将图像存储到本地，命名格式为User.用户id.照片id.jpg
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
 	
        cv2.imshow('image', img)
 
    k = cv2.waitKey(100) & 0xff # 按下esc键中断
    if k == 27:
        break
    elif count >= 30: # 得到30张训练样本后关闭摄像头
         break
 
# 释放资源
print("\n [INFO] 程序成功退出")
cam.release()
cv2.destroyAllWindows()
