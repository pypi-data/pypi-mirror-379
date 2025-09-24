"""
Este módulo contiene funciones para cálculos de gravitación.
"""

from cinetica.units import ureg

G = 6.67430e-11 * ureg.newton * ureg.meter**2 / ureg.kilogram**2

class Gravitacion:
    def __init__(self, m1, r, m2=None):
        self.m1 = m1
        self.m2 = m2
        self.r = r

    def fuerza_gravitacional(self):
        """Calcula la fuerza gravitacional entre dos masas."""
        if self.m2 is None:
            raise ValueError("Se requieren dos masas para calcular la fuerza gravitacional.")
        return G * self.m1 * self.m2 / self.r**2

    def campo_gravitacional(self):
        """Calcula el campo gravitacional de una masa."""
        return G * self.m1 / self.r**2

    def energia_potencial_gravitacional(self):
        """Calcula la energía potencial gravitacional entre dos masas."""
        if self.m2 is None:
            raise ValueError("Se requieren dos masas para calcular la energía potencial gravitacional.")
        return (-G * self.m1 * self.m2 / self.r).to(ureg.joule)
