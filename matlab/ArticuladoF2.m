function F2 = ArticuladoF2(th1 , th2 , th3 , th4 , th5 , th6 , l1 , l2 , l3 , l4 , l5 , l6)

F2 = [ -cos(th2)*sin(th1),  sin(th1)*sin(th2), -cos(th1), -l2*cos(th2)*sin(th1);
        cos(th1)*cos(th2), -cos(th1)*sin(th2), -sin(th1),  l2*cos(th1)*cos(th2);
                -sin(th2),          -cos(th2),         0,      l1 - l2*sin(th2);
                        0,                  0,         0,                     1];
           
end