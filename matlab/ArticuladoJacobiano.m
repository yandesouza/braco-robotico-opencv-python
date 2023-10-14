function J = ArticuladoJacobiano(th1 , th2 , th3, th4 , th5 , th6 , l1 , l2 , l3 , l4 , l5 , l6)

% Calculando cada um dos termos do Jacobiano
J011 = cos(th6)*(cos(th1)*cos(th2)*cos(th3)*sin(th4)*sin(th5) - cos(th5)*sin(th1) + cos(th1)*cos(th2)*cos(th4)*sin(th3)*sin(th5) + cos(th1)*cos(th3)*cos(th4)*sin(th2)*sin(th5) - cos(th1)*sin(th2)*sin(th3)*sin(th4)*sin(th5)) + cos(th2 + th3 + th4)*cos(th1)*sin(th6);
J012 = -cos(th6)*(cos(th2)*sin(th1)*sin(th3)*sin(th4)*sin(th5) - cos(th2)*cos(th3)*cos(th4)*sin(th1)*sin(th5) + cos(th3)*sin(th1)*sin(th2)*sin(th4)*sin(th5) + cos(th4)*sin(th1)*sin(th2)*sin(th3)*sin(th5)) - sin(th2 + th3 + th4)*sin(th1)*sin(th6);
J013 = -cos(th6)*(cos(th2)*sin(th1)*sin(th3)*sin(th4)*sin(th5) - cos(th2)*cos(th3)*cos(th4)*sin(th1)*sin(th5) + cos(th3)*sin(th1)*sin(th2)*sin(th4)*sin(th5) + cos(th4)*sin(th1)*sin(th2)*sin(th3)*sin(th5)) - sin(th2 + th3 + th4)*sin(th1)*sin(th6);
J014 = -cos(th6)*(cos(th2)*sin(th1)*sin(th3)*sin(th4)*sin(th5) - cos(th2)*cos(th3)*cos(th4)*sin(th1)*sin(th5) + cos(th3)*sin(th1)*sin(th2)*sin(th4)*sin(th5) + cos(th4)*sin(th1)*sin(th2)*sin(th3)*sin(th5)) - sin(th2 + th3 + th4)*sin(th1)*sin(th6);
J015 = cos(th6)*(cos(th2)*cos(th3)*cos(th5)*sin(th1)*sin(th4) - cos(th1)*sin(th5) + cos(th2)*cos(th4)*cos(th5)*sin(th1)*sin(th3) + cos(th3)*cos(th4)*cos(th5)*sin(th1)*sin(th2) - cos(th5)*sin(th1)*sin(th2)*sin(th3)*sin(th4));
J016 = cos(th2 + th3 + th4)*cos(th6)*sin(th1) - sin(th6)*(cos(th1)*cos(th5) + cos(th2)*cos(th3)*sin(th1)*sin(th4)*sin(th5) + cos(th2)*cos(th4)*sin(th1)*sin(th3)*sin(th5) + cos(th3)*cos(th4)*sin(th1)*sin(th2)*sin(th5) - sin(th1)*sin(th2)*sin(th3)*sin(th4)*sin(th5));

