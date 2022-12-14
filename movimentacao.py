# Make sure to have CoppeliaSim running, with followig scene loaded:
#
# scenes/messaging/ikMovementViaRemoteApi.ttt
#
# Do not launch simulation, then run this script

from zmqRemoteApi import RemoteAPIClient

print('Program started')

client = RemoteAPIClient()
sim = client.getObject('sim')

executedMovId = 'notReady'
targetArm = '/LBRiiwa14R820'
ObjC1 = '/ObjC1'
ObjC2 = '/ObjC2'
ObjP1 = '/ObjP1'
ObjP2 = '/ObjP2'
stringSignalName = targetArm + '_executedMovId'
objHandle = sim.getObject(targetArm)
scriptHandle = sim.getScript(sim.scripttype_childscript,objHandle)


def waitForMovementExecuted(id_):
    global executedMovId, stringSignalName
    while executedMovId != id_:
        s = sim.getStringSignal(stringSignalName)
        executedMovId = s


# Set-up some movement variables:
maxVel = 0.1
maxAccel = 0.01

# Start simulation:
sim.startSimulation()

# Wait until ready:
waitForMovementExecuted('ready')

# Get initial pose:
initialPose, initialConfig = sim.callScriptFunction('remoteApi_getPoseAndConfig',scriptHandle)

# Send first movement sequence:
targetPose=sim.getObjectPose(sim.getObject(ObjP1),sim.handle_world)
movementData = {
    'id': 'movSeq1',
    'targetPose': targetPose,
    'maxVel': maxVel,
    'maxAccel': maxAccel
}
sim.callScriptFunction('remoteApi_movementDataFunction',scriptHandle,movementData)

# Execute first movement sequence:
sim.callScriptFunction('remoteApi_executeMovement',scriptHandle,'movSeq1')

# Wait until above movement sequence finished executing:
#waitForMovementExecuted('movSeq1')

# Send second and third movement sequence, where third one should execute
# immediately after the second one:
targetPose=sim.getObjectPose(sim.getObject(ObjP2),sim.handle_world)
movementData = {
    'id': 'movSeq2',
    'targetPose': targetPose,
    'maxVel': maxVel,
    'maxAccel': maxAccel
}
sim.callScriptFunction('remoteApi_movementDataFunction',scriptHandle,movementData)


# Execute second and third movement sequence:
sim.callScriptFunction('remoteApi_executeMovement',scriptHandle,'movSeq2')
waitForMovementExecuted('movSeq2')


movementData = {
    'id': 'movInit',
    'targetPose': initialPose,
    'maxVel': maxVel,
    'maxAccel': maxAccel
}
sim.callScriptFunction('remoteApi_movementDataFunction',scriptHandle,movementData)

sim.callScriptFunction('remoteApi_executeMovement',scriptHandle,'movInit')

# Wait until above 2 movement sequences finished executing:
waitForMovementExecuted('movInit')


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

movementData = {
    'id': 'movInit',
    'targetPose': initialPose,
    'maxVel': maxVel,
    'maxAccel': maxAccel
}
sim.callScriptFunction('remoteApi_movementDataFunction',scriptHandle,movementData)

sim.callScriptFunction('remoteApi_executeMovement',scriptHandle,'movInit')

# Wait until above 2 movement sequences finished executing:
waitForMovementExecuted('movInit')

sim.stopSimulation()

print('Program ended')
