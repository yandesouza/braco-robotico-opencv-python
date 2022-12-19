from zmqRemoteApi import RemoteAPIClient
import numpy as np


def AnalisaPecas():
    targetPose=sim.getObjectPose(sim.getObject(ObjP1),sim.handle_world)
    movementData = {
        'id': 'movSeq1',
        'targetPose': targetPose,
        'maxVel': maxVel,
        'maxAccel': maxAccel
    }
    sim.callScriptFunction('remoteApi_movementDataFunction',scriptHandle,movementData)

    targetPose=sim.getObjectPose(sim.getObject(ObjP2),sim.handle_world)
    movementData = {
        'id': 'movSeq2',
        'targetPose': targetPose,
        'maxVel': maxVel,
        'maxAccel': maxAccel
    }
    sim.callScriptFunction('remoteApi_movementDataFunction',scriptHandle,movementData)
    sim.callScriptFunction('remoteApi_executeMovement',scriptHandle,'movSeq1')
    sim.callScriptFunction('remoteApi_executeMovement',scriptHandle,'movSeq2')
    waitForMovementExecuted('movSeq2')


def AnalisaCaixas():
    targetPose=sim.getObjectPose(sim.getObject(ObjC1),sim.handle_world)
    movementData = {
        'id': 'movSeq3',
        'targetPose': targetPose,
        'maxVel': maxVel,
        'maxAccel': maxAccel
    }
    sim.callScriptFunction('remoteApi_movementDataFunction',scriptHandle,movementData)

    targetPose=sim.getObjectPose(sim.getObject(ObjC2),sim.handle_world)
    movementData = {
        'id': 'movSeq4',
        'targetPose': targetPose,
        'maxVel': maxVel,
        'maxAccel': maxAccel
    }
    sim.callScriptFunction('remoteApi_movementDataFunction',scriptHandle,movementData)
    sim.callScriptFunction('remoteApi_executeMovement',scriptHandle,'movSeq3')
    sim.callScriptFunction('remoteApi_executeMovement',scriptHandle,'movSeq4')
    waitForMovementExecuted('movSeq4')


def PosZero():
    # movementData = {
    #     'id': 'movInit',
    #     'targetPose': initialPose,
    #     'maxVel': maxVel,
    #     'maxAccel': maxAccel
    # }
    # sim.callScriptFunction('remoteApi_movementDataFunction',scriptHandle,movementData)
    # sim.callScriptFunction('remoteApi_executeMovement',scriptHandle,'movInit')
    # waitForMovementExecuted('movInit')
    vel=110  
    accel=40
    jerk=80
    movementData = {
        'id' : 'posZero',
        'handles' : simJoints,
        'maxVelJ' : [vel*np.pi/180,vel*np.pi/180,vel*np.pi/180,vel*np.pi/180,vel*np.pi/180,vel*np.pi/180,vel*np.pi/180],
        'maxAccelJ' : [accel*np.pi/180,accel*np.pi/180,accel*np.pi/180,accel*np.pi/180,accel*np.pi/180,accel*np.pi/180,accel*np.pi/180],
        'maxJerkJ' : [jerk*np.pi/180,jerk*np.pi/180,jerk*np.pi/180,jerk*np.pi/180,jerk*np.pi/180,jerk*np.pi/180,jerk*np.pi/180],
        'targetConf' : [0,0,0,0,0,0,0]
    }
    sim.callScriptFunction('moveToConfig',scriptHandle,movementData)


def waitForMovementExecuted(id_):
    global executedMovId, stringSignalName
    while executedMovId != id_:
        s = sim.getStringSignal(stringSignalName)
        executedMovId = s



#print('Program started')

client = RemoteAPIClient()
sim = client.getObject('sim')

executedMovId = 'notReady'
targetArm = '/LBRiiwa14R820'
ObjC1 = '/ObjC1'
ObjC2 = '/ObjC2'
ObjP1 = '/ObjP1'
ObjP2 = '/ObjP2'
stringSignalName = targetArm + '_executedMovId'
manipulatorHandle = sim.getObject(targetArm)
scriptHandle = sim.getScript(sim.scripttype_childscript,manipulatorHandle)

simJoints={}
for i in range(1,8,1):
    simJoints[i]=sim.getObject('./joint',{'index':i-1})



maxVel = 0.1
maxAccel = 0.01

# sim.startSimulation()

waitForMovementExecuted('ready')

initialPose, initialConfig = sim.callScriptFunction('remoteApi_getPoseAndConfig',scriptHandle)

# # PASSAGEM DA CÂMERA SOBRE AS PEÇAS PARA ANÁLISE
# AnalisaPecas()

# # PASSAGEM NO PONTO INICIAL PARA NÃO EXCEDER OS LIMITES DAS JUNTAS
# PosZero()

# # PASSAGEM DA CÂMERA SOBRE AS CAIXAS PARA ANÁLISE
# AnalisaCaixas()

# # RETORNO PARA A POSIÇÃO DE DESCANSO PARA FINALIZAÇÃO DO PROGRAMA
# PosZero()

# sim.stopSimulation()
# print('Program ended')
