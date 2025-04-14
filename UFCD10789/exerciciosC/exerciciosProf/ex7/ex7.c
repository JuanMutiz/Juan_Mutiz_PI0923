#include <stdio.h>

int main() {

    float n1, n2, n3, media;

    printf("Insira a nota da primeira prova: ");
    scanf("%f", &n1);
    printf("Insira a nota da segunda prova: ");
    scanf("%f", &n2);
    printf("Insira a nota da terceira prova: ");
    scanf("%f", &n3);

    n1 == (n1 * 2) / 10;
    n2 == (n2 * 3) / 10;
    n3 == (n3 * 5) / 10;
    media = (n1 + n2 + n3) / 3;

    if (media>=6) {
        printf("Media: %.2f\n", media);
        printf("APROVADO");
    } else {
        printf("Media: %.2f\n", media);
        printf("REPROVADO");
    }

}
