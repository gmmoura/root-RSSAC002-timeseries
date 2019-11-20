# root-RSSAC002-timeseries


  * Show timeseries of *incoming* TCP and UDP  queries for each Root Server Letter
     * Except for G root -- could not get the data

  * Uses data from https://github.com/rssac-caucus/RSSAC002-data

  * To reproduce it:
  ```
  $ git clone https://github.com/gmmoura/root-RSSAC002-timeseries
  $ cd root-RSSAC002-timeseries
  #clone the data from @wessels repository
  $ git clone https://github.com/rssac-caucus/RSSAC002-data
  #crunch the  data
  python tcpStats.py RSSAC002-data
  #generate figs
  cd tcp_udp
  $gnuplot graph.gp
  ```



## Ratio of TCP queries per Root Server Letter


### A Root:

![alt text](https://github.com/gmmoura/root-RSSAC002-timeseries/blob/master/tcp_udp/a.png "A Root")

### B Root:

![alt text](https://github.com/gmmoura/root-RSSAC002-timeseries/blob/master/tcp_udp/b.png "B Root")

### C Root:

![alt text](https://github.com/gmmoura/root-RSSAC002-timeseries/blob/master/tcp_udp/c.png "C Root")


### D Root:

![alt text](https://github.com/gmmoura/root-RSSAC002-timeseries/blob/master/tcp_udp/d.png "D Root")


### E Root:

![alt text](https://github.com/gmmoura/root-RSSAC002-timeseries/blob/master/tcp_udp/e.png "E Root")

### F Root:

![alt text](https://github.com/gmmoura/root-RSSAC002-timeseries/blob/master/tcp_udp/f.png "F Root")

### H Root:

![alt text](https://github.com/gmmoura/root-RSSAC002-timeseries/blob/master/tcp_udp/h.png "H Root")

### I Root:

![alt text](https://github.com/gmmoura/root-RSSAC002-timeseries/blob/master/tcp_udp/i.png "I Root")

### J Root:

![alt text](https://github.com/gmmoura/root-RSSAC002-timeseries/blob/master/tcp_udp/j.png "J Root")

### K Root:

![alt text](https://github.com/gmmoura/root-RSSAC002-timeseries/blob/master/tcp_udp/k.png "K Root")

### L Root:

![alt text](https://github.com/gmmoura/root-RSSAC002-timeseries/blob/master/tcp_udp/l.png "L Root")

### M Root:

![alt text](https://github.com/gmmoura/root-RSSAC002-timeseries/blob/master/tcp_udp/m.png "L Root")
