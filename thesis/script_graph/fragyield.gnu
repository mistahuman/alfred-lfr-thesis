set xlabel "Massa atomica dei prodotti [u]"
set ylabel "Resa dei prodotti di fissione [%]"
#set logscale x 10 
#set logscale y 10 
set grid 
#set xrange [0.00001:10000000]
#set yrange [0.01:100000]
set key top right
set border

#set format x "10^{%L}"

#styleline
set style line 1 lc rgb 'red' lt 1 lw 1.5 pt 6 ps 1   # red
set style line 2 lc rgb 'green' lt 1 lw 1.5 pt 4 ps 1  # green
set style line 3 lc rgb 'blue' lt 1 lw 1.5 pt 4 ps 1 # blue
set style line 4 lc rgb 'orange' lt 1 lw 1 pt 2 ps 1 # orange
set style line 5 lc rgb '#005A32' lt 1 lw 1.5 pt 10 ps 1   # dg
set style line 6 lc rgb '#dd181f' lt 1 lw 0.9 pt 7 ps 1.5   # red


pl './data/fragyield.dat' u 5:6 t 'Uranio-233' w lp ls 5,'./data/fragyield.dat' u 3:4 t 'Uranio-235' w lp ls 1, './data/fragyield.dat' u 1:2 t 'Plutonio-239' w lp ls 3

set output '../graph/fragyield.eps'
set terminal postscript eps color enhanced
replot



