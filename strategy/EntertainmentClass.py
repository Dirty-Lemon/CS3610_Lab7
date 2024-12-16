
class Entertainment:
    '''
    Base class: Entertainment types
    '''
    
    def __init__(self) -> None:
        self._buying = None
        self._genre = None
        self._interacting = None
        
    @property
    def buying(self):
        return self._buying

    @buying.setter
    def buying(self, buying):
        self._buying = buying

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, genre):
        self._genre = genre

    @property
    def interacting(self):
        return self._interacting

    @interacting.setter
    def interacting(self, interacting):
        self._interacting = interacting
        
        
    def Service(self, buying,genre,interacting=None):
        self._buying = buying
        self._genre = genre
        self._interacting = interacting
        print("Entertainment is ready now")
        
    def GenreType(self):
        self._genre.genreType()
        
    def CopyType(self):
        self._buying.buy()
        
    def Int_Type(self):
        self._interacting.interact()