J021 = cos(th6)*(cos(th1)*cos(th5) + cos(th2)*cos(th3)*sin(th1)*sin(th4)*sin(th5) + cos(th2)*cos(th4)*sin(th1)*sin(th3)*sin(th5) + cos(th3)*cos(th4)*sin(th1)*sin(th2)*sin(th5) - sin(th1)*sin(th2)*sin(th3)*sin(th4)*sin(th5)) + cos(th2 + th3 + th4)*sin(th1)*sin(th6);
J022 = cos(th6)*(cos(th1)*cos(th2)*sin(th3)*sin(th4)*sin(th5) - cos(th1)*cos(th2)*cos(th3)*cos(th4)*sin(th5) + cos(th1)*cos(th3)*sin(th2)*sin(th4)*sin(th5) + cos(th1)*cos(th4)*sin(th2)*sin(th3)*sin(th5)) + sin(th2 + th3 + th4)*cos(th1)*sin(th6);
J023 = cos(th6)*(cos(th1)*cos(th2)*sin(th3)*sin(th4)*sin(th5) - cos(th1)*cos(th2)*cos(th3)*cos(th4)*sin(th5) + cos(th1)*cos(th3)*sin(th2)*sin(th4)*sin(th5) + cos(th1)*cos(th4)*sin(th2)*sin(th3)*sin(th5)) + sin(th2 + th3 + th4)*cos(th1)*sin(th6);
J024 = cos(th6)*(cos(th1)*cos(th2)*sin(th3)*sin(th4)*sin(th5) - cos(th1)*cos(th2)*cos(th3)*cos(th4)*sin(th5) + cos(th1)*cos(th3)*sin(th2)*sin(th4)*sin(th5) + cos(th1)*cos(th4)*sin(th2)*sin(th3)*sin(th5)) + sin(th2 + th3 + th4)*cos(th1)*sin(th6);
J025 = -cos(th6)*(sin(th1)*sin(th5) + cos(th1)*cos(th2)*cos(th3)*cos(th5)*sin(th4) + cos(th1)*cos(th2)*cos(th4)*cos(th5)*sin(th3) + cos(th1)*cos(th3)*cos(th4)*cos(th5)*sin(th2) - cos(th1)*cos(th5)*sin(th2)*sin(th3)*sin(th4));
J026 = sin(th6)*(cos(th1)*cos(th2)*cos(th3)*sin(th4)*sin(th5) - cos(th5)*sin(th1) + cos(th1)*cos(th2)*cos(th4)*sin(th3)*sin(th5) + cos(th1)*cos(th3)*cos(th4)*sin(th2)*sin(th5) - cos(th1)*sin(th2)*sin(th3)*sin(th4)*sin(th5)) - cos(th2 + th3 + th4)*cos(th1)*cos(th6);

J031 = 0;
J032 = sin(th2 + th3 + th4 + th6)/2 - sin(th2 + th3 + th4 - th6)/2 + sin(th2 + th3 + th4)*cos(th6)*sin(th5);
J033 = sin(th2 + th3 + th4 + th6)/2 - sin(th2 + th3 + th4 - th6)/2 + sin(th2 + th3 + th4)*cos(th6)*sin(th5);
J034 = sin(th2 + th3 + th4 + th6)/2 - sin(th2 + th3 + th4 - th6)/2 + sin(th2 + th3 + th4)*cos(th6)*sin(th5);
J035 = -cos(th2 + th3 + th4)*cos(th5)*cos(th6);
J036 = sin(th2 + th3 + th4 - th6)/2 + sin(th2 + th3 + th4 + th6)/2 + cos(th2 + th3 + th4)*sin(th5)*sin(th6);

J041 = cos(th2 + th3 + th4)*cos(th1)*cos(th6) - sin(th6)*(cos(th1)*cos(th2)*cos(th3)*sin(th4)*sin(th5) - cos(th5)*sin(th1) + cos(th1)*cos(th2)*cos(th4)*sin(th3)*sin(th5) + cos(th1)*cos(th3)*cos(th4)*sin(th2)*sin(th5) - cos(th1)*sin(th2)*sin(th3)*sin(th4)*sin(th5));
J042 = sin(th6)*(cos(th2)*sin(th1)*sin(th3)*sin(th4)*sin(th5) - cos(th2)*cos(th3)*cos(th4)*sin(th1)*sin(th5) + cos(th3)*sin(th1)*sin(th2)*sin(th4)*sin(th5) + cos(th4)*sin(th1)*sin(th2)*sin(th3)*sin(th5)) - sin(th2 + th3 + th4)*cos(th6)*sin(th1);
J043 = sin(th6)*(cos(th2)*sin(th1)*sin(th3)*sin(th4)*sin(th5) - cos(th2)*cos(th3)*cos(th4)*sin(th1)*sin(th5) + cos(th3)*sin(th1)*sin(th2)*sin(th4)*sin(th5) + cos(th4)*sin(th1)*sin(th2)*sin(th3)*sin(th5)) - sin(th2 + th3 + th4)*cos(th6)*sin(th1);
J044 = sin(th6)*(cos(th2)*sin(th1)*sin(th3)*sin(th4)*sin(th5) - cos(th2)*cos(th3)*cos(th4)*sin(th1)*sin(th5) + cos(th3)*sin(th1)*sin(th2)*sin(th4)*sin(th5) + cos(th4)*sin(th1)*sin(th2)*sin(th3)*sin(th5)) - sin(th2 + th3 + th4)*cos(th6)*sin(th1);
J045 = -sin(th6)*(cos(th2)*cos(th3)*cos(th5)*sin(th1)*sin(th4) - cos(th1)*sin(th5) + cos(th2)*cos(th4)*cos(th5)*sin(th1)*sin(th3) + cos(th3)*cos(th4)*cos(th5)*sin(th1)*sin(th2) - cos(th5)*sin(th1)*sin(th2)*sin(th3)*sin(th4));
J046 = -cos(th6)*(cos(th1)*cos(th5) + cos(th2)*cos(th3)*sin(th1)*sin(th4)*sin(th5) + cos(th2)*cos(th4)*sin(th1)*sin(th3)*sin(th5) + cos(th3)*cos(th4)*sin(th1)*sin(th2)*sin(th5) - sin(th1)*sin(th2)*sin(th3)*sin(th4)*sin(th5)) - cos(th2 + th3 + th4)*sin(th1)*sin(th6);

