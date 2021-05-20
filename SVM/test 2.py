import os
import cv2 as cv
import numpy as np
from sklearn.decomposition import PCA


def get_features(array):
    # 拿到数组的高度和宽度
    h, w = array.shape
    data = []
    for x in range(0, w // 4):
        offset_y = x * 4
        temp = []
        for y in range(0, h // 4):
            offset_x = y * 4
            temp.append(sum(sum(array[0 + offset_y:4 + offset_y,
                                0 + offset_x:4 + offset_x])))
        data.append(temp)
    return np.asarray(data)


def process(filePath):
    img = cv.imread(filePath)
    img = cv.resize(img, (32, 32))
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    _, img = cv.threshold(img, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY)
    feature_array = get_features(img/255)
    return feature_array.reshape(feature_array.shape[0] * feature_array.shape[1])


def extractLetters(path):
    x = []
    y = []
    #i = 0
    for root, sub_dirs, files in os.walk(path):
        for dirs in sub_dirs:
            for fileName in os.listdir(path + '/' + dirs):
                #i = i+1
                print(root + '/' + dirs + '/' + fileName)
                x.append(process(root + '/' + dirs + '/' + fileName))
                y.append(dirs)
                #if i > 1000:
                #    break
    return x, y


if __name__ == "__main__":
    pca = PCA(n_components=100)
    path = './data'
    x, y = extractLetters(path)
    print(len(y))
    print(x[:10])
    print(y[:10])
