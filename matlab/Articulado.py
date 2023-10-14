import numpy as np

def ArticuladoF1(th1 , th2 , th3 , th4 , th5 , th6 , l1 , l2 , l3 , l4 , l5 , l6):
    F1 = [[ -np.sin(th1),  0, -np.cos(th1),  0], 
          [  np.cos(th1),  0, -np.sin(th1),  0], 
          [            0, -1,            0, l1], 
          [            0,  0,            0,  1]]
    return np.array(F1)

def ArticuladoF2(th1 , th2 , th3 , th4 , th5 , th6 , l1 , l2 , l3 , l4 , l5 , l6):
    F2 = [[ -np.cos(th2)*np.sin(th1),  np.sin(th1)*np.sin(th2), -np.cos(th1), -l2*np.cos(th2)*np.sin(th1)],
          [  np.cos(th1)*np.cos(th2), -np.cos(th1)*np.sin(th2), -np.sin(th1),  l2*np.cos(th1)*np.cos(th2)],
          [             -np.sin(th2),             -np.cos(th2),            0,         l1 - l2*np.sin(th2)],
          [                        0,                        0,            0,                           1]]
    return np.array(F2)

def ArticuladoF3(th1 , th2 , th3 , th4 , th5 , th6 , l1 , l2 , l3 , l4 , l5 , l6):
    F3_11 = -np.cos(th2 + th3)*np.sin(th1)
    F3_12 = np.sin(th2 + th3)*np.sin(th1) 
    F3_13 = -np.cos(th1)
    F3_14 = -np.sin(th1)*(l3*np.cos(th2 + th3) + l2*np.cos(th2))

    F3_21 = np.cos(th2 + th3)*np.cos(th1)
    F3_22 = -np.sin(th2 + th3)*np.cos(th1)
    F3_23 = -np.sin(th1)
    F3_24 = np.cos(th1)*(l3*np.cos(th2 + th3) + l2*np.cos(th2))

    F3_31 = -np.sin(th2 + th3)
    F3_32 = -np.cos(th2 + th3)
    F3_33 = 0
    F3_34 = l1 - l3*np.sin(th2 + th3) - l2*np.sin(th2)

    F3_41 = 0
    F3_42 = 0
    F3_43 = 0
    F3_44 = 1

    F3 = [[F3_11 , F3_12 , F3_13 , F3_14],
          [F3_21 , F3_22 , F3_23 , F3_24],
          [F3_31 , F3_32 , F3_33 , F3_34],
          [F3_41 , F3_42 , F3_43 , F3_44]]
    return np.array(F3)

def ArticuladoF4(th1 , th2 , th3 , th4 , th5 , th6 , l1 , l2 , l3 , l4 , l5 , l6):
    F4_11 = np.cos(th1 + th2 + th3 + th4)/2 - np.cos(th2 - th1 + th3 + th4)/2
    F4_12 = np.cos(th1)
    F4_13 = np.sin(th2 - th1 + th3 + th4)/2 - np.sin(th1 + th2 + th3 + th4)/2
    F4_14 = l3*np.sin(th1)*np.sin(th2)*np.sin(th3) - l2*np.cos(th2)*np.sin(th1) - l3*np.cos(th2)*np.cos(th3)*np.sin(th1) - l4*np.cos(th1)

    F4_21 = np.sin(th2 - th1 + th3 + th4)/2 + np.sin(th1 + th2 + th3 + th4)/2
    F4_22 = np.sin(th1)
    F4_23 = np.cos(th1 + th2 + th3 + th4)/2 + np.cos(th2 - th1 + th3 + th4)/2
    F4_24 = l2*np.cos(th1)*np.cos(th2) - l4*np.sin(th1) + l3*np.cos(th1)*np.cos(th2)*np.cos(th3) - l3*np.cos(th1)*np.sin(th2)*np.sin(th3)

    F4_31 = np.cos(th2 + th3 + th4)
    F4_32 = 0
    F4_33 = -np.sin(th2 + th3 + th4)
    F4_34 = l1 - l3*np.sin(th2 + th3) - l2*np.sin(th2)

    F4_41 = 0
    F4_42 = 0
    F4_43 = 0
    F4_44 = 1

    F4 = [[F4_11 , F4_12 , F4_13 , F4_14],
          [F4_21 , F4_22 , F4_23 , F4_24],
          [F4_31 , F4_32 , F4_33 , F4_34],
          [F4_41 , F4_42 , F4_43 , F4_44]]
    return np.array(F4)

