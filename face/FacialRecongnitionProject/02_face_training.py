import numpy as np
from PIL import Image
import os
import cv2
 
# 训练图像存放路径
path = 'dataset'
 
recognizer = cv2.face.LBPHFaceRecognizer_create() # opencv 分类器模型
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml"); # opencv识别器及其参数
 
# 得到图片及其对应的id
def getImagesAndLabels(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []
    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L') # 转换为灰度图
        img_numpy = np.array(PIL_img,'uint8') # 图像转为numpy数组
        id = int(os.path.split(imagePath)[-1].split(".")[1]) # 分割字符串得到用户id
        faces = detector.detectMultiScale(img_numpy) # 识别出人脸区域
        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w]) 
            ids.append(id)
    return faceSamples,ids
 
print ("\n [INFO] 正在训练，可能会花费一点时间，请耐心等待")
faces,ids = getImagesAndLabels(path) # 得到训练集
recognizer.train(faces, np.array(ids)) # 训练
 
# 将训练得到的参数存储到相应文件
recognizer.write('trainer/trainer.yml') 
 
# 显示本次训练共训练了多少个人的人脸
print("\n [INFO] 本次训练 {0} 个用户人脸. 程序退出".format(len(np.unique(ids))))

