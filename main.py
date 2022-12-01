# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 13:48:19 2022

@author: Yan de Souza Pereira
"""

import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import numpy as np
import cv2
import time

#import tensorflow as tf
#from tensorflow import keras
#from tensorflow.keras import layers
#from keras.models import load_model

from zmqRemoteApi import RemoteAPIClient

""" NECESSITA INSTALAÇÃO DE CBOR E PYZMQ no ambiente python
pip install pyzmq
pip install cbor
"""

#Stack Images
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

#Get Contours
def getContours(imag):
    contours,hierarchy = cv2.findContours(imag,cv2.RETR_EXTERNAL ,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #print("area: "+str(area))
        if area>1000 and area<5000:
            cv2.drawContours(img, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            #print(peri)
            approx = cv2.approxPolyDP(cnt,0.01*peri,True)
            #print("faces: " + str(len(approx)))
            #print("\n")
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if objCor == 3 : objectType = "Triangle"
            elif objCor == 6 : objectType = "Hexagon"
            elif objCor == 8 : objectType = "Octogon"
            elif objCor > 10 : objectType = "Circle"
            else : objectType = ""



            cv2.rectangle(img,(x,y),(x+w,y+h),(255,53,184),2)
            cv2.putText(img,objectType,
                        (x+(w//2)-50, y+(h//2)-10),cv2.FONT_HERSHEY_DUPLEX,0.7,
                        (50,50,50),2)

#model = load_model('model_dataset\model.h5')


######    CAPTURA DE IMAGENS    #####################

myPath = 'data/images'
moduleVal = 10  # SAVE EVERY ITH FRAME TO AVOID REPETITION
minBlur = 0  # SMALLER VALUE MEANS MORE BLURRINESS PRESENT
grayImage = True # IMAGES SAVED COLORED OR GRAY
cannyImage = False # IMAGES SAVED COLORED OR CANNY
saveData = True   # SAVE DATA FLAG
imgWidth = 180
imgHeight = 120

global countFolder

count = 0
countSave =0

def saveDataFunc():
    global countFolder
    countFolder = 0
    while os.path.exists( myPath+ str(countFolder)):
        countFolder += 1
    os.makedirs(myPath + str(countFolder))

if saveData:saveDataFunc()

#####################################################

print('Programa iniciado')

client = RemoteAPIClient()
sim = client.getObject('sim')

visionSensorHandle = sim.getObject('/Vision_sensor')
manipulatorHandle = sim.getObject('/LBRiiwa14R820')
vacuumHandle = sim.getObject('/BaxterVacuumCup')
trianguloHandle = sim.getObject('/Triangulo')
discoHandle = sim.getObject('/Disco')
hexagonoHandle = sim.getObject('/Hexagono')
octogonoHandle = sim.getObject('/Octogono')


# When simulation is not running, ZMQ message handling could be a bit
# slow, since the idle loop runs at 8 Hz by default. So let's make
# sure that the idle loop runs at full speed for this program:
defaultIdleFps = sim.getInt32Param(sim.intparam_idle_fps)
sim.setInt32Param(sim.intparam_idle_fps, 0)


client.setStepping(True)
sim.startSimulation()

while (True):
    img, res = sim.getVisionSensorImg(visionSensorHandle)
    img = np.frombuffer(img, dtype=np.uint8).reshape(res[0], res[1], 3)    
    if saveData:
        img2 = cv2.resize(img,(imgWidth,imgHeight))
        if grayImage:
            img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
        if cannyImage:
            img2 = cv2.Canny(img,100,100)
        
        blur = cv2.Laplacian(img2, cv2.CV_64F).var()
        if count % moduleVal ==0 and blur > minBlur:
            nowTime = time.time()
            cv2.imwrite(myPath + str(countFolder) +
                    '/' + str(countSave)+"_"+ str(int(blur))+"_"+str(nowTime)+".png", img2)
            countSave+=1
        count += 1

    

    # In CoppeliaSim images are left to right (x-axis), and bottom to top (y-axis)
    # (consistent with the axes of vision sensors, pointing Z outwards, Y up)
    # and color format is RGB triplets, whereas OpenCV uses BGR:
    '''
    img = cv2.flip(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), 0)
    img = cv2.resize(img, (541 , 541))
    img_tensor = tf.convert_to_tensor(img, dtype=tf.uint8)
    img_tensor = tf.expand_dims(img_tensor , 0)
    '''
    # prediction = model.predict(img_tensor)
    #boxes, scores, classes, num_detections = model(img_tensor)
    imgCanny = cv2.Canny(img,100,100)
    #kernel = np.ones((5,5),np.uint8)
    #imgDialation = cv2.dilate(imgCanny,kernel,iterations=3) #dilata as linhas
    #imgEroded = cv2.erode(imgDialation,kernel,iterations=3) #contrai as linhas
    #getContours(imgEroded)
    
    getContours(imgCanny)

    #imgStack = stackImages(1,[img,imgCanny,imgEroded])
    imgStack = stackImages(1,[img,imgCanny])

    cv2.imshow('Camera_robo', imgStack)
    #cv2.imshow('Camera_robo',img)
    cv2.waitKey(1)
    client.step()  # triggers next simulation step

sim.stopSimulation()

# Restore the original idle loop frequency:
sim.setInt32Param(sim.intparam_idle_fps, defaultIdleFps)

input("Pressione qualquer tecla para finalizar.")
cv2.destroyAllWindows()

print('Program ended')

#sim.stopSimulation()

"""
Rotina do Robô:
    Vasculhar a área de peças;
    Após encontrar uma peça, deverá:
        reconhecer qual formato;
        pegar peça;
        colocá-la no local adequado (possivelmente ajustando sua orientação);
        retornar a vasculhar a área para encontrar outra peça;    
"""

