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

# import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras import layers
# from keras.models import load_model

from zmqRemoteApi import RemoteAPIClient
import handles_UR5e as handles
import IK_numerico as IK

######################################################
#####              BLOCO DE FUNÇÕES              #####
######################################################

# Callback
def movCallback(config,vel,accel,handles):
    for i in range(len(handles)):
        if sim.getJointMode(handles[i])[0]==sim.jointmode_force and sim.isDynamicallyEnabled(handles[i]):
            sim.setJointTargetPosition(handles[i],config[i])
        else:
            sim.setJointPosition(handles[i],config[i])

# Stack Images
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

# Get Contours
def getContours(imag):
    contours,hierarchy = cv2.findContours(imag,cv2.RETR_EXTERNAL ,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #print("area: "+str(area))
        if area>1000 and area<5000:
            cv2.drawContours(img, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.01*peri,True)
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

# Salvar Imagens Capturadas
def saveDataFunc():
    global countFolder
    countFolder = 0
    while os.path.exists( myPath+ str(countFolder)):
        countFolder += 1
    os.makedirs(myPath + str(countFolder))

# Analise Peças
def partsAnalyze():
    intermed(handles.inter1)

    targetPose=sim.getObjectPose(sim.getObject(handles.objP1),sim.handle_world)
    movementData = {
        'id': 'partsInit',
        'targetPose': targetPose,
        'maxVel': maxVel,
        'maxAccel': maxAccel
    }
    sim.callScriptFunction('remoteApi_movementDataFunction',handles.script,movementData)

    targetPose=sim.getObjectPose(sim.getObject(handles.objP2),sim.handle_world)
    movementData = {
        'id': 'partsEnd',
        'targetPose': targetPose,
        'maxVel': maxVel,
        'maxAccel': maxAccel
    }
    sim.callScriptFunction('remoteApi_movementDataFunction',handles.script,movementData)
    sim.callScriptFunction('remoteApi_executeMovement',handles.script,'partsInit')
    sim.callScriptFunction('remoteApi_executeMovement',handles.script,'partsEnd')
    waitForMovementExecuted('partsInit')
    camera('partsEnd')

    intermed(handles.inter1)

# Analisa locais para depositar as peças
def boxAnalyze():
    intermed(handles.inter2)

    targetPose=sim.getObjectPose(sim.getObject(handles.objC1),sim.handle_world)
    movementData = {
        'id': 'boxInit',
        'targetPose': targetPose,
        'maxVel': maxVel,
        'maxAccel': maxAccel
    }
    sim.callScriptFunction('remoteApi_movementDataFunction',handles.script,movementData)

    targetPose=sim.getObjectPose(sim.getObject(handles.objC2),sim.handle_world)
    movementData = {
        'id': 'boxEnd',
        'targetPose': targetPose,
        'maxVel': maxVel,
        'maxAccel': maxAccel
    }
    sim.callScriptFunction('remoteApi_movementDataFunction',handles.script,movementData)
    sim.callScriptFunction('remoteApi_executeMovement',handles.script,'boxInit')
    sim.callScriptFunction('remoteApi_executeMovement',handles.script,'boxEnd')
    waitForMovementExecuted('boxInit')
    camera('boxEnd')

    intermed(handles.inter2)

# Ponto de movimento intermediário de movimentação para evitar limite de juntas
def intermed(position):
    global currentConf, targetConfig
    targetPosition = sim.getObjectPosition(sim.getObject(position),sim.handle_world)
    initPosition = sim.getObjectPosition(handles.jointHandles[6],sim.handle_world)
    targetConfig = IK.movement(initPosition,targetPosition)
    movementData = {
        'id': 'inter',
        'targetPos': targetConfig,
        'maxVel': maxVel,
        'maxJerk': maxJerk,
        'maxAccel': maxAccel
    }
    '''sim.moveToConfig(-1,
                     currentConf,
                     None,
                     None,
                     maxVel * np.ones(6),
                     maxAccel * np.ones(6),
                     maxJerk * np.ones(6),
                     targetConfig,
                     None,
                     movCallback,
                     handles.jointHandles)'''
    sim.callScriptFunction('remoteApi_movementDataFunction',handles.script,movementData)
    sim.callScriptFunction('remoteApi_executeMovement',handles.script,'inter')
    waitForMovementExecuted('inter')
    currentConf = targetConfig

# Ponto zero do manipulador
def posZero():
    targetPose=sim.getObjectPose(sim.getObject(handles.zero),sim.handle_world)
    movementData = {
        'id': 'movInit',
        'targetPose': targetPose,
        'maxVel': maxVel,
        'maxAccel': maxAccel
    }
    movementData2 = {
        'id' : 'posZero',
        'handles'    : handles.simJoints,
        'maxVelJ'    : [ 0.01,  0.01,  0.01,  0.01,  0.01,  0.01,  0.01],
        'maxAccelJ'  : [0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001],
        'maxJerkJ'   : [   80,    80,    80,    80,    80,    80,    80],
        'targetConf' : [    0,     0,     0,     0,     0,     0,     0]
    }

    sim.callScriptFunction('remoteApi_movementDataFunction',handles.script,movementData)
    sim.callScriptFunction('remoteApi_executeMovement',handles.script,'movInit')
    
    waitForMovementExecuted('movInit')
    sim.callScriptFunction('moveToConfig',handles.script,movementData2)

# Interrompe execução de outras partes do código enquanto algum movimento é executado
def waitForMovementExecuted(id_):
    global executedMovId
    while executedMovId != id_:
        s = sim.getStringSignal(handles.stringSignalName)
        executedMovId = s


def empty(a):
    pass


def camera(id_):
    global img, executedMovId, imgCanny, imgGray
    while executedMovId != id_:
        img, res = sim.getVisionSensorImg(handles.visionSensor)
        img = np.frombuffer(img, dtype=np.uint8).reshape(res[0], res[1], 3)
        img = cv2.flip(img, 0)
        

        # # TENSORFLOW CODE
        # img_tf = cv2.resize(img, (224, 224), interpolation=cv2.INTER_AREA)
        # # Make the image a numpy array and reshape it to the models input shape.
        # img_tf = np.asarray(img_tf, dtype=np.float32).reshape(1, 224, 224, 3)
        # # Normalize the image array
        # img_tf = (img_tf / 127.5) - 1
        # # Have the model predict what the current image is. Model.predict
        # # returns an array of percentages. Example:[0.2,0.8] meaning its 20% sure
        # # it is the first label and 80% sure its the second label.
        # probabilities = model.predict(img_tf)
        # # Print what the highest value probabilitie label
        # print(labels[np.argmax(probabilities)])
        
        # # END TENSORFLOW CODE
        

        # In CoppeliaSim images are left to right (x-axis), and bottom to top (y-axis)
        # (consistent with the axes of vision sensors, pointing Z outwards, Y up)
        # and color format is RGB triplets, whereas OpenCV uses BGR:
        
               
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

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (300 , 300))
       
        #img_tensor = tf.convert_to_tensor(img, dtype=tf.uint8)
        #img_tensor = tf.expand_dims(img_tensor , 0)
        #prediction = model.predict(img_tensor)
        #boxes, scores, classes, num_detections = model(img_tensor)

        cMin = cv2.getTrackbarPos("cMin", "Camera")
        cMax = cv2.getTrackbarPos("cMax", "Camera")
        imgCanny = cv2.Canny(img,cMin,cMax)
        imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

        #kernel = np.ones((5,5),np.uint8)
        #imgDialation = cv2.dilate(imgCanny,kernel,iterations=3) #dilata as linhas
        #imgEroded = cv2.erode(imgDialation,kernel,iterations=3) #contrai as linhas
        #getContours(imgEroded)
        
        #getContours(imgCanny)

        #imgStack = stackImages(1,[img,imgCanny,imgEroded])
        imgStack = stackImages(1,[img,imgCanny])

        cascades()
        
        cv2.imshow('Camera', imgStack)
        #cv2.imshow('Camera', img)
        cv2.waitKey(1)
        
        
        executedMovId = sim.getStringSignal(handles.stringSignalName)
    #pass


