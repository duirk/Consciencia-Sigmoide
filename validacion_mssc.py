import sympy as sp
import torch
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# PARTE 1: DEFINICIÓN DE LA ONTOLOGÍA MATEMÁTICA
# Definimos las variables simbólicas que rigen el sistema de consciencia
L, alpha, beta, gamma = sp.symbols('L alpha beta gamma', real=True, positive=True)
# Ley de estado: V(L) = alpha * tanh(beta * L) + gamma * L
modelo_teorico = alpha * sp.tanh(beta * L) + gamma * L
print(f"Modelo MSSC propuesto: V(L) = {modelo_teorico}")

# PARTE 2: GENERACIÓN DE DATOS SINTÉTICOS (Modelado)
# Simulamos datos con ruido gaussiano para emular un entorno de estrés informativo
def generar_datos(n=100):
    L_data = np.linspace(0.1, 10, n)
    # Función de generación con ruido para validar robustez
    V_data = 2.0 * np.tanh(0.5 * L_data) + 0.05 * np.random.normal(size=n)
    return L_data, V_data

L_val, V_val = generar_datos()

# PARTE 3: AJUSTE Y VALIDACIÓN (Regresión No Lineal)
# Ajustamos los parámetros del modelo a los datos generados
def funcion_ajuste(L, a, b):
    return a * np.tanh(b * L)

# Aplicamos la optimización de curva para encontrar alpha y beta
parametros, _ = curve_fit(funcion_ajuste, L_val, V_val)
print(f"Parámetros optimizados -> Alpha: {parametros[0]:.4f}, Beta: {parametros[1]:.4f}")

# PARTE 4: VISUALIZACIÓN DE RESULTADOS
plt.figure(figsize=(10, 6))
plt.scatter(L_val, V_val, label='Datos Experimentales (Simulados)', alpha=0.5, color='gray')
plt.plot(L_val, funcion_ajuste(L_val, *parametros), label='Ajuste MSSC (tanh)', color='red', linewidth=3)
plt.title('Validación Empírica del Modelo de Saturación de la Consciencia')
plt.xlabel('Intensidad de Consciencia (L)')
plt.ylabel('Nivel Vibratorio (V)')
plt.legend()
plt.grid(True)
plt.show()