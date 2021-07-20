import matplotlib.pyplot as plt
import cv2

img = cv2.imread("dog.png")#this imdhow is of opencv2 and does not need the cpnversion og bgr to rgb
gray = cv2.imread("dog.png", cv2.IMREAD_GRAYSCALE)

cv2.imshow('Bot Image', img)
cv2.imshow('Bot Image 2', gray)

cv2.waitKey(0)#zero arguments depicts infinite time any other argument is in milli sec
cv2.destroyAllWindows()