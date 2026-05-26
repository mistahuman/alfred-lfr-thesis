set grid 
#set xrange [0.00001:10000000]
#set yrange [0.01:100000]
set key top right
set border


#styleline
set style line 1 lc rgb 'red' lt 1 lw 2 pt 6 ps 1.5   # red
set style line 2 lc rgb '#9400D3' lt 1 lw 2 pt 10 ps 1.5  # violet
set style line 3 lc rgb 'blue' lt 1 lw 2 pt 8 ps 1.5 # blue
set style line 4 lc rgb '#005A32' lt 1 lw 2 pt 4 ps 1.5 # darkgreen
set style line 5 lc rgb '#0060ad' lt 1 lw 0.9 pt 5 ps 1.5   # blue
set style line 6 lc rgb '#dd181f' lt 1 lw 0.9 pt 7 ps 1.5   # red

##########################################################################

set xlabel "Tempi di bruciamento [Giorni]"
set ylabel "K-effettivo [-]"

pl 'keff_alfred.dat' u 1:2 t 'Tf=550 [Celsius] (estratte) ' w lp ls 1, 'keff_alfred.dat' u 1:4 t 'Tf=550 [Celsius] (inserite)' w lp ls 2, 'keff_alfred.dat' u 1:11 t 'Tf=1000 [Celsius] (estratte)' w lp ls 3, 'keff_alfred.dat' u 1:12 t 'Tf=1000 [Celsius] (inserite)' w lp ls 4

set output '../graph/keff_in_out_side0.eps'
set terminal postscript eps color enhanced
replot

set xlabel "Temperatura [Celsius]"

pl 'keff_alfred.dat' u 6:7 t 'BOC (estratte)' w lp ls 1, 'keff_alfred.dat' u 6:9 t 'EOC (estratte)' w lp ls 2, 'keff_alfred.dat' u 6:8 t 'BOC (inserite)' w lp ls 3, 'keff_alfred.dat' u 6:10 t 'EOC (inserite)' w lp ls 4

set output '../graph/keff_temp.eps'
set terminal postscript eps color enhanced
replot


#######################################################reattività
set key top left
set xlabel "Tempi di bruciamento [Giorni]"
set ylabel "Inserzione di reattivita [pcm]"

pl 'reattivita.dat' u 1:2 t 'Tf=550 [Celsius] (estratte) ' w lp ls 1, 'reattivita.dat' u 1:3 t 'Tf=550 [Celsius] (inserite)' w lp ls 2

set output '../graph/reatt_burnup.eps'
set terminal postscript eps color enhanced
replot

set xlabel "Temperatura [Celsius]"

pl 'reattivita.dat' u 4:5 t 'BOC (estratte)' w lp ls 1, 'reattivita.dat' u 4:7 t 'EOC (estratte)' w lp ls 2, 'reattivita.dat' u 4:6 t 'BOC (inserite)' w lp ls 3, 'reattivita.dat' u 4:8 t 'EOC (inserite)' w lp ls 4

set output '../graph/reatt_doppler.eps'
set terminal postscript eps color enhanced
replot
