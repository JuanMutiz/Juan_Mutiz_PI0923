#include <stdio.h>

int main() {
    int num1, num2, num3;

    printf("Insira o primeiro numero: ");
    scanf("%d", &num1);

    printf("Insira o segundo numero: ");
    scanf("%d", &num2);

    printf("Insira o terceiro numero: ");
    scanf("%d", &num3);

    if (num1 <= num2 && num1 <= num3) {
        printf("%d ", num1);
        if (num2 <= num3) printf("%d %d", num2, num3);
        else printf("%d %d", num3, num2);
    } else if (num2 <= num1 && num2 <= num3) {
        printf("%d ", num2);
        if (num1 <= num3) printf("%d %d", num1, num3);
        else printf("%d %d", num3, num1);
    } else {
        printf("%d ", num3);
        if (num1 <= num2) printf("%d %d", num1, num2);
        else printf("%d %d", num2, num1);
    }

    printf("\nOrdem decrescente: ");
    if (num1 >= num2 && num1 >= num3) {
        printf("%d ", num1);
        if (num2 >= num3) printf("%d %d", num2, num3);
        else printf("%d %d", num3, num2);
    } else if (num2 >= num1 && num2 >= num3) {
        printf("%d ", num2);
        if (num1 >= num3) printf("%d %d", num1, num3);
        else printf("%d %d", num3, num1);
    } else {
        printf("%d ", num3);
        if (num1 >= num2) printf("%d %d", num1, num2);
        else printf("%d %d", num2, num1);
    }

}
