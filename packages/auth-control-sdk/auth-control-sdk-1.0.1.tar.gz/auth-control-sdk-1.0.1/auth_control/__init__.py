"""
Authorization Control SDK - Granular and flexible access control
Version 1.0.0
"""

# --- ESTA PARTE ES 100% REUTILIZABLE ---
# Try imports: Cython -> Python fallback
try:
    from .core import Field, AdaptiveFormula
    _BACKEND = "Cython (Optimized)"
except ImportError:
    from .core_py import Field, AdaptiveFormula
    _BACKEND = "Pure Python"

# --- ESTA PARTE DEBE SER ADAPTADA PARA CADA PROYECTO ---
# Importar las clases y funciones específicas del nuevo SDK
from .permission import PermissionManager
from .policies import (
    get_standard_policies,
    PolicyPresets
)
from .models import (
    AuthorizationResult,
    PermissionContext
)

__version__ = "1.0.1"

# Actualizar __all__ con la nueva API pública
__all__ = [
    'PermissionManager',
    'Field',
    'AuthorizationResult',
    'PermissionContext',
    'get_standard_policies',
    'PolicyPresets'
]

# --- ESTA PARTE ES 100% REUTILIZABLE ---
def get_backend():
    """Returns which backend is being used"""
    return _BACKEND