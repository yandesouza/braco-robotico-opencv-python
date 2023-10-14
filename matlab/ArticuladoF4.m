function F4 = ArticuladoF4(th1 , th2 , th3 , th4 , th5 , th6 , l1 , l2 , l3 , l4 , l5 , l6)

% Calculando cada um dos termos do frame

F4_11 = cos(th1 + th2 + th3 + th4)/2 - cos(th2 - th1 + th3 + th4)/2;
F4_12 = cos(th1);
F4_13 = sin(th2 - th1 + th3 + th4)/2 - sin(th1 + th2 + th3 + th4)/2;
F4_14 = l3*sin(th1)*sin(th2)*sin(th3) - l2*cos(th2)*sin(th1) - l3*cos(th2)*cos(th3)*sin(th1) - l4*cos(th1);

F4_21 = sin(th2 - th1 + th3 + th4)/2 + sin(th1 + th2 + th3 + th4)/2;
F4_22 = sin(th1);
F4_23 = cos(th1 + th2 + th3 + th4)/2 + cos(th2 - th1 + th3 + th4)/2;
F4_24 = l2*cos(th1)*cos(th2) - l4*sin(th1) + l3*cos(th1)*cos(th2)*cos(th3) - l3*cos(th1)*sin(th2)*sin(th3);

F4_31 = cos(th2 + th3 + th4);
F4_32 = 0;
F4_33 = -sin(th2 + th3 + th4);
F4_34 = l1 - l3*sin(th2 + th3) - l2*sin(th2);

F4_41 = 0;
F4_42 = 0;
F4_43 = 0;
F4_44 = 1;

% Frame F3 do robô
F4 = [F4_11 , F4_12 , F4_13 , F4_14;
      F4_21 , F4_22 , F4_23 , F4_24;
      F4_31 , F4_32 , F4_33 , F4_34;
      F4_41 , F4_42 , F4_43 , F4_44;];
  
end