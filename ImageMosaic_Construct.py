#This program constructs an image mosaic from the data gathered by ImageiMosaic_Analyze and the Library either created by imagePull
#The target image must be called Target.jpg and be in the same folder as the python files. The size of the image will depend on the
#resolution set in this program. The resX and resY must be the same as the ones used in Analyze, or else it wont load the generated file.
#imgX and imgY is the resolution of the output image, and need to be a multiple of resX and resY (and maintain the same ratio)
#If the imgX/imgY are not multiples of resX or resY, and do not maintain the ratio, unintended results may occur

import cv2
import numpy as np
import os
import time
from sys import exit

filename = os.listdir(os.getcwd() + "/Library")

maxImages = len(filename)
imgX = 12000
imgY = 18000
resX = 100
resY = 150
img = []

if (imgX % resX != 0):
    print "Warning: imgX not divisible by resX"
    exit()
if (imgY % resY != 0):
    print "Warning: imgY not divisible by resY"
    exit()

start = time.time()
print "Reading scores from a document..."
#Output the scores to a document that can be loaded for faster use
#rgbScore = np.fromfile("X_" + str(imgY) + "_Y_" + str(imgX) + "_x_" + str(resY) + "_y_" + str(resX),dtype='int32')

f = open("_x_" + str(resX) + "_y_" + str(resY), "r+")

rgbScore = []
ff = f.read().splitlines()

for i in range(len(ff)):
    rgbScore.append(ff[i].split(','))

for i in range(len(rgbScore)):
    rgbScore[i][0] = int(rgbScore[i][0])
    rgbScore[i][1] = int(rgbScore[i][1])
    rgbScore[i][2] = int(rgbScore[i][2])
    rgbScore[i][3] = int(rgbScore[i][3])

print "Time taken: ", (time.time() - start)
start = time.time()

#print "Thing"
#testo = np.zeros((len(rgbScore),100,3), np.uint8)

#for i in range (len(rgbScore)):
#    for k in range(100):
#        testo[i,k][0] = rgbScore[i][0]
#        testo[i,k][1] = rgbScore[i][1]
#        testo[i,k][2] = rgbScore[i][2]

#cv2.imwrite ("goieg.png", testo)
#hov = cv2.cvtColor (testo, cv2.COLOR_BGR2HSV)
#cv2.imwrite ("goieg2.png", hov)


#for i in range (len(rgbScore)):
#        rgbScore[i][0] = hov[i,0][0]
#        rgbScore[i][1] = hov[i,0][1]
#        rgbScore[i][2] = hov[i,0][2]


#print "Time taken: ", (time.time() - start)
#start = time.time()
print "Loading target image..."
#Load the image we're going to make out of other images    
imgTarget = cv2.imread("Target.jpg")

imgTarget = cv2.resize(imgTarget, (imgX,imgY))

print "Time taken: ", (time.time() - start)
start = time.time()

print "Calculating RGB scores for cells in the target image..."    
#Calculate RGB scores for subsections of targetImage

rgbScoreTarget = []
hsv = cv2.cvtColor (imgTarget, cv2.COLOR_BGR2HSV)

for i in range(imgY/resY):
    for j in range(imgX/resX):
        avg = [0,0,0]
        for k in range(resY):
            for l in range(resX):
                avg += imgTarget[(i*resY)+k,(j*resX)+l]
        avg /= resY*resX
        rgbScoreTarget.append(avg)
        
print "Time taken: ", (time.time() - start)
start = time.time()

print "Finding the best fitting pixels for the image..."
#Find the closest match of each 'pixel' to each cell

mosaicd = np.zeros((imgY,imgX,3), np.uint8)
t = []
sums = []

for j in range(maxImages):
    sums.append(sum((rgbScore[j][0],rgbScore[j][1],rgbScore[j][2])))

for i in range(len(rgbScoreTarget)):
    t.append(0)
    
    #if ((rgbScoreTarget[i][1]>30)or(rgbScoreTarget[i][2]>30)):
    curDiff = [10000,10000,10000] #Arbitrarily large number
    curSum = sum(rgbScoreTarget[i])
    
    
    for j in range(maxImages):
        if (abs(curSum-sums[j]) <= 200):
            diff = []
            diff.append(abs(rgbScoreTarget[i][0] - rgbScore[j][0]))
            diff.append(abs(rgbScoreTarget[i][1] - rgbScore[j][1]))
            diff.append(abs(rgbScoreTarget[i][2] - rgbScore[j][2]))
            if (sum(diff) < sum(curDiff)):
                t[i] = rgbScore[j][3]
                curDiff = diff
    #else:
    #    curDiff = [1000,1000] #Arbitrarily large number
    #    
    #    for j in range(maxImages):
    #        diff = []
    #        diff.append(abs(rgbScoreTarget[i][1] - rgbScore[j][1]))
    #        diff.append(abs(rgbScoreTarget[i][2] - rgbScore[j][2]))
    #        gg = sum(diff)/2
    #        gh = sum(curDiff)/2
    #        if (gg < gh):
    #            t[i] = rgbScore[j][3]
    #            curDiff = diff

print "Time taken: ", (time.time() - start)
start = time.time()

print "Loading pixels..."
#Load all the images that will make up the final image
for i in range(maxImages):
    load = False
    for j in range(len(t)):
        if (i==t[j]):
            load = True
    if (load==True):
        img.append(cv2.imread("Library/" + filename[i]))
    else:
        img.append(0)#Don't spend time loading images we're not using
    
#Resize all the images we loaded
resImg = []

print "Time taken: ", (time.time() - start)
start = time.time()

print "Resizing pixels..."
for i in range(maxImages):
    resImg.append(cv2.resize(img[i], (resX,resY)))


print "Time taken: ", (time.time() - start)
start = time.time()

print "Stitching the image together..."
#Create the final image and output it
for i in range(imgY/resY):
    for j in range(imgX/resX):
        for k in range(resY):
            for l in range(resX):
                mosaicd[(i*resY)+k, (j*resX)+l] = resImg[t[(i*imgX/resX)+j]][k,l]

print "Time taken: ", (time.time() - start)

print "Outputting image..."
cv2.imwrite("Output"+str(imgX)+"x"+str(imgY)+"_"+str(resX)+"x"+str(resY)+".jpeg", mosaicd)
print "Done :)"
