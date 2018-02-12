set terminal png

l(x)=a1*x + a0
p(x)=a2*x*x + a1*x + a0
c(x)=a3*x*x*x + a2*x*x + a1*x + a0

set output "punto8.png"
set title "Punto8"
set xlabel "Size (n)"
set ylabel "Time (s)"
fit p(x) "Punto8.res" using 1:3 via a2, a1, a0
plot "punto8.res" using 1:3 with lines notitle, p(x)

