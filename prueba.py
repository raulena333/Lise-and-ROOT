import numpy as np
import matplotlib.pyplot as plt

# Definir constantes
R_G = 60  # Radio de la esfera (mm)
r_b = 8   # Radio del blanco (mm)
haz_radio = 1.5  # Radio del haz (mm)
theta_A = 38 * np.pi / 180  # Ángulo polar para el telescopio A (rad)
phi_A = 270 * np.pi / 180  # Ángulo azimutal para el telescopio A (rad)

# Coordenadas cartesianas del telescopio A
x_A = R_G * np.sin(theta_A) * np.cos(phi_A)
y_A = R_G * np.sin(theta_A) * np.sin(phi_A)
z_A = R_G * np.cos(theta_A)

# Coordenadas del centro del blanco (suponiendo que está en el origen)
x_C = 0
y_C = 0
z_C = 0

# Imprimir las coordenadas del telescopio A
print(f"Coordenadas del telescopio A: ({x_A:.2f}, {y_A:.2f}, {z_A:.2f})")

# Generación de 10 puntos dispersados aleatoriamente dentro del área del haz (1.5 mm)
num_puntos = 10
puntos_disp = []

for _ in range(num_puntos):
    # Generar puntos aleatorios dentro del círculo de radio 1.5 mm en el plano XY
    r = haz_radio * np.sqrt(np.random.uniform(0, 1))  # Radio dentro del círculo
    theta = np.random.uniform(0, 2 * np.pi)  # Ángulo aleatorio en [0, 2pi]
    
    x_disp = r * np.cos(theta)
    y_disp = r * np.sin(theta)
    z_disp = 0  # El haz está en el plano XY
    
    puntos_disp.append([x_disp, y_disp, z_disp])

# Convertir los puntos dispersados a un array de numpy para facilidad de cálculo
puntos_disp = np.array(puntos_disp)

# Calcular los ángulos de dispersión para cada punto generado
ang_disp = []

for punto_disp in puntos_disp:
    # Vectores de posición: desde el centro del blanco (P_c) al telescopio A y al punto dispersado
    vec_P_C_A = np.array([x_A - x_C, y_A - y_C, z_A - z_C])
    vec_P_C_disp = punto_disp - np.array([x_C, y_C, z_C])

    # Calcular el ángulo de dispersión entre los vectores
    cos_theta_disp = np.dot(vec_P_C_A, vec_P_C_disp) / (np.linalg.norm(vec_P_C_A) * np.linalg.norm(vec_P_C_disp))
    theta_disp = np.arccos(cos_theta_disp)
    ang_disp.append(np.degrees(theta_disp))  # Convertir a grados

# Imprimir los ángulos de dispersión calculados
print("Ángulos de dispersión (en grados) para los 10 puntos dispersados:")
for i, ang in enumerate(ang_disp):
    print(f"Punto {i+1}: {ang:.2f} grados")

# Visualización de la geometría
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Graficar el centro del blanco (origen)
ax.scatter(0, 0, 0, color='red', label='Centro del Blanco')

# Graficar el telescopio A
ax.scatter(x_A, y_A, z_A, color='blue', label='Telescopio A')

# Graficar los 10 puntos dispersados
ax.scatter(puntos_disp[:, 0], puntos_disp[:, 1], puntos_disp[:, 2], color='green', label='Puntos Dispersados')

# Vectores: desde el centro del blanco hacia el telescopio y los puntos dispersados
ax.quiver(0, 0, 0, x_A, y_A, z_A, color='blue', length=1, label='Vector al Telescopio A')

# Etiquetas y configuraciones de visualización
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.title('Geometría del telescopio y los puntos dispersados')
plt.show()
import numpy as np
import matplotlib.pyplot as plt

# Definir constantes
R_G = 60  # Radio de la esfera (mm)
r_b = 8   # Radio del blanco (mm)
haz_radio = 1.5  # Radio del haz (mm)
theta_A = 38 * np.pi / 180  # Ángulo polar para el telescopio A (rad)
phi_A = 270 * np.pi / 180  # Ángulo azimutal para el telescopio A (rad)

# Coordenadas cartesianas del telescopio A
x_A = R_G * np.sin(theta_A) * np.cos(phi_A)
y_A = R_G * np.sin(theta_A) * np.sin(phi_A)
z_A = R_G * np.cos(theta_A)

# Coordenadas del centro del blanco (suponiendo que está en el origen)
x_C = 0
y_C = 0
z_C = 0

# Imprimir las coordenadas del telescopio A
print(f"Coordenadas del telescopio A: ({x_A:.2f}, {y_A:.2f}, {z_A:.2f})")

# Definir un haz dispersado en el centro del blanco (por ejemplo, sin dispersión inicial)
# Las coordenadas de dispersión (punto dispersado en el plano XY)
delta_x = haz_radio * np.random.uniform(-1, 1)
delta_y = haz_radio * np.random.uniform(-1, 1)

# Calcular el ángulo de dispersión para el haz en el plano XY
# Generamos un punto dispersado al azar en el rango del haz
x_disp = delta_x
y_disp = delta_y
z_disp = 0  # El haz está en el plano XY

# Vectores de posición: desde el centro del blanco (P_c) al telescopio A y al punto dispersado
vec_P_C_A = np.array([x_A - x_C, y_A - y_C, z_A - z_C])
vec_P_C_disp = np.array([x_disp - x_C, y_disp - y_C, z_disp - z_C])

# Calcular el ángulo de dispersión entre los vectores
cos_theta_disp = np.dot(vec_P_C_A, vec_P_C_disp) / (np.linalg.norm(vec_P_C_A) * np.linalg.norm(vec_P_C_disp))
theta_disp = np.arccos(cos_theta_disp)

# Convertir el ángulo a grados
theta_disp_deg = np.degrees(theta_disp)
print(f"Ángulo de dispersión: {theta_disp_deg:.2f} grados")

# Visualización de la geometría
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Graficar el centro del blanco (origen)
ax.scatter(0, 0, 0, color='red', label='Centro del Blanco')

# Graficar el telescopio A
ax.scatter(x_A, y_A, z_A, color='blue', label='Telescopio A')

# Graficar el punto dispersado
ax.scatter(x_disp, y_disp, z_disp, color='green', label='Punto Dispersado')

# Vectores: desde el centro del blanco hacia el telescopio y el punto dispersado
ax.quiver(0, 0, 0, x_A, y_A, z_A, color='blue', length=1, label='Vector al Telescopio A')
ax.quiver(0, 0, 0, x_disp, y_disp, z_disp, color='green', length=1, label='Vector al Punto Dispersado')

# Etiquetas y configuraciones de visualización
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.title('Geometría del telescopio y el haz dispersado')
plt.show()