J051 = cos(th2 + th3 + th4)*cos(th6)*sin(th1) - sin(th6)*(cos(th1)*cos(th5) + cos(th2)*cos(th3)*sin(th1)*sin(th4)*sin(th5) + cos(th2)*cos(th4)*sin(th1)*sin(th3)*sin(th5) + cos(th3)*cos(th4)*sin(th1)*sin(th2)*sin(th5) - sin(th1)*sin(th2)*sin(th3)*sin(th4)*sin(th5));
J052 = sin(th2 + th3 + th4)*cos(th1)*cos(th6) - sin(th6)*(cos(th1)*cos(th2)*sin(th3)*sin(th4)*sin(th5) - cos(th1)*cos(th2)*cos(th3)*cos(th4)*sin(th5) + cos(th1)*cos(th3)*sin(th2)*sin(th4)*sin(th5) + cos(th1)*cos(th4)*sin(th2)*sin(th3)*sin(th5));
J053 = sin(th2 + th3 + th4)*cos(th1)*cos(th6) - sin(th6)*(cos(th1)*cos(th2)*sin(th3)*sin(th4)*sin(th5) - cos(th1)*cos(th2)*cos(th3)*cos(th4)*sin(th5) + cos(th1)*cos(th3)*sin(th2)*sin(th4)*sin(th5) + cos(th1)*cos(th4)*sin(th2)*sin(th3)*sin(th5));
J054 = sin(th2 + th3 + th4)*cos(th1)*cos(th6) - sin(th6)*(cos(th1)*cos(th2)*sin(th3)*sin(th4)*sin(th5) - cos(th1)*cos(th2)*cos(th3)*cos(th4)*sin(th5) + cos(th1)*cos(th3)*sin(th2)*sin(th4)*sin(th5) + cos(th1)*cos(th4)*sin(th2)*sin(th3)*sin(th5));
J055 = sin(th6)*(sin(th1)*sin(th5) + cos(th1)*cos(th2)*cos(th3)*cos(th5)*sin(th4) + cos(th1)*cos(th2)*cos(th4)*cos(th5)*sin(th3) + cos(th1)*cos(th3)*cos(th4)*cos(th5)*sin(th2) - cos(th1)*cos(th5)*sin(th2)*sin(th3)*sin(th4));
J056 = cos(th6)*(cos(th1)*cos(th2)*cos(th3)*sin(th4)*sin(th5) - cos(th5)*sin(th1) + cos(th1)*cos(th2)*cos(th4)*sin(th3)*sin(th5) + cos(th1)*cos(th3)*cos(th4)*sin(th2)*sin(th5) - cos(th1)*sin(th2)*sin(th3)*sin(th4)*sin(th5)) + cos(th2 + th3 + th4)*cos(th1)*sin(th6);

J061 = 0;
J062 = cos(th2 + th3 + th4 + th6)/2 + cos(th2 + th3 + th4 - th6)/2 - sin(th2 + th3 + th4)*sin(th5)*sin(th6);
J063 = cos(th2 + th3 + th4 + th6)/2 + cos(th2 + th3 + th4 - th6)/2 - sin(th2 + th3 + th4)*sin(th5)*sin(th6);
J064 = cos(th2 + th3 + th4 + th6)/2 + cos(th2 + th3 + th4 - th6)/2 - sin(th2 + th3 + th4)*sin(th5)*sin(th6);
J065 = cos(th2 + th3 + th4)*cos(th5)*sin(th6);
J066 = cos(th2 + th3 + th4 + th6)/2 - cos(th2 + th3 + th4 - th6)/2 + cos(th2 + th3 + th4)*cos(th6)*sin(th5);

