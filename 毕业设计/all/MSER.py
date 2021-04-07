import cv2
imagePath = '../TEST.jpg'
img = cv2.imread(imagePath)
# 灰度化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
vis = img.copy()
orig = img.copy()

# MSER
mser = cv2.MSER_create()
regions, _ = mser.detectRegions(gray)
hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
cv2.polylines(img, hulls, 1, (0, 255, 0))
cv2.imshow('img', img)

# 将不规则检测框处理成矩形框
keep = []
for c in hulls:
    x, y, w, h = cv2.boundingRect(c)
    keep.append([x, y, x + w, y + h])
    cv2.rectangle(vis, (x, y), (x + w, y + h), (255, 255, 0), 1)

cv2.imshow("hulls", vis)
cv2.waitKey(0)