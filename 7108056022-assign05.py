from skimage import color, io
import numpy as np
import csv
from collections import Counter
img = io.imread("stegosaurus.bmp")
w = img.shape[0]
h = img.shape[1]
size = w * h
countoldR = []
countoldG = []
countoldB = []
countnewR = []
countnewG = []
countnewB = []
for i in range(256):
    countoldR.append(0)
    countoldG.append(0)
    countoldB.append(0)
    countnewR.append(0)
    countnewG.append(0)
    countnewB.append(0)
arr = color.rgb2lab(img)
countLab = []
for i in range(w):
    for j in range(h):
        nuR = img[i, j][0]
        nuG = img[i, j][1]
        nuB = img[i, j][2]
        countoldR[nuR] = countoldR[nuR] + 1
        countoldG[nuG] = countoldG[nuG] + 1
        countoldB[nuB] = countoldB[nuB] + 1
        countLab.append(arr[i, j, 0])
countLab2 = Counter(countLab)
result = {}
sum1 = 0
sum2 = 0
for k in sorted(countLab2):
    sum1 += countLab2[k]
    sum2 = sum1 / size * 100
    countLab2[k] = sum2
    result[k] = countLab2[k]

for i in range(w):
    for j in range(h):
            arr[i, j, 0] = result[arr[i, j, 0]]

#arr = match(arr, result)
img = color.lab2rgb(arr)
for i in range(w):
    for j in range(h):
        nR = int(img[i, j][0] * 255)
        nG = int(img[i, j][1] * 255)
        nB = int(img[i, j][2] * 255)
        countnewR[nR] = countnewR[nR] + 1
        countnewG[nG] = countnewG[nG] + 1
        countnewB[nB] = countnewB[nB] + 1
io.imsave("2after-stegosaurus.bmp", img)
io.imshow(img)
io.show()


with open('stegosaurus.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['stegosaurus'])
    writer.writerow(['h*w', '', 'oldRed', 'oldGreen', 'oldBlue', 'newRed', 'newGreen', 'newBlue'])
    writer.writerow(['resolution', 'value', 'count', 'count', 'count', 'count', 'count', 'count'])
    for i in range(256):
        writer.writerow([size, i, countoldR[i], countoldG[i], countoldB[i], countnewR[i], countnewG[i], countnewB[i]])
