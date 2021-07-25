def perfromer():
    return "Paramore"

def durationInMinutes():
    return 190 / 60

def song():
    return "Hard Times"


print(perfromer())
print(durationInMinutes())
print(song())

Year_of_release = 2017
def isSongFrom2010s(Year_of_release):
    if Year_of_release > 2010:
        return True
    else:
        return False

print(isSongFrom2010s(Year_of_release))
print(isSongFrom2010s(2005))
