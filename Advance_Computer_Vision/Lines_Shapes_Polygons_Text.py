import cv2
import numpy as np

# Creating a canvas 500X500 (Three Channels)
canvas = np.zeros((500,500,3))

# Drawing a Line
cv2.line(canvas,(0,0),(100,100),(0,255,0),2, cv2.LINE_4)
cv2.line(canvas,(0,20),(120,120),(0,255,0),2, cv2.LINE_AA)

# Drawing Rectangle
cv2.rectangle(canvas, (200,200),(250,270),(0,0,255),-1)

# Drawing circle
cv2.circle(canvas,(250,250),10,(255,0,0),3)

# Drawing Arrow lines
cv2.arrowedLine(canvas,(400,400),(400,500),(255,255,255),tipLength=0.3)





cv2.imshow("winname",canvas)
cv2.waitKey(20000)









