  <br>
	<h1>Tarea no.1</h1>

<br> Métodos Numéricos en Ingeniería (clave 1151039) Trimestre 26-O <br>
Profesor: M. en C. Gabriel Hurtado Avilés <br>
Alumno: Trejo Ponce Julio Antonio <br>
Matricula: 2243038326 <br>
Carrera: Ingeniería en electrónica <br>
Fecha de entrega: 10/10/2026 <br>

---

<br> 
1. ¿Qué son los metodoso numéricos?<br> 
<p align="justify">
Los metodos numericos son tecnicas que modifican un problema matematico para poder resolverlo solo con operaciones aritmeticas (Chapra & Canale, 2007, p. 3).
A diferencia de una solución analitica la cual nos da una formula exacta y un valor verdadero, los metodos numericos los sustituyen por esquemas discretos(convierte un problema infinito en uno finito) y algoritmos iterativos(repetir un mismo paso muchas veces, usando el resultado anterior como punto de partida del siguiente) que calculan valores estimados.
El resultado numérico es aproximado por dos fuentes de error: el truncamiento, que aparece al representar un proceso infinito con uno finito (Chapra & Canale, 2007, p. 60; Burden & Faires, 2011, p. 11) y el redondeo, que surge porque las computadoras almacenan los números con un número finito de dígitos (Chapra & Canale, 2007, p. 61).
El error es lo que permite saber qué tan confiable es un resultado aproximado. Se define como la diferencia entre el valor verdadero y la aproximación (Chapra & Canale, 2007, p. 63). El error absoluto es |p − p*| y el relativo es |p − p*| / |p|; el relativo es una mejor medida de exactitud porque toma en cuenta el tamaño del valor que se aproxima (Burden & Faires, 2011, pp. 20–21).
</p>

2. ¿Cómo de aplican en su ingenieria?<br>
<p align="justify">
En ingeniería electrónica, los métodos numéricos se pueden aplicar para analizar, diseñar o resolver circuitos, los cuales, mientras más complejos son, tienen ecuaciones muy complicadas o muy grandes para resolverlas de forma analítica. Por ejemplo, se utilizan para calcular las corrientes y voltajes en circuitos con múltiples mallas y nodos, ya que se generan sistemas de ecuaciones difíciles de resolver manualmente. También permiten analizar las señales electrónicas en circuitos RLC, calculando su respuesta transitoria a lo largo del tiempo, debido a que las ecuaciones diferenciales involucradas pueden ser difíciles de resolver mediante una fórmula cerrada, especialmente en circuitos complejos.
</p>

<p align="center">
<img width="324" height="133" alt="image" src="https://github.com/user-attachments/assets/7b12a76b-1f22-45f7-84b1-a9d0909f7604" /><br>
	Figura A: Corriente en una red de resistores.
</p>
<p align="justify">
a) Corrientes en una red de resistores. Con las leyes de Kirchhoff, un circuito de seis nodos con resistores y fuentes de 200 V y 0 V se convierte en un sistema de seis ecuaciones lineales, y lo que se calcula son las seis corrientes desconocidas. No basta una fórmula cerrada porque los sistemas de circuitos reales crecen con el número de nodos y son demasiado grandes para resolverse a mano, así que se usa un método sistemático como la eliminación de Gauss (Chapra & Canale, 2007, pp. 329, 336–337).
</p>

<p align="center">
<img width="350" height="148" alt="image" src="https://github.com/user-attachments/assets/a748eb49-9ba6-48dd-b138-39d22b9a28b2" /><br>
	Figura B: resistencias de un circuito RLC.
</p>

<p align="justify">
b) Resistencia de un circuito RLC. Se busca la resistencia R para que la carga de un capacitor baje al 1 % en 0.05 s. No se puede despejar R, porque aparece dentro de un exponencial y un coseno, así que se aproxima con bisección y resulta R ≈ 328.15 Ω (Chapra & Canale, 2007, pp. 213–215). Este tipo de ecuación, en la que la incógnita no se puede despejar de forma explícita, se resuelve con métodos numéricos con la exactitud que se desee (Burden & Faires, 2011, pp. 48–49).
</p>
   
