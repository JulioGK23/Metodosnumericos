# Práctica 1 · La serie de Maclaurin y el criterio de paro

**UEA 1151039 · Métodos Numéricos en Ingeniería · Trimestre 26-O · UAM Azcapotzalco**
**Profesor:** M. en C. Gabriel Hurtado Avilés

| | |
|---|---|
| Equipo | |
| Integrantes (nombre, matrícula y licenciatura) |*Fuentes Bayona luis Fernando-2243038451-Licenciatura en Ingenieria Mecanica *Trejo Ponce Julio Antonio- 2243038326-Licenciatura en Ingenieria Electronica |
| Repositorio de la Tarea 1 de | JulioGk23|
| Fecha | 12/Octubre/2026|

## 1. Octave y Python

![Octave](img/01-octave.png)
![Python](img/02-python.png)

¿Coinciden con la lámina 25 de la unidad I?
si coinciden los resultados, en los programas se alcanza una misma  aproximacion y el mismo error relativo que coincide con la lamina 25 de la unidad 1

## 2. Las dos líneas que completamos en `maclaurin.c`

```c
termino = termino * X / n;
ea = fabs((aprox - anterior) / aprox) * 100.0;
```

![C](img/03-c.png)

## 3. Más cifras significativas

| Cifras | εs (%) | Términos | Aproximación | Error verdadero (%) |
|---|---|---|---|---|
| 3 | 0.05	|6 | 1.648697916666667|	0.00141649 |
| 6 | 	0.00005 (5e-05)| 9| 1.648721265035962|3.43549e-07 |
| 17 | 5e-16| 16| 1.648721270700128|2.69354e-14 |

1. ¿Cuántos términos hacen falta en cada caso?
Para obtener 3 cifras significativas se necesitan 6 términos, para 6 cifras se necesitan 9 términos y para 17 cifras se necesitan 16 términos, según los resultados de la tabla. Esto muestra que, mientras mayor sea la precisión que buscamos, más términos de la serie de Maclaurin debemos calcular.

2. En cada fila de la tabla, ¿εa es mayor o menor que εt? ¿Por qué conviene detenerse con εa?
Para 3 y 6 cifras significativas, el error aproximado (εa) es mayor que el error verdadero (εt). Sin embargo, para 17 cifras, εa es igual a 0 mientras que εt es 2.69354×10⁻¹⁴ %. Esto ocurre porque el término que se suma es tan pequeño que ya no modifica el valor almacenado debido a los límites de precisión de la computadora. Conviene utilizar εa como criterio de paro porque no necesitamos conocer el valor verdadero, aunque cerca del límite de precisión de la máquina puede dejar de ser confiable.

4. Con 17 cifras el programa termina. ¿Cuántas cifras del resultado son correctas en realidad?
   Relaciónenlo con 0.1 + 0.2 de la Tarea 1.

Aunque solicitamos 17 cifras significativas, en realidad obtenemos aproximadamente 15 cifras correctas, debido a que Python utiliza números float de doble precisión, que permiten alrededor de 15 a 16 cifras significativas. El error verdadero de 2.69354×10⁻¹⁴ % equivale a un error relativo de aproximadamente 2.7×10⁻¹⁶. El programa terminó en el término 16 porque εa llegó a 0, no porque alcanzara la precisión solicitada, ya que εt sigue siendo mayor que εs (5×10⁻¹⁶ %). Esto se relaciona con 0.1 + 0.2, que en Python produce 0.30000000000000004 debido a que algunos números decimales no pueden representarse exactamente en binario. De la misma manera, al calcular la serie de Maclaurin, la precisión está limitada por la representación numérica, aunque 

## Uso de inteligencia artificial

Ninguno / Cuál y para qué.

## Referencias

