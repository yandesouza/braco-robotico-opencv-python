% PLOT DOS FRAMES {A} E {B}
% Entradas: Frames FA e FB no formato de Transformações Homogêneas
% Saídas: Figura de ambos os frames e sua transição.
function PlotTransicaoAB(FA , FB)
% Transição do frame {A} para o {B}: ligação das origens de {A} e {B}
plot3([FA(1,4) FB(1,4)] , [FA(2,4) FB(2,4)] , [FA(3,4) FB(3,4)] , 'color', [244,140,40]/256 , 'linewidth', 4)
end