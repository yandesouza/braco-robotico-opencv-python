import cv2
import os
import time

#####################################################

myPath = 'data/images'
cameraNo = 0
cameraBrightness = 180
moduleVal = 10  # SAVE EVERY ITH FRAME TO AVOID REPETITION
minBlur = 500  # SMALLER VALUE MEANS MORE BLURRINESS PRESENT
grayImage = False # IMAGES SAVED COLORED OR GRAY
saveData = True   # SAVE DATA FLAG
showImage = True  # IMAGE DISPLAY FLAG
imgWidth = 180
imgHeight = 120


#####################################################

global countFolder
cap = cv2.VideoCapture(cameraNo)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10,cameraBrightness)


count = 0
countSave =0

def saveDataFunc():
    global countFolder
    countFolder = 0
    while os.path.exists( myPath+ str(countFolder)):
        countFolder += 1
    os.makedirs(myPath + str(countFolder))

if saveData:saveDataFunc()


while True:

    if showImage:
        cv2.imshow("Image", img)

    success, img = cap.read()
    if saveData:
        img2 = cv2.resize(img,(imgWidth,imgHeight))
        if grayImage:
            img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
        
        blur = cv2.Laplacian(img2, cv2.CV_64F).var()
        if count % moduleVal ==0 and blur > minBlur:
            nowTime = time.time()
            cv2.imwrite(myPath + str(countFolder) +
                    '/' + str(countSave)+"_"+ str(int(blur))+"_"+str(nowTime)+".png", img2)
            countSave+=1
        count += 1
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()