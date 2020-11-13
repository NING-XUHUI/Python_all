#!/usr/bin/env python
# coding=utf-8

import RPi.GPIO as GPIO
import cv2
import time
import numpy as np
import os
from PIL import ImageFont, ImageDraw, Image

colors = [0xFF00, 0x00FF, 0x0000]
makerobo_pins = (11,12)
GPIO.setmode(GPIO.BOARD)     # 采用实际的物理管脚给GPIO口
GPIO.setwarnings(False)      # 去除GPIO口警告
GPIO.setup(makerobo_pins, GPIO.OUT)   # 设置Pin模式为输出模式
GPIO.output(makerobo_pins, GPIO.LOW)  # 设置Pin管脚为低电平(0V)关闭LED

p_R = GPIO.PWM(makerobo_pins[0], 2000)  # 设置频率为2KHz
p_G = GPIO.PWM(makerobo_pins[1], 2000)  # 设置频率为2KHz

p_R.start(0) 
p_G.start(0)

# 放缩至0-100
def makerobo_pwm_map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


# 设置led灯颜色
def makerobo_set_color(col):
    R_val = col >> 8
    G_val = col & 0x00FF
    R_val = makerobo_pwm_map(R_val, 0, 255, 0, 100)
    G_val = makerobo_pwm_map(G_val, 0, 255, 0, 100)
    #print(R_val)
    #print(G_val)
    p_R.ChangeDutyCycle(R_val)
    p_G.ChangeDutyCycle(G_val)

def makerobo_destroy():
    p_G.stop()
    p_R.stop()
    GPIO.output(makerobo_pins, GPIO.LOW)
    GPIO.cleanup()
    
    

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);



# 中文字体设置
fontpath = "SimHei.ttf"
font = ImageFont.truetype(fontpath, 15)

# 初始化用户id
id = 0

# 每一个id对应一个用户的名字
names = ['陌生人', '宁旭晖','李一德']

# 初始化摄像头
cam = cv2.VideoCapture(0)
cam.set(3, 640) # 摄像头宽
cam.set(4, 480) # 摄像头高

# 定义最小的可以被识别的人脸尺寸
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:
     
    ret, img =cam.read()
    img = cv2.flip(img, -1) # 反转摄像头
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    # 得到人脸
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )
    # 如果为识别到人脸，led无颜色
    if len(faces) == 0:
        makerobo_set_color(colors[2])
    #print(len(faces))    
    for(x,y,w,h) in faces:
        #cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        #print(confidence)
        # 查看置信度，越低越确定
        if (confidence < 50):
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            id = names[id]
            #makerobo_set_color(colors[1])
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            id = '陌生人'
            #makerobo_set_color(colors[0])
            confidence = "  {0}%".format(round(100 - confidence))
        
        # 陌生人则红灯
        if id == '陌生人':
            makerobo_set_color(colors[0])
            #time.sleep(0.5)
        # 否则绿灯
        else:
            makerobo_set_color(colors[1])   
            #time.sleep(0.5)
        img_pil = Image.fromarray(img)
        draw = ImageDraw.Draw(img_pil)
        draw.text((x+5,y+15),str(id),font=font,fill=(255,255,255,2))
        img = np.array(img_pil)
#        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
#        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)

    cv2.imshow('camera',img)

    k = cv2.waitKey(10) & 0xff # 按下esc键退出
    if k == 27:
        break

# 释放资源
print("\n [INFO] 程序成功退出")
cam.release()
makerobo_destroy()
cv2.destroyAllWindows()



