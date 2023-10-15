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

import tensorflow as tf
from tensorflow import keras
#from tensorflow.keras import layers
from keras.models import load_model

from zmqRemoteApi import RemoteAPIClient
import handles
import positions as pos

######################################################
#####              BLOCO DE FUNÇÕES              #####
######################################################

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

# Salvar Imagens Capturadas
def saveDataFunc():
    global countFolder
    countFolder = 0
    while os.path.exists( myPath+ str(countFolder)):
        countFolder += 1
    os.makedirs(myPath + str(countFolder))

# Analise Peças
def partsAnalyze():
    movementData = {
        'id' : 'partsInit',
        'handles'    : handles.simJoints,
        'maxVelJ'    : [ maxVel ] * 7,
        'maxAccelJ'  : [ maxAccel ] * 7,
        'maxJerkJ'   : [ maxJerk ] * 7,
        'targetConf' : pos.ObjP1
    }
    sim.callScriptFunction('remoteApi_movementDataFunction',handles.script,movementData)

    movementData2 = {
        'id' : 'partsMid',
        'handles'    : handles.simJoints,
        'maxVelJ'    : [ maxVel ] * 7,
        'maxAccelJ'  : [ maxAccel ] * 7,
        'maxJerkJ'   : [ maxJerk ] * 7,
        'targetConf' : pos.ObjP2
    }
    sim.callScriptFunction('remoteApi_movementDataFunction',handles.script,movementData2)
    
    movementData3 = {
        'id' : 'partsEnd',
        'handles'    : handles.simJoints,
        'maxVelJ'    : [ maxVel ] * 7,
        'maxAccelJ'  : [ maxAccel ] * 7,
        'maxJerkJ'   : [ maxJerk ] * 7,
        'targetConf' : pos.ObjP3
    }

    sim.callScriptFunction('remoteApi_movementDataFunction',handles.script,movementData3)
    sim.callScriptFunction('remoteApi_executeMovement',handles.script,'partsInit')
    sim.callScriptFunction('remoteApi_executeMovement',handles.script,'partsMid')
    sim.callScriptFunction('remoteApi_executeMovement',handles.script,'partsEnd')
    waitForMovementExecuted('partsInit')
    camera('partsMid')
    camera('partsEnd')

# Analisa locais para depositar as peças
def boxAnalyze():
    movementData = {
        'id' : 'boxInit',
        'handles'    : handles.simJoints,
        'maxVelJ'    : [ maxVel ] * 7,
        'maxAccelJ'  : [ maxAccel ] * 7,
        'maxJerkJ'   : [ maxJerk ] * 7,
        'targetConf' : pos.ObjC1
    }
    sim.callScriptFunction('remoteApi_movementDataFunction',handles.script,movementData)

    movementData2 = {
        'id' : 'boxMid',
        'handles'    : handles.simJoints,
        'maxVelJ'    : [ maxVel ] * 7,
        'maxAccelJ'  : [ maxAccel ] * 7,
        'maxJerkJ'   : [ maxJerk ] * 7,
        'targetConf' : pos.ObjC2
    }
    sim.callScriptFunction('remoteApi_movementDataFunction',handles.script,movementData2)
    
    movementData3 = {
        'id' : 'boxEnd',
        'handles'    : handles.simJoints,
        'maxVelJ'    : [ maxVel ] * 7,
        'maxAccelJ'  : [ maxAccel ] * 7,
        'maxJerkJ'   : [ maxJerk ] * 7,
        'targetConf' : pos.ObjC3
    }

    sim.callScriptFunction('remoteApi_movementDataFunction',handles.script,movementData3)
    sim.callScriptFunction('remoteApi_executeMovement',handles.script,'boxInit')
    sim.callScriptFunction('remoteApi_executeMovement',handles.script,'boxMid')
    sim.callScriptFunction('remoteApi_executeMovement',handles.script,'boxEnd')
    waitForMovementExecuted('boxInit')
    camera('boxMid')
    camera('boxEnd')

