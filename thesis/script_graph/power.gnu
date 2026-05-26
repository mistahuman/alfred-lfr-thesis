set xlabel "Asse y [cm]"
set ylabel "Potenza termica [W]"
#set logscale y 10 
#set grid 
#set xrange [0.00001:10000000]
#set yrange [0.01:100000]
set key top right
set border
set autoscale


#styleline
set style line 1 lc rgb 'red' lt 1 lw 1.5 pt 6 ps 0.8   # red
set style line 2 lc rgb 'green' lt 1 lw 1 pt 6 ps 0.8  # green
set style line 3 lc rgb 'blue' lt 1 lw 1.5 pt 6 ps 0.8 # blue
set style line 4 lc rgb 'orange' lt 1 lw 1 pt 6 ps 0.8 # orange
set style line 5 lc rgb '#0060ad' lt 1 lw 0.9 pt 5 ps 1.5   # blue
set style line 6 lc rgb '#dd181f' lt 1 lw 0.9 pt 7 ps 1.5   # red


pl './data/powery.dat' u 1:2 t 'barre inserite (EOC)' w l ls 1, './data/powery.dat' u 1:3 t 'barre estratte (EOC)' w l ls 3

set output '../graph/powery.eps'
set terminal postscript eps color enhanced
replot


