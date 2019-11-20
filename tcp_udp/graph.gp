set datafile sep ',' 

set term png  truecolor enhanced 


set ylab 'TCP queries (% w.r.t. total)'
set xlab 'Date (Year-Month)'
set title 'A Root' 
set xdata time
set timefmt '%Y%m%d'
set format x "%Y-%m"
set output 'a.png'

set xtic  rotate by -45
set yrange [0:40]

plot  'a.csv' u 1:5  w lp ti 'IPv4', ''  u 1:9 w lp ti 'IPv6'


set title 'B Root' 
set output 'b.png'
plot  'b.csv' u 1:5  w lp ti 'IPv4', ''  u 1:9 w lp ti 'IPv6'


set title 'C Root' 
set output 'c.png'
plot  'c.csv' u 1:5  w lp ti 'IPv4', ''  u 1:9 w lp ti 'IPv6'


set title 'D Root' 
set output 'd.png'
plot  'd.csv' u 1:5  w lp ti 'IPv4', ''  u 1:9 w lp ti 'IPv6'


set title 'E Root' 
set output 'e.png'
plot  'e.csv' u 1:5  w lp ti 'IPv4', ''  u 1:9 w lp ti 'IPv6'

set title 'F Root' 
set output 'f.png'
plot  'f.csv' u 1:5  w lp ti 'IPv4', ''  u 1:9 w lp ti 'IPv6'

#set title 'G Root' 
#set output 'g.png'
#plot  'g.csv' u 1:5  w lp ti 'IPv4', ''  u 1:9 w lp ti 'IPv6'

set title 'H Root' 
set output 'h.png'
plot  'h.csv' u 1:5  w lp ti 'IPv4', ''  u 1:9 w lp ti 'IPv6'


set title 'I Root' 
set output 'i.png'
plot  'i.csv' u 1:5  w lp ti 'IPv4', ''  u 1:9 w lp ti 'IPv6'

set title 'J Root' 
set output 'j.png'
plot  'j.csv' u 1:5  w lp ti 'IPv4', ''  u 1:9 w lp ti 'IPv6'

set title 'K Root' 
set output 'k.png'
plot  'k.csv' u 1:5  w lp ti 'IPv4', ''  u 1:9 w lp ti 'IPv6'

set title 'L Root' 
set output 'l.png'
plot  'l.csv' u 1:5  w lp ti 'IPv4', ''  u 1:9 w lp ti 'IPv6'


set title 'M Root' 
set output 'l.png'
plot  'm.csv' u 1:5  w lp ti 'IPv4', ''  u 1:9 w lp ti 'IPv6'
