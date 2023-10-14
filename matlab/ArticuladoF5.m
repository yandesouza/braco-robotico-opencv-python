function F5 = ArticuladoF5(th1 , th2 , th3 , th4 , th5 , th6 , l1 , l2 , l3 , l4 , l5 , l6)

% Calculando cada um dos termos do frame
F5_11 = cos(th1)*cos(th5) + cos(th2)*cos(th3)*sin(th1)*sin(th4)*sin(th5) + cos(th2)*cos(th4)*sin(th1)*sin(th3)*sin(th5) + cos(th3)*cos(th4)*sin(th1)*sin(th2)*sin(th5) - sin(th1)*sin(th2)*sin(th3)*sin(th4)*sin(th5);
F5_12 = sin(th1 + th2 + th3 + th4)/2 - sin(th2 - th1 + th3 + th4)/2;
F5_13 = cos(th2)*cos(th3)*cos(th5)*sin(th1)*sin(th4) - cos(th1)*sin(th5) + cos(th2)*cos(th4)*cos(th5)*sin(th1)*sin(th3) + cos(th3)*cos(th4)*cos(th5)*sin(th1)*sin(th2) - cos(th5)*sin(th1)*sin(th2)*sin(th3)*sin(th4);
F5_14 = l3*sin(th1)*sin(th2)*sin(th3) - l2*cos(th2)*sin(th1) - l3*cos(th2)*cos(th3)*sin(th1) - l4*cos(th1) - l5*cos(th2)*cos(th3)*cos(th4)*sin(th1) + l5*cos(th2)*sin(th1)*sin(th3)*sin(th4) + l5*cos(th3)*sin(th1)*sin(th2)*sin(th4) + l5*cos(th4)*sin(th1)*sin(th2)*sin(th3);

F5_21 = cos(th5)*sin(th1) - cos(th1)*cos(th2)*cos(th3)*sin(th4)*sin(th5) - cos(th1)*cos(th2)*cos(th4)*sin(th3)*sin(th5) - cos(th1)*cos(th3)*cos(th4)*sin(th2)*sin(th5) + cos(th1)*sin(th2)*sin(th3)*sin(th4)*sin(th5);
F5_22 = - cos(th1 + th2 + th3 + th4)/2 - cos(th2 - th1 + th3 + th4)/2;
F5_23 = cos(th1)*cos(th5)*sin(th2)*sin(th3)*sin(th4) - cos(th1)*cos(th2)*cos(th3)*cos(th5)*sin(th4) - cos(th1)*cos(th2)*cos(th4)*cos(th5)*sin(th3) - cos(th1)*cos(th3)*cos(th4)*cos(th5)*sin(th2) - sin(th1)*sin(th5);
F5_24 = l2*cos(th1)*cos(th2) - l4*sin(th1) + l3*cos(th1)*cos(th2)*cos(th3) - l3*cos(th1)*sin(th2)*sin(th3) + l5*cos(th1)*cos(th2)*cos(th3)*cos(th4) - l5*cos(th1)*cos(th2)*sin(th3)*sin(th4) - l5*cos(th1)*cos(th3)*sin(th2)*sin(th4) - l5*cos(th1)*cos(th4)*sin(th2)*sin(th3);

F5_31 = sin(th2 + th3 + th4 - th5)/2 - sin(th2 + th3 + th4 + th5)/2;
F5_32 = sin(th2 + th3 + th4);
F5_33 = - cos(th2 + th3 + th4 + th5)/2 - cos(th2 + th3 + th4 - th5)/2;
F5_34 = l1 - l3*sin(th2 + th3) - l2*sin(th2) - l5*sin(th2 + th3 + th4);

F5_41 = 0;
F5_42 = 0;
F5_43 = 0;
F5_44 = 1;

% Frame F3 do robô
F5 = [F5_11 , F5_12 , F5_13 , F5_14;
      F5_21 , F5_22 , F5_23 , F5_24;
      F5_31 , F5_32 , F5_33 , F5_34;
      F5_41 , F5_42 , F5_43 , F5_44;];
  
end