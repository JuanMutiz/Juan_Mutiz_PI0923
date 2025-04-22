#include <stdio.h>

int main(){

    float notas[10];
    float soma;
    float media;
    int alunos = 0;

    for(int i = 0; i < 10; i++){
        printf("Insira a nota do aluno %d: ", i + 1);
        scanf("%f", &notas[i]);
        while(notas[i] < 0 || notas[i] > 20){
            printf("Insira uma nota valida (0 a 20): ");
            scanf("%f", &notas[i]);
        }
        soma += notas[i];
    }

    media = soma / 10;
    printf("\nMedia: %.2f", media);

    for(int i = 0; i < 10; i++){
        if(notas[i] >= media){
            alunos++;
        }
    }

    printf("\nQuantidade de alunos com nota igual ou acima da media: %d", alunos);

    return 0;

}