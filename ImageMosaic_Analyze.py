#This program searches a subfolder called Library for all images and loads them. The Library must contain only image files, or else errors will occur.
#After the images are loaded, it averages the pixel value over the entire image and stores this data in a seperate text file based off
#the resolution given in the program (resX, resY)


import cv2
import numpy as np
import os
import time

filename = os.listdir(os.getcwd() + "/Library")

maxImages = len(filename)
resX = 100
resY = 150
img = []

start = time.time()
print "Loading pixels..."
#Load all the images that will make up the final image
for i in range(maxImages):
    img.append(cv2.imread("Library/" + filename[i]))
    
print "Time taken: ", (time.time() - start)
start = time.time()

#Resize all the images we loaded
resImg = []

print "Resizing pixels..."
for i in range(maxImages):
    resImg.append(cv2.resize(img[i], (resX,resY)))
                
print "Time taken: ", (time.time() - start)
start = time.time()

print "Calculating RGB scores for pixels..."
#Calculate RGB scores for images

rgbScore = []
hsvScore = []

for i in range(maxImages):
    avg = [0,0,0]
    avgh = [0,0,0]
    hsv = cv2.cvtColor(resImg[i], cv2.COLOR_BGR2HSV)
    for j in range(resY):
        for k in range(resX):
            avg += resImg[i][j,k]
            avgh += hsv[j,k]
    avg /= resY*resX
    avgh /= resY*resX
    rgbScore.append((avg, i))
    hsvScore.append(avgh)
    
print "Time taken: ", (time.time() - start)
start = time.time()

print "Sorting..."

#for i in range(len(rgbScore)):
#    for j in range(i, len(rgbScore)):
#        if (rgbScore[i][0][0] > rgbScore[j][0][0]):
#            temp = rgbScore[i]
#            rgbScore[i] = rgbScore[j]
#            rgbScore[j] = temp


#tempImg = np.zeros((imgY,imgX,3), np.uint8)
#for i in range(len(resImg)):
    

#for i in range(len(hsvScore)):
#    for j in range(i, len(hsvScore)):
#        if (hsvScore[i][1] > hsvScore[j][1]):
#            temp = hsvScore[i]
#            hsvScore[i] = hsvScore[j]
#            hsvScore[j] = temp
#            
#            temp = rgbScore[i]
#            rgbScore[i] = rgbScore[j]
#            rgbScore[j] = temp
#        elif (hsvScore[i][1] == hsvScore[j][1]):
#            if (hsvScore[i][0] > hsvScore[j][0]):
#                temp = hsvScore[i]
#                hsvScore[i] = hsvScore[j]
#                hsvScore[j] = temp
#                
#                temp = rgbScore[i]
#                rgbScore[i] = rgbScore[j]
#                rgbScore[j] = temp
#            elif (hsvScore[i][0] == hsvScore[j][0]):
#                if (hsvScore[i][2] > hsvScore[j][2]):
#                    temp = hsvScore[i]
#                    hsvScore[i] = hsvScore[j]
#                    hsvScore[j] = temp
#                    
#                    temp = rgbScore[i]
#                    rgbScore[i] = rgbScore[j]
#                    rgbScore[j] = temp
#            


#rgbScore.sort()
rgbSums = []
for i in range(len(rgbScore)):
    rgbSums.append (sum(rgbScore[i][0]))
    

#def pivot (a, b, first, last):
#    pValue = a[first]
#    
#    leftmark = first+1
#    rightmark = last
#    
#    done = False
#    while not done:
#        while leftmark <= rightmark and a[leftmark] <= pValue:
#            leftmark = leftmark+1
#        
#        while a[rightmark] >= pValue and rightmark >= leftmark:
#            rightmark = rightmark-1
#            
#        if rightmark < leftmark:
#            done = True
#        else:
#            temp = a[leftmark]
#            a[leftmark] = a[rightmark]
#            a[rightmark] = temp
#            
#            temp = b[leftmark]
#            b[leftmark] = b[rightmark]
#            b[rightmark] = temp
#    
#    return rightmark
    
#def quickSort (a, b, first, last):
#    if (first < last):
#        mid = pivot(a,b,first,last)
        
#        quickSort(a,b,first,mid-1)
#        quickSort(a,b,mid+1,last)
    


#quickSort (rgbSums, rgbScore, 0, len(rgbSums)-1)

def swap (array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp

for i in range(len(rgbSums)):
    for j in range(len(rgbSums)):
        if (rgbSums[i] > rgbSums[j]):
            swap (rgbSums, i, j)
            swap (rgbScore, i, j)


print "Time taken: ", (time.time() - start)


print "Writing scores to a document..."
#Output the scores to a document that can be loaded for faster use
f = open("_x_" + str(resX) + "_y_" + str(resY), 'w')
x = np.empty((len(rgbScore), 3), dtype=float)
x = rgbScore
#np.asarray(rgbScore).tofile("X_" + str(imgX) + "_Y_" + str(imgY) + "_x_" + str(resY) + "_y_" + str(resX), 'w')

#print type(np.asarray(rgbScore))
#print np.asarray(rgbScore).dtype

for i in range(len(rgbScore)):
    f.write(str(rgbScore[i][0][0]))
    f.write(',')
    f.write(str(rgbScore[i][0][1]))
    f.write(',')
    f.write(str(rgbScore[i][0][2]))
    f.write(',')
    f.write(str(rgbScore[i][1]))
    f.write("\n")

f.close()
print "Time taken: ", (time.time() - start)