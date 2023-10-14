% ==============================
% Cinemática Inversa do robô RRR
% ==============================
clear all; clc; close all;
% Caminho a ser percorrido pelo robô
N = -1:0.1:1;
Caminho1 = [-1* ones(size(N));
            0* ones(size(N));
            0* ones(size(N));
            
            0* ones(size(N));
            1* ones(size(N));
            0* ones(size(N));
            
            0* ones(size(N));
            0* ones(size(N));
           -1* ones(size(N));
            
           -0.5 * ones(size(N));
           -0.350 * N;
           0.25 * ones(size(N))];

Caminho2 = [-1* ones(size(N));
            0* ones(size(N));
            0* ones(size(N));
            
            0* ones(size(N));
            1* ones(size(N));
            0* ones(size(N));
            
            0* ones(size(N));
            0* ones(size(N));
           -1* ones(size(N));
            
           0.5 * ones(size(N));
           -0.350 * N;
           0.25 * ones(size(N))];
Caminho = [Caminho1,Caminho2];
% Comprimento dos links
L1 = 0.0661+0.0085; L2 = 0.4251; L3 = 0.3922; L4 = 0.0397+0.0703; L5 = 0.0492+0.04545; L6 = 0.0996-0.02465;
% Inicializando o robô
th1 = deg2rad(90); th2 = deg2rad(-60); th3 = deg2rad(100); th4 = deg2rad(140); th5 = deg2rad(180); th6 = deg2rad(90); Th = [th1;th2;th3;th4;th5;th6]; TH=Th;
F0 = eye(4);
F1 = ArticuladoF1(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6);
F2 = ArticuladoF2(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6);
F3 = ArticuladoF3(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6);
F4 = ArticuladoF4(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6);
F5 = ArticuladoF5(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6);
F6 = ArticuladoF6(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6);

% Função da posição do end-effectordo robô
fe = [F6(1:3,1);F6(1:3,2);F6(1:3,3);F6(1:3,4)];
% Taxa de aprendizado
n = 0.2;
% Tolerância
ksi= (0.01)^2;

% == LOOP DE OTIMIZACAO ==
% Para cada um dos pontos do caminho
for k = 1:size(Caminho,2)
    % Obtém o objetivo atual
    fg = Caminho(:,k);
    % Calcula a posição atual do robô
    F1 = ArticuladoF1(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6);
    F2 = ArticuladoF2(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6);
    F3 = ArticuladoF3(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6);
    F4 = ArticuladoF4(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6);
    F5 = ArticuladoF5(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6);
    F6 = ArticuladoF6(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6);
    % Função da posição do end-effectordo robô
    fe = [fe , [F6(1:3,1);F6(1:3,2);F6(1:3,3);F6(1:3,4)]];
    % Erro quadrático médio inicial
    E = 1/2 * (fg -fe(:,end))' * (fg -fe(:,end));
    % Loop para convergir ao ponto desejado
    while (E > ksi)
        % Calcula o Gradiente cartesiano atual
        dE = -(fg-fe(:,end));
        % Calcula o Jacobiano para a posicaoangular corrente
        J = ArticuladoJacobiano(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5 , L6);
        % Obtenha o Gradiente no espaço de juntas observando a degeneração
        dTh = pinv(J) * dE;
        % Atualize o valor das juntas
        Th = Th - n * dTh;
        % Atualiza o robô
        th1 = Th(1); th2 = Th(2); th3 = Th(3); th4 = Th(4); th5 = Th(5); th6 = Th(6);
        F1 = ArticuladoF1(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6);
        F2 = ArticuladoF2(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6);
        F3 = ArticuladoF3(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6);
        F4 = ArticuladoF4(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6);
        F5 = ArticuladoF5(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6);
        F6 = ArticuladoF6(th1 , th2 , th3, th4 , th5 , th6 , L1 , L2 , L3 , L4 , L5, L6);
        
        % Função da posição do end-effector do robô
        fe = [fe, [F6(1:3,1);F6(1:3,2);F6(1:3,3);F6(1:3,4)]];
        
        % Erro quadrático médio inicial
        E = 1/2 * (fg-fe(:,end))' * (fg-fe(:,end));
        
        % == PLOT ==
        % Caminho a ser percorrido
        plot3(Caminho(10,:) , Caminho(11,:) , Caminho(12,:) , 'ob', 'linewidth', 2 , 'markersize', 10), hold on,
        
       % Ponto objetivo atual
        plot3(Caminho(10,k) , Caminho(11,k) , Caminho(12,k) , 'or', 'linewidth', 2 , 'markersize', 10)
        
        % Caminho executado pelo robo
        plot3(fe(10,:) , fe(11,:) , fe(12,:) , 'm', 'linewidth', 2)
        
        % Robô
        PlotTransicaoAB(F0 , F1), PlotFrameA(F0), PlotFrameA(F1),
        PlotTransicaoAB(F1 , F2),PlotFrameA(F2),
        PlotTransicaoAB(F2 , F3),PlotFrameA(F3),
        PlotTransicaoAB(F3 , F4),PlotFrameA(F4),
        PlotTransicaoAB(F4 , F5),PlotFrameA(F5),
        PlotTransicaoAB(F5 , F6),PlotFrameA(F6),
        hold off, xlabel('x'); ylabel('y'); zlabel('z');
        axis equal; grid on;
        drawnow;
    end
    TH = [TH,Th];
end