J071 = sin(th1)*sin(th5) + cos(th1)*cos(th2)*cos(th3)*cos(th5)*sin(th4) + cos(th1)*cos(th2)*cos(th4)*cos(th5)*sin(th3) + cos(th1)*cos(th3)*cos(th4)*cos(th5)*sin(th2) - cos(th1)*cos(th5)*sin(th2)*sin(th3)*sin(th4);
J072 = cos(th2 + th3 + th4)*cos(th5)*sin(th1);
J073 = cos(th2 + th3 + th4)*cos(th5)*sin(th1);
J074 = cos(th2 + th3 + th4)*cos(th5)*sin(th1);
J075 = sin(th1)*sin(th2)*sin(th3)*sin(th4)*sin(th5) - cos(th2)*cos(th3)*sin(th1)*sin(th4)*sin(th5) - cos(th2)*cos(th4)*sin(th1)*sin(th3)*sin(th5) - cos(th3)*cos(th4)*sin(th1)*sin(th2)*sin(th5) - cos(th1)*cos(th5);
J076 = 0;

J081 = cos(th2)*cos(th3)*cos(th5)*sin(th1)*sin(th4) - cos(th1)*sin(th5) + cos(th2)*cos(th4)*cos(th5)*sin(th1)*sin(th3) + cos(th3)*cos(th4)*cos(th5)*sin(th1)*sin(th2) - cos(th5)*sin(th1)*sin(th2)*sin(th3)*sin(th4);
J082 = -cos(th2 + th3 + th4)*cos(th1)*cos(th5);
J083 = -cos(th2 + th3 + th4)*cos(th1)*cos(th5);
J084 = -cos(th2 + th3 + th4)*cos(th1)*cos(th5);
J085 = cos(th1)*cos(th2)*cos(th3)*sin(th4)*sin(th5) - cos(th5)*sin(th1) + cos(th1)*cos(th2)*cos(th4)*sin(th3)*sin(th5) + cos(th1)*cos(th3)*cos(th4)*sin(th2)*sin(th5) - cos(th1)*sin(th2)*sin(th3)*sin(th4)*sin(th5);
J086 = 0;

J091 = 0;
J092 = sin(th2 + th3 + th4 - th5)/2 + sin(th2 + th3 + th4 + th5)/2;
J093 = sin(th2 + th3 + th4 - th5)/2 + sin(th2 + th3 + th4 + th5)/2;
J094 = sin(th2 + th3 + th4 - th5)/2 + sin(th2 + th3 + th4 + th5)/2;
J095 = sin(th2 + th3 + th4 + th5)/2 - sin(th2 + th3 + th4 - th5)/2;
J096 = 0;

J101 = l4*sin(th1) - l2*cos(th1)*cos(th2) + l6*sin(th1)*sin(th5) - l3*cos(th1)*cos(th2)*cos(th3) + l3*cos(th1)*sin(th2)*sin(th3) - l5*cos(th1)*cos(th2)*cos(th3)*cos(th4) + l5*cos(th1)*cos(th2)*sin(th3)*sin(th4) + l5*cos(th1)*cos(th3)*sin(th2)*sin(th4) + l5*cos(th1)*cos(th4)*sin(th2)*sin(th3) + l6*cos(th1)*cos(th2)*cos(th3)*cos(th5)*sin(th4) + l6*cos(th1)*cos(th2)*cos(th4)*cos(th5)*sin(th3) + l6*cos(th1)*cos(th3)*cos(th4)*cos(th5)*sin(th2) - l6*cos(th1)*cos(th5)*sin(th2)*sin(th3)*sin(th4);
J102 = sin(th1)*((l6*cos(th2 + th3 + th4 + th5))/2 + l3*sin(th2 + th3) + l2*sin(th2) + (l6*cos(th2 + th3 + th4 - th5))/2 + l5*sin(th2 + th3 + th4));
J103 = sin(th1)*((l6*cos(th2 + th3 + th4 + th5))/2 + l3*sin(th2 + th3) + (l6*cos(th2 + th3 + th4 - th5))/2 + l5*sin(th2 + th3 + th4));
J104 = sin(th1)*((l6*cos(th2 + th3 + th4 + th5))/2 + (l6*cos(th2 + th3 + th4 - th5))/2 + l5*sin(th2 + th3 + th4));
J105 = l6*sin(th1)*sin(th2)*sin(th3)*sin(th4)*sin(th5) - l6*cos(th2)*cos(th3)*sin(th1)*sin(th4)*sin(th5) - l6*cos(th2)*cos(th4)*sin(th1)*sin(th3)*sin(th5) - l6*cos(th3)*cos(th4)*sin(th1)*sin(th2)*sin(th5) - l6*cos(th1)*cos(th5);
J106 = 0;

