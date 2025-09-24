"""
Módulo para análisis de cuerpos rígidos y sus propiedades de rotación.
"""

import numpy as np
from typing import Union, Optional, Dict
from ...units import ureg, Q_
from ...logger import get_logger

logger = get_logger('cinetica.dinamica.rotacional.cuerpos_rigidos')


class CuerposRigidos:
    """
    Clase para análisis de cuerpos rígidos y sus propiedades rotacionales.
    
    Attributes:
        forma (str): Forma del cuerpo rígido
        dimensiones (dict): Dimensiones del cuerpo
        masa (Q_): Masa del cuerpo
        inercia (Q_): Momento de inercia
    """
    
    def __init__(self):
        """Inicializa la clase CuerposRigidos."""
        self.forma = ""
        self.dimensiones = {}
        self.masa = Q_(0, 'kg')
        self.inercia = Q_(0, 'kg * m**2')
    
    def inercia_cilindro_solido(self, masa: Q_, radio: Q_) -> Q_:
        """
        Calcula el momento de inercia de un cilindro sólido respecto a su eje.
        
        Args:
            masa: Masa del cilindro [kg]
            radio: Radio del cilindro [m]
            
        Returns:
            Momento de inercia [kg·m²]
            
        Formula:
            I = (1/2) * m * r²
        """
        # Validar unidades
        try:
            masa.to('kg')
        except Exception:
            raise Exception("Unidades incompatibles: la masa debe tener unidades de masa")
        
        try:
            radio.to('m')
        except Exception:
            raise Exception("Unidades incompatibles: el radio debe tener unidades de longitud")
        
        inercia = 0.5 * masa * radio**2
        self.forma = "cilindro_solido"
        self.dimensiones = {"radio": radio}
        self.masa = masa
        self.inercia = inercia
        
        logger.info(f"Momento de inercia cilindro sólido: {inercia}")
        return inercia
    
    def inercia_cilindro_vacio(self, masa: Q_, radio_interno: Q_, radio_externo: Q_) -> Q_:
        """
        Calcula el momento de inercia de un cilindro hueco.
        
        Args:
            masa: Masa del cilindro [kg]
            radio_interno: Radio interno [m]
            radio_externo: Radio externo [m]
            
        Returns:
            Momento de inercia [kg·m²]
        """
        # Para cilindro hueco: I = (1/2) * m * (r_ext² + r_int²)
        inercia = 0.5 * masa * (radio_externo**2 + radio_interno**2)
        self.forma = "cilindro_hueco"
        self.dimensiones = {"radio_interno": radio_interno, "radio_externo": radio_externo}
        self.masa = masa
        self.inercia = inercia
        
        logger.info(f"Momento de inercia cilindro hueco: {inercia}")
        return inercia
    
    def inercia_esfera_solido(self, masa: Q_, radio: Q_) -> Q_:
        """
        Calcula el momento de inercia de una esfera sólida.
        
        Args:
            masa: Masa de la esfera [kg]
            radio: Radio de la esfera [m]
            
        Returns:
            Momento de inercia [kg·m²]
            
        Formula:
            I = (2/5) * m * r²
        """
        inercia = (2/5) * masa * radio**2
        self.forma = "esfera_solida"
        self.dimensiones = {"radio": radio}
        self.masa = masa
        self.inercia = inercia
        
        logger.info(f"Momento de inercia esfera sólida: {inercia}")
        return inercia
    
    def inercia_varilla_centro(self, masa: Q_, longitud: Q_) -> Q_:
        """
        Calcula el momento de inercia de una varilla respecto a su centro.
        
        Args:
            masa: Masa de la varilla [kg]
            longitud: Longitud de la varilla [m]
            
        Returns:
            Momento de inercia [kg·m²]
            
        Formula:
            I = (1/12) * m * L²
        """
        inercia = (1/12) * masa * longitud**2
        self.forma = "varilla_centro"
        self.dimensiones = {"longitud": longitud}
        self.masa = masa
        self.inercia = inercia
        
        logger.info(f"Momento de inercia varilla (centro): {inercia}")
        return inercia
    
    def inercia_varilla_extremo(self, masa: Q_, longitud: Q_) -> Q_:
        """
        Calcula el momento de inercia de una varilla respecto a un extremo.
        
        Args:
            masa: Masa de la varilla [kg]
            longitud: Longitud de la varilla [m]
            
        Returns:
            Momento de inercia [kg·m²]
            
        Formula:
            I = (1/3) * m * L²
        """
        inercia = (1/3) * masa * longitud**2
        self.forma = "varilla_extremo"
        self.dimensiones = {"longitud": longitud}
        self.masa = masa
        self.inercia = inercia
        
        logger.info(f"Momento de inercia varilla (extremo): {inercia}")
        return inercia
    
    def inercia_placa_rectangular(self, masa: Q_, ancho: Q_, alto: Q_, eje: str = "centro") -> Q_:
        """
        Calcula el momento de inercia de una placa rectangular.
        
        Args:
            masa: Masa de la placa [kg]
            ancho: Ancho de la placa [m]
            alto: Alto de la placa [m]
            eje: Eje de rotación ("centro", "ancho", "alto")
            
        Returns:
            Momento de inercia [kg·m²]
        """
        if eje == "centro":
            # Respecto al centro, perpendicular al plano
            inercia = (1/12) * masa * (ancho**2 + alto**2)
        elif eje == "ancho":
            # Respecto al eje del ancho
            inercia = (1/12) * masa * alto**2
        elif eje == "alto":
            # Respecto al eje del alto
            inercia = (1/12) * masa * ancho**2
        else:
            raise ValueError("Eje debe ser 'centro', 'ancho' o 'alto'")
        
        self.forma = f"placa_rectangular_{eje}"
        self.dimensiones = {"ancho": ancho, "alto": alto}
        self.masa = masa
        self.inercia = inercia
        
        logger.info(f"Momento de inercia placa rectangular ({eje}): {inercia}")
        return inercia
    
    def radio_giro(self, inercia: Q_, masa: Q_) -> Q_:
        """
        Calcula el radio de giro de un cuerpo.
        
        Args:
            inercia: Momento de inercia [kg·m²]
            masa: Masa del cuerpo [kg]
            
        Returns:
            Radio de giro [m]
            
        Formula:
            k = √(I/m)
        """
        # Validar que la masa tenga unidades de masa
        try:
            masa.to('kg')
        except Exception:
            raise Exception("Unidades incompatibles: la masa debe tener unidades de masa")
        
        if masa.magnitude == 0:
            raise ZeroDivisionError("La masa no puede ser cero")
        
        radio = np.sqrt(inercia.magnitude / masa.magnitude) * ureg.meter
        
        logger.info(f"Radio de giro: {radio}")
        return radio
    
    def inercia_cilindro_hueco(self, masa: Q_, radio: Q_) -> Q_:
        """
        Calcula el momento de inercia de un cilindro hueco (tubo delgado).
        
        Args:
            masa: Masa del cilindro [kg]
            radio: Radio del cilindro [m]
            
        Returns:
            Momento de inercia [kg·m²]
            
        Formula:
            I = m * r²
        """
        inercia = masa * radio**2
        self.forma = "cilindro_hueco"
        self.dimensiones = {"radio": radio}
        self.masa = masa
        self.inercia = inercia
        
        logger.info(f"Momento de inercia cilindro hueco: {inercia}")
        return inercia
    
    def inercia_esfera_hueco(self, masa: Q_, radio: Q_) -> Q_:
        """
        Calcula el momento de inercia de una esfera hueca (cascarón esférico).
        
        Args:
            masa: Masa de la esfera [kg]
            radio: Radio de la esfera [m]
            
        Returns:
            Momento de inercia [kg·m²]
            
        Formula:
            I = (2/3) * m * r²
        """
        inercia = (2/3) * masa * radio**2
        self.forma = "esfera_hueco"
        self.dimensiones = {"radio": radio}
        self.masa = masa
        self.inercia = inercia
        
        logger.info(f"Momento de inercia esfera hueco: {inercia}")
        return inercia
    
    def inercia_placa_rectangular_centro(self, masa: Q_, ancho: Q_, largo: Q_) -> Q_:
        """
        Calcula el momento de inercia de una placa rectangular respecto al centro.
        
        Args:
            masa: Masa de la placa [kg]
            ancho: Ancho de la placa [m]
            largo: Largo de la placa [m]
            
        Returns:
            Momento de inercia [kg·m²]
            
        Formula:
            I = (1/12) * m * (w² + l²)
        """
        inercia = (1/12) * masa * (ancho**2 + largo**2)
        self.forma = "placa_rectangular_centro"
        self.dimensiones = {"ancho": ancho, "largo": largo}
        self.masa = masa
        self.inercia = inercia
        
        logger.info(f"Momento de inercia placa rectangular (centro): {inercia}")
        return inercia
    
    def inercia_placa_rectangular_eje_ancho(self, masa: Q_, ancho: Q_, largo: Q_) -> Q_:
        """
        Calcula el momento de inercia de una placa rectangular respecto al eje del ancho.
        
        Args:
            masa: Masa de la placa [kg]
            ancho: Ancho de la placa [m]
            largo: Largo de la placa [m]
            
        Returns:
            Momento de inercia [kg·m²]
            
        Formula:
            I = (1/12) * m * l²
        """
        inercia = (1/12) * masa * largo**2
        self.forma = "placa_rectangular_eje_ancho"
        self.dimensiones = {"ancho": ancho, "largo": largo}
        self.masa = masa
        self.inercia = inercia
        
        logger.info(f"Momento de inercia placa rectangular (eje ancho): {inercia}")
        return inercia
    
    def momento_inercia_combinado(self, momentos: list) -> Q_:
        """
        Calcula el momento de inercia combinado de varios cuerpos.
        
        Args:
            momentos: Lista de momentos de inercia [kg·m²]
            
        Returns:
            Momento de inercia total [kg·m²]
        """
        if not momentos:
            return Q_(0.0, 'kg * m**2')
        
        inercia_total = sum(momentos)
        
        self.forma = "sistema_combinado"
        self.dimensiones = {"n_componentes": len(momentos)}
        self.masa = Q_(0.0, 'kg')  # No se especifica masa total
        self.inercia = inercia_total
        
        logger.info(f"Momento de inercia combinado: {inercia_total}")
        return inercia_total
    
    def inercia_compuesta(self, masas: list, inercias: list, distancias: list = None) -> Q_:
        """
        Calcula el momento de inercia de un sistema compuesto.
        
        Args:
            masas: Lista de masas [kg]
            inercias: Lista de momentos de inercia individuales [kg·m²]
            distancias: Lista de distancias al eje de rotación [m]
            
        Returns:
            Momento de inercia total [kg·m²]
        """
        if len(masas) != len(inercias):
            raise ValueError("Las listas de masas e inercias deben tener igual longitud")
        
        inercia_total = sum(inercias)
        
        # Aplicar teorema de ejes paralelos si se proporcionan distancias
        if distancias is not None:
            if len(distancias) != len(masas):
                raise ValueError("Las listas de distancias y masas deben tener igual longitud")
            
            for i in range(len(masas)):
                inercia_total += masas[i] * distancias[i]**2
        
        self.forma = "sistema_compuesto"
        self.dimensiones = {"n_componentes": len(masas)}
        self.masa = sum(masas)
        self.inercia = inercia_total
        
        logger.info(f"Momento de inercia sistema compuesto: {inercia_total}")
        return inercia_total
    
    def informacion_cuerpo(self) -> Dict:
        """
        Retorna información del cuerpo rígido.
        
        Returns:
            Diccionario con información del cuerpo
        """
        info = {
            "forma": self.forma,
            "masa": self.masa,
            "inercia": self.inercia,
            "dimensiones": self.dimensiones,
            "radio_giro": self.radio_giro(self.inercia, self.masa) if self.masa.magnitude > 0 else None
        }
        
        return info