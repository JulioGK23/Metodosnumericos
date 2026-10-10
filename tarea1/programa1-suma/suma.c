#include <stdio.h>

int main() {
    double numero1, numero2, resultado;

    printf("Digite el primer numero: ");
    scanf("%lf", &numero1);

    printf("Digite el segundo numero: ");
    scanf("%lf", &numero2);

    resultado = numero1 + numero2;

    printf("%.17g\n", resultado);

    return 0;
}
