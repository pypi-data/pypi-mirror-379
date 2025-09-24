"""
Módulo para cálculos de momento angular en sistemas rotacionales.
"""

import numpy as np
from typing import Union, Optional
from ...units import ureg, Q_
from ...logger import get_logger

logger = get_logger('cinetica.dinamica.rotacional.momento_angular')


class MomentoAngular:
    """
    Clase para cálculos de momento angular y su conservación.
    
    Attributes:
        momento_angular (Q_): Momento angular del sistema
        inercia (Q_): Momento de inercia
        velocidad_angular (Q_): Velocidad angular
    """
    
    def __init__(self):
        """Inicializa la clase MomentoAngular."""
        self.momento_angular = Q_(0, 'kg * m**2 / s')
        self.inercia = Q_(0, 'kg * m**2')
        self.velocidad_angular = Q_(0, 'rad/s')
    
    def calcular_momento_angular(self, inercia: Q_, velocidad_angular: Q_) -> Q_:
        """
        Calcula el momento angular L = I * ω.
        
        Args:
            inercia: Momento de inercia [kg·m²]
            velocidad_angular: Velocidad angular [rad/s]
            
        Returns:
            Momento angular [kg·m²/s]
            
        Raises:
            ValueError: Si los valores son negativos
        """
        if inercia.magnitude < 0:
            raise ValueError("El momento de inercia no puede ser negativo")
        if velocidad_angular.magnitude < 0:
            logger.warning("Velocidad angular negativa - interpretando como dirección")
        
        self.inercia = inercia
        self.velocidad_angular = velocidad_angular
        self.momento_angular = inercia * velocidad_angular
        
        logger.info(f"Momento angular calculado: {self.momento_angular}")
        return self.momento_angular
    
    def momento_angular_particula(self, masa: Q_, posicion: np.ndarray, velocidad: np.ndarray) -> Q_:
        """
        Calcula el momento angular de una partícula L = r × p.
        
        Args:
            masa: Masa de la partícula [kg]
            posicion: Vector de posición [m]
            velocidad: Vector de velocidad [m/s]
            
        Returns:
            Momento angular [kg·m²/s]
        """
        # Convertir a unidades base
        r = posicion * ureg.meter
        v = velocidad * ureg.meter / ureg.second
        m = masa
        
        # Momento lineal p = m * v
        momento_lineal = m * v
        
        # Momento angular L = r × p
        momento_angular_vec = np.cross(r.magnitude, momento_lineal.magnitude) * ureg.kg * ureg.meter**2 / ureg.second
        
        self.momento_angular = momento_angular_vec
        logger.info(f"Momento angular de partícula: {momento_angular_vec}")
        return momento_angular_vec
    
    def conservacion_momento_angular(self, momento_inicial: Q_, momento_final: Q_) -> bool:
        """
        Verifica la conservación del momento angular.
        
        Args:
            momento_inicial: Momento angular inicial
            momento_final: Momento angular final
            
        Returns:
            True si se conserva el momento angular
        """
        tolerancia = 1e-10
        conservado = abs(momento_final.magnitude - momento_inicial.magnitude) < tolerancia
        
        if conservado:
            logger.info("Se conserva el momento angular")
        else:
            logger.warning(f"No se conserva el momento angular: {momento_inicial} → {momento_final}")
        
        return conservado
    
    def inercia_varios_cuerpos(self, inercias: list) -> Q_:
        """
        Calcula el momento de inercia total para varios cuerpos.
        
        Args:
            inercias: Lista de momentos de inercia individuales
            
        Returns:
            Momento de inercia total
        """
        inercia_total = sum(inercias)
        logger.info(f"Momento de inercia total: {inercia_total}")
        return inercia_total
    
    def velocidad_angular_cambio_inercia(self, momento_angular: Q_, inercia_inicial: Q_, inercia_final: Q_) -> Q_:
        """
        Calcula la velocidad angular después de un cambio en el momento de inercia.
        
        Args:
            momento_angular: Momento angular conservado
            inercia_inicial: Momento de inercia inicial
            inercia_final: Momento de inercia final
            
        Returns:
            Nueva velocidad angular
            
        Example:
            Patinador que jala los brazos hacia adentro
        """
        if inercia_final.magnitude == 0:
            raise ValueError("El momento de inercia final no puede ser cero")
        
        velocidad_final = momento_angular / inercia_final
        logger.info(f"Cambio de velocidad angular: {self.velocidad_angular} → {velocidad_final}")
        
        self.velocidad_angular = velocidad_final
        self.inercia = inercia_final
        return velocidad_final