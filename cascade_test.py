import cv2

################################################################
path = 'cascades/canny_cascade_triangle.xml'  # PATH OF THE CASCADE
#cameraNo = 0                       # CAMERA NUMBER
objectName = 'Triangle'       # OBJECT NAME TO DISPLAY
frameWidth= 240                     # DISPLAY WIDTH
frameHeight = 240                  # DISPLAY HEIGHT
color= (255,0,255)
#################################################################


#cap = cv2.VideoCapture(cameraNo)
#cap.set(3, frameWidth)
#cap.set(4, frameHeight)

def empty(a):
    pass

# CREATE TRACKBAR
cv2.namedWindow("Result")
cv2.resizeWindow("Result",frameWidth,frameHeight+100)
cv2.createTrackbar("Scale","Result",36,1000,empty)
cv2.createTrackbar("Neig","Result",0,50,empty)
cv2.createTrackbar("Min Area","Result",33000,100000,empty)
#cv2.createTrackbar("Brightness","Result",180,255,empty)

# LOAD THE CLASSIFIERS DOWNLOADED
cascade = cv2.CascadeClassifier(path)

while True:
    # SET CAMERA BRIGHTNESS FROM TRACKBAR VALUE
    #cameraBrightness = cv2.getTrackbarPos("Brightness", "Result")
    #cap.set(10, cameraBrightness)
    # GET CAMERA IMAGE AND CONVERT TO GRAYSCALE
    img = cv2.imread('img_train/triangulo/t_r00-2.png')
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    canny = cv2.Canny(gray,100,100)
    
    # DETECT THE OBJECT USING THE CASCADE
    scaleVal =1 + (cv2.getTrackbarPos("Scale", "Result") /1000)
    neig=cv2.getTrackbarPos("Neig", "Result")
    objects = cascade.detectMultiScale(canny,scaleVal, neig)
    # DISPLAY THE DETECTED OBJECTS
    for (x,y,w,h) in objects:
        area = w*h
        minArea = cv2.getTrackbarPos("Min Area", "Result")
        if area >minArea:
            cv2.rectangle(canny,(x,y),(x+w,y+h),color,3)
            cv2.putText(canny,objectName,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            roi_color = canny[y:y+h, x:x+w]

    cv2.imshow("Result", canny)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(objects)
        break