% PLOT DO FRAME {A}
% Entrada: Frame {A} no formato de Transformações Homogêneas
% Saída: Figura do frame.
function PlotFrameA(FA)
% FRAME {A}:
% Nome do frame {A} para ser impresso na figura
escala = 0.05;
nome = inputname(1);
% Eixo-x no robô no frame {A}
plot3([FA(1,4) FA(1,4)+escala*FA(1,1)] , [FA(2,4) FA(2,4)+escala*FA(2,1)] , [FA(3,4) FA(3,4)+escala*FA(3,1)] , 'b', 'linewidth', 2)
text(FA(1,4)+escala*FA(1,1) , FA(2,4)+escala*FA(2,1) , FA(3,4)+escala*FA(3,1) , ['x_{\{' nome '\}}'])
% Eixo-y no robô no frame {A}
plot3([FA(1,4) FA(1,4)+escala*FA(1,2)] , [FA(2,4) FA(2,4)+escala*FA(2,2)] , [FA(3,4) FA(3,4)+escala*FA(3,2)] , 'r', 'linewidth', 2)
text(FA(1,4)+escala*FA(1,2) , FA(2,4)+escala*FA(2,2) , FA(3,4)+escala*FA(3,2) , ['y_{\{' nome '\}}'])
% Eixo-z no robô no frame {A}
plot3([FA(1,4) FA(1,4)+escala*FA(1,3)] , [FA(2,4) FA(2,4)+escala*FA(2,3)] , [FA(3,4) FA(3,4)+escala*FA(3,3)] , 'g', 'linewidth', 2)
text(FA(1,4)+escala*FA(1,3) , FA(2,4)+escala*FA(2,3) , FA(3,4)+escala*FA(3,3) , ['z_{\{' nome '\}}'])
% Posição da origem do frame {A}
plot3(FA(1,4) , FA(2,4) , FA(3,4) , 'ok', 'linewidth', 2 , 'markersize', 5);
text(FA(1,4) , FA(2,4) , FA(3,4) , ['\{' nome '\}'])
end