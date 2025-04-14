#include <stdio.h>

int main (){
int ns;

printf("Segundos: ");
scanf("%d",&ns);

int nm=ns/60;
int nh=nm/60;

printf("segundos: %d,minutos: %d,Horas:%d",ns,nm,nh);


}
