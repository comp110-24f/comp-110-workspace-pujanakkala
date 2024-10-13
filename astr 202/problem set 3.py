import numpy as np
import matplotlib.pyplot as plt

# Constants
h = 6.626e-27  # Planck's constant in erg.s
c = 3.0e10  # Speed of light in cm/s
k = 1.38e-16  # Boltzmann constant in erg/K
T = 6000  # Temperature in K

# Wavelength range in cm (1 Å = 1e-8 cm), from 0 to 50,000 Å
wavelengths = np.linspace(1e-8, 5e-5, 1000)


# Blackbody function
def blackbody_flux(lam, T):
    exponent = h * c / (lam * k * T)
    exponent = np.clip(exponent, None, 700)  # Prevent overflow in exp
    return (2 * np.pi * h * c**2) / (lam**5 * (np.exp(exponent) - 1))


# Rayleigh-Jeans approximation
def rayleigh_jeans(lam, T):
    return (2 * np.pi * c * k * T) / lam**4


# Wien approximation
def wien_approx(lam, T):
    return (2 * np.pi * h * c**2) / lam**5 * np.exp(-h * c / (lam * k * T))


# Calculate flux for each function
flux_blackbody = blackbody_flux(wavelengths, T)
flux_rayleigh_jeans = rayleigh_jeans(wavelengths, T)
flux_wien = wien_approx(wavelengths, T)

# Convert wavelengths to Ångstroms for plotting (1 cm = 1e8 Å)
wavelengths_angstrom = wavelengths * 1e8

# Plot
plt.figure(figsize=(10, 6))
plt.plot(wavelengths_angstrom, flux_blackbody, label="Blackbody", color="black")
plt.plot(
    wavelengths_angstrom,
    flux_rayleigh_jeans,
    label="Rayleigh-Jeans",
    color="red",
    linestyle="--",
)
plt.plot(
    wavelengths_angstrom,
    flux_wien,
    label="Wien Approximation",
    color="blue",
    linestyle="--",
)

# Set limits and labels
plt.xlim(0, 50000)  # Wavelength up to 50,000 Å
plt.ylim(0, 1e15)  # Adjust y-limits to match the scale in the example
plt.xlabel("Wavelength [Å]")
plt.ylabel("Flux [erg s$^{-1}$ cm$^{-2}$ Å$^{-1}$]")
plt.title("T=6000K Blackbody")

# Add grid and legend
plt.legend()
plt.grid(True)

# Show plot
plt.show()
