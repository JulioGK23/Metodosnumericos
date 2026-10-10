#include <stdio.h>

int main() {
    int opcion = 0;
    double num1, num2, resultado;

    while (opcion != 5) {
        printf("\n--- CALCULADORA ---\n");
        printf("1. Suma\n");
        printf("2. Resta\n");
        printf("3. Multiplicacion\n");
        printf("4. Division\n");
        printf("5. Salir\n");
        printf("Elija una opcion: ");

        if (scanf("%d", &opcion) != 1) {
            printf("Error: Debe ingresar un numero.\n");
            while (getchar() != '\n');
            continue;
        }

        if (opcion >= 1 && opcion <= 4) {
            printf("Digite el primer numero: ");
            if (scanf("%lf", &num1) != 1) {
                printf("Error: Debe ingresar un numero valido.\n");
                while (getchar() != '\n');
                continue;
            }

            printf("Digite el segundo numero: ");
            if (scanf("%lf", &num2) != 1) {
                printf("Error: Debe ingresar un numero valido.\n");
                while (getchar() != '\n');
                continue;
            }

            if (opcion == 1) {
                resultado = num1 + num2;
                printf("Resultado: %g\n", resultado);
            } else if (opcion == 2) {
                resultado = num1 - num2;
                printf("Resultado: %g\n", resultado);
            } else if (opcion == 3) {
                resultado = num1 * num2;
                printf("Resultado: %g\n", resultado);
            } else if (opcion == 4) {
                if (num2 == 0) {
                    printf("Error: No se puede dividir entre cero.\n");
                } else {
                    resultado = num1 / num2;
                    printf("Resultado: %g\n", resultado);
                }
            }
        } else if (opcion != 5) {
            printf("Opcion no valida. Intente de nuevo.\n");
        }
    }

    return 0;
}
