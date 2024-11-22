import numpy as np
import matplotlib.pyplot as plt

# Define constants
R_G = 60  # Radius of the sphere (tangential point) in mm
r_b = 1.5  # Radius of the beam at the position of the target in mm
beta = 30  # Inclination angle of target in degrees

# Convert beta to radians once for reuse
beta_rad = np.deg2rad(beta)

# Define spherical coordinates for telescopes A, B, C, D, E, F
telescopes = {
    'A': {'theta': 38, 'phi': 270},
    'B': {'theta': 38, 'phi': 90},
    'C': {'theta': 142, 'phi': 90},
    'D': {'theta': 142, 'phi': 270},
    'E': {'theta': 105, 'phi': 0},
    'F': {'theta': 75, 'phi': 180}
}

# Function to calculate r_alpha(phi), the distance from the center of the target to the ellipse at phi
def r_alpha(phi):
    """
    Calculate the radius at a given angle `phi` considering the target's inclination angle `beta`.
    """
    phi_rad = np.deg2rad(phi)
    return r_b * np.sqrt(np.sin(phi_rad)**2 + (np.cos(phi_rad) / np.cos(beta_rad))**2)

# Function to calculate the position vector P_Pi for a given telescope (theta, phi)
def calculate_PPi(theta, phi):
    """
    Calculate the position vector P_i for a given telescope using spherical coordinates.
    The result is a 3D cartesian vector.
    """
    # Convert theta and phi to radians
    theta_rad = np.deg2rad(theta)
    phi_rad = np.deg2rad(phi)

    # Telescope position components (radius R_G)
    x_i = R_G * np.sin(theta_rad) * np.cos(phi_rad)
    y_i = R_G * np.sin(theta_rad) * np.sin(phi_rad)
    z_i = R_G * np.cos(theta_rad)

    # Calculate radial distance at angle phi for the ellipse
    r_E = -r_alpha(phi)

    # Calculate position components of the ellipse point
    x = r_E * np.sin(theta_rad) * np.cos(phi_rad)
    y = r_E * np.sin(theta_rad) * np.sin(phi_rad)
    z = r_E * np.cos(theta_rad)

    # Return the sum of the position vectors as a 3D numpy array
    return np.array([x_i + x, y_i + y, z_i + z])

# Function to calculate the modulus (magnitude) of the position vector P_Pi
def calculate_modulus_PPi(P_Pi):
    """
    Calculate the modulus (magnitude) of the position vector P_Pi.
    """
    return np.linalg.norm(P_Pi)

# Function to calculate the dot product of the position vector P_Pi and the unit vector k (which is along the z-axis)
def dot_product_PPi_with_k(P_Pi):
    """
    Calculate the dot product of the position vector P_i and the unit vector k (along the z-axis).
    """
    # Define the unit vector k (along the z-axis)
    k = np.array([0, 0, 1])

    # Return the dot product of P_Pi and k (just the z-component)
    return np.dot(P_Pi, k)

# Function to calculate the normalized dot product (which is the cosine of the angle)
def normalized_dot_product_PPi_with_k(P_Pi, modulus_PPi):
    """
    Calculate the normalized dot product of the position vector P_i and the unit vector k (along the z-axis).
    This corresponds to cos(theta) of the angle between them.
    """
    dot_product = dot_product_PPi_with_k(P_Pi)
    return dot_product / modulus_PPi

# Function to calculate the dispersion angle (arccos of the normalized dot product)
def calculate_dispersion_angle(value):
    """
    Calculate the dispersion angle (in radians) from the normalized dot product.
    """
    return np.arccos(value)

# Example usage: Calculate the dot product for telescopes A and B
def calculate_for_telescope(theta, phi):
    """
    Perform all necessary calculations for a given telescope.
    """
    P_Pi = calculate_PPi(theta, phi)
    modulus_PPi = calculate_modulus_PPi(P_Pi)
    normalized_dot = normalized_dot_product_PPi_with_k(P_Pi, modulus_PPi)
    dispersion_angle = calculate_dispersion_angle(normalized_dot)
    
    return normalized_dot, np.degrees(dispersion_angle)

# Calculate for telescopes A and B
for telescope, coords in telescopes.items():
    theta, phi = coords['theta'], coords['phi']
    normalized_dot, dispersion_angle = calculate_for_telescope(theta, phi)
    print(f"Telescope {telescope}:")
    print(f"  Normalized dot product: {normalized_dot}")
    print(f"  Dispersion angle: {dispersion_angle} degrees")
