# import cv2
# cap=cv2.VideoCapture(0)
# #infinite loop
# while True:
#     ret, frame = cap.read()  
#     cv2.imshow("Devansh's camera", frame)

#     if cv2.waitKey(1)== 13: #13 is ASCII code of ENTER
#         break

# cap.release()
# cv2.destroyAllWindows()

#open webcamera-par pta nhi kyu ulta aara saala

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2Lab) 

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()