def cascades():
    global disc, triangle, hexagon, octogon
    scaleVal = 1 + ((cv2.getTrackbarPos("Scale", "Camera") + 1) /1000)
    neig = cv2.getTrackbarPos("Neig", "Camera")
    
    #TESTA COM IMAGEM CANNY
    if canny==1:
        disc = discCascade.detectMultiScale(imgCanny,scaleVal, neig)
        for (x,y,w,h) in disc: 
            cv2.rectangle(imgCanny,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(imgCanny,"Disco",(x+(w//2)-50, y+(h//2)-10),cv2.FONT_HERSHEY_DUPLEX,0.7,(50,50,50),2)
        
        hexagon = hexagonCascade.detectMultiScale(imgCanny,scaleVal,neig)
        for (x,y,w,h) in hexagon: 
            cv2.rectangle(imgCanny,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgCanny,"Hexagono",(x+(w//2)-50, y+(h//2)-10),cv2.FONT_HERSHEY_DUPLEX,0.7,(50,50,50),2)
        
        octogon = octogonCascade.detectMultiScale(imgCanny,scaleVal,neig)
        for (x,y,w,h) in octogon: 
            cv2.rectangle(imgCanny,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(imgCanny,"Octogono",(x+(w//2)-50, y+(h//2)-10),cv2.FONT_HERSHEY_DUPLEX,0.7,(50,50,50),2)
        
        triangle = triangleCascade.detectMultiScale(imgCanny,scaleVal,neig)
        for (x,y,w,h) in triangle: 
            cv2.rectangle(imgCanny,(x,y),(x+w,y+h),(255,255,0),2)
            cv2.putText(imgCanny,"Triangulo",(x+(w//2)-50, y+(h//2)-10),cv2.FONT_HERSHEY_DUPLEX,0.7,(50,50,50),2)
    
    #TESTA COM ESCALA DE CINZA
    else:
        disc = discCascade.detectMultiScale(img,scaleVal, neig)
        for (x,y,w,h) in disc: 
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(img,"Disco",(x+(w//2)-50, y+(h//2)-10),cv2.FONT_HERSHEY_DUPLEX,0.7,(50,50,50),2)
        
        hexagon = hexagonCascade.detectMultiScale(img,scaleVal,neig)
        for (x,y,w,h) in hexagon: 
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(img,"Hexagono",(x+(w//2)-50, y+(h//2)-10),cv2.FONT_HERSHEY_DUPLEX,0.7,(50,50,50),2)
        
        octogon = octogonCascade.detectMultiScale(img,scaleVal,neig)
        for (x,y,w,h) in octogon: 
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(img,"Octogono",(x+(w//2)-50, y+(h//2)-10),cv2.FONT_HERSHEY_DUPLEX,0.7,(50,50,50),2)
        
        triangle = triangleCascade.detectMultiScale(img,scaleVal,neig)
        for (x,y,w,h) in triangle: 
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
            cv2.putText(img,"Triangulo",(x+(w//2)-50, y+(h//2)-10),cv2.FONT_HERSHEY_DUPLEX,0.7,(50,50,50),2)

    
    



######    CAPTURA DE IMAGENS    #####################
saveData = False   # SAVE DATA FLAG

myPath = 'data/images'
moduleVal = 10  # SAVE EVERY ITH FRAME TO AVOID REPETITION
minBlur = 0  # SMALLER VALUE MEANS MORE BLURRINESS PRESENT
colorImage = True # IMAGES SAVED COLORED
grayImage = False # IMAGES SAVED GRAY
cannyImage = False # IMAGES SAVED CANNY

imgWidth = 240
imgHeight = 240

global countFolder

count = 0
countSave = 0

if saveData:saveDataFunc()
#####################################################


# model = load_model('keras_model_new.h5')
# labels = open('labels.txt', 'r').readlines()


global linux, canny
linux=0
canny=0

if linux==1 and canny==1:
    discCascade = cv2.CascadeClassifier("cascades/linux_canny_cascade_disc.xml")
    hexagonCascade = cv2.CascadeClassifier("cascades/linux_canny_cascade_hexagon.xml")
    octogonCascade = cv2.CascadeClassifier("cascades/linux_canny_cascade_octogon.xml")
    triangleCascade = cv2.CascadeClassifier("cascades/linux_canny_cascade_triangle.xml")
elif linux==1 and canny==0:
    discCascade = cv2.CascadeClassifier("cascades/linux_cascade_disc.xml")
    hexagonCascade = cv2.CascadeClassifier("cascades/linux_cascade_hexagon.xml")
    octogonCascade = cv2.CascadeClassifier("cascades/linux_cascade_octogon.xml")
    triangleCascade = cv2.CascadeClassifier("cascades/linux_cascade_triangle.xml")
elif linux==0 and canny==1:
    discCascade = cv2.CascadeClassifier("cascades/canny_cascade_disc.xml")
    hexagonCascade = cv2.CascadeClassifier("cascades/canny_cascade_hexagon.xml")
    octogonCascade = cv2.CascadeClassifier("cascades/canny_cascade_octogon.xml")
    triangleCascade = cv2.CascadeClassifier("cascades/canny_cascade_triangle.xml")
else:
    discCascade = cv2.CascadeClassifier("cascades/cascade_disc.xml")
    hexagonCascade = cv2.CascadeClassifier("cascades/cascade_hexagon.xml")
    octogonCascade = cv2.CascadeClassifier("cascades/cascade_octogon.xml")
    triangleCascade = cv2.CascadeClassifier("cascades/cascade_triangle.xml")


print('Programa iniciado')

client = RemoteAPIClient()
sim = client.getObject('sim')

executedMovId = 'notReady'

# Set-up some movement variables:
mVel = 100 * np.pi / 180
mAccel = 150 * np.pi / 180
mJerk = 100 * np.pi / 180
maxVel=[mVel,mVel,mVel,mVel,mVel,mVel]
maxAccel=[mAccel,mAccel,mAccel,mAccel,mAccel,mAccel]
maxJerk=[mJerk,mJerk,mJerk,mJerk,mJerk,mJerk]

global currentConf
currentConf = [0, 0, 0, 0, 0, 0]

maxVel = 0.005
maxAccel = 0.005


cv2.namedWindow("Camera")
cv2.resizeWindow("Camera",imgWidth,imgHeight)
cv2.createTrackbar("Scale","Camera",50,100,empty)
cv2.createTrackbar("Neig","Camera",0,50,empty)
#cv2.createTrackbar("Min Area","Camera",33000,100000,empty)
cv2.createTrackbar("cMax","Camera",500,1000,empty)
cv2.createTrackbar("cMin","Camera",200,1000,empty)


# When simulation is not running, ZMQ message handling could be a bit
# slow, since the idle loop runs at 8 Hz by default. So let's make
# sure that the idle loop runs at full speed for this program:
defaultIdleFps = sim.getInt32Param(sim.intparam_idle_fps)
sim.setInt32Param(sim.intparam_idle_fps, 0)


#client.setStepping(True)
operando = True

## VARIAVEIS DE VERIFICAÇÃO DE ÚLTIMA ANÁLISE
analyzed = True # True = Peças / False = Caixas
escape = 0
limit = 2

sim.startSimulation()
waitForMovementExecuted('ready')
#initialPose, initialConfig = sim.callScriptFunction('remoteApi_getPoseAndConfig',handles.script)

while (operando):
    if analyzed:
        partsAnalyze()
    else:
        boxAnalyze()
    
    ###

    ###
    
    if analyzed:
        analyzed = False
        posZero()
        escape = escape+1
    else:
        analyzed = True
        posZero()
        escape = escape+1
    
    if escape == limit:
        operando = False

sim.stopSimulation()

# Restore the original idle loop frequency:
sim.setInt32Param(sim.intparam_idle_fps, defaultIdleFps)

#input("Pressione qualquer tecla para finalizar.")
cv2.destroyAllWindows()

print('Program ended')


"""
Rotina do Robô:
    Vasculhar a área de peças;
    Após encontrar uma peça, deverá:
        reconhecer qual formato;
        pegar peça;
        colocá-la no local adequado (possivelmente ajustando sua orientação);
        retornar a vasculhar a área para encontrar outra peça;    
"""

