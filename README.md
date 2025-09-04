# Parcial Primer Corte

Este repositorio contiene 5 ejercicios implementados en **Python, C, Haskell y ANTLR**.  
Cada ejercicio corresponde a un problema de diseño e implementación de **autómatas, expresiones regulares, análisis léxico/sintáctico o comparación de lenguajes**.

## Contenido

1. **Expresiones regulares y AFD en Python**  
   Expresión regular sobre `{a, b, c}` donde todas las `a` preceden a las `b` y estas a las `c`.

2. **Reconocimiento de identificadores (ID) en Python con AFD**  
   Implementación de un AFD para verificar identificadores válidos.

3. **Calculadora en C con Flex y Bison**  
   Calculadora que soporta operaciones y raíz cúbica de números reales.

4. **Algoritmo de Euclides en C vs Haskell**  
   Comparación de rendimiento entre un lenguaje imperativo y uno declarativo.

5. **Serie de Maclaurin en ANTLR (Java)**  
   Implementación de un parser que calcula los primeros `n` términos de la serie de Maclaurin para `e^x`.

## Ejercicio 1: Expresión Regular y AFD en Python

Diseñar una expresión regular para el conjunto de cadenas sobre {a, b, c} en el cual todas las a preceden a las b y estas a su vez preceden a las c. Es posible que no haya a, b o c.

- Expresión regular:

```
a* b* c*
```

- Implementación:
  
  Se construyó un AFD en Python que lee una cadena y determina si pertenece al       lenguaje descrito.

- Resultados:

<img width="181" height="196" alt="image" src="https://github.com/user-attachments/assets/bc3a2111-e8f4-40ec-a0bf-6655b58960a5" />

- Conclusión:
  
  El AFD valida correctamente las cadenas, asegurando que el orden siempre sea       a...b...c....


## Ejercicio 2: Identificadores en Python

Un identificador válido en muchos lenguajes de programación comienza con una letra y puede continuar con letras o dígitos.

- La expresión regular es:

```
[A-Za-z][A-Za-z0-9]*
```

- Implementación:
  
  Se diseñó un AFD en Python que valida si una cadena es un identificador correcto.

- Resultados:

  <img width="174" height="115" alt="image" src="https://github.com/user-attachments/assets/76fafa1f-e47d-4a41-8eea-2e1623384b52" />

- Conclusión:

  El programa diferencia correctamente identificadores válidos e inválidos según     la expresión regular.

## Ejercicio 3: Calculadora en C con Flex y Bison

Implementar una calculadora que soporte operaciones aritméticas y cálculo de raíz cúbica de números reales.

- Implementación:

  Se usaron:

    - Flex → analizador léxico.

    - Bison → analizador sintáctico.

     - C → integración y ejecución.

- Ejemplo de entrada:

```
cbrt(27)
cbrt(8)
cbrt(125)
cbrt(64)
10
```

- Salida:

  <img width="182" height="120" alt="image" src="https://github.com/user-attachments/assets/1a0a1eaf-54c0-46b1-8e9f-247f6fa50dc0" />

- Conclusión:

  Se construyó un analizador léxico/sintáctico que reconoce expresiones y permite    extender la calculadora fácilmente.


## Ejercicio 4: Algoritmo de Euclides (C vs Haskell)

Implementar el algoritmo recursivo de Euclides en C (imperativo) y Haskell (declarativo).
Luego, comparar el rendimiento.

- Implementación en C:

```
int euclides(int a, int b) {
    if (b == 0) return a;
    return euclides(b, a % b);
}
```

- Implementación en Haskell:

```
euclides :: Int -> Int -> Int
euclides a 0 = a
euclides a b = euclides b (a `mod` b)
```

- Análisis de resultados:

    - C: más rápido, debido a compilación nativa y optimización de bajo nivel.

    - Haskell: más conciso y expresivo, aunque menos eficiente en tiempo de             ejecución.

    - En entradas grandes (números de 9-10 dígitos), la diferencia de rendimiento       favorece claramente a C.
  
- Conclusión:

  Se evidencia la diferencia entre lenguajes imperativos y declarativos:            eficiencia frente a expresividad.

## Ejercicio 5: Serie de Maclaurin en ANTLR (Java)

Escribir un programa en ANTLR que calcule los primeros n términos de la serie de Maclaurin para e^x

- Implementación:

    - Gramática definida en ExpSeries.g4.

     - Código Java (Main.java) para interpretar expresiones como:

     ```
     exp(1, 5)

     ```
- Conclusión:

ANTLR permitió construir un parser personalizado, demostrando cómo una gramática formal puede utilizarse para cálculos matemáticos.


## Conclusiones generales

- Python fue útil para modelar AFDs de manera clara y práctica.

- Flex y Bison en C mostraron cómo se construyen analizadores léxicos y sintácticos en compiladores.

- C vs Haskell permitió comparar rendimientos y determinar que C es mas optimo y rapido que Haskell.

- ANTLR facilitó la creación de un intérprete con gramáticas formales.
  
