import cv2
cap = cv2.VideoCapture(0)  #here 0 is the id number for our camera

while True:
    success, img = cap.read()
    cv2.imshow("Image", img)
    cv2.waitKey(1)          #delay for 1 miili second