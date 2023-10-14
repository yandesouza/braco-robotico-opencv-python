function F6 = ArticuladoF6(th1 , th2 , th3 , th4 , th5 , th6 , l1 , l2 , l3 , l4 , l5 , l6)

% Calculando cada um dos termos do frame
F6_11 = cos(th6)*(cos(th1)*cos(th5) + cos(th2)*cos(th3)*sin(th1)*sin(th4)*sin(th5) + cos(th2)*cos(th4)*sin(th1)*sin(th3)*sin(th5) + cos(th3)*cos(th4)*sin(th1)*sin(th2)*sin(th5) - sin(th1)*sin(th2)*sin(th3)*sin(th4)*sin(th5)) + cos(th2 + th3 + th4)*sin(th1)*sin(th6);
F6_12 = cos(th2 + th3 + th4)*cos(th6)*sin(th1) - sin(th6)*(cos(th1)*cos(th5) + cos(th2)*cos(th3)*sin(th1)*sin(th4)*sin(th5) + cos(th2)*cos(th4)*sin(th1)*sin(th3)*sin(th5) + cos(th3)*cos(th4)*sin(th1)*sin(th2)*sin(th5) - sin(th1)*sin(th2)*sin(th3)*sin(th4)*sin(th5));
F6_13 = cos(th2)*cos(th3)*cos(th5)*sin(th1)*sin(th4) - cos(th1)*sin(th5) + cos(th2)*cos(th4)*cos(th5)*sin(th1)*sin(th3) + cos(th3)*cos(th4)*cos(th5)*sin(th1)*sin(th2) - cos(th5)*sin(th1)*sin(th2)*sin(th3)*sin(th4);
F6_14 = l3*sin(th1)*sin(th2)*sin(th3) - l2*cos(th2)*sin(th1) - l6*cos(th1)*sin(th5) - l3*cos(th2)*cos(th3)*sin(th1) - l4*cos(th1) - l5*cos(th2)*cos(th3)*cos(th4)*sin(th1) + l5*cos(th2)*sin(th1)*sin(th3)*sin(th4) + l5*cos(th3)*sin(th1)*sin(th2)*sin(th4) + l5*cos(th4)*sin(th1)*sin(th2)*sin(th3) + l6*cos(th2)*cos(th3)*cos(th5)*sin(th1)*sin(th4) + l6*cos(th2)*cos(th4)*cos(th5)*sin(th1)*sin(th3) + l6*cos(th3)*cos(th4)*cos(th5)*sin(th1)*sin(th2) - l6*cos(th5)*sin(th1)*sin(th2)*sin(th3)*sin(th4);

F6_21 = - cos(th6)*(cos(th1)*cos(th2)*cos(th3)*sin(th4)*sin(th5) - cos(th5)*sin(th1) + cos(th1)*cos(th2)*cos(th4)*sin(th3)*sin(th5) + cos(th1)*cos(th3)*cos(th4)*sin(th2)*sin(th5) - cos(th1)*sin(th2)*sin(th3)*sin(th4)*sin(th5)) - cos(th2 + th3 + th4)*cos(th1)*sin(th6);
F6_22 = sin(th6)*(cos(th1)*cos(th2)*cos(th3)*sin(th4)*sin(th5) - cos(th5)*sin(th1) + cos(th1)*cos(th2)*cos(th4)*sin(th3)*sin(th5) + cos(th1)*cos(th3)*cos(th4)*sin(th2)*sin(th5) - cos(th1)*sin(th2)*sin(th3)*sin(th4)*sin(th5)) - cos(th2 + th3 + th4)*cos(th1)*cos(th6);
F6_23 = cos(th1)*cos(th5)*sin(th2)*sin(th3)*sin(th4) - cos(th1)*cos(th2)*cos(th3)*cos(th5)*sin(th4) - cos(th1)*cos(th2)*cos(th4)*cos(th5)*sin(th3) - cos(th1)*cos(th3)*cos(th4)*cos(th5)*sin(th2) - sin(th1)*sin(th5);
F6_24 = l2*cos(th1)*cos(th2) - l4*sin(th1) - l6*sin(th1)*sin(th5) + l3*cos(th1)*cos(th2)*cos(th3) - l3*cos(th1)*sin(th2)*sin(th3) + l5*cos(th1)*cos(th2)*cos(th3)*cos(th4) - l5*cos(th1)*cos(th2)*sin(th3)*sin(th4) - l5*cos(th1)*cos(th3)*sin(th2)*sin(th4) - l5*cos(th1)*cos(th4)*sin(th2)*sin(th3) - l6*cos(th1)*cos(th2)*cos(th3)*cos(th5)*sin(th4) - l6*cos(th1)*cos(th2)*cos(th4)*cos(th5)*sin(th3) - l6*cos(th1)*cos(th3)*cos(th4)*cos(th5)*sin(th2) + l6*cos(th1)*cos(th5)*sin(th2)*sin(th3)*sin(th4);

F6_31 = cos(th2 + th3 + th4 - th6)/2 - cos(th2 + th3 + th4 + th6)/2 - cos(th2 + th3 + th4)*cos(th6)*sin(th5);
F6_32 = sin(th2 + th3 + th4 - th6)/2 + sin(th2 + th3 + th4 + th6)/2 + cos(th2 + th3 + th4)*sin(th5)*sin(th6);
F6_33 = - cos(th2 + th3 + th4 + th5)/2 - cos(th2 + th3 + th4 - th5)/2;
F6_34 = l1 - (l6*cos(th2 + th3 + th4 + th5))/2 - l3*sin(th2 + th3) - l2*sin(th2) - (l6*cos(th2 + th3 + th4 - th5))/2 - l5*sin(th2 + th3 + th4);

F6_41 = 0;
F6_42 = 0;
F6_43 = 0;
F6_44 = 1;

% Frame F3 do robô
F6 = [F6_11 , F6_12 , F6_13 , F6_14;
      F6_21 , F6_22 , F6_23 , F6_24;
      F6_31 , F6_32 , F6_33 , F6_34;
      F6_41 , F6_42 , F6_43 , F6_44;];
  
end