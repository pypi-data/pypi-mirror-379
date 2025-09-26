
from abc import ABC, abstractmethod

class StreetProcessor(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def predict(self, images_street, images_arial):
        pass
