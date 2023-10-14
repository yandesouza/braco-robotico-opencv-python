# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 13:48:19 2022

@author: Yan de Souza Pereira
"""

import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

from zmqRemoteApi import RemoteAPIClient
import handles


def intermed(position):
    
    targetPose=sim.getObjectPose(sim.getObject(position),sim.handle_world)
    movementData = {
        'id': position,
        'targetPose': targetPose,
        'maxVel': maxVel * 0.1,
        'maxAccel': maxAccel * 0.1
    }
    sim.callScriptFunction('remoteApi_movementDataFunction',handles.script,movementData)
    sim.callScriptFunction('remoteApi_executeMovement',handles.script,position)
    waitForMovementExecuted(position)


# Interrompe execução de outras partes do código enquanto algum movimento é executado
def waitForMovementExecuted(id_):
    global executedMovId
    while executedMovId != id_:
        s = sim.getStringSignal(handles.stringSignalName)
        executedMovId = s
   
def positions():
        file2 = open("locais.txt")
        j=1
        loc={}
        while True:
            loc[j] = file2.readline()[:-1]
            if loc[j] == "quit":
                break
            j=j+1
        for j in loc:
            file1 = open("positions.txt", "a")
            if loc[j] == "quit":
                break
            intermed(loc[j])
            pos={}
            file1.write(str(loc[j]) + "\n")
            for i in handles.simJoints:
                pos = sim.getJointPosition(handles.simJoints[i])
                file1.write(""+str(pos)+";")
            file1.write("\n")
            file1.close()
        

print('Programa iniciado')

client = RemoteAPIClient()
sim = client.getObject('sim')

executedMovId = 'notReady'

maxVel = 0.05
maxAccel = 0.005
maxJerk = 80


# When simulation is not running, ZMQ message handling could be a bit
# slow, since the idle loop runs at 8 Hz by default. So let's make
# sure that the idle loop runs at full speed for this program:
defaultIdleFps = sim.getInt32Param(sim.intparam_idle_fps)
sim.setInt32Param(sim.intparam_idle_fps, 0)


sim.startSimulation()
waitForMovementExecuted('ready')

positions()

sim.stopSimulation()

# Restore the original idle loop frequency:
sim.setInt32Param(sim.intparam_idle_fps, defaultIdleFps)

print('Program ended')


