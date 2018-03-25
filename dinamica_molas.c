#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>

double k12=1;

double a(double x1,double x2,double k1,double m1);

void main()
{

    FILE *arq;
    arq = fopen("dinamica_mola.txt", "w+");


    double t,dt,a1,a2,x1,x2,v1,v2,k1,k2,m1,m2,y1,y2,d1,d2,d3;
    int tmax;

d1 =1;
d2 =1;
d3 =1;
y1 = 1;
y2 = 2;


m1 = 1;
k1 = 1;
x1 = (y1-d1)+0.1;
v1 =0;

m2 = 1;
k2 = 1;
x2 = (y2-d1-d2);
v2 =0;


tmax = 100;
t=0;
dt=0.01;
fprintf(arq,"%lf %lf %lf %lf %lf\n",t,x1,v1,x2,v2);

for(t = 0;t < tmax;t= t+dt)
{

a1 = a(x1,x2,k1,m1);
a2 = a(x2,x1,k2,m2);
x1 = x1 + v1*dt +0.5*a1*pow(dt,2);
x2 = x2 + v2*dt +0.5*a2*pow(dt,2);
v1 = v1 + + 0.5*(a1+a(x1,x2,k1,m1))*dt;
v2 = v2 + 0.5*(a2+a(x2,x1,k2,m2))*dt;


fprintf(arq,"%lf %lf %lf %lf %lf\n",t,x1,v1,x2,v2);

}


    fclose(arq);

}


double a(double x1,double x2,double k1,double m1)
{

double ac;

ac = ((-(k1+k12)*x1)+k12*x2)/m1;

return ac;


}
