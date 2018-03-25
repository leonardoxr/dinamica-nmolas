#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>

double a(double x_atual,double x_anterior,double x_seguinte,double k,double m);

void main()
{

    FILE *arq;
    arq = fopen("dinamica_n_molas.txt", "w+");

    int NMAX,tmax,j;
    NMAX = 10;
    double t,dt,ac[NMAX],ac_antigo[NMAX],m,x[NMAX],k,v[NMAX];
    k = 1;
    tmax = 1000;
    dt=0.01;
    m = 1;


    for( j=0; j<NMAX; j++)
    {
        x[j] = 0;
        v[j] = 0;
        ac_antigo[j] = 0;
    }
    //x[1] = 0.1;
    x[5]=0.1;

    fprintf(arq,"%lf\t", 0.);
    for( j=0; j<NMAX; j++)
    {
        fprintf(arq,"%lf\t", x[j]);
    }
    fprintf(arq,"\n");


    for(t = 0; t < tmax; t = t+dt)
    {


//a1 = a(x1,x2,k1,m1);
//a2 = a(x2,x1,k2,m2);
//x1 = x1 + v1*dt +0.5*a1*pow(dt,2);
//x2 = x2 + v2*dt +0.5*a2*pow(dt,2);
//v1 = v1 + + 0.5*(a1+a(x1,x2,k1,m1))*dt;
//v2 = v2 + 0.5*(a2+a(x2,x1,k2,m2))*dt;


        for(j = 1; j<NMAX-1; j++)
        {

            ac_antigo[j] = a(x[j],x[j-1],x[j+1],k,m);


        }

        for(j = 1; j<NMAX-1; j++)
        {

            x[j] = x[j] + v[j]*dt + 0.5 * ac_antigo[j] * pow(dt,2);

        }

                for(j = 1; j<NMAX-1; j++)
        {
            ac[j] = a(x[j],x[j-1],x[j+1],k,m);


        }

            for(j = 1; j<NMAX-1; j++)
        {
            v[j] = v[j] + 0.5 * (ac_antigo[j] + ac[j])*dt;

            ac[j] = ac_antigo[j] ;

        }






        fprintf(arq,"%lf\t", t);
        for( j=0; j<NMAX; j++)
        {

            fprintf(arq,"%lf\t", x[j]);

        }
        fprintf(arq,"\n");



    }


    fclose(arq);

}


double a(double x_atual,double x_anterior,double x_seguinte,double k,double m)
{

    double ac;

    ac = (-k*( x_atual - x_anterior )+k*( x_seguinte - x_atual ))/m;

    return ac;


}
