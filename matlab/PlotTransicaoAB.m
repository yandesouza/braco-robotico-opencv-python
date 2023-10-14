% PLOT DOS FRAMES {A} E {B}
% Entradas: Frames FA e FB no formato de Transforma��es Homog�neas
% Sa�das: Figura de ambos os frames e sua transi��o.
function PlotTransicaoAB(FA , FB)
% Transi��o do frame {A} para o {B}: liga��o das origens de {A} e {B}
plot3([FA(1,4) FB(1,4)] , [FA(2,4) FB(2,4)] , [FA(3,4) FB(3,4)] , 'color', [244,140,40]/256 , 'linewidth', 4)
end