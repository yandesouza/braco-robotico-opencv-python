% ============================
% Denavit-Hartenbergem MATLAB
% ============================
clear all; clc; close all;

% Vari�veis simb�licas D-H:
syms d theta a alpha real

% Matriz de transla��o em x
Tx = [1 0 0 a
      0 1 0 0
      0 0 1 0
      0 0 0 1];

% Matriz de transla��o em z
Tz = [1 0 0 0
      0 1 0 0
      0 0 1 d
      0 0 0 1];

% Matriz de rota��o em x
Rx = [1 0 0 0
      0 cos(alpha) -sin(alpha) 0
      0 sin(alpha) cos(alpha) 0
      0 0 0 1];

% Matriz de rota��o em z
Rz = [cos(theta) -sin(theta) 0 0
      sin(theta) cos(theta) 0 0
      0 0 1 0
      0 0 0 1];

% Matriz D-H:
A = simplify(Tz* Rz* Tx* Rx);

% Rob� ARTICULADO 3DOF:
% Tabela D-H (Coppeliasim):
% |======================================|
% | Ai |  d   |    theta   |  a  | alpha |
% |----|------|------------|-----|-------|
% | 1  |  L1  | 90 + th1*  |   0 |  -90  |
% | 2  |   0  |    th2*    |  L2 |    0  |
% | 3  |   0  |    th3*    |  L3 |    0  |
% | 4  |  L4  | -90 + th4* |   0 |  -90  |
% | 5  |  L5  |  90 + th5* |   0 |  -90  |
% | 6  |  L6  |    th6*    |   0 |    0  |
% |======================================|

% Tabela D-H (Universal-robots):
% |==================================|
% | Ai |  d   | theta  |  a  | alpha |
% |----|------|--------|-----|-------|
% | 1  |  L1  |  th1*  |   0 |   90  |
% | 2  |   0  |  th2*  |  L2 |    0  |
% | 3  |   0  |  th3*  |  L3 |    0  |
% | 4  |  L4  |  th4*  |   0 |   90  |
% | 5  |  L5  |  th5*  |   0 |  -90  |
% | 6  |  L6  |  th6*  |   0 |    0  |
% |==================================|

% Vari�veis simb�licas do rob� em quest�o:
syms th1 th2 th3 th4 th5 th6 l1 l2 l3 l4 l5 l6 real

% Frame {0}:
F0 = eye(4);

% Transforma��o D-H do frame {1} para o frame {2}:
% Primeira transforma��o D-H
A1 = subs(A , [d theta a alpha] , [l1 deg2rad(90)+th1 0 deg2rad(-90)]);
% A1 = subs(A , [d theta a alpha] , [l1 th1 0 deg2rad(90)]);
% Frame {1}:
F1 = simplify(A1);

% Transforma��o D-H do frame {2} para o frame {3}:
% Primeira transforma��o D-H
A2 = subs(A , [d theta a alpha] , [0 th2 l2 0]);
% Frame {2}:
F2 = simplify(A1 * A2);

% Transforma��o D-H do frame {3} para o frame {4}:
% Primeira transforma��o D-H
A3 = subs(A , [d theta a alpha] , [0 th3 l3 0]);
% Frame {3}:
F3 = simplify(A1 * A2 * A3);

% Transforma��o D-H do frame {4} para o frame {5}:
% Primeira transforma��o D-H
A4 = subs(A , [d theta a alpha] , [l4 deg2rad(-90)+th4 0 deg2rad(-90)]);
% A4 = subs(A , [d theta a alpha] , [l4 th4 0 deg2rad(90)]);
% Frame {3}:
F4 = simplify(A1 * A2 * A3 * A4);

% Transforma��o D-H do frame {5} para o frame {6}:
% Primeira transforma��o D-H
A5 = subs(A , [d theta a alpha] , [l5 deg2rad(90)+th5 0 deg2rad(-90)]);
% A5 = subs(A , [d theta a alpha] , [l5 th5 0 deg2rad(-90)]);
% Frame {3}:
F5 = simplify(A1 * A2 * A3 * A4 * A5);

