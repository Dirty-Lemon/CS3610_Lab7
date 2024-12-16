from HardCopyClass import HardCopy
from DigitalClass import Digital 
from Non_FictionClass import Non_Fiction
from FictionClass import Fiction
from WatchClass import Watch
from ReadClass import Read
from ListenClass import Listen
from EntertainmentClass import Entertainment

Hobby=Entertainment() 

#enter the type, genre, interact for the service
Hobby.Service(HardCopy(),Fiction(),Read())

#displays the genre type
Hobby.GenreType()
#displays the Interaction type
Hobby.Int_Type()
#displays the entertainment type your buying
Hobby.CopyType()

print("\n Changing genre using setter:")
#changing the genre type
Hobby.genre= Non_Fiction()
#displays the genre type
Hobby.GenreType()
