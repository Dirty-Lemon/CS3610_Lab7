
from abc import ABC, abstractmethod

class I_Interact(ABC):
    '''
    Defining interface for interaction to entertainment
    '''
    @abstractmethod
    def interact(self):
        pass