3. ¿Qué herramientas se usan para trabajar con metodos numericos?<br>
<p align="justify">
-Lenguajes compilados (C, C++, Fortran). Son lenguajes cuyo código se traduce a un ejecutable antes de correr, y por eso son rápidos. Burden y Faires (2011, pp. ix–x) ofrecen un programa por algoritmo en FORTRAN, Pascal, C y Java. También explican que la mayor parte del software numérico estándar está escrito en FORTRAN, con algunos paquetes en C, C++ y Fortran 90 (2011, p. 44). Chapra y Canale (2007, sección 15.3) usan Fortran 90 en sus ejemplos de programas principales que llaman funciones de la biblioteca IMSL.}
</p>
<p align="justify">
-Lenguajes interpretados. Son lenguajes cuyas instrucciones se ejecutan una por una sin generar antes un ejecutable. Chapra y Canale (2007, sección 15.3) muestran cómo las macros de Visual Basic de Excel dan acceso a algoritmos de optimización dentro de una hoja de cálculo, un ejemplo de lenguaje interpretado dentro de una aplicación.
</p>
<p align="justify">
-Entornos matriciales (MATLAB, GNU Octave). Burden y Faires (2011, p. 45) explican que MATLAB nació como un “laboratorio de matrices” basado en las rutinas EISPACK y LINPACK, y que después se le añadieron integración, ecuaciones diferenciales, ajuste de curvas y gráficos. Chapra y Canale (2007) dedican un apéndice a MATLAB (Apéndice C, según el índice). GNU Octave es un entorno gratuito con sintaxis en gran parte compatible con MATLAB, aunque ninguno de los dos libros lo menciona.
</p>	
<p align="justify">
-Python científico (NumPy, SciPy, Matplotlib). Ninguno de los dos libros trata Python ni sus bibliotecas científicas, porque son anteriores a su adopción general (2007 y 2011). NumPy aporta arreglos y álgebra lineal, SciPy métodos de integración, ecuaciones diferenciales, optimización e interpolación, y Matplotlib las gráficas.
</p>
<p align="justify">
-Álgebra simbólica. Burden y Faires (2011, p. 46) eligen Maple como sistema de álgebra computacional del libro, porque da respuestas exactas (integrales, ecuaciones diferenciales, sistemas lineales) además de cálculo numérico. Mencionan Mathematica como alternativa equivalente. Chapra y Canale (2007) trabajan con Mathcad (Apéndice B, según el índice).
</p>
<p align="justify">
-Bibliotecas de base (BLAS, LAPACK). Burden y Faires (2011, pp. 44–45) describen LINPACK y EISPACK, y LAPACK (disponible desde 1992), que las sustituye y reúne sus algoritmos. BLAS son las subrutinas básicas de álgebra lineal que se distribuyen junto con LAPACK. Describen además las bibliotecas comerciales IMSL y NAG (2011, p. 45). Chapra y Canale (2007, sección 15.3.4) usan IMSL.
</p>
<p align="justify">
	
<ins>Qué herramientas usa cada libro</ins>

Chapra y Canale (2007)

Lenguajes compilados: Fortran 90, junto con la biblioteca IMSL.
Lenguajes interpretados: macros de Visual Basic dentro de Excel.
Entornos matriciales: MATLAB.
Python científico: no lo trata.
Álgebra simbólica: Mathcad.
Bibliotecas de base: IMSL.

Burden y Faires (2011)

Lenguajes compilados: FORTRAN, Pascal, C y Java.
Lenguajes interpretados: no los trata como tema aparte.
Entornos matriciales: MATLAB.
Python científico: no lo trata.
Álgebra simbólica: Maple (el principal) y Mathematica.
Bibliotecas de base: LINPACK, EISPACK, LAPACK, BLAS, IMSL y NAG.
</p>
   
   
4.¿Qué herramientas usamos en este curso?<br> 
<p align="justify">
Docker. Docker es una plataforma que empaqueta una aplicación y todo lo que necesita (sistema base, bibliotecas, herramientas) en una imagen, y la ejecuta como contenedor. Para este curso sirve porque todos trabajamos con exactamente el mismo entorno (Octave, Python y gcc ya instalados), sin importar el sistema operativo de cada quien. 

