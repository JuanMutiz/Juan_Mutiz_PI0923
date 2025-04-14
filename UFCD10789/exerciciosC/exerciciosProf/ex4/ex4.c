#include <stdio.h>

int main() {
    int saldoCliente, cheque;

    printf("Insira o seu saldo: ");
    scanf("%d", &saldoCliente);

    printf("Insira o valor do cheque: ");
    scanf("%d", &cheque);

    if(saldoCliente < cheque) {
        printf("Erro! Saldo insuficiente!\n");
        printf("Saldo: %d", saldoCliente);
    } else {
        printf("Saldo: %d\n", saldoCliente);
        printf("\nO cheque no valor de %d foi descontado na sua conta!\n", cheque);

        int transacao = saldoCliente - cheque;

        printf("\nSaldo pos transacao: %d\n", transacao);
    }

}
