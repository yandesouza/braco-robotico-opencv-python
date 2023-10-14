function F1 = ArticuladoF1(th1 , th2 , th3 , th4 , th5 , th6 , l1 , l2 , l3 , l4 , l5 , l6)

F1 = [ -sin(th1),  0, -cos(th1),  0;
        cos(th1),  0, -sin(th1),  0;
               0, -1,         0, l1;
               0,  0,         0,  1];

end