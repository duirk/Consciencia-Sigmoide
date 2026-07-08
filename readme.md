# Modelo de Saturación Sigmoide de la Consciencia (MSSC)

Este repositorio contiene la implementación computacional y la validación empírica del **Modelo de Saturación Sigmoide de la Consciencia (MSSC)**, una propuesta teórica que describe la consciencia como un sistema regulador de información.

## Descripción del Proyecto
El MSSC postula que la tasa de procesamiento consciente sigue una dinámica no lineal, tendiendo a la saturación asintótica ante niveles crecientes de estímulo. Este repositorio incluye:
* **Fundamentos Formales**: La definición matemática del nivel vibratorio ($V$) en función de la intensidad de información ($L$).
* **Validación Computacional**: Un script en Python que genera datos sintéticos y realiza una regresión no lineal para verificar la robustez del modelo.

## Contenido del Repositorio
* `Nadal_Ferra_MSSC_2026-2.pdf`: Documento académico que detalla la teoría, metodología y análisis de dinámica del modelo.
* `validacion_mssc.py`: Script de Python para la generación de datos, ajuste de parámetros ($\alpha, \beta, \gamma$) y visualización del modelo.

## Requisitos
Para ejecutar el script de validación, necesitas instalar las siguientes librerías:
```bash
pip install numpy sympy scipy matplotlib torch
