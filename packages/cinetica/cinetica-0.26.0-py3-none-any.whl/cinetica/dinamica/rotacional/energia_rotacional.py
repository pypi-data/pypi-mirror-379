"""
Módulo para cálculos de energía en sistemas rotacionales.
"""

import numpy as np
from typing import Union, Optional
from ...units import ureg, Q_
from ...logger import get_logger

logger = get_logger('cinetica.dinamica.rotacional.energia_rotacional')


class EnergiaRotacional:
    """
    Clase para cálculos de energía en sistemas rotacionales.
    
    Attributes:
        energia_cinetica (Q_): Energía cinética rotacional
        energia_potencial (Q_): Energía potencial gravitacional
        energia_total (Q_): Energía total del sistema
    """
    
    def __init__(self):
        """Inicializa la clase EnergiaRotacional."""
        self.energia_cinetica = Q_(0, 'J')
        self.energia_potencial = Q_(0, 'J')
        self.energia_total = Q_(0, 'J')
    
    def energia_cinetica_rotacional(self, inercia: Q_, velocidad_angular: Q_) -> Q_:
        """
        Calcula la energía cinética rotacional.
        
        Args:
            inercia: Momento de inercia [kg·m²]
            velocidad_angular: Velocidad angular [rad/s]
            
        Returns:
            Energía cinética rotacional [J]
            
        Formula:
            K_rot = (1/2) * I * ω²
        """
        # Validar unidades
        try:
            inercia.to('kg * m**2')
        except Exception:
            raise Exception("Unidades incompatibles: el momento de inercia debe tener unidades de kg·m²")
        
        try:
            velocidad_angular.to('rad/s')
        except Exception:
            raise Exception("Unidades incompatibles: la velocidad angular debe tener unidades de rad/s")
        
        energia = 0.5 * inercia * velocidad_angular**2
        self.energia_cinetica = energia
        
        logger.info(f"Energía cinética rotacional: {energia}")
        return energia
    
    def energia_cinetica_total(self, masa: Q_, velocidad_lineal: Q_, inercia: Q_, velocidad_angular: Q_) -> Q_:
        """
        Calcula la energía cinética total (traslación + rotación).
        
        Args:
            masa: Masa del objeto [kg]
            velocidad_lineal: Velocidad del centro de masa [m/s]
            inercia: Momento de inercia [kg·m²]
            velocidad_angular: Velocidad angular [rad/s]
            
        Returns:
            Energía cinética total [J]
            
        Formula:
            K_total = (1/2) * m * v² + (1/2) * I * ω²
        """
        energia_traslacional = 0.5 * masa * velocidad_lineal**2
        energia_rotacional = 0.5 * inercia * velocidad_angular**2
        energia_total = energia_traslacional + energia_rotacional
        
        self.energia_cinetica = energia_total
        
        logger.info(f"Energía cinética total: {energia_total}")
        logger.info(f"  Traslacional: {energia_traslacional}")
        logger.info(f"  Rotacional: {energia_rotacional}")
        
        return energia_total
    
    def energia_potencial_gravitacional(self, masa: Q_, altura: Q_, gravedad: Q_ = None) -> Q_:
        """
        Calcula la energía potencial gravitacional.
        
        Args:
            masa: Masa del objeto [kg]
            altura: Altura respecto al nivel de referencia [m]
            gravedad: Aceleración gravitacional (por defecto 9.81 m/s²)
            
        Returns:
            Energía potencial gravitacional [J]
        """
        if gravedad is None:
            gravedad = Q_(9.81, 'm/s**2')
        
        energia = masa * gravedad * altura
        self.energia_potencial = energia
        
        logger.info(f"Energía potencial gravitacional: {energia}")
        return energia
    
    def conservacion_energia_mecanica(self, energia_inicial: Q_, energia_final: Q_) -> bool:
        """
        Verifica la conservación de la energía mecánica.
        
        Args:
            energia_inicial: Energía mecánica inicial [J]
            energia_final: Energía mecánica final [J]
            
        Returns:
            True si se conserva la energía mecánica
        """
        tolerancia = 1e-10
        conservada = abs(energia_final.magnitude - energia_inicial.magnitude) < tolerancia
        
        if conservada:
            logger.info("Se conserva la energía mecánica")
        else:
            perdida = energia_inicial - energia_final
            logger.warning(f"No se conserva la energía mecánica. Pérdida: {perdida}")
        
        return conservada
    
    def trabajo_torque(self, torque: Q_, angulo: Q_) -> Q_:
        """
        Calcula el trabajo realizado por un torque.
        
        Args:
            torque: Torque aplicado [N·m]
            angulo: Ángulo de rotación [rad]
            
        Returns:
            Trabajo realizado [J]
            
        Formula:
            W = τ * θ
        """
        trabajo = torque * angulo
        
        logger.info(f"Trabajo por torque: {trabajo}")
        return trabajo
    
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
    
    def energia_cinetica_cilindro_rodando(self, masa: Q_, radio: Q_, velocidad_cm: Q_) -> Q_:
        """
        Calcula la energía cinética de un cilindro rodando sin deslizar.
        
        Args:
            masa: Masa del cilindro [kg]
            radio: Radio del cilindro [m]
            velocidad_cm: Velocidad del centro de masa [m/s]
            
        Returns:
            Energía cinética total [J]
            
        Note:
            Para cilindro: I = (1/2) * m * r²
            ω = v_cm / r
        """
        # Momento de inercia del cilindro
        inercia = 0.5 * masa * radio**2
        
        # Velocidad angular
        velocidad_angular = velocidad_cm / radio
        
        # Energía cinética total
        energia = self.energia_cinetica_total(masa, velocidad_cm, inercia, velocidad_angular)
        
        return energia
    
    def energia_cilindro_rodando(self, masa: Q_, velocidad: Q_, radio: Q_) -> Q_:
        """
        Calcula la energía cinética de un cilindro rodando sin deslizar.
        
        Args:
            masa: Masa del cilindro [kg]
            velocidad: Velocidad del centro de masa [m/s]
            radio: Radio del cilindro [m]
            
        Returns:
            Energía cinética total [J]
        """
        return self.energia_cinetica_cilindro_rodando(masa, radio, velocidad)
    
    def teorema_ejes_paralelos(self, inercia_cm: Q_, masa: Q_, distancia: Q_) -> Q_:
        """
        Aplica el teorema de ejes paralelos para calcular el momento de inercia.
        
        Args:
            inercia_cm: Momento de inercia respecto al CM [kg·m²]
            masa: Masa del objeto [kg]
            distancia: Distancia al nuevo eje [m]
            
        Returns:
            Momento de inercia respecto al nuevo eje [kg·m²]
            
        Formula:
            I = I_cm + m * d²
        """
        inercia_nuevo = inercia_cm + masa * distancia**2
        
        logger.info(f"Momento de inercia (ejes paralelos): {inercia_nuevo}")
        return inercia_nuevo