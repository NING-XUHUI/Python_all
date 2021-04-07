import cv2

# 讀取圖檔
im = cv2.imread('../../TEST.jpg')

# 建立 Selective Search 分割器
ss = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()

# 設定要進行分割的圖形
ss.setBaseImage(im)

# 使用快速模式（精準度較差）
#ss.switchToSelectiveSearchFast()

# 使用精準模式（速度較慢）
ss.switchToSelectiveSearchQuality()

# 執行 Selective Search 分割
rects = ss.process()

print('候選區域總數量： {}'.format(len(rects)))

# 要顯示的候選區域數量
numShowRects = 20

# 每次增加或減少顯示的候選區域數量
increment = 2

# 複製一份原始影像
imOut = im.copy()

# 以迴圈處理每一個候選區域
for i, rect in enumerate(rects):
    # 以方框標示候選區域
    if (i < numShowRects):
        x, y, w, h = rect
        cv2.rectangle(imOut, (x, y), (x + w, y + h), (0, 255, 0), 1, cv2.LINE_AA)
    else:
        break

# 顯示結果
cv2.imshow("Output", imOut)
cv2.waitKey(0)