def ArticuladoF5(th1 , th2 , th3 , th4 , th5 , th6 , l1 , l2 , l3 , l4 , l5 , l6):
      F5_11 = np.cos(th1)*np.cos(th5) + np.cos(th2)*np.cos(th3)*np.sin(th1)*np.sin(th4)*np.sin(th5) + np.cos(th2)*np.cos(th4)*np.sin(th1)*np.sin(th3)*np.sin(th5) + np.cos(th3)*np.cos(th4)*np.sin(th1)*np.sin(th2)*np.sin(th5) - np.sin(th1)*np.sin(th2)*np.sin(th3)*np.sin(th4)*np.sin(th5)
      F5_12 = np.sin(th1 + th2 + th3 + th4)/2 - np.sin(th2 - th1 + th3 + th4)/2
      F5_13 = np.cos(th2)*np.cos(th3)*np.cos(th5)*np.sin(th1)*np.sin(th4) - np.cos(th1)*np.sin(th5) + np.cos(th2)*np.cos(th4)*np.cos(th5)*np.sin(th1)*np.sin(th3) + np.cos(th3)*np.cos(th4)*np.cos(th5)*np.sin(th1)*np.sin(th2) - np.cos(th5)*np.sin(th1)*np.sin(th2)*np.sin(th3)*np.sin(th4)
      F5_14 = l3*np.sin(th1)*np.sin(th2)*np.sin(th3) - l2*np.cos(th2)*np.sin(th1) - l3*np.cos(th2)*np.cos(th3)*np.sin(th1) - l4*np.cos(th1) - l5*np.cos(th2)*np.cos(th3)*np.cos(th4)*np.sin(th1) + l5*np.cos(th2)*np.sin(th1)*np.sin(th3)*np.sin(th4) + l5*np.cos(th3)*np.sin(th1)*np.sin(th2)*np.sin(th4) + l5*np.cos(th4)*np.sin(th1)*np.sin(th2)*np.sin(th3)

      F5_21 = np.cos(th5)*np.sin(th1) - np.cos(th1)*np.cos(th2)*np.cos(th3)*np.sin(th4)*np.sin(th5) - np.cos(th1)*np.cos(th2)*np.cos(th4)*np.sin(th3)*np.sin(th5) - np.cos(th1)*np.cos(th3)*np.cos(th4)*np.sin(th2)*np.sin(th5) + np.cos(th1)*np.sin(th2)*np.sin(th3)*np.sin(th4)*np.sin(th5)
      F5_22 = - np.cos(th1 + th2 + th3 + th4)/2 - np.cos(th2 - th1 + th3 + th4)/2
      F5_23 = np.cos(th1)*np.cos(th5)*np.sin(th2)*np.sin(th3)*np.sin(th4) - np.cos(th1)*np.cos(th2)*np.cos(th3)*np.cos(th5)*np.sin(th4) - np.cos(th1)*np.cos(th2)*np.cos(th4)*np.cos(th5)*np.sin(th3) - np.cos(th1)*np.cos(th3)*np.cos(th4)*np.cos(th5)*np.sin(th2) - np.sin(th1)*np.sin(th5)
      F5_24 = l2*np.cos(th1)*np.cos(th2) - l4*np.sin(th1) + l3*np.cos(th1)*np.cos(th2)*np.cos(th3) - l3*np.cos(th1)*np.sin(th2)*np.sin(th3) + l5*np.cos(th1)*np.cos(th2)*np.cos(th3)*np.cos(th4) - l5*np.cos(th1)*np.cos(th2)*np.sin(th3)*np.sin(th4) - l5*np.cos(th1)*np.cos(th3)*np.sin(th2)*np.sin(th4) - l5*np.cos(th1)*np.cos(th4)*np.sin(th2)*np.sin(th3)

      F5_31 = np.sin(th2 + th3 + th4 - th5)/2 - np.sin(th2 + th3 + th4 + th5)/2
      F5_32 = np.sin(th2 + th3 + th4)
      F5_33 = - np.cos(th2 + th3 + th4 + th5)/2 - np.cos(th2 + th3 + th4 - th5)/2
      F5_34 = l1 - l3*np.sin(th2 + th3) - l2*np.sin(th2) - l5*np.sin(th2 + th3 + th4)

      F5_41 = 0
      F5_42 = 0
      F5_43 = 0
      F5_44 = 1

      F5 = [[F5_11 , F5_12 , F5_13 , F5_14],
            [F5_21 , F5_22 , F5_23 , F5_24],
            [F5_31 , F5_32 , F5_33 , F5_34],
            [F5_41 , F5_42 , F5_43 , F5_44]]
      return np.array(F5)

