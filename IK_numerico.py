import numpy as np
from scipy import io, integrate, linalg, signal
import Articulado

def movement(init,target):
  N = 10
  Caminho = np.array(
      [-1,# * np.ones(N),
        0,# * np.ones(N),
        0,# * np.ones(N),
        
        0,# * np.ones(N),
        1,# * np.ones(N),
        0,# * np.ones(N),
              
        0,# * np.ones(N),
        0,# * np.ones(N),
        -1,# * np.ones(N),
              
        target[0],#np.linspace(init[0], target[0], num=N),
        target[1],#np.linspace(init[1], target[1], num=N),
        target[2]])#np.linspace(init[2], target[2], num=N)])
  Caminho = Caminho.reshape(12,1)

  L1 = 0.0661+0.0085
  L2 = 0.4251
  L3 = 0.3922
  L4 = 0.0397+0.0703
  L5 = 0.0492+0.04545
  L6 = 0.0996-0.02465

  th1 = np.deg2rad(90)
  th2 = np.deg2rad(-60)
  th3 = np.deg2rad(100)
  th4 = np.deg2rad(140)
  th5 = np.deg2rad(180)
  th6 = np.deg2rad(90)
  '''th1 = np.deg2rad(0)
  th2 = np.deg2rad(0)
  th3 = np.deg2rad(0)
  th4 = np.deg2rad(0)
  th5 = np.deg2rad(0)
  th6 = np.deg2rad(0)'''
  Th = np.array([th1,th2,th3,th4,th5,th6])
  Th = Th.reshape(6,1)
  TH=Th
  F0 = np.eye(4)
  F1 = Articulado.ArticuladoF1(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
  F2 = Articulado.ArticuladoF2(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
  F3 = Articulado.ArticuladoF3(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
  F4 = Articulado.ArticuladoF4(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
  F5 = Articulado.ArticuladoF5(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
  F6 = Articulado.ArticuladoF6(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)

  for index,x in np.ndenumerate(F6):
    if index[0]==3:
      break
    elif index==(0,0):
      fe=np.array([x])
    else:
      fe=np.append(fe,np.array([x]),axis=0)

  fe = fe.reshape(12,1)
  n = 0.2
  ksi= (0.01)**2

  for k in range(Caminho.shape[1]):
    fg = Caminho.T[k]
    fg = fg.reshape(12,1)
    F1 = Articulado.ArticuladoF1(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
    F2 = Articulado.ArticuladoF2(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
    F3 = Articulado.ArticuladoF3(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
    F4 = Articulado.ArticuladoF4(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
    F5 = Articulado.ArticuladoF5(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
    F6 = Articulado.ArticuladoF6(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
    aux = np.append(F6[0:3,0],np.append(F6[0:3,1],np.append(F6[0:3,2],F6[0:3,3])))
    aux = aux.reshape(12,1)
    fe = np.concatenate((fe,aux),1)
    aux = fe[:,-1]
    aux = aux.reshape(12,1)
    E = 0.5 * (fg - aux).T @ (fg - aux)
    while E.item() > ksi :
      dE = -(fg-aux)
      J = Articulado.ArticuladoJacobiano(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
      dTh = linalg.pinv(J) @ dE
      Th = Th - n * dTh
      th1 = Th.item(0)
      th2 = Th.item(1)
      th3 = Th.item(2)
      th4 = Th.item(3)
      th5 = Th.item(4)
      th6 = Th.item(5)
      F1 = Articulado.ArticuladoF1(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
      F2 = Articulado.ArticuladoF2(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
      F3 = Articulado.ArticuladoF3(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
      F4 = Articulado.ArticuladoF4(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
      F5 = Articulado.ArticuladoF5(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
      F6 = Articulado.ArticuladoF6(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
      aux = np.append(F6[0:3,0],np.append(F6[0:3,1],np.append(F6[0:3,2],F6[0:3,3])))
      aux = aux.reshape(12,1)
      fe = np.concatenate((fe,aux),1)
      aux = fe[:,-1]
      aux = aux.reshape(12,1)
      E = 0.5 * (fg - aux).T @ (fg - aux)
      print("Error:",E,"- ksi:",k)
    TH = np.concatenate((TH,Th),1)
  return(TH.transpose()[-1])


'''
N = np.arange(-1,1,0.1)
Caminho1 = np.array(
    [-1 * np.ones(N.size),
      0 * np.ones(N.size),
      0 * np.ones(N.size),
       
      0 * np.ones(N.size),
      1 * np.ones(N.size),
      0 * np.ones(N.size),
            
      0 * np.ones(N.size),
      0 * np.ones(N.size),
     -1 * np.ones(N.size),
            
     -0.5 * np.ones(N.size),
     -0.350 * N,
      0.25 * np.ones(N.size)])

Caminho2 = np.array(
    [-1 * np.ones(N.size),
      0 * np.ones(N.size),
      0 * np.ones(N.size),
       
      0 * np.ones(N.size),
      1 * np.ones(N.size),
      0 * np.ones(N.size),
            
      0 * np.ones(N.size),
      0 * np.ones(N.size),
     -1 * np.ones(N.size),
            
      0.5 * np.ones(N.size),
     -0.350 * N,
      0.25 * np.ones(N.size)])

Caminho = np.append(Caminho1,Caminho2,axis=1)
L1 = 0.0661+0.0085
L2 = 0.4251
L3 = 0.3922
L4 = 0.0397+0.0703
L5 = 0.0492+0.04545
L6 = 0.0996-0.02465

th1 = np.deg2rad(90)
th2 = np.deg2rad(-60)
th3 = np.deg2rad(100)
th4 = np.deg2rad(140)
th5 = np.deg2rad(180)
th6 = np.deg2rad(90)
Th = np.array([th1,th2,th3,th4,th5,th6])
Th = Th.reshape(6,1)
TH=Th
F0 = np.eye(4)
F1 = Articulado.ArticuladoF1(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
F2 = Articulado.ArticuladoF2(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
F3 = Articulado.ArticuladoF3(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
F4 = Articulado.ArticuladoF4(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
F5 = Articulado.ArticuladoF5(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
F6 = Articulado.ArticuladoF6(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)

for index,x in np.ndenumerate(F6):
  if index[0]==3:
    break
  elif index==(0,0):
    fe=np.array([x])
  else:
    fe=np.append(fe,np.array([x]),axis=0)

fe = fe.reshape(12,1)
n = 0.2
ksi= (0.01)**2

for k in range(Caminho.shape[1]):
  fg = Caminho.T[k]
  fg = fg.reshape(12,1)
  F1 = Articulado.ArticuladoF1(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
  F2 = Articulado.ArticuladoF2(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
  F3 = Articulado.ArticuladoF3(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
  F4 = Articulado.ArticuladoF4(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
  F5 = Articulado.ArticuladoF5(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
  F6 = Articulado.ArticuladoF6(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
  aux = np.append(F6[0:3,0],np.append(F6[0:3,1],np.append(F6[0:3,2],F6[0:3,3])))
  aux = aux.reshape(12,1)
  fe = np.concatenate((fe,aux),1)
  aux = fe[:,-1]
  aux = aux.reshape(12,1)
  E = 0.5 * (fg - aux).T @ (fg - aux)
  while E.item() > ksi :
    dE = -(fg-aux)
    J = Articulado.ArticuladoJacobiano(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
    dTh = linalg.pinv(J) @ dE
    Th = Th - n * dTh
    th1 = Th.item(0)
    th2 = Th.item(1)
    th3 = Th.item(2)
    th4 = Th.item(3)
    th5 = Th.item(4)
    th6 = Th.item(5)
    F1 = Articulado.ArticuladoF1(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
    F2 = Articulado.ArticuladoF2(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
    F3 = Articulado.ArticuladoF3(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
    F4 = Articulado.ArticuladoF4(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
    F5 = Articulado.ArticuladoF5(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
    F6 = Articulado.ArticuladoF6(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6)
    aux = np.append(F6[0:3,0],np.append(F6[0:3,1],np.append(F6[0:3,2],F6[0:3,3])))
    aux = aux.reshape(12,1)
    fe = np.concatenate((fe,aux),1)
    aux = fe[:,-1]
    aux = aux.reshape(12,1)
    E = 0.5 * (fg - aux).T @ (fg - aux)
  TH = np.concatenate((TH,Th),1)
print(TH)
'''