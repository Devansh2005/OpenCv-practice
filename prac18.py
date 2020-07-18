# BLUE COLOR FILTER
import cv2
import numpy as np
device = cv2. VideoCapture(0)
while True:
    ret, frame= device.read()

    hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# 110-130 range for blue color
    #(R, G, B) to (H,S, V)  # hue change krne p blue chNGE HOORA
    # (0,0,0)- black
    # (225,225,225)- white


#     Hue : This channel encodes color color information. 
#     Hue can be thought of an angle where 0 degree corresponds to the red color, 120 degrees
#      corresponds to the green color, and 240 degrees corresponds to the blue color.
# Saturation : This channel encodes the intensity/purity of color. For example, pink is less saturated than red.
# Value : This channel encodes the brightness of color. Shading and gloss components of an image appear in this channel.


    lower_range = np.array([110, 50, 50])
    upper_range = np.array([130,255,255])


  # filter only blue color
    mask = cv2.inRange(hsv, lower_range, upper_range)

    cv2.imshow("show", mask) #mask-filter output
    
    cv2.imshow("show1", frame)  #orignal output
    if cv2.waitKey(1)==13:
        break
device.release()
cv2.destroyAllWindows()
 