% Transforma��o D-H do frame {6} para o frame {7}:
% Primeira transforma��o D-H
A6 = subs(A , [d theta a alpha] , [l6 th6 0 0]);
% Frame {3}:
F6 = simplify(A1 * A2 * A3 * A4 * A5 * A6);


% Utilizando vari�veis simb�licas:
% Fun��o que descreve o rob�:
fe = [F6(1:3,1);F6(1:3,2);F6(1:3,3);F6(1:3,4)];
% C�lculo do Jacobiano da fun��o do rob�:
J = simplify(jacobian(fe , [th1 th2 th3 th4 th5 th6]));


%----
% Substituir simbolico
% ----

% Comprimento dos links
L1 = 0.0661+0.0085; L2 = 0.4251; L3 = 0.3922; L4 = 0.0397+0.0703; L5 = 0.0492+0.04545; L6 = 0.0996-0.02465;
%L1 = 0.089159; L2 = -0.425; L3 = -0.39225; L4 = 0.10915; L5 = 0.09465; L6 = 0.0823;



% �ngulos das juntas
TH1 = deg2rad(0); TH2 = deg2rad(-90); TH3 = deg2rad(0);
TH4 = deg2rad(0); TH5 = deg2rad(90); TH6 = deg2rad(0);

% Frame {0} num�rico
f0 = F0;
% Frame {1} num�rico
f1 = double(subs(F1 , [l1 l2 l3 l4 l5 l6 th1 th2 th3 th4 th5 th6] , [L1 L2 L3 L4 L5 L6 TH1 TH2 TH3 TH4 TH5 TH6]));
% Frame {2} num�rico
f2 = double(subs(F2 , [l1 l2 l3 l4 l5 l6 th1 th2 th3 th4 th5 th6] , [L1 L2 L3 L4 L5 L6 TH1 TH2 TH3 TH4 TH5 TH6]));
% Frame {3} num�rico
f3 = double(subs(F3 , [l1 l2 l3 l4 l5 l6 th1 th2 th3 th4 th5 th6] , [L1 L2 L3 L4 L5 L6 TH1 TH2 TH3 TH4 TH5 TH6]));
% Frame {4} num�rico
f4 = double(subs(F4 , [l1 l2 l3 l4 l5 l6 th1 th2 th3 th4 th5 th6] , [L1 L2 L3 L4 L5 L6 TH1 TH2 TH3 TH4 TH5 TH6]));
% Frame {5} num�rico
f5 = double(subs(F5 , [l1 l2 l3 l4 l5 l6 th1 th2 th3 th4 th5 th6] , [L1 L2 L3 L4 L5 L6 TH1 TH2 TH3 TH4 TH5 TH6]));
% Frame {6} num�rico
f6 = double(subs(F6 , [l1 l2 l3 l4 l5 l6 th1 th2 th3 th4 th5 th6] , [L1 L2 L3 L4 L5 L6 TH1 TH2 TH3 TH4 TH5 TH6]));

% ----
% Plot
% ----
% Transi��es entre os frames (origens)
PlotTransicaoAB(f0 , f1), hold on,
PlotTransicaoAB(f1 , f2), 
PlotTransicaoAB(f2 , f3),
PlotTransicaoAB(f3 , f4),
PlotTransicaoAB(f4 , f5),
PlotTransicaoAB(f5 , f6),

% Plotdos frames calculados na cinem�tica
PlotFrameA(f0), PlotFrameA(f1), PlotFrameA(f2), PlotFrameA(f3),
PlotFrameA(f4), PlotFrameA(f5), PlotFrameA(f6),
hold off, xlabel('x'); ylabel('y'); zlabel('z');
axis equal; 
grid on; view(30 , 30); drawnow;