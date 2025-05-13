#include <stdio.h>

int main (){
int segs, mins, horas;

printf("Segundos: ");
scanf("%d",&segs);

int mins=segs/60;
int horas=mins/60;

printf("segundos: %d,minutos: %d,Horas:%d",segs,mins,horas);


}
