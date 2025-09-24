from typing import Dict, List, Tuple
from .core import Field, AdaptiveFormula
from .policies import get_standard_policies

class PermissionManager:
    def __init__(self, tier='community', license_key=None):
        self.tier = tier
        self.license_key = license_key
        self.fields = get_standard_policies()
        self._setup_formula()
    
    def _setup_formula(self):
        config = {field.name: field.to_dict() for field in self.fields}
        self.formula = AdaptiveFormula(config, self.tier, self.license_key)
    
    def can_access(self, context: Dict) -> Tuple[bool, float, str]:
        score = self.formula.evaluate(context)
        threshold = self.formula.get_confidence_level()
        allowed = score > threshold
        
        if allowed:
            message = f"Access granted (score: {score:.3f})"
        else:
            message = f"Access denied (score: {score:.3f})"
        
        return allowed, score, message
    
    def check_role_permission(self, role: str, action: str, resource: str) -> bool:
        context = {
            'role_hierarchy_level': {'admin': 4, 'manager': 3, 'employee': 2, 'guest': 1}.get(role, 1),
            'action_severity': {'read': 1, 'write': 2, 'delete': 3}.get(action, 1),
            'resource_sensitivity_level': {'public': 1, 'internal': 2, 'confidential': 3}.get(resource, 1)
        }
        allowed, _, _ = self.can_access(context)
        return allowed