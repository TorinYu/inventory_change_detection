import numpy as np
import sys
import cv2
from matplotlib import pyplot as plt

def detectCornor(image):
    img = cv2.imread(image)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    corners = cv2.goodFeaturesToTrack(gray,1000,0.1,10)
    corners = np.int0(corners)

    for i in corners:
        x,y = i.ravel()
        cv2.circle(img,(x,y),3,255,-1)
    #cv2.imwrite(sys.argv[2], img)
    #cv2.imshow("image",img)
    plt.imshow(img),plt.show()

if __name__=="__main__":
    #img = cv2.imread(sys.argv[1],0)
    detectCornor(sys.argv[1])
