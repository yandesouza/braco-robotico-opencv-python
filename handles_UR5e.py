from zmqRemoteApi import RemoteAPIClient

global stringSignalName, zero

client = RemoteAPIClient()
sim = client.getObject('sim')

targetArm = '/UR5'
manipulator = sim.getObject(targetArm)
visionSensor = sim.getObject('/Vision_sensor')
vacuum = sim.getObject('/suctionPad')

triangulo = sim.getObject('/Triangulo')
disco = sim.getObject('/Disco')
hexagono = sim.getObject('/Hexagono')
octogono = sim.getObject('/Octogono')

#pontos de movimentação
objC1 = '/ObjC1'
objC2 = '/ObjC2'
objP1 = '/ObjP1'
objP2 = '/ObjP2'
inter1 = '/Inter1'
inter2 = '/Inter2'
zero = '/Zero'

#posição das peças
posP1 = '/P1'
posP2 = '/P2'
posP3 = '/P3'
posP4 = '/P4'

#posição de encaixe das caixas
posC1 = '/C1'
posC2 = '/C2'
posC3 = '/C3'
posC4 = '/C4'

stringSignalName = targetArm + '_executedMovId'
script = sim.getScript(sim.scripttype_childscript,manipulator)

jointHandles={}
for i in range(1,7,1):
    jointHandles[i]=sim.getObject('./joint',{'index':i-1})