J111 = l3*sin(th1)*sin(th2)*sin(th3) - l2*cos(th2)*sin(th1) - l6*cos(th1)*sin(th5) - l3*cos(th2)*cos(th3)*sin(th1) - l4*cos(th1) - l5*cos(th2)*cos(th3)*cos(th4)*sin(th1) + l5*cos(th2)*sin(th1)*sin(th3)*sin(th4) + l5*cos(th3)*sin(th1)*sin(th2)*sin(th4) + l5*cos(th4)*sin(th1)*sin(th2)*sin(th3) + l6*cos(th2)*cos(th3)*cos(th5)*sin(th1)*sin(th4) + l6*cos(th2)*cos(th4)*cos(th5)*sin(th1)*sin(th3) + l6*cos(th3)*cos(th4)*cos(th5)*sin(th1)*sin(th2) - l6*cos(th5)*sin(th1)*sin(th2)*sin(th3)*sin(th4);
J112 = -cos(th1)*((l6*cos(th2 + th3 + th4 + th5))/2 + l3*sin(th2 + th3) + l2*sin(th2) + (l6*cos(th2 + th3 + th4 - th5))/2 + l5*sin(th2 + th3 + th4));
J113 = -cos(th1)*((l6*cos(th2 + th3 + th4 + th5))/2 + l3*sin(th2 + th3) + (l6*cos(th2 + th3 + th4 - th5))/2 + l5*sin(th2 + th3 + th4));
J114 = -cos(th1)*((l6*cos(th2 + th3 + th4 + th5))/2 + (l6*cos(th2 + th3 + th4 - th5))/2 + l5*sin(th2 + th3 + th4));
J115 = l6*cos(th1)*cos(th2)*cos(th3)*sin(th4)*sin(th5) - l6*cos(th5)*sin(th1) + l6*cos(th1)*cos(th2)*cos(th4)*sin(th3)*sin(th5) + l6*cos(th1)*cos(th3)*cos(th4)*sin(th2)*sin(th5) - l6*cos(th1)*sin(th2)*sin(th3)*sin(th4)*sin(th5);
J116 = 0;

J121 = 0;
J122 = (l6*sin(th2 + th3 + th4 + th5))/2 - l3*cos(th2 + th3) - l2*cos(th2) + (l6*sin(th2 + th3 + th4 - th5))/2 - l5*cos(th2 + th3 + th4);
J123 = (l6*sin(th2 + th3 + th4 + th5))/2 - l3*cos(th2 + th3) + (l6*sin(th2 + th3 + th4 - th5))/2 - l5*cos(th2 + th3 + th4);
J124 = (l6*sin(th2 + th3 + th4 + th5))/2 + (l6*sin(th2 + th3 + th4 - th5))/2 - l5*cos(th2 + th3 + th4);
J125 = -(l6*(sin(th2 + th3 + th4 - th5) - sin(th2 + th3 + th4 + th5)))/2;
J126 = 0;


% Jacobiano do robô
J = [J011 , J012 , J013 , J014 , J015 , J016;
     J021 , J022 , J023 , J024 , J025 , J026;
     J031 , J032 , J033 , J034 , J035 , J036;
     J041 , J042 , J043 , J044 , J045 , J046;
     J051 , J052 , J053 , J054 , J055 , J056;
     J061 , J062 , J063 , J064 , J065 , J066;
     J071 , J072 , J073 , J074 , J075 , J076;
     J081 , J082 , J083 , J084 , J085 , J086;
     J091 , J092 , J093 , J094 , J095 , J096;
     J101 , J102 , J103 , J104 , J105 , J106;
     J111 , J112 , J113 , J114 , J115 , J116;
     J121 , J122 , J123 , J124 , J125 , J126];
 
 
end