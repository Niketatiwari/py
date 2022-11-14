#pip install opencv-contrib-python mediapipe

import cv2

cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
color_black = (0,0,0 ) #black
color_white = (255,255,255) #white
while cam.isOpened():
    status, image = cam.read()
    if status:
        #draw a box
        cv2.rectangle(image, (5,5), (300,40), (0, 255, 0), -1)

        cv2.imshow("Live Camera", image)

        #add text
        cv2.putText(image, "Live Camera Feed", (10,30), font, 1, color_black, 2)
        #add a clock
        timestr = dt.now().strftime("%H:%M:%S")


        if cv2.waitKey(1) == 27: #27 is the ASCII code for the escape key
            break
cam.release()
cv2.destroyAllWindows()






m