set xlabel "Asse y [cm]"
set ylabel "Flusso Neutronico [-]"
#set logscale y 10 
#set grid 
#set xrange [0.00001:10000000]
#set yrange [0.01:100000]
set key top right
set border
set autoscale


#styleline
set style line 1 lc rgb 'red' lt 1 lw 1.5 pt 6 ps 0.8   # red
set style line 2 lc rgb 'green' lt 1 lw 1.5 pt 6 ps 0.8  # green
set style line 3 lc rgb 'blue' lt 1 lw 1.5 pt 6 ps 0.8 # blue
set style line 4 lc rgb '#9400D3' lt 1 lw 1.5 pt 10 ps 1.5  # violet
set style line 5 lc rgb '#800000' lt 1 lw 1.5 pt 6 ps 0.8 # marrone
set style line 6 lc rgb '#005A32' lt 1 lw 1.5 pt 4 ps 1.5 # darkgreen


pl './data/fluxgroup.dat' u 1:7 t 'Gruppo 7' w l ls 1, './data/fluxgroup.dat' u 1:2 t 'Gruppo 11' w l ls 2, './data/fluxgroup.dat' u 1:3 t 'Gruppo 15' w l ls 3, './data/fluxgroup.dat' u 1:4 t 'Gruppo 19' w l ls 4, './data/fluxgroup.dat' u 1:5 t 'Gruppo 23' w l ls 5, './data/fluxgroup.dat' u 1:6 t 'Gruppo 27' w l ls 6

set output '../graph/energyy.eps'
set terminal postscript eps color enhanced
replot

