import numpy as np
import matplotlib.pyplot as plt

# Parámetros del modelo v2.0
gain = 0.5
wx, wint, wAT = 0.4, 0.3, 0.2
temp_cuerpo = 310.0 # Temperatura base (Kelvin)

def calcular_L(t):
    """Simulación de la convergencia: Memoria, Presente, Futuro"""
    memoria = np.sin(t / 10)     # Pasado cíclico
    presente = np.cos(t / 5)     # Percepción actual
    futuro = np.sin(t / 2)       # Proyección
    return memoria + presente + futuro

def calcular_Cnew(L, T_actual):
    """Métrica de activación Cnew según la ecuación (1)"""
    # AT = |T - 310.0|
    AT = abs(T_actual - temp_cuerpo)
    # Sincronía (S) y Coherencia (Cq) como factores dinámicos
    S = 0.8 
    Cq = 0.9
    
    # Ecuación (1): exp(gain * [wx*x + wint(Cq*S) - wAT*AT])
    exponente = gain * (wx * L + wint * (Cq * S) - wAT * AT)
    return np.exp(exponente)

# Simulación
t = np.linspace(0, 50, 500)
L_t = calcular_L(t)
# Variación homeostática simulada (ligera fluctuación de temperatura)
T_t = 310.0 + np.random.normal(0, 0.5, 500) 

C_new_t = [calcular_Cnew(L_t[i], T_t[i]) for i in range(len(t))]

# Visualización
plt.figure(figsize=(12, 6))
plt.plot(t, C_new_t, label='Activación Consciente (Cnew)', color='purple', linewidth=2)
plt.axhline(y=np.mean(C_new_t), color='red', linestyle='--', label='Umbral de Coherencia')
plt.title('MSSC v2.0: Dinámica de Unificación Temporal y Punto de Ignición')
plt.xlabel('Tiempo (Evolución de la Identidad)')
plt.ylabel('Activación de Unificación (Cnew)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()