# Ponto zero do manipulador
def posZero():
    movementData2 = {
        'id' : 'posZero',
        'handles'    : handles.simJoints,
        'maxVelJ'    : [ maxVel ] * 7,
        'maxAccelJ'  : [ maxAccel] * 7,
        'maxJerkJ'   : [ maxJerk ] * 7,
        'targetConf' : [ 0 ] * 7
    }

    sim.callScriptFunction('remoteApi_movementDataFunction',handles.script,movementData2)
    sim.callScriptFunction('remoteApi_executeMovement',handles.script,'posZero')
    
    waitForMovementExecuted('posZero')

# Interrompe execução de outras partes do código enquanto algum movimento é executado
def waitForMovementExecuted(id_):
    global executedMovId
    while executedMovId != id_:
        s = sim.getStringSignal(handles.stringSignalName)
        executedMovId = s


def empty(a):
    pass


def camera(id_):
    global img, executedMovId#, imgCanny, imgGray
    while executedMovId != id_:
        img, res = sim.getVisionSensorImg(handles.visionSensor)
        img = np.frombuffer(img, dtype=np.uint8).reshape(res[0], res[1], 3)
        img = cv2.flip(img, 0)
        

        # # TENSORFLOW CODE

        img_tf = cv2.resize(img, (224, 224), interpolation=cv2.INTER_AREA)
        # Make the image a numpy array and reshape it to the models input shape.
        img_tf = np.asarray(img_tf, dtype=np.float32).reshape(1, 224, 224, 3)
        # Normalize the image array
        img_tf = (img_tf / 127.5) - 1
        # Have the model predict what the current image is. Model.predict
        # returns an array of percentages. Example:[0.2,0.8] meaning its 20% sure
        # it is the first label and 80% sure its the second label.
        probabilities = model.predict(img_tf)
        # Print what the highest value probabilitie label
        print(labels[np.argmax(probabilities)])
        label = labels[np.argmax(probabilities)]
        if id_== 'partsEnd' :
            if label not in partsSeq:
                partsSeq.append(label)
        
        if id_== 'boxEnd' :
            if label not in boxSeq:
                boxSeq.append(label)


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
       
        """ img_tensor = tf.convert_to_tensor(img, dtype=tf.uint8)
        img_tensor = tf.expand_dims(img_tensor , 0)
        prediction = model.predict(img_tensor)
        boxes, scores, classes, num_detections = model(img_tensor) """

                
        #cv2.imshow('Camera', imgStack)
        cv2.imshow('Camera', img)
        cv2.waitKey(1)
        
        
        executedMovId = sim.getStringSignal(handles.stringSignalName)



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


model = load_model('keras_model_new.h5', compile=False)
labels = open('labels.txt', 'r').readlines()

global partsSeq, boxSeq
partsSeq = []
boxSeq = []


print('Programa iniciado')

client = RemoteAPIClient()
sim = client.getObject('sim')

executedMovId = 'notReady'

maxVel = 0.05
maxAccel = 0.01
maxJerk = 80

 
cv2.namedWindow("Camera")

# When simulation is not running, ZMQ message handling could be a bit
# slow, since the idle loop runs at 8 Hz by default. So let's make
# sure that the idle loop runs at full speed for this program:
defaultIdleFps = sim.getInt32Param(sim.intparam_idle_fps)
sim.setInt32Param(sim.intparam_idle_fps, 0)


operando = True

## VARIAVEIS DE VERIFICAÇÃO DE ÚLTIMA ANÁLISE
analyzed = True # True = Peças / False = Caixas
escape = 0
limit = 2

sim.startSimulation()
waitForMovementExecuted('ready')

while (operando):
    if analyzed:
        partsAnalyze()
    else:
        boxAnalyze()
    
    ###

    ###
    
    if analyzed:
        analyzed = False
        escape = escape+1
    else:
        analyzed = True
        escape = escape+1
    
    if escape == limit:
        operando = False

posZero()
sim.stopSimulation()

# Restore the original idle loop frequency:
sim.setInt32Param(sim.intparam_idle_fps, defaultIdleFps)

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

