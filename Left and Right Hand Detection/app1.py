import cv2
import numpy as np
def imgsketch(img):
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blr_img=cv2.GaussianBlur(gray_img,(5,5),0)
    canny_edges=cv2.Canny(blr_img,10,70)
    ret,mask=cv2.threshold(canny_edges,80,255,cv2.THRESH_BINARY_INV)
    return mask

#Connecting to web cam

cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    cv2.imshow("Live Sketching Expert",imgsketch(frame))
    if cv2.waitKey(1) & 0xFF ==ord('q'):  # next 3 commands are for closing video frame after pressing 'q'
        break
cap.release()
cv2.destroyAllWindows()