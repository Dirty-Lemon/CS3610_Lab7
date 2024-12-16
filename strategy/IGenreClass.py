
from abc import ABC, abstractmethod

class IGenre(ABC):
    '''
    Defining interface for entertainment genre
    '''
    @abstractmethod
    def genreType(self):
        pass