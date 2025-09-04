#include <stdio.h>
#include <time.h>

// Algoritmo recursivo de Euclides
long gcd(long a, long b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

int main() {
    long a = 987654321, b = 123456789;
    long resultado;
    
    clock_t inicio = clock();

    for (int i = 0; i < 1000000; i++) {  // 1 millón de iteraciones para medir rendimiento
        resultado = gcd(a, b);
    }

    clock_t fin = clock();
    double tiempo = (double)(fin - inicio) / CLOCKS_PER_SEC;

    printf("MCD(%ld, %ld) = %ld\n", a, b, resultado);
    printf("Tiempo en C: %f segundos\n", tiempo);

    return 0;
}
