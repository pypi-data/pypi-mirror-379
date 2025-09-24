from .core import Field

def get_standard_policies():
    return [
        Field('role_hierarchy_level', 2, 4.0, 3.0),
        Field('action_severity', 1, 4.5, 3.5),
        Field('resource_sensitivity_level', 2, 4.0, 4.0),
        Field('user_seniority_years', 2.0, 3.5, 2.5),
        Field('department_match', True, 3.0, 2.0),
        Field('time_restriction_compliance', True, 3.0, 4.0),
        Field('compliance_training', True, 2.5, 3.0)
    ]

class PolicyPresets:
    @staticmethod
    def strict_security():
        return [Field(f.name, f.reference, f.importance*1.5, f.sensitivity*1.5) 
                for f in get_standard_policies()]
    
    @staticmethod
    def relaxed():
        return [Field(f.name, f.reference, f.importance*0.7, f.sensitivity*0.7) 
                for f in get_standard_policies()]