import sys
import numpy as np
import cv2
if len(sys.argv) > 2:
    height, width = sys.argv[1:2]
else:
    height, width = 9000, 9000
r,g,b = 200,80, 189
image =np.zeros((height, width, 3), np.uint8)
image[:,:,0] = r
image[:,:,1] = g
image[:,:,2] = b
if len(sys.argv) > 3:
    name = sys.argv[3]
else:
    name = 'generated_image.jpeg'
cv2.imwrite(name, image)
