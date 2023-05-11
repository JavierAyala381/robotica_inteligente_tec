import cv2
import os
import numpy as np

# font
font = cv2.FONT_HERSHEY_SIMPLEX

# org
org = (00, 185)
  
# fontScale
fontScale = 1
   
# Red color in BGR
color = (0, 0, 255)
  
# Line thickness of 2 px
thickness = 2

def check_cameras():
    cams_test = 0
    cams = []
    while True:
        cap = cv2.VideoCapture(cams_test)
        test, frame = cap.read()
        if test == True:
            text = 'The camera number is: ' + str(cams_test)
            frame = cv2.putText(frame, text, org, font, fontScale, 
                 color, thickness, cv2.LINE_AA, False)
            #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            name_camera = 'Video cam num: ' + str(cams_test)
            cv2.imshow(name_camera, frame)
            key = cv2.waitKey(1500)
            cams.append(cams_test)
            if key == 27:#if ESC is pressed, exit loop
                break
        else: # break if no more cameras are found
            break
        print("Camera : " + str(cams_test) + " /// result: " + str(test))
        cap.release()
        cams_test += 1
    return cams
    
    # When everything done, release the capture
    
    cv2.destroyAllWindows()

if __name__ == "__main__": 
    # Obtain default the camera originals       
    c = check_cameras()  

    print(c)
