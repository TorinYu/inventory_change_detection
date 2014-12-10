import cv2
import sys
import os
import numpy as np


def detectCornor(image):
    img = cv2.imread(image)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    corners = cv2.goodFeaturesToTrack(gray,1000,0.1,10)
    corners = np.int0(corners)
    
    return corners
    #for i in corners:
     #   x,y = i.ravel()
      #  cv2.circle(img,(x,y),3,255,-1)
        #cv2.imwrite(sys.argv[2], img)
        #cv2.imshow("image",img)
    #plt.imshow(img),plt.show()



def preprocess(image):
    mv = cv2.split(image)
    mv[0] = cv2.equalizeHist(mv[0])
    mv[1] = cv2.equalizeHist(mv[1])
    mv[2] = cv2.equalizeHist(mv[2])
    color = cv2.merge(mv)
    return color

def sift(img1, img2, k):
    img1 = preprocess(img1)
    img2 = preprocess(img2)

    img1 = cv2.fastNlMeansDenoisingColored(img1, h=10)
    img2 = cv2.fastNlMeansDenoisingColored(img2, h=10)

    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    sift = cv2.SIFT()

    cornor1 = detectCornor(img1)
    cornor2 = detectCornor(img2)
    kp1, des1 = sift.compute(img1_gray, cornor1)
    kp2, des2 = sift.compute(img1_gray, cornor2)
    #kp1, des1 = sift.detectAndCompute(img1_gray, None)
    #kp2, des2 = sift.detectAndCompute(img2_gray, None)

    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)

    good = []
    for m,n in matches:
        if m.distance < k*n.distance:
            good.append([m])

    ratio = float(len(good))/float(len(matches))
    ratios.append(ratio)

    return ratio

def main(argv):
    ratio = sift(cv2.imread(argv[1]), cv2.imread(argv[2]), 0.5)


if __name__ == "__main__":
    main(sys.argv)