def ArticuladoF6(th1 , th2 , th3 , th4 , th5 , th6 , l1 , l2 , l3 , l4 , l5 , l6):
      F6_11 = np.cos(th6)*(np.cos(th1)*np.cos(th5) + np.cos(th2)*np.cos(th3)*np.sin(th1)*np.sin(th4)*np.sin(th5) + np.cos(th2)*np.cos(th4)*np.sin(th1)*np.sin(th3)*np.sin(th5) + np.cos(th3)*np.cos(th4)*np.sin(th1)*np.sin(th2)*np.sin(th5) - np.sin(th1)*np.sin(th2)*np.sin(th3)*np.sin(th4)*np.sin(th5)) + np.cos(th2 + th3 + th4)*np.sin(th1)*np.sin(th6)
      F6_12 = np.cos(th2 + th3 + th4)*np.cos(th6)*np.sin(th1) - np.sin(th6)*(np.cos(th1)*np.cos(th5) + np.cos(th2)*np.cos(th3)*np.sin(th1)*np.sin(th4)*np.sin(th5) + np.cos(th2)*np.cos(th4)*np.sin(th1)*np.sin(th3)*np.sin(th5) + np.cos(th3)*np.cos(th4)*np.sin(th1)*np.sin(th2)*np.sin(th5) - np.sin(th1)*np.sin(th2)*np.sin(th3)*np.sin(th4)*np.sin(th5))
      F6_13 = np.cos(th2)*np.cos(th3)*np.cos(th5)*np.sin(th1)*np.sin(th4) - np.cos(th1)*np.sin(th5) + np.cos(th2)*np.cos(th4)*np.cos(th5)*np.sin(th1)*np.sin(th3) + np.cos(th3)*np.cos(th4)*np.cos(th5)*np.sin(th1)*np.sin(th2) - np.cos(th5)*np.sin(th1)*np.sin(th2)*np.sin(th3)*np.sin(th4)
      F6_14 = l3*np.sin(th1)*np.sin(th2)*np.sin(th3) - l2*np.cos(th2)*np.sin(th1) - l6*np.cos(th1)*np.sin(th5) - l3*np.cos(th2)*np.cos(th3)*np.sin(th1) - l4*np.cos(th1) - l5*np.cos(th2)*np.cos(th3)*np.cos(th4)*np.sin(th1) + l5*np.cos(th2)*np.sin(th1)*np.sin(th3)*np.sin(th4) + l5*np.cos(th3)*np.sin(th1)*np.sin(th2)*np.sin(th4) + l5*np.cos(th4)*np.sin(th1)*np.sin(th2)*np.sin(th3) + l6*np.cos(th2)*np.cos(th3)*np.cos(th5)*np.sin(th1)*np.sin(th4) + l6*np.cos(th2)*np.cos(th4)*np.cos(th5)*np.sin(th1)*np.sin(th3) + l6*np.cos(th3)*np.cos(th4)*np.cos(th5)*np.sin(th1)*np.sin(th2) - l6*np.cos(th5)*np.sin(th1)*np.sin(th2)*np.sin(th3)*np.sin(th4)

      F6_21 = - np.cos(th6)*(np.cos(th1)*np.cos(th2)*np.cos(th3)*np.sin(th4)*np.sin(th5) - np.cos(th5)*np.sin(th1) + np.cos(th1)*np.cos(th2)*np.cos(th4)*np.sin(th3)*np.sin(th5) + np.cos(th1)*np.cos(th3)*np.cos(th4)*np.sin(th2)*np.sin(th5) - np.cos(th1)*np.sin(th2)*np.sin(th3)*np.sin(th4)*np.sin(th5)) - np.cos(th2 + th3 + th4)*np.cos(th1)*np.sin(th6)
      F6_22 = np.sin(th6)*(np.cos(th1)*np.cos(th2)*np.cos(th3)*np.sin(th4)*np.sin(th5) - np.cos(th5)*np.sin(th1) + np.cos(th1)*np.cos(th2)*np.cos(th4)*np.sin(th3)*np.sin(th5) + np.cos(th1)*np.cos(th3)*np.cos(th4)*np.sin(th2)*np.sin(th5) - np.cos(th1)*np.sin(th2)*np.sin(th3)*np.sin(th4)*np.sin(th5)) - np.cos(th2 + th3 + th4)*np.cos(th1)*np.cos(th6)
      F6_23 = np.cos(th1)*np.cos(th5)*np.sin(th2)*np.sin(th3)*np.sin(th4) - np.cos(th1)*np.cos(th2)*np.cos(th3)*np.cos(th5)*np.sin(th4) - np.cos(th1)*np.cos(th2)*np.cos(th4)*np.cos(th5)*np.sin(th3) - np.cos(th1)*np.cos(th3)*np.cos(th4)*np.cos(th5)*np.sin(th2) - np.sin(th1)*np.sin(th5)
      F6_24 = l2*np.cos(th1)*np.cos(th2) - l4*np.sin(th1) - l6*np.sin(th1)*np.sin(th5) + l3*np.cos(th1)*np.cos(th2)*np.cos(th3) - l3*np.cos(th1)*np.sin(th2)*np.sin(th3) + l5*np.cos(th1)*np.cos(th2)*np.cos(th3)*np.cos(th4) - l5*np.cos(th1)*np.cos(th2)*np.sin(th3)*np.sin(th4) - l5*np.cos(th1)*np.cos(th3)*np.sin(th2)*np.sin(th4) - l5*np.cos(th1)*np.cos(th4)*np.sin(th2)*np.sin(th3) - l6*np.cos(th1)*np.cos(th2)*np.cos(th3)*np.cos(th5)*np.sin(th4) - l6*np.cos(th1)*np.cos(th2)*np.cos(th4)*np.cos(th5)*np.sin(th3) - l6*np.cos(th1)*np.cos(th3)*np.cos(th4)*np.cos(th5)*np.sin(th2) + l6*np.cos(th1)*np.cos(th5)*np.sin(th2)*np.sin(th3)*np.sin(th4)

      F6_31 = np.cos(th2 + th3 + th4 - th6)/2 - np.cos(th2 + th3 + th4 + th6)/2 - np.cos(th2 + th3 + th4)*np.cos(th6)*np.sin(th5)
      F6_32 = np.sin(th2 + th3 + th4 - th6)/2 + np.sin(th2 + th3 + th4 + th6)/2 + np.cos(th2 + th3 + th4)*np.sin(th5)*np.sin(th6)
      F6_33 = - np.cos(th2 + th3 + th4 + th5)/2 - np.cos(th2 + th3 + th4 - th5)/2
      F6_34 = l1 - (l6*np.cos(th2 + th3 + th4 + th5))/2 - l3*np.sin(th2 + th3) - l2*np.sin(th2) - (l6*np.cos(th2 + th3 + th4 - th5))/2 - l5*np.sin(th2 + th3 + th4)

      F6_41 = 0
      F6_42 = 0
      F6_43 = 0
      F6_44 = 1

      F6 = [[F6_11 , F6_12 , F6_13 , F6_14],
            [F6_21 , F6_22 , F6_23 , F6_24],
            [F6_31 , F6_32 , F6_33 , F6_34],
            [F6_41 , F6_42 , F6_43 , F6_44]]
      return np.array(F6)

