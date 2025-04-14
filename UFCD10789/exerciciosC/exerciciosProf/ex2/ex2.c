#include <stdio.h>

int main() {
    int num1, num2, num3;


    printf("Digite o primeiro numero: ");
    scanf("%d", &num1);

    printf("Digite o segundo numero: ");
    scanf("%d", &num2);

    printf("Digite o terceiro numero: ");
    scanf("%d", &num3);


    int maior = num1;
    int menor = num1;


    if (num2 > maior) {
        maior = num2;
    }
    if (num3 > maior) {
        maior = num3;
    }

    if (num2 < menor) {
        menor = num2;
    }
    if (num3 < menor) {
        menor = num3;
    }


    printf("O maior valor e: %d\n", maior);
    printf("O menor valor e: %d\n", menor);

    return 0;
}
