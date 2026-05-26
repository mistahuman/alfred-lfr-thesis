set xlabel "Energia neutrone incidente [eV]"
set ylabel "Numero totale di neutroni prodotti per evento di fissione [-]"
set logscale x 10 
#set logscale y 10 
#set grid 
#set xrange [0.00001:10000000]
#set yrange [0.01:100000]
set key top right
set border

set format x "10^{%L}"

#styleline
set style line 1 lc rgb 'red' lt 1 lw 1 pt 6 ps 0.8   # red
set style line 2 lc rgb 'green' lt 1 lw 1 pt 6 ps 0.8  # green
set style line 3 lc rgb 'blue' lt 1 lw 1 pt 6 ps 0.8 # blue
set style line 4 lc rgb 'orange' lt 1 lw 1 pt 6 ps 0.8 # orange
set style line 5 lc rgb '#0060ad' lt 1 lw 0.9 pt 5 ps 1.5   # blue
set style line 6 lc rgb '#dd181f' lt 1 lw 0.9 pt 7 ps 1.5   # red


pl 'nubar.dat' u 3:4 t 'Uranio-235' w l ls 3,'nubar.dat' u 1:2 t 'Plutonio-239' w l ls 1, 'nubar.dat' u 5:6 t 'Uranio-233' w l ls 2

set output '../graph/nubar.eps'
set terminal postscript eps color enhanced
replot