def ArticuladoJacobiano(th1 , th2 , th3, th4 , th5 , th6 , l1 , l2 , l3 , l4 , l5 , l6):
      J011 = np.cos(th6)*(np.cos(th1)*np.cos(th2)*np.cos(th3)*np.sin(th4)*np.sin(th5) - np.cos(th5)*np.sin(th1) + np.cos(th1)*np.cos(th2)*np.cos(th4)*np.sin(th3)*np.sin(th5) + np.cos(th1)*np.cos(th3)*np.cos(th4)*np.sin(th2)*np.sin(th5) - np.cos(th1)*np.sin(th2)*np.sin(th3)*np.sin(th4)*np.sin(th5)) + np.cos(th2 + th3 + th4)*np.cos(th1)*np.sin(th6)
      J012 = -np.cos(th6)*(np.cos(th2)*np.sin(th1)*np.sin(th3)*np.sin(th4)*np.sin(th5) - np.cos(th2)*np.cos(th3)*np.cos(th4)*np.sin(th1)*np.sin(th5) + np.cos(th3)*np.sin(th1)*np.sin(th2)*np.sin(th4)*np.sin(th5) + np.cos(th4)*np.sin(th1)*np.sin(th2)*np.sin(th3)*np.sin(th5)) - np.sin(th2 + th3 + th4)*np.sin(th1)*np.sin(th6)
      J013 = -np.cos(th6)*(np.cos(th2)*np.sin(th1)*np.sin(th3)*np.sin(th4)*np.sin(th5) - np.cos(th2)*np.cos(th3)*np.cos(th4)*np.sin(th1)*np.sin(th5) + np.cos(th3)*np.sin(th1)*np.sin(th2)*np.sin(th4)*np.sin(th5) + np.cos(th4)*np.sin(th1)*np.sin(th2)*np.sin(th3)*np.sin(th5)) - np.sin(th2 + th3 + th4)*np.sin(th1)*np.sin(th6)
      J014 = -np.cos(th6)*(np.cos(th2)*np.sin(th1)*np.sin(th3)*np.sin(th4)*np.sin(th5) - np.cos(th2)*np.cos(th3)*np.cos(th4)*np.sin(th1)*np.sin(th5) + np.cos(th3)*np.sin(th1)*np.sin(th2)*np.sin(th4)*np.sin(th5) + np.cos(th4)*np.sin(th1)*np.sin(th2)*np.sin(th3)*np.sin(th5)) - np.sin(th2 + th3 + th4)*np.sin(th1)*np.sin(th6)
      J015 = np.cos(th6)*(np.cos(th2)*np.cos(th3)*np.cos(th5)*np.sin(th1)*np.sin(th4) - np.cos(th1)*np.sin(th5) + np.cos(th2)*np.cos(th4)*np.cos(th5)*np.sin(th1)*np.sin(th3) + np.cos(th3)*np.cos(th4)*np.cos(th5)*np.sin(th1)*np.sin(th2) - np.cos(th5)*np.sin(th1)*np.sin(th2)*np.sin(th3)*np.sin(th4))
      J016 = np.cos(th2 + th3 + th4)*np.cos(th6)*np.sin(th1) - np.sin(th6)*(np.cos(th1)*np.cos(th5) + np.cos(th2)*np.cos(th3)*np.sin(th1)*np.sin(th4)*np.sin(th5) + np.cos(th2)*np.cos(th4)*np.sin(th1)*np.sin(th3)*np.sin(th5) + np.cos(th3)*np.cos(th4)*np.sin(th1)*np.sin(th2)*np.sin(th5) - np.sin(th1)*np.sin(th2)*np.sin(th3)*np.sin(th4)*np.sin(th5))

      J021 = np.cos(th6)*(np.cos(th1)*np.cos(th5) + np.cos(th2)*np.cos(th3)*np.sin(th1)*np.sin(th4)*np.sin(th5) + np.cos(th2)*np.cos(th4)*np.sin(th1)*np.sin(th3)*np.sin(th5) + np.cos(th3)*np.cos(th4)*np.sin(th1)*np.sin(th2)*np.sin(th5) - np.sin(th1)*np.sin(th2)*np.sin(th3)*np.sin(th4)*np.sin(th5)) + np.cos(th2 + th3 + th4)*np.sin(th1)*np.sin(th6)
      J022 = np.cos(th6)*(np.cos(th1)*np.cos(th2)*np.sin(th3)*np.sin(th4)*np.sin(th5) - np.cos(th1)*np.cos(th2)*np.cos(th3)*np.cos(th4)*np.sin(th5) + np.cos(th1)*np.cos(th3)*np.sin(th2)*np.sin(th4)*np.sin(th5) + np.cos(th1)*np.cos(th4)*np.sin(th2)*np.sin(th3)*np.sin(th5)) + np.sin(th2 + th3 + th4)*np.cos(th1)*np.sin(th6)
      J023 = np.cos(th6)*(np.cos(th1)*np.cos(th2)*np.sin(th3)*np.sin(th4)*np.sin(th5) - np.cos(th1)*np.cos(th2)*np.cos(th3)*np.cos(th4)*np.sin(th5) + np.cos(th1)*np.cos(th3)*np.sin(th2)*np.sin(th4)*np.sin(th5) + np.cos(th1)*np.cos(th4)*np.sin(th2)*np.sin(th3)*np.sin(th5)) + np.sin(th2 + th3 + th4)*np.cos(th1)*np.sin(th6)
      J024 = np.cos(th6)*(np.cos(th1)*np.cos(th2)*np.sin(th3)*np.sin(th4)*np.sin(th5) - np.cos(th1)*np.cos(th2)*np.cos(th3)*np.cos(th4)*np.sin(th5) + np.cos(th1)*np.cos(th3)*np.sin(th2)*np.sin(th4)*np.sin(th5) + np.cos(th1)*np.cos(th4)*np.sin(th2)*np.sin(th3)*np.sin(th5)) + np.sin(th2 + th3 + th4)*np.cos(th1)*np.sin(th6)
      J025 = -np.cos(th6)*(np.sin(th1)*np.sin(th5) + np.cos(th1)*np.cos(th2)*np.cos(th3)*np.cos(th5)*np.sin(th4) + np.cos(th1)*np.cos(th2)*np.cos(th4)*np.cos(th5)*np.sin(th3) + np.cos(th1)*np.cos(th3)*np.cos(th4)*np.cos(th5)*np.sin(th2) - np.cos(th1)*np.cos(th5)*np.sin(th2)*np.sin(th3)*np.sin(th4))
      J026 = np.sin(th6)*(np.cos(th1)*np.cos(th2)*np.cos(th3)*np.sin(th4)*np.sin(th5) - np.cos(th5)*np.sin(th1) + np.cos(th1)*np.cos(th2)*np.cos(th4)*np.sin(th3)*np.sin(th5) + np.cos(th1)*np.cos(th3)*np.cos(th4)*np.sin(th2)*np.sin(th5) - np.cos(th1)*np.sin(th2)*np.sin(th3)*np.sin(th4)*np.sin(th5)) - np.cos(th2 + th3 + th4)*np.cos(th1)*np.cos(th6)

      J031 = 0
      J032 = np.sin(th2 + th3 + th4 + th6)/2 - np.sin(th2 + th3 + th4 - th6)/2 + np.sin(th2 + th3 + th4)*np.cos(th6)*np.sin(th5)
      J033 = np.sin(th2 + th3 + th4 + th6)/2 - np.sin(th2 + th3 + th4 - th6)/2 + np.sin(th2 + th3 + th4)*np.cos(th6)*np.sin(th5)
      J034 = np.sin(th2 + th3 + th4 + th6)/2 - np.sin(th2 + th3 + th4 - th6)/2 + np.sin(th2 + th3 + th4)*np.cos(th6)*np.sin(th5)
      J035 = -np.cos(th2 + th3 + th4)*np.cos(th5)*np.cos(th6)
      J036 = np.sin(th2 + th3 + th4 - th6)/2 + np.sin(th2 + th3 + th4 + th6)/2 + np.cos(th2 + th3 + th4)*np.sin(th5)*np.sin(th6)

      J041 = np.cos(th2 + th3 + th4)*np.cos(th1)*np.cos(th6) - np.sin(th6)*(np.cos(th1)*np.cos(th2)*np.cos(th3)*np.sin(th4)*np.sin(th5) - np.cos(th5)*np.sin(th1) + np.cos(th1)*np.cos(th2)*np.cos(th4)*np.sin(th3)*np.sin(th5) + np.cos(th1)*np.cos(th3)*np.cos(th4)*np.sin(th2)*np.sin(th5) - np.cos(th1)*np.sin(th2)*np.sin(th3)*np.sin(th4)*np.sin(th5))
      J042 = np.sin(th6)*(np.cos(th2)*np.sin(th1)*np.sin(th3)*np.sin(th4)*np.sin(th5) - np.cos(th2)*np.cos(th3)*np.cos(th4)*np.sin(th1)*np.sin(th5) + np.cos(th3)*np.sin(th1)*np.sin(th2)*np.sin(th4)*np.sin(th5) + np.cos(th4)*np.sin(th1)*np.sin(th2)*np.sin(th3)*np.sin(th5)) - np.sin(th2 + th3 + th4)*np.cos(th6)*np.sin(th1)
      J043 = np.sin(th6)*(np.cos(th2)*np.sin(th1)*np.sin(th3)*np.sin(th4)*np.sin(th5) - np.cos(th2)*np.cos(th3)*np.cos(th4)*np.sin(th1)*np.sin(th5) + np.cos(th3)*np.sin(th1)*np.sin(th2)*np.sin(th4)*np.sin(th5) + np.cos(th4)*np.sin(th1)*np.sin(th2)*np.sin(th3)*np.sin(th5)) - np.sin(th2 + th3 + th4)*np.cos(th6)*np.sin(th1)
      J044 = np.sin(th6)*(np.cos(th2)*np.sin(th1)*np.sin(th3)*np.sin(th4)*np.sin(th5) - np.cos(th2)*np.cos(th3)*np.cos(th4)*np.sin(th1)*np.sin(th5) + np.cos(th3)*np.sin(th1)*np.sin(th2)*np.sin(th4)*np.sin(th5) + np.cos(th4)*np.sin(th1)*np.sin(th2)*np.sin(th3)*np.sin(th5)) - np.sin(th2 + th3 + th4)*np.cos(th6)*np.sin(th1)
      J045 = -np.sin(th6)*(np.cos(th2)*np.cos(th3)*np.cos(th5)*np.sin(th1)*np.sin(th4) - np.cos(th1)*np.sin(th5) + np.cos(th2)*np.cos(th4)*np.cos(th5)*np.sin(th1)*np.sin(th3) + np.cos(th3)*np.cos(th4)*np.cos(th5)*np.sin(th1)*np.sin(th2) - np.cos(th5)*np.sin(th1)*np.sin(th2)*np.sin(th3)*np.sin(th4))
      J046 = -np.cos(th6)*(np.cos(th1)*np.cos(th5) + np.cos(th2)*np.cos(th3)*np.sin(th1)*np.sin(th4)*np.sin(th5) + np.cos(th2)*np.cos(th4)*np.sin(th1)*np.sin(th3)*np.sin(th5) + np.cos(th3)*np.cos(th4)*np.sin(th1)*np.sin(th2)*np.sin(th5) - np.sin(th1)*np.sin(th2)*np.sin(th3)*np.sin(th4)*np.sin(th5)) - np.cos(th2 + th3 + th4)*np.sin(th1)*np.sin(th6)

      J051 = np.cos(th2 + th3 + th4)*np.cos(th6)*np.sin(th1) - np.sin(th6)*(np.cos(th1)*np.cos(th5) + np.cos(th2)*np.cos(th3)*np.sin(th1)*np.sin(th4)*np.sin(th5) + np.cos(th2)*np.cos(th4)*np.sin(th1)*np.sin(th3)*np.sin(th5) + np.cos(th3)*np.cos(th4)*np.sin(th1)*np.sin(th2)*np.sin(th5) - np.sin(th1)*np.sin(th2)*np.sin(th3)*np.sin(th4)*np.sin(th5))
      J052 = np.sin(th2 + th3 + th4)*np.cos(th1)*np.cos(th6) - np.sin(th6)*(np.cos(th1)*np.cos(th2)*np.sin(th3)*np.sin(th4)*np.sin(th5) - np.cos(th1)*np.cos(th2)*np.cos(th3)*np.cos(th4)*np.sin(th5) + np.cos(th1)*np.cos(th3)*np.sin(th2)*np.sin(th4)*np.sin(th5) + np.cos(th1)*np.cos(th4)*np.sin(th2)*np.sin(th3)*np.sin(th5))
      J053 = np.sin(th2 + th3 + th4)*np.cos(th1)*np.cos(th6) - np.sin(th6)*(np.cos(th1)*np.cos(th2)*np.sin(th3)*np.sin(th4)*np.sin(th5) - np.cos(th1)*np.cos(th2)*np.cos(th3)*np.cos(th4)*np.sin(th5) + np.cos(th1)*np.cos(th3)*np.sin(th2)*np.sin(th4)*np.sin(th5) + np.cos(th1)*np.cos(th4)*np.sin(th2)*np.sin(th3)*np.sin(th5))
      J054 = np.sin(th2 + th3 + th4)*np.cos(th1)*np.cos(th6) - np.sin(th6)*(np.cos(th1)*np.cos(th2)*np.sin(th3)*np.sin(th4)*np.sin(th5) - np.cos(th1)*np.cos(th2)*np.cos(th3)*np.cos(th4)*np.sin(th5) + np.cos(th1)*np.cos(th3)*np.sin(th2)*np.sin(th4)*np.sin(th5) + np.cos(th1)*np.cos(th4)*np.sin(th2)*np.sin(th3)*np.sin(th5))
      J055 = np.sin(th6)*(np.sin(th1)*np.sin(th5) + np.cos(th1)*np.cos(th2)*np.cos(th3)*np.cos(th5)*np.sin(th4) + np.cos(th1)*np.cos(th2)*np.cos(th4)*np.cos(th5)*np.sin(th3) + np.cos(th1)*np.cos(th3)*np.cos(th4)*np.cos(th5)*np.sin(th2) - np.cos(th1)*np.cos(th5)*np.sin(th2)*np.sin(th3)*np.sin(th4))
      J056 = np.cos(th6)*(np.cos(th1)*np.cos(th2)*np.cos(th3)*np.sin(th4)*np.sin(th5) - np.cos(th5)*np.sin(th1) + np.cos(th1)*np.cos(th2)*np.cos(th4)*np.sin(th3)*np.sin(th5) + np.cos(th1)*np.cos(th3)*np.cos(th4)*np.sin(th2)*np.sin(th5) - np.cos(th1)*np.sin(th2)*np.sin(th3)*np.sin(th4)*np.sin(th5)) + np.cos(th2 + th3 + th4)*np.cos(th1)*np.sin(th6)

      J061 = 0
      J062 = np.cos(th2 + th3 + th4 + th6)/2 + np.cos(th2 + th3 + th4 - th6)/2 - np.sin(th2 + th3 + th4)*np.sin(th5)*np.sin(th6)
      J063 = np.cos(th2 + th3 + th4 + th6)/2 + np.cos(th2 + th3 + th4 - th6)/2 - np.sin(th2 + th3 + th4)*np.sin(th5)*np.sin(th6)
      J064 = np.cos(th2 + th3 + th4 + th6)/2 + np.cos(th2 + th3 + th4 - th6)/2 - np.sin(th2 + th3 + th4)*np.sin(th5)*np.sin(th6)
      J065 = np.cos(th2 + th3 + th4)*np.cos(th5)*np.sin(th6)
      J066 = np.cos(th2 + th3 + th4 + th6)/2 - np.cos(th2 + th3 + th4 - th6)/2 + np.cos(th2 + th3 + th4)*np.cos(th6)*np.sin(th5)

      J071 = np.sin(th1)*np.sin(th5) + np.cos(th1)*np.cos(th2)*np.cos(th3)*np.cos(th5)*np.sin(th4) + np.cos(th1)*np.cos(th2)*np.cos(th4)*np.cos(th5)*np.sin(th3) + np.cos(th1)*np.cos(th3)*np.cos(th4)*np.cos(th5)*np.sin(th2) - np.cos(th1)*np.cos(th5)*np.sin(th2)*np.sin(th3)*np.sin(th4)
      J072 = np.cos(th2 + th3 + th4)*np.cos(th5)*np.sin(th1)
      J073 = np.cos(th2 + th3 + th4)*np.cos(th5)*np.sin(th1)
      J074 = np.cos(th2 + th3 + th4)*np.cos(th5)*np.sin(th1)
      J075 = np.sin(th1)*np.sin(th2)*np.sin(th3)*np.sin(th4)*np.sin(th5) - np.cos(th2)*np.cos(th3)*np.sin(th1)*np.sin(th4)*np.sin(th5) - np.cos(th2)*np.cos(th4)*np.sin(th1)*np.sin(th3)*np.sin(th5) - np.cos(th3)*np.cos(th4)*np.sin(th1)*np.sin(th2)*np.sin(th5) - np.cos(th1)*np.cos(th5)
      J076 = 0

      J081 = np.cos(th2)*np.cos(th3)*np.cos(th5)*np.sin(th1)*np.sin(th4) - np.cos(th1)*np.sin(th5) + np.cos(th2)*np.cos(th4)*np.cos(th5)*np.sin(th1)*np.sin(th3) + np.cos(th3)*np.cos(th4)*np.cos(th5)*np.sin(th1)*np.sin(th2) - np.cos(th5)*np.sin(th1)*np.sin(th2)*np.sin(th3)*np.sin(th4)
      J082 = -np.cos(th2 + th3 + th4)*np.cos(th1)*np.cos(th5)
      J083 = -np.cos(th2 + th3 + th4)*np.cos(th1)*np.cos(th5)
      J084 = -np.cos(th2 + th3 + th4)*np.cos(th1)*np.cos(th5)
      J085 = np.cos(th1)*np.cos(th2)*np.cos(th3)*np.sin(th4)*np.sin(th5) - np.cos(th5)*np.sin(th1) + np.cos(th1)*np.cos(th2)*np.cos(th4)*np.sin(th3)*np.sin(th5) + np.cos(th1)*np.cos(th3)*np.cos(th4)*np.sin(th2)*np.sin(th5) - np.cos(th1)*np.sin(th2)*np.sin(th3)*np.sin(th4)*np.sin(th5)
      J086 = 0

      J091 = 0
      J092 = np.sin(th2 + th3 + th4 - th5)/2 + np.sin(th2 + th3 + th4 + th5)/2
      J093 = np.sin(th2 + th3 + th4 - th5)/2 + np.sin(th2 + th3 + th4 + th5)/2
      J094 = np.sin(th2 + th3 + th4 - th5)/2 + np.sin(th2 + th3 + th4 + th5)/2
      J095 = np.sin(th2 + th3 + th4 + th5)/2 - np.sin(th2 + th3 + th4 - th5)/2
      J096 = 0

      J101 = l4*np.sin(th1) - l2*np.cos(th1)*np.cos(th2) + l6*np.sin(th1)*np.sin(th5) - l3*np.cos(th1)*np.cos(th2)*np.cos(th3) + l3*np.cos(th1)*np.sin(th2)*np.sin(th3) - l5*np.cos(th1)*np.cos(th2)*np.cos(th3)*np.cos(th4) + l5*np.cos(th1)*np.cos(th2)*np.sin(th3)*np.sin(th4) + l5*np.cos(th1)*np.cos(th3)*np.sin(th2)*np.sin(th4) + l5*np.cos(th1)*np.cos(th4)*np.sin(th2)*np.sin(th3) + l6*np.cos(th1)*np.cos(th2)*np.cos(th3)*np.cos(th5)*np.sin(th4) + l6*np.cos(th1)*np.cos(th2)*np.cos(th4)*np.cos(th5)*np.sin(th3) + l6*np.cos(th1)*np.cos(th3)*np.cos(th4)*np.cos(th5)*np.sin(th2) - l6*np.cos(th1)*np.cos(th5)*np.sin(th2)*np.sin(th3)*np.sin(th4)
      J102 = np.sin(th1)*((l6*np.cos(th2 + th3 + th4 + th5))/2 + l3*np.sin(th2 + th3) + l2*np.sin(th2) + (l6*np.cos(th2 + th3 + th4 - th5))/2 + l5*np.sin(th2 + th3 + th4))
      J103 = np.sin(th1)*((l6*np.cos(th2 + th3 + th4 + th5))/2 + l3*np.sin(th2 + th3) + (l6*np.cos(th2 + th3 + th4 - th5))/2 + l5*np.sin(th2 + th3 + th4))
      J104 = np.sin(th1)*((l6*np.cos(th2 + th3 + th4 + th5))/2 + (l6*np.cos(th2 + th3 + th4 - th5))/2 + l5*np.sin(th2 + th3 + th4))
      J105 = l6*np.sin(th1)*np.sin(th2)*np.sin(th3)*np.sin(th4)*np.sin(th5) - l6*np.cos(th2)*np.cos(th3)*np.sin(th1)*np.sin(th4)*np.sin(th5) - l6*np.cos(th2)*np.cos(th4)*np.sin(th1)*np.sin(th3)*np.sin(th5) - l6*np.cos(th3)*np.cos(th4)*np.sin(th1)*np.sin(th2)*np.sin(th5) - l6*np.cos(th1)*np.cos(th5)
      J106 = 0

      J111 = l3*np.sin(th1)*np.sin(th2)*np.sin(th3) - l2*np.cos(th2)*np.sin(th1) - l6*np.cos(th1)*np.sin(th5) - l3*np.cos(th2)*np.cos(th3)*np.sin(th1) - l4*np.cos(th1) - l5*np.cos(th2)*np.cos(th3)*np.cos(th4)*np.sin(th1) + l5*np.cos(th2)*np.sin(th1)*np.sin(th3)*np.sin(th4) + l5*np.cos(th3)*np.sin(th1)*np.sin(th2)*np.sin(th4) + l5*np.cos(th4)*np.sin(th1)*np.sin(th2)*np.sin(th3) + l6*np.cos(th2)*np.cos(th3)*np.cos(th5)*np.sin(th1)*np.sin(th4) + l6*np.cos(th2)*np.cos(th4)*np.cos(th5)*np.sin(th1)*np.sin(th3) + l6*np.cos(th3)*np.cos(th4)*np.cos(th5)*np.sin(th1)*np.sin(th2) - l6*np.cos(th5)*np.sin(th1)*np.sin(th2)*np.sin(th3)*np.sin(th4)
      J112 = -np.cos(th1)*((l6*np.cos(th2 + th3 + th4 + th5))/2 + l3*np.sin(th2 + th3) + l2*np.sin(th2) + (l6*np.cos(th2 + th3 + th4 - th5))/2 + l5*np.sin(th2 + th3 + th4))
      J113 = -np.cos(th1)*((l6*np.cos(th2 + th3 + th4 + th5))/2 + l3*np.sin(th2 + th3) + (l6*np.cos(th2 + th3 + th4 - th5))/2 + l5*np.sin(th2 + th3 + th4))
      J114 = -np.cos(th1)*((l6*np.cos(th2 + th3 + th4 + th5))/2 + (l6*np.cos(th2 + th3 + th4 - th5))/2 + l5*np.sin(th2 + th3 + th4))
      J115 = l6*np.cos(th1)*np.cos(th2)*np.cos(th3)*np.sin(th4)*np.sin(th5) - l6*np.cos(th5)*np.sin(th1) + l6*np.cos(th1)*np.cos(th2)*np.cos(th4)*np.sin(th3)*np.sin(th5) + l6*np.cos(th1)*np.cos(th3)*np.cos(th4)*np.sin(th2)*np.sin(th5) - l6*np.cos(th1)*np.sin(th2)*np.sin(th3)*np.sin(th4)*np.sin(th5)
      J116 = 0

      J121 = 0
      J122 = (l6*np.sin(th2 + th3 + th4 + th5))/2 - l3*np.cos(th2 + th3) - l2*np.cos(th2) + (l6*np.sin(th2 + th3 + th4 - th5))/2 - l5*np.cos(th2 + th3 + th4)
      J123 = (l6*np.sin(th2 + th3 + th4 + th5))/2 - l3*np.cos(th2 + th3) + (l6*np.sin(th2 + th3 + th4 - th5))/2 - l5*np.cos(th2 + th3 + th4)
      J124 = (l6*np.sin(th2 + th3 + th4 + th5))/2 + (l6*np.sin(th2 + th3 + th4 - th5))/2 - l5*np.cos(th2 + th3 + th4)
      J125 = -(l6*(np.sin(th2 + th3 + th4 - th5) - np.sin(th2 + th3 + th4 + th5)))/2
      J126 = 0

      J = [ [J011 , J012 , J013 , J014 , J015 , J016],
            [J021 , J022 , J023 , J024 , J025 , J026],
            [J031 , J032 , J033 , J034 , J035 , J036],
            [J041 , J042 , J043 , J044 , J045 , J046],
            [J051 , J052 , J053 , J054 , J055 , J056],
            [J061 , J062 , J063 , J064 , J065 , J066],
            [J071 , J072 , J073 , J074 , J075 , J076],
            [J081 , J082 , J083 , J084 , J085 , J086],
            [J091 , J092 , J093 , J094 , J095 , J096],
            [J101 , J102 , J103 , J104 , J105 , J106],
            [J111 , J112 , J113 , J114 , J115 , J116],
            [J121 , J122 , J123 , J124 , J125 , J126]]
      return np.array(J)

