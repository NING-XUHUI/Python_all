import cv2
import numpy as np
from datetime import datetime
np.set_printoptions(suppress=True)

def my_humoments(img_gray):
    moments = cv2.moments(img_gray)
    humoments = cv2.HuMoments(moments)
    humoments = np.log(np.abs(humoments))
    print(humoments)
    
if __name__ == "__main__":
    t1 = datetime.now()
    fp = "../TEST.jpg"
    img = cv2.imread(fp)
    h, w, _ = img.shape
    img = cv2.resize(img, (h // 2, w // 2), cv2.INTER_LINEAR)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray", img_gray)
    cv2.waitKey(0)