import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
(x,y)=(image.shape[:2])
for i in range(x):
    for j in range(y):
        image[i,j]=0.001125*image[i,j][0]+0.5150*image[i,j][1]+0.070*image[i,j][2]
cv2.imshow('gray',image)
cv2.waitKey(0)
cv2.destroyAllWindows()