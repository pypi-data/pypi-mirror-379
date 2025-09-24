"""
Cinetica - Una librería para cálculos de cinemática

Esta biblioteca proporciona herramientas para cálculos de física, incluyendo:
- Cinemática (movimiento rectilíneo, parabólico, circular, etc.)
- Dinámica (leyes de Newton, fuerzas, trabajo y energía)
- Herramientas de visualización gráfica

La configuración se puede personalizar a través de variables de entorno o un archivo .env.
"""

__version__ = "0.26.0"

# Importaciones principales
from . import cinematica
from . import dinamica
from . import graficos
from .config import settings as config
from .logger import get_logger, setup_logger
from .units import Q_, ureg

# Configurar logger raíz por defecto
logger = get_logger("cinetica")

__all__ = [
    "cinematica",
    "dinamica",
    "graficos",
    "setup_logger",
    "get_logger",
    "config",
    "logger",
    "ureg",
    "Q_",
    "__version__",
]