Docker frente a una máquina virtual. Una máquina virtual emula hardware completo y corre su propio sistema operativo con su propio kernel, por lo que pesa más y tarda en arrancar. Un contenedor comparte el kernel del sistema anfitrión y solo aísla procesos, red y archivos, así que es mucho más ligero y arranca casi al instante. A cambio, su aislamiento es menor que el de una máquina virtual.

Lo que vimos de Docker. El Dockerfile es la receta para construir la imagen: parte de una imagen base e instala los paquetes necesarios. El archivo compose.yaml describe cómo se ejecuta el servicio (imagen o construcción, volúmenes, nombre del servicio) para levantarlo con un solo comando. Los comandos que usamos son estos:

docker compose up -d crea y arranca el contenedor en segundo plano.<br> 
docker compose exec <servicio> <comando> ejecuta un comando dentro de un contenedor que ya está corriendo.<br> 
docker compose stop apaga el contenedor.<br> 
docker compose down detiene el contenedor y lo borra.<br> 
docker compose ps lista los contenedores y su estado.<br> 
docker compose logs muestra la salida del contenedor.<br> 

Apagar y borrar no son lo mismo. Con stop el contenedor sigue existiendo y se puede volver a arrancar con su estado intacto. Con down el contenedor (y la red que Compose creó) se elimina, y al siguiente up se crea uno nuevo a partir de la imagen. Los archivos que viven en un volumen o en una carpeta montada del anfitrión sobreviven al down.

Octave: docker compose exec metodos octave --version → GNU Octave, version 7.3.0
Python: docker compose exec metodos python3 --version → Python 3.11.2
C con gcc: docker compose exec metodos gcc --version → gcc (Debian 12.2.0-14+deb12u1) 12.2.0
</p>

---

Capturas de pantalla del entorno 
<img width="1672" height="706" alt="image" src="https://github.com/user-attachments/assets/d27c7b95-56f8-4f0d-935e-69daa2da6db6" />
Figura 1: Contenedor encendido

1. docker compose up -d --build
   <img width="1096" height="545" alt="image" src="https://github.com/user-attachments/assets/2b4eabff-c744-4c6e-acc6-d4ca3bb5e14b" />
Figura 2: Contenedor encendido ejecutado en segundo plano <br> 
2. docker compose ps

<img width="1171" height="236" alt="image" src="https://github.com/user-attachments/assets/512dc3f1-c496-4236-b4ea-480631cc65f3" />
   
Figura 3: Status del contenedor <br> 
   
3. Dentro del contenedor: octave --version, python3 --version y gcc --version.<br>
  
   <img width="1288" height="737" alt="image" src="https://github.com/user-attachments/assets/69482142-532b-459e-99df-00238c8b4fee" />
    Figura 4:versiones de pyton, c y octave<br> 

4. Docker Desktop con el contenedor del curso en la lista.
   <img width="1919" height="1012" alt="image" src="https://github.com/user-attachments/assets/6d9b57ad-5796-469a-b05b-3b92e2c1a275" />
   Figura 5: Contenerdor encendido en Docker Desktop<br>
  

5. Sus dos programas ejecutándose dentro del contenedor.
   <img width="1082" height="362" alt="image" src="https://github.com/user-attachments/assets/6f151445-4351-49ba-a985-4b7e85d5bfde" />
      Figura 6: Programa 1 suma de dos numeros<br>

	  ¿Por qué 0.1 + 0.2 no da exactamente 0.3 y si los tres lenguajes coinciden? por que la computadora trabaja internamente en binario el cual solo puede representar fracciones cuyo denominador es una potencia de 2.
  
   <img width="1263" height="868" alt="image" src="https://github.com/user-attachments/assets/a3159cf9-f0b8-4f87-a083-69b5872184b3" />
      Figura 7: programa 2 calculadora<br>
	  
| Casos | Entradas | Salidas |
| :--- | :--- | :--- |
| Dividir entre 0 | 1/0 | no se puede dividir entre 0 |
| Simbolo que no es un numero | n/39 | debe ingresar un numero valido |

## Referencias

Burden, R. L., & Faires, J. D. (2011). *Numerical analysis* (9th ed.). Brooks/Cole, Cengage Learning.

Chapra, S. C., & Canale, R. P. (2007). *Métodos numéricos para ingenieros* (5.ª ed.). McGraw-Hill Interamericana.
   
