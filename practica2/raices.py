#!/usr/bin/env python3
"""raices.py — Práctica 2: raíces de ecuaciones no lineales, en Python.

Los cinco métodos de la unidad II sobre la misma ecuación. Imprime una tabla
por método y un resumen; las tablas deben coincidir, cifra por cifra, con las
de raices.m, raices.c y las de las láminas.

Python es la herramienta de verificación del curso: al final compara contra
scipy.optimize.brentq y genera las gráficas con la función graficar().

UEA 1151039 · Métodos Numéricos en Ingeniería · UAM Azcapotzalco · 26-O

Dentro del contenedor, en la carpeta practica2:
    python3 raices.py
"""
import math
import os

import matplotlib
matplotlib.use("Agg")                    # figuras a archivo, no a ventana
import matplotlib.pyplot as plt
from scipy.optimize import brentq

# ======================== BLOQUE DEL PROBLEMA ========================
# Ecuación 14 · Electrónica · Ángulo de extinción de un rectificador de media onda con carga RL

DESCRIPCION = 'f(b) = sin(b) - Q cos(b) + Q exp(-b / Q),  Q = wL/R = 2'
DESCR_G = 'g(b) = b + f(b) / 2'

WLR = 2.0   # cociente wL/R de la carga

A, B = 3.0, 6.0   # intervalo de los métodos cerrados
X0 = 4.0         # inicio de los métodos abiertos
DELTA = 0.01      # incremento de la secante modificada
TOL = 0.5           # tolerancia: ea en %
NMAX = 50           # máximo de iteraciones


def f(x):
    """La función cuya raíz se busca."""
    return math.sin(x) - WLR*math.cos(x) + WLR*math.exp(-x/WLR)


def fp(x):
    """Su derivada, para Newton-Raphson."""
    return math.cos(x) + WLR*math.sin(x) - math.exp(-x/WLR)


def g(x):
    """Despeje x = g(x) para punto fijo."""
    return x + f(x)/2

# =====================================================================

ENC_CERRADO = "   k             a             b             x            f(x)     ea (%)"
ENC_ABIERTO = "   k             x            f(x)     ea (%)"
ENC_RESUMEN = "            x  iter.     ea (%)            f(x)   método"


def error_aprox(nuevo, anterior):
    """Error relativo aproximado, en porcentaje: |(nuevo - anterior) / nuevo| · 100."""
    return abs((nuevo - anterior) / nuevo) * 100.0


def fila_cerrado(k, a, b, x, ea):
    texto = f"{ea:10.4f}" if ea is not None else f"{'-':>10}"
    print(f"{k:4d} {a:13.6f} {b:13.6f} {x:13.6f} {f(x):15.6e} {texto}")


def fila_abierto(k, x, ea):
    texto = f"{ea:10.4f}" if ea is not None else f"{'-':>10}"
    print(f"{k:4d} {x:13.6f} {f(x):15.6e} {texto}")


def cierre(r):
    if r["ok"]:
        print(f"   Raíz aproximada: {r['x']:.6f}  "
              f"({r['k']} iteraciones, ea = {r['ea']:.4f} %)")
    else:
        print(f"   No alcanzó la tolerancia en {NMAX} iteraciones.")
    print()


def biseccion(a, b):
    """Bisección: parte el intervalo a la mitad y conserva la mitad con cambio de signo."""
    r = {"nombre": "Bisección", "x": 0.0, "ea": 0.0, "k": 0, "ok": False, "historia": []}
    print(f"1. Bisección en [{a:g}, {b:g}]")
    print(ENC_CERRADO)
    x_ant = 0.0
    for k in range(1, NMAX + 1):
        x = (a + b) / 2.0                        # punto medio
        ea = error_aprox(x, x_ant) if k > 1 else None
        fila_cerrado(k, a, b, x, ea)
        r.update(x=x, ea=ea or 0.0, k=k)
        r["historia"].append((k, x, ea))
        if k > 1 and ea <= TOL:
            r["ok"] = True
            break
        if f(a) * f(x) < 0.0:
            b = x                                # la raíz está en [a, x]
        else:
            a = x                                # la raíz está en [x, b]
        x_ant = x
    cierre(r)
    return r


def falsa_posicion(a, b):
    """Falsa posición: corta la recta que une (a, f(a)) y (b, f(b)) con el eje x."""
    r = {"nombre": "Falsa posición", "x": 0.0, "ea": 0.0, "k": 0, "ok": False, "historia": []}
    print(f"2. Falsa posición en [{a:g}, {b:g}]")
    print(ENC_CERRADO)
    x_ant = 0.0
    for k in range(1, NMAX + 1):
        x = b - f(b) * (a - b) / (f(a) - f(b))   # cero de la recta
        ea = error_aprox(x, x_ant) if k > 1 else None
        fila_cerrado(k, a, b, x, ea)
        r.update(x=x, ea=ea or 0.0, k=k)
        r["historia"].append((k, x, ea))
        if k > 1 and ea <= TOL:
            r["ok"] = True
            break
        if f(a) * f(x) < 0.0:
            b = x
        else:
            a = x
        x_ant = x
    cierre(r)
    return r


def punto_fijo(x):
    """Punto fijo: repite x <- g(x)."""
    r = {"nombre": "Punto fijo", "x": x, "ea": 0.0, "k": 0, "ok": False, "historia": []}
    print(f"3. Punto fijo desde x0 = {x:g}, con {DESCR_G}")
    print(ENC_ABIERTO)
    fila_abierto(0, x, None)
    for k in range(1, NMAX + 1):
        x_nuevo = g(x)
        ea = error_aprox(x_nuevo, x)
        x = x_nuevo
        fila_abierto(k, x, ea)
        r.update(x=x, ea=ea, k=k)
        r["historia"].append((k, x, ea))
        if ea <= TOL:
            r["ok"] = True
            break
    cierre(r)
    return r


