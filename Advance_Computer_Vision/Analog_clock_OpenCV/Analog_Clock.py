import numpy as np
import cv2
from Modules import tick , draw
from Color_Size import COLORS,CANVAS_SIZE,RADIUS

image = np.zeros(CANVAS_SIZE,dtype=np.uint8)
image[:] = [255,255,255]

hours_initial , hours_destination = tick()

for i in range(len(hours_initial)):
    if i % 5 == 0:
        cv2.line(image,hours_initial[i],hours_destination[i],COLORS["black"],3)
    else:
        cv2.circle(image,hours_initial[i],5,COLORS["black"],-1)

cv2.circle(image,(320,320),RADIUS+10,COLORS["yellow"],2)
cv2.putText(image,"TITAN",(215,230),cv2.FONT_HERSHEY_TRIPLEX,2,COLORS["dark_gray"],1,cv2.LINE_AA)

while True:
	image_original = image.copy()

	# Use draw time to make clock hands on the canvas
	clock_face = draw(image_original)

	#Show the watch
	cv2.imshow('clock', image_original)
	if(cv2.waitKey(1)==ord('q')):
		break

cv2.destroyAllWindows()