from .species import Species


class Inert(Species):
    CLASS = "inert"
    MOL_WEIGHT = None
    
    def __init__(self, T=None):
        pass
