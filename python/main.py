import cv2
import datetime
import numpy as np

lastMinute = 0
pixelBrightness = 200
maxPixelsLimit = 100

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = frame.copy()
    gray = gray[:,:,0]
    
    '''
    red = frame.copy()
    red[:, :, 0] = 0
    red[:, :, 1] = 0    

    green = frame.copy()
    green[:, :, 0] = 0
    green[:, :, 2] = 0

    blue = frame.copy()
    blue[:, :, 1] = 0
    blue[:, :, 2] = 0
    '''

    numberPixels = np.sum(gray >= pixelBrightness)

    now = datetime.datetime.now()
    if now.minute != lastMinute or numberPixels > maxPixelsLimit:
        
        print('Number of white pixels:', numberPixels)

    
    cv2.imshow("frame", gray)
    key = cv2.waitKey(1)
    if key == 27:
        break
    
        
cap.release()
cv2.destroyAllWindows()