"""
Data models for the Authorization Control SDK.
"""

from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Any
from datetime import datetime

# --- MODELO DE RESULTADO ---
# Reemplaza a ValidationResult

@dataclass
class AuthorizationResult:
    """
    Represents the result of a permission check.
    """
    is_allowed: bool
    score: float
    threshold: float
    message: str
    details: Dict[str, Any]
    timestamp: datetime = None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()

    def to_dict(self) -> Dict:
        """Converts the result to a dictionary for logging or inspection."""
        return {
            'allowed': self.is_allowed,
            'score': round(self.score, 3),
            'threshold': round(self.threshold, 3),
            'message': self.message,
            'details': self.details,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None
        }

# --- MODELO DE MÉTRICAS (REUTILIZABLE) ---
# Se renombra de RequestMetrics a PerformanceMetrics para ser más genérico

@dataclass
class PerformanceMetrics:
    """
    Represents performance and usage metrics for the SDK.
    """
    total_evaluations: int
    avg_score: float
    current_threshold: float
    min_score: float
    max_score: float
    tier: str = 'community'
    license_valid: bool = False
    adaptive_weights: bool = False
    weight_changes: Optional[Dict[str, float]] = None

    def __post_init__(self):
        if self.weight_changes is None:
            self.weight_changes = {}

    def to_dict(self) -> Dict:
        """Converts the metrics to a dictionary."""
        # Esta lógica es reutilizable y no necesita cambios
        result = {
            'total_evaluations': self.total_evaluations,
            'average_score': round(self.avg_score, 3),
            'threshold': round(self.current_threshold, 3),
            'score_range': {
                'min': round(self.min_score, 3),
                'max': round(self.max_score, 3)
            },
            'tier': self.tier,
            'license_valid': self.license_valid
        }
        if self.tier == 'enterprise' and self.adaptive_weights:
            result['adaptive_weights'] = True
            if self.weight_changes:
                result['weight_optimization'] = {
                    'fields_optimized': len(self.weight_changes),
                    'avg_weight_change': round(sum(self.weight_changes.values()) / len(self.weight_changes), 3) if self.weight_changes else 0
                }
        return result

# --- MODELO DE CONTEXTO DE ENTRADA ---
# Reemplaza a APIRequest con un modelo más adecuado para permisos

@dataclass
class PermissionContext:
    """
    Represents the structured context for an authorization request.
    """
    # User attributes
    user_id: str
    user_role: str
    user_seniority_years: float = 0.0
    department: Optional[str] = None
    compliance_training_completed: bool = False

    # Action attributes
    action: str

    # Resource attributes
    resource_id: str
    resource_type: str
    resource_owner_id: Optional[str] = None
    resource_sensitivity: str = 'internal'

    # Environmental attributes
    time_of_day_24h: int = 12
    is_weekend: bool = False

    def to_dict(self) -> Dict:
        """
        Converts the context object to a flat dictionary that the
        core formula can evaluate. This is where you can add
        calculated/engineered features.
        """
        # Usamos asdict para convertir el dataclass a un diccionario
        data = asdict(self)

        # Añadimos campos calculados que el motor usará
        data['resource_ownership_match'] = (self.user_id == self.resource_owner_id)

        role_map = {'guest': 1, 'employee': 2, 'manager': 3, 'admin': 4}
        data['role_hierarchy_level'] = role_map.get(self.user_role, 1)

        action_map = {'read': 1, 'write': 2, 'share': 2, 'approve': 3, 'delete': 4}
        data['action_severity'] = action_map.get(self.action, 1)

        sensitivity_map = {'public': 1, 'internal': 2, 'confidential': 3, 'critical': 4}
        data['resource_sensitivity_level'] = sensitivity_map.get(self.resource_sensitivity, 2)

        return data