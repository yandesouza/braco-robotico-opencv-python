function F3 = ArticuladoF3(th1 , th2 , th3 , th4 , th5 , th6 , l1 , l2 , l3 , l4 , l5 , l6)

% Calculando cada um dos termos do frame
 
F3_11 = -cos(th2 + th3)*sin(th1);  
F3_12 = sin(th2 + th3)*sin(th1); 
F3_13 = -cos(th1);
F3_14 = -sin(th1)*(l3*cos(th2 + th3) + l2*cos(th2));

F3_21 = cos(th2 + th3)*cos(th1);
F3_22 = -sin(th2 + th3)*cos(th1);
F3_23 = -sin(th1);
F3_24 = cos(th1)*(l3*cos(th2 + th3) + l2*cos(th2));

F3_31 = -sin(th2 + th3);
F3_32 = -cos(th2 + th3);
F3_33 = 0;
F3_34 = l1 - l3*sin(th2 + th3) - l2*sin(th2);

F3_41 = 0;
F3_42 = 0;
F3_43 = 0;
F3_44 = 1;

% Frame F3 do robô
F3 = [F3_11 , F3_12 , F3_13 , F3_14;
      F3_21 , F3_22 , F3_23 , F3_24;
      F3_31 , F3_32 , F3_33 , F3_34;
      F3_41 , F3_42 , F3_43 , F3_44;];
  
end