def newton(x):
    """Newton-Raphson: el cero de la recta tangente en x."""
    r = {"nombre": "Newton-Raphson", "x": x, "ea": 0.0, "k": 0, "ok": False, "historia": []}
    print(f"4. Newton-Raphson desde x0 = {x:g}")
    print(ENC_ABIERTO)
    fila_abierto(0, x, None)
    for k in range(1, NMAX + 1):
        x_nuevo = x - f(x) / fp(x)
        ea = error_aprox(x_nuevo, x)
        x = x_nuevo
        fila_abierto(k, x, ea)
        r.update(x=x, ea=ea, k=k)
        r["historia"].append((k, x, ea))
        if ea <= TOL:
            r["ok"] = True
            break
    cierre(r)
    return r


def secante_modificada(x, delta):
    """Secante modificada: Newton con la derivada aproximada por una diferencia."""
    r = {"nombre": "Secante modificada", "x": x, "ea": 0.0, "k": 0, "ok": False, "historia": []}
    print(f"5. Secante modificada desde x0 = {x:g}, delta = {delta:g}")
    print(ENC_ABIERTO)
    fila_abierto(0, x, None)
    for k in range(1, NMAX + 1):
        x_nuevo = x - delta * f(x) / (f(x + delta) - f(x))
        ea = error_aprox(x_nuevo, x)
        x = x_nuevo
        fila_abierto(k, x, ea)
        r.update(x=x, ea=ea, k=k)
        r["historia"].append((k, x, ea))
        if ea <= TOL:
            r["ok"] = True
            break
    cierre(r)
    return r


def graficar(resultados, carpeta="img"):
    """Guarda dos figuras en la carpeta img/:

    1. img/funcion.png: f(x) en [A, B], la recta y = 0 y la raíz de cada método.
    2. img/convergencia.png: ea (%) contra k, una curva por método, con el eje
       vertical en escala logarítmica y la tolerancia como línea horizontal.
    """
    os.makedirs(carpeta, exist_ok=True)
    marcadores = ["o", "s", "^", "D", "v"]

    # ---- Figura 1: f(x) y la raíz de cada método ----
    # El rango cubre el intervalo [A, B] y también cualquier raíz que haya
    # quedado fuera de él (por ejemplo, la de un método abierto).
    raices = [r["x"] for r in resultados]
    margen = 0.05 * (B - A)
    inicio = min([A] + raices) - margen
    fin = max([B] + raices) + margen
    n = 400
    xs = [inicio + (fin - inicio) * i / (n - 1) for i in range(n)]
    ys = [f(x) for x in xs]

    plt.figure(figsize=(8, 5))
    plt.plot(xs, ys, color="black", label="f(x)")
    plt.axhline(0.0, color="gray", linewidth=0.8)
    for i, r in enumerate(resultados):
        plt.plot(r["x"], f(r["x"]), marcadores[i % len(marcadores)],
                 markersize=8, label=f"{r['nombre']}: {r['x']:.6f}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("f(x) y la raíz de cada método")
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(carpeta, "funcion.png"), dpi=150, bbox_inches="tight")
    plt.close()

    # ---- Figura 2: convergencia, ea contra k en escala logarítmica ----
    plt.figure(figsize=(8, 5))
    for i, r in enumerate(resultados):
        # Se omiten los None (primera fila de los métodos cerrados) y los
        # ceros, que la escala logarítmica no puede dibujar.
        puntos = [(k, ea) for (k, _, ea) in r["historia"]
                  if ea is not None and ea > 0.0]
        if not puntos:
            continue
        ks = [p[0] for p in puntos]
        eas = [p[1] for p in puntos]
        plt.semilogy(ks, eas, marker=marcadores[i % len(marcadores)],
                     label=r["nombre"])
    plt.axhline(TOL, color="red", linestyle="--", label=f"Tolerancia {TOL:g} %")
    plt.xlabel("k (iteración)")
    plt.ylabel("ea (%)")
    plt.title("Convergencia de los cinco métodos")
    plt.legend()
    plt.grid(True, which="both", alpha=0.4)
    plt.savefig(os.path.join(carpeta, "convergencia.png"), dpi=150, bbox_inches="tight")
    plt.close()

    print(f"Figuras guardadas en {carpeta}/funcion.png y {carpeta}/convergencia.png")


def main():
    print("Práctica 2 · Raíces de ecuaciones no lineales · Python")
    print(DESCRIPCION)
    print(f"Tolerancia: ea <= {TOL:g} %, máximo {NMAX} iteraciones")
    print()
    resultados = [biseccion(A, B), falsa_posicion(A, B), punto_fijo(X0),
                  newton(X0), secante_modificada(X0, DELTA)]

    print("Resumen")
    print(ENC_RESUMEN)
    for r in resultados:
        aviso = "" if r["ok"] else " (no convergió)"
        print(f"{r['x']:13.6f} {r['k']:6d} {r['ea']:10.4f} {f(r['x']):15.6e}   {r['nombre']}{aviso}")
    print()

    # Verificación: SciPy encuentra la raíz con precisión de máquina.
    referencia = brentq(f, A, B, xtol=1e-14)
    print(f"Verificación con SciPy, brentq en [{A:g}, {B:g}]: x = {referencia:.9f}")
    print("   Error verdadero, en %:")
    for r in resultados:
        et = abs((referencia - r["x"]) / referencia) * 100.0
        print(f"   {et:10.6f}   {r['nombre']}")
    print()

    graficar(resultados)


if __name__ == "__main__":
    main()