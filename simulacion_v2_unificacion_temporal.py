import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
pasos = 500
t = np.linspace(0, 100, pasos)
alpha = 1.0        # Capacidad máxima
beta = 0.5         # Sensibilidad
gamma = 0.02       # Deriva lineal (entrada de información)
umbral = 0.85      # Punto donde se activa el reset (sueño)

# Variables de estado
L = np.zeros(pasos)  # Nivel de consciencia
activacion = np.zeros(pasos)

# Simulación de la dinámica temporal
for i in range(1, pasos):
    # Crecimiento de la consciencia (MSSC v2.0)
    L[i] = L[i-1] + (gamma - 0.001 * L[i-1]) 
    activacion[i] = alpha * np.tanh(beta * L[i])
    
    # Mecanismo de Reset (v3.0) - Si llega al umbral, ocurre el sueño
    if activacion[i] > umbral:
        L[i] = L[i] * 0.1  # El "reset" reduce la carga de información
        print(f"Punto de reset detectado en t={i}")

# Visualización
plt.figure(figsize=(12, 6))
plt.plot(t, activacion, label='Nivel de Activación Consciente', color='blue', linewidth=2)
plt.axhline(y=umbral, color='red', linestyle='--', label='Umbral de Saturación (Necesidad de sueño)')
plt.title('Dinámica Temporal: Ciclo de Integración y Reset del MSSC v3.0')
plt.xlabel('Tiempo (Integración Temporal)')
plt.ylabel('Activación (C)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()