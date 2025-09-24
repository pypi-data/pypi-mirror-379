"""
Módulo para cálculos de torque y su relación con el momento angular.
"""

import numpy as np
from typing import Union, Optional
from ...units import ureg, Q_
from ...logger import get_logger

logger = get_logger('cinetica.dinamica.rotacional.torque')


class Torque:
    """
    Clase para cálculos de torque y su relación con el momento angular.
    
    Attributes:
        torque (pint.Quantity): Vector torque
        momento_angular (pint.Quantity): Momento angular
        tiempo (pint.Quantity): Tiempo de aplicación
    """
    
    def __init__(self):
        """Inicializa la clase Torque."""
        self.torque = Q_(0, 'N * m')
        self.momento_angular = Q_(0, 'kg * m**2 / s')
        self.tiempo = Q_(0, 's')
    
    def calcular_torque(self, fuerza: Q_, posicion: np.ndarray, origen: np.ndarray = None) -> Q_:
        """
        Calcula el torque τ = r × F.
        
        Args:
            fuerza: Vector fuerza [N]
            posicion: Vector de posición desde el origen [m]
            origen: Origen del sistema (por defecto [0, 0, 0])
            
        Returns:
            Vector torque [N·m]
            
        Example:
            >>> from cinetica.dinamica.rotacional.torque import Torque
            >>> from cinetica.units import Q_
            >>> import numpy as np
            >>> torque = Torque()
            >>> fuerza = Q_([0.0, 10.0, 0.0], 'N')
            >>> posicion = np.array([2.0, 0.0, 0.0])
            >>> resultado = torque.calcular_torque(fuerza, posicion)
            >>> print(resultado)
            [0. 0. 20.] newton * meter
        """
        if origen is None:
            origen = np.array([0, 0, 0])
        
        # Asegurar que los arrays tengan al menos 1 dimensión
        posicion = np.atleast_1d(posicion)
        if origen is not None:
            origen = np.atleast_1d(origen)
        
        # Vector posición relativo al origen
        r_vec = (posicion - origen) * ureg.meter
        
        # Asegurar que la fuerza sea un vector
        if not hasattr(fuerza, 'magnitude') or np.isscalar(fuerza.magnitude):
            raise ValueError("La fuerza debe ser un vector con unidades.")

        F_vec = fuerza
        
        # Torque τ = r × F
        torque_vec = np.cross(r_vec.magnitude, F_vec.magnitude) * ureg.newton * ureg.meter
        
        self.torque = torque_vec
        logger.info(f"Torque calculado: {torque_vec}")
        return torque_vec
    
    def torque_magnitud(self, fuerza: Q_, brazo_perpendicular: Q_) -> Q_:
        """
        Calcula el torque usando la magnitud y el brazo de palanca.
        
        Args:
            fuerza: Magnitud de la fuerza [N]
            brazo_perpendicular: Distancia perpendicular [m]
            
        Returns:
            Magnitud del torque [N·m]

        Example:
            >>> from cinetica.dinamica.rotacional.torque import Torque
            >>> from cinetica.units import Q_
            >>> torque = Torque()
            >>> fuerza = Q_(10.0, 'N')
            >>> brazo = Q_(2.0, 'm')
            >>> resultado = torque.torque_magnitud(fuerza, brazo)
            >>> print(resultado)
            20.0 newton * meter
        """
        # Validar unidades
        try:
            fuerza.to('N')
        except:
            raise ValueError("La fuerza debe estar en Newtons (N)")
            
        try:
            brazo_perpendicular.to('m')
        except:
            raise ValueError("El brazo de palanca debe estar en metros (m)")
            
        torque_mag = fuerza * brazo_perpendicular
        self.torque = torque_mag
        
        logger.info(f"Torque (magnitud): {torque_mag}")
        return torque_mag
    
    def calcular_torque_vectorial(self, fuerza: np.ndarray, posicion: np.ndarray) -> np.ndarray:
        """
        Calcula el torque vectorial τ = r × F.
        
        Args:
            fuerza: Vector fuerza [N]
            posicion: Vector de posición [m]
            
        Returns:
            Vector torque [N·m]
            
        Example:
            Torque vectorial en 3D
        """
        # Asegurar que los arrays tengan al menos 1 dimensión
        fuerza = np.atleast_1d(fuerza)
        posicion = np.atleast_1d(posicion)
        
        # Validar que los arrays tengan la dimensión correcta
        if len(fuerza) != 3 or len(posicion) != 3:
            raise ValueError("Los vectores deben tener dimensión 3")
            
        # Calcular el producto cruz r × F
        torque_vec = np.cross(posicion, fuerza)
        
        logger.info(f"Torque vectorial calculado: {torque_vec}")
        return torque_vec
    
    def segunda_ley_newton_rotacional(self, inercia: Q_, aceleracion_angular: Q_) -> Q_:
        """
        Calcula el torque usando la segunda ley de Newton para rotación.
        
        Args:
            inercia: Momento de inercia [kg·m²]
            aceleracion_angular: Aceleración angular [rad/s²]
            
        Returns:
            Torque [N·m]
            
        Formula:
            τ = I * α

        Example:
            >>> from cinetica.dinamica.rotacional.torque import Torque
            >>> from cinetica.units import Q_
            >>> torque = Torque()
            >>> momento_inercia = Q_(3.0, 'kg * m**2')
            >>> aceleracion_angular = Q_(4.0, 'rad/s**2')
            >>> resultado = torque.segunda_ley_newton_rotacional(momento_inercia, aceleracion_angular)
            >>> print(resultado)
            12.0 kilogram * meter ** 2 * radian / second ** 2
        """
        torque = inercia * aceleracion_angular
        self.torque = torque
        
        logger.info(f"Torque (2ª ley rotacional): {torque}")
        return torque
    
    def cambio_momento_angular(self, momento_inicial: Q_, momento_final: Q_, tiempo: Q_) -> Q_:
        """
        Calcula el cambio en el momento angular debido a un torque.
        
        Args:
            momento_inicial: Momento angular inicial [kg·m²/s]
            momento_final: Momento angular final [kg·m²/s]
            tiempo: Tiempo de aplicación [s]
            
        Returns:
            Torque calculado [N·m]
            
        Formula:
            τ = (L_final - L_inicial) / Δt
        """
        if tiempo.magnitude == 0:
            raise ZeroDivisionError("El tiempo no puede ser cero")
            
        delta_L = momento_final - momento_inicial
        torque = delta_L / tiempo
        
        self.momento_angular = momento_final
        self.tiempo = tiempo
        self.torque = torque
        
        logger.info(f"Cambio en momento angular: {delta_L}")
        return torque
    
    def torque_equilibrio(self, torques: list) -> Q_:
        """
        Calcula el torque neto para verificar equilibrio rotacional.
        
        Args:
            torques: Lista de torques [N·m]
            
        Returns:
            Torque neto [N·m]
            
        Note:
            Equilibrio cuando τ_net = 0
        """
        torque_net = sum(torques)
        
        if abs(torque_net.magnitude) < 1e-10:
            logger.info("Sistema en equilibrio rotacional")
        else:
            logger.info(f"Torque neto: {torque_net}")
        
        return torque_net
    
    def potencia_rotacional(self, torque: Q_, velocidad_angular: Q_) -> Q_:
        """
        Calcula la potencia en sistemas rotacionales.
        
        Args:
            torque: Torque aplicado [N·m]
            velocidad_angular: Velocidad angular [rad/s]
            
        Returns:
            Potencia [W]
            
        Formula:
            P = τ * ω
        """
        potencia = torque * velocidad_angular
        
        logger.info(f"Potencia rotacional: {potencia}")
        return potencia
    
    def torque_centro_masa(self, fuerza: Q_, posicion_cm: np.ndarray, posicion_fuerza: np.ndarray) -> Q_:
        """
        Calcula el torque respecto al centro de masa.
        
        Args:
            fuerza: Vector fuerza [N]
            posicion_cm: Posición del centro de masa [m]
            posicion_fuerza: Posición donde se aplica la fuerza [m]
            
        Returns:
            Torque respecto al CM [N·m]
        """
        # Vector desde CM al punto de aplicación de la fuerza
        r_cm = (posicion_fuerza - posicion_cm) * ureg.meter
        F_vec = fuerza
        
        # Torque = r × F
        torque_cm = np.cross(r_cm.magnitude, F_vec.magnitude) * ureg.newton * ureg.meter
        
        logger.info(f"Torque respecto a CM: {torque_cm}")
        return torque_cm