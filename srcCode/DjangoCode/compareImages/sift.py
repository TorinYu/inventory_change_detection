import cv2
import sys
import os
import numpy as np
import distribution
import test

THREASHOLD = 0.1695

ratios = []

#scores, bins = distribution.calc_score_table(
#    test.ratios_changed, test.ratios_unchanged)

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

    

    kp1, des1 = sift.detectAndCompute(img1_gray, None)
    kp2, des2 = sift.detectAndCompute(img2_gray, None)

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
    print distribution.get_score(ratio, scores, bins)

def compareImage(argv):
    ratio = sift(cv2.imread(argv[1]), cv2.imread(argv[2]), 0.75)
    
    print 'The ratio is: ' + (str)(ratio)
    if ratio > 0.3:
        print 'unchanged'
    else: 
        print 'changed'

def test_k(argv):
    for f in os.listdir(argv[1]):
        if f.endswith("_inbound.jpg"):
            f = f.replace("_inbound.jpg", "")
            print f
            file1 = argv[1] + "/" + f + "_inbound.jpg"
            file2 = argv[1] + "/" + f + "_outbound.jpg"
            for i in range(17):
                k = 0.1 + i*0.05
                ratio = sift(cv2.imread(file1), cv2.imread(file2), k)
                print k, ratio

def test(argv):
    i = 0
    for f in os.listdir(argv[1]):
        if f.endswith("inbound.jpg"):
            i = i + 1
            file1 = argv[1] + "/" + f
            file2 = argv[1] + "/" + f.replace("inbound.jpg", "outbound.jpg")
            ratio = sift(cv2.imread(file1), cv2.imread(file2))
            return distribution.get_score(ratio, scores, bins)

    print 'avg: ', float(sum(ratios))/float(i)
    print 'std: ', np.std(ratios)

if __name__ == "__main__":
    #main(sys.argv)
    #test(sys.argv)
    #test_k(sys.argv)
    compareImage(sys.argv)
