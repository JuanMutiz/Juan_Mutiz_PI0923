#include <stdio.h>

int main() {
    int compra;
    char nome[50];
    float desconto;
    float vd;


    printf("Insira seu nome: ");
    scanf("%s", &nome);

    printf("Insira o valor da sua compra: ");
    scanf("%d", &compra);

    if(compra <= 200) {
        desconto = (compra * 0.1);
        vd = compra - desconto;

    } else if (compra <= 500) {
        desconto = (compra * 0.15);
        vd = compra - desconto;

    } else {
        desconto = (compra * 0.20);
        vd = compra - desconto;
    }

    printf("\n---------------------------------\n");
    printf("---------- Nome: %s -----------\n", nome);
    printf("--------- Subtotal: %d ---------\n", compra);
    printf("---------- Total: %.1f ---------\n", vd);
    printf("---------------------------------\n");
}
