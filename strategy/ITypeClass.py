
from abc import ABC, abstractmethod

class I_Type(ABC):
    '''
    Defining interface for entertainment type
    '''
    @abstractmethod
    def buy(self):
        pass
