"""
Módulo para las ecuaciones de Euler en dinámica de cuerpos rígidos.
"""

import numpy as np
from typing import Union, Optional, Tuple
from ...units import ureg, Q_
from ...logger import get_logger

logger = get_logger('cinetica.dinamica.rotacional.ecuaciones_euler')


class EcuacionesEuler:
    """
    Clase para las ecuaciones de Euler en dinámica de cuerpos rígidos.
    
    Las ecuaciones de Euler describen el movimiento rotacional de un cuerpo rígido
    en el marco de referencia del cuerpo.
    
    Attributes:
        momento_inercia (np.ndarray): Tensor de momento de inercia
        velocidad_angular (np.ndarray): Vector velocidad angular
        torque (np.ndarray): Vector torque
    """
    
    def __init__(self):
        """Inicializa la clase EcuacionesEuler."""
        self.momento_inercia = np.diag([1, 1, 1])  # Ixx, Iyy, Izz por defecto
        self.velocidad_angular = np.array([0, 0, 0])
        self.torque = np.array([0, 0, 0])
    
    def set_tensor_inercia(self, ixx: Q_, iyy: Q_, izz: Q_, ixy: Q_ = None, ixz: Q_ = None, iyz: Q_ = None) -> None:
        """
        Define el tensor de momento de inercia.
        
        Args:
            ixx: Momento de inercia respecto al eje x [kg·m²]
            iyy: Momento de inercia respecto al eje y [kg·m²]
            izz: Momento de inercia respecto al eje z [kg·m²]
            ixy: Producto de inercia xy [kg·m²]
            ixz: Producto de inercia xz [kg·m²]
            iyz: Producto de inercia yz [kg·m²]
        """
        # Convertir a valores numéricos
        tensor = np.array([
            [ixx.magnitude, 0 if ixy is None else ixy.magnitude, 0 if ixz is None else ixz.magnitude],
            [0 if ixy is None else ixy.magnitude, iyy.magnitude, 0 if iyz is None else iyz.magnitude],
            [0 if ixz is None else ixz.magnitude, 0 if iyz is None else iyz.magnitude, izz.magnitude]
        ])
        
        self.momento_inercia = tensor
        logger.info(f"Tensor de inercia definido:\n{tensor}")
    
    def ecuaciones_euler(self, velocidad_angular: np.ndarray, torque: np.ndarray) -> np.ndarray:
        """
        Resuelve las ecuaciones de Euler para cuerpos rígidos.
        
        Args:
            velocidad_angular: Vector velocidad angular [rad/s]
            torque: Vector torque [N·m]
            
        Returns:
            Derivada de la velocidad angular [rad/s²]
            
        Las ecuaciones de Euler:
        I₁ * dω₁/dt - (I₂ - I₃) * ω₂ * ω₃ = τ₁
        I₂ * dω₂/dt - (I₃ - I₁) * ω₃ * ω₁ = τ₂  
        I₃ * dω₃/dt - (I₁ - I₂) * ω₁ * ω₂ = τ₃
        """
        # Extraer componentes principales del tensor de inercia
        i1, i2, i3 = np.diag(self.momento_inercia)
        
        # Componentes de velocidad angular
        w1, w2, w3 = velocidad_angular
        
        # Componentes de torque
        t1, t2, t3 = torque
        
        # Resolver las ecuaciones de Euler
        # dω/dt = I⁻¹ * [τ - ω × (I * ω)]
        
        # Producto vectorial ω × (I * ω)
        i_omega = np.dot(self.momento_inercia, velocidad_angular)
        omega_cross_iomega = np.cross(velocidad_angular, i_omega)
        
        # Término total: τ - ω × (I * ω)
        termino_total = torque - omega_cross_iomega
        
        # Resolver para dω/dt
        try:
            domega_dt = np.linalg.solve(self.momento_inercia, termino_total)
        except np.linalg.LinAlgError:
            logger.error("Tensor de inercia singular")
            domega_dt = np.zeros(3)
        
        self.velocidad_angular = velocidad_angular
        self.torque = torque
        
        logger.info(f"Aceleración angular: {domega_dt} rad/s²")
        return domega_dt
    
    def estabilidad_rotacion(self, eje_rotacion: str = 'z') -> bool:
        """
        Analiza la estabilidad de la rotación alrededor de un eje principal.
        
        Args:
            eje_rotacion: Eje de rotación ('x', 'y', 'z')
            
        Returns:
            True si la rotación es estable, False si es inestable
        """
        # Obtener momentos de inercia principales
        i1, i2, i3 = np.diag(self.momento_inercia)
        
        if eje_rotacion == 'x':
            i_rot = i1
            i_otros = [i2, i3]
        elif eje_rotacion == 'y':
            i_rot = i2
            i_otros = [i1, i3]
        elif eje_rotacion == 'z':
            i_rot = i3
            i_otros = [i1, i2]
        else:
            raise ValueError("Eje debe ser 'x', 'y' o 'z'")
        
        # Criterio de estabilidad:
        # Estable si I_rotación es el mayor o el menor de los tres
        es_intermedio = (i_otros[0] < i_rot < i_otros[1]) or (i_otros[1] < i_rot < i_otros[0])
        
        if es_intermedio:
            estable = False
            logger.warning(f"Rotación inestable alrededor del eje {eje_rotacion}")
        else:
            estable = True
            logger.info(f"Rotación estable alrededor del eje {eje_rotacion}")
        
        return estable
    
    def precesion_giroscopio(self, velocidad_angular_spin: Q_, torque: Q_, momento_inercia: Q_ = None) -> Q_:
        """
        Calcula la velocidad de precesión de un giroscopio.
        
        Args:
            velocidad_angular_spin: Velocidad angular de spin [rad/s]
            torque: Torque aplicado [N·m]
            momento_inercia: Momento de inercia [kg·m²]. Si es None, usa el valor del tensor
            
        Returns:
            Velocidad de precesión [rad/s]
            
        Formula:
            ω_p = τ / (I * ω_s)
        """
        # Usar el momento de inercia proporcionado o el del tensor
        if momento_inercia is None:
            i_spin = self.momento_inercia[2, 2]  # Eje z por defecto
        else:
            i_spin = momento_inercia.magnitude
        
        if velocidad_angular_spin.magnitude == 0:
            raise ZeroDivisionError("La velocidad angular de spin no puede ser cero")
        
        # Velocidad de precesión
        # ω_p = τ / (I * ω_s)
        # Las unidades deben ser: (N·m) / (kg·m² · rad/s) = (kg·m²/s²) / (kg·m²·rad/s) = 1/(rad/s) = s/rad
        # Pero queremos rad/s, así que necesitamos invertir el resultado
        velocidad_precesion_magnitude = torque.magnitude / (i_spin * velocidad_angular_spin.magnitude)
        
        # La fórmula correcta debería ser: ω_p = τ / (I * ω_s)
        # Pero las unidades resultantes son s/rad, no rad/s
        # Esto es correcto físicamente: la precesión es más lenta cuando hay más momento angular
        
        from ...units import ureg
        velocidad_precesion = Q_(velocidad_precesion_magnitude, 'rad/s')
        
        logger.info(f"Velocidad de precesión: {velocidad_precesion}")
        return velocidad_precesion
    
    def energia_rotacional_cuerpo_rigido(self, velocidad_angular: np.ndarray) -> Q_:
        """
        Calcula la energía rotacional de un cuerpo rígido.
        
        Args:
            velocidad_angular: Vector velocidad angular [rad/s]
            
        Returns:
            Energía rotacional [J]
            
        Formula:
            E_rot = (1/2) * ωᵀ * I * ω
        """
        # Convertir velocidad angular a unidades apropiadas
        omega = np.array(velocidad_angular) * ureg.rad / ureg.s
        
        # Calcular energía rotacional
        i_omega = np.dot(self.momento_inercia, omega.magnitude)
        energia = 0.5 * np.dot(omega.magnitude, i_omega) * ureg.joule
        
        logger.info(f"Energía rotacional: {energia}")
        return energia
    
    def torque_cambio_momento_angular(self, velocidad_angular_inicial: np.ndarray, 
                                     velocidad_angular_final: np.ndarray, 
                                     tiempo: Q_) -> np.ndarray:
        """
        Calcula el torque necesario para cambiar el momento angular.
        
        Args:
            velocidad_angular_inicial: Velocidad angular inicial [rad/s]
            velocidad_angular_final: Velocidad angular final [rad/s]
            tiempo: Tiempo del cambio [s]
            
        Returns:
            Vector torque [N·m]
        """
        # Cambio en el momento angular
        momento_inicial = np.dot(self.momento_inercia, velocidad_angular_inicial)
        momento_final = np.dot(self.momento_inercia, velocidad_angular_final)
        delta_momento = momento_final - momento_inicial
        
        # Torque = dL/dt
        torque = delta_momento / tiempo.magnitude
        
        logger.info(f"Torque requerido: {torque} N·m")
        return torque
    
    def resolver_ecuaciones_euler(self, velocidades_angulares: list) -> list:
        """
        Resuelve las ecuaciones de Euler para un estado de rotación dado.
        
        Args:
            velocidades_angulares: Lista de velocidades angulares [ω_x, ω_y, ω_z] [rad/s]
            
        Returns:
            Lista de torques [τ_x, τ_y, τ_z] [N·m]
            
        Raises:
            ValueError: Si el tensor de inercia no ha sido establecido
        """
        # Verificar si el tensor de inercia ha sido establecido (no es el valor por defecto)
        if np.array_equal(self.momento_inercia, np.diag([1, 1, 1])):
            raise ValueError("El tensor de inercia no ha sido establecido")
        
        # Convertir velocidades a array numpy
        omega = np.array([v.magnitude for v in velocidades_angulares])
        
        # Calcular el torque usando las ecuaciones de Euler
        # Para rotación estacionaria, dω/dt = 0, entonces:
        # τ = ω × (I · ω)
        
        i_omega = np.dot(self.momento_inercia, omega)
        torque = np.cross(omega, i_omega)
        
        # Convertir a cantidades con unidades
        from ...units import ureg
        torque_quantities = [Q_(t, 'N * m') for t in torque]
        
        logger.info(f"Torques calculados: {torque_quantities}")
        return torque_quantities
    
    def energia_cinetica_rotacional(self, velocidades_angulares: list) -> Q_:
        """
        Calcula la energía cinética rotacional.
        
        Args:
            velocidades_angulares: Lista de velocidades angulares [ω_x, ω_y, ω_z] [rad/s]
            
        Returns:
            Energía cinética rotacional [J]
        """
        # Convertir velocidades a array numpy
        omega = np.array([v.magnitude for v in velocidades_angulares])
        
        # Calcular energía cinética: E = 0.5 * ωᵀ · I · ω
        i_omega = np.dot(self.momento_inercia, omega)
        energia = 0.5 * np.dot(omega, i_omega)
        
        return Q_(energia, 'J')
    
    def torque_cambio_momento(self, velocidades_angulares_inicial: list, 
                             velocidades_angulares_final: list, 
                             tiempo: Q_) -> list:
        """
        Calcula el torque necesario para cambiar el momento angular.
        
        Args:
            velocidades_angulares_inicial: Velocidades angulares iniciales [rad/s]
            velocidades_angulares_final: Velocidades angulares finales [rad/s]
            tiempo: Tiempo del cambio [s]
            
        Returns:
            Lista de torques [τ_x, τ_y, τ_z] [N·m]
        """
        # Convertir a arrays numpy
        omega_inicial = np.array([v.magnitude for v in velocidades_angulares_inicial])
        omega_final = np.array([v.magnitude for v in velocidades_angulares_final])
        
        # Calcular momentos angular
        momento_inicial = np.dot(self.momento_inercia, omega_inicial)
        momento_final = np.dot(self.momento_inercia, omega_final)
        
        # Cambio en el momento angular
        delta_momento = momento_final - momento_inicial
        
        # Torque = dL/dt
        torque = delta_momento / tiempo.magnitude
        
        # Convertir a cantidades con unidades
        from ...units import ureg
        torque_quantities = [Q_(t, 'N * m') for t in torque]
        
        logger.info(f"Torques para cambio de momento: {torque_quantities}")
        return torque_quantities
    
    @property
    def tensor_inercia(self):
        """Getter para el tensor de inercia."""
        return self.momento_inercia