import random

class Vehicle:
    def __init__(self, Make, Model, Year, Weight, NeedsMaintenance = False, TripsSinceMaintenance = 0):
        self.Make = Make
        self.Model = Model
        self.Year = Year
        self.Weight = Weight
        self.NeedsMaintenance = NeedsMaintenance
        self.TripsSinceMaintenance = TripsSinceMaintenance

    def Repair(self):
        self.TripsSinceMaintenance = 0
        self.NeedsMaintenance = False

class Cars(Vehicle):
    def __init__(self, Make, Model, Year, Weight, isDriving = False):
        Vehicle.__init__(self,Make,Model,Year,Weight)
        self.isDriving = isDriving
    
    def Drive(self):
        self.isDriving = True
    
    def Stop(self):
        if self.isDriving:
            self.TripsSinceMaintenance += 1

            if self.TripsSinceMaintenance > 100:
                self.NeedsMaintenance = True
        
        self.isDriving = False

    def __str__(self):
        string = '-------------------------------\n'
        string += 'Make: ' + self.Make +'\n'
        string += 'Model: ' + self.Model + '\n'
        string += 'Year: ' + str(self.Year) +'\n'
        string += 'Weight: ' + str(self.Weight) +'\n'
        string += 'NeedsMaintenance: ' + str(self.NeedsMaintenance) +'\n'
        string += 'TripsSinceMaintenance: ' + str(self.TripsSinceMaintenance) +'\n'
        string += '-------------------------------\n'
        return string


class Planes(Vehicle):
    def __init__(self, Make, Model, Year, Weight, isFlying = False):
        Vehicle.__init__(self, Make, Model, Year, Weight)
        self.isFlying = isFlying

    def Flying(self):
        if self.NeedsMaintenance == True:
            return False
        else:
            self.isFlying = True
            return True

    def Landing(self):
        if self.isFlying:
            self.TripsSinceMaintenance += 1

            if self.TripsSinceMaintenance > 100:
                self.NeedsMaintenance = True

    def __str__(self):
        string = '-------------------------------\n'
        string += 'Make: ' + self.Make +'\n'
        string += 'Model: ' + self.Model + '\n'
        string += 'Year: ' + str(self.Year) +'\n'
        string += 'Weight: ' + str(self.Weight) +'\n'
        string += 'NeedsMaintenance: ' + str(self.NeedsMaintenance) +'\n'
        string += 'TripsSinceMaintenance: ' + str(self.TripsSinceMaintenance) +'\n'
        string += '-------------------------------\n'
        return string

def driveCarRandomTimes(car):
    times = random.randint(1,201)
    for i in range(times):
        car.Drive()
        car.Stop()

carOne = Cars("Audi", "A4", 2020, 1645)
carTwo = Cars("Volkswagen", "Golf 8", 2021, 1261)
carThree = Cars("Mercedes", "E 220", 2019, 1705)

driveCarRandomTimes(carOne)
driveCarRandomTimes(carTwo)
driveCarRandomTimes(carThree)
        
print(carOne)
print(carTwo)
print(carThree)

def flyPlaneRandomTimes(plane):
    times = random.randint(1,201)
    for i in range(times):
        isFlying = plane.Flying()
        if isFlying:
            plane.Landing()
        else:
            print("Plane",plane.Model,"can't fly until it's repaired")
            print('---Repairing---')
            plane.Repair()
            print("Plane",plane.Model,"is repaired\n")



planeOne = Planes("Boeing","747-8",2010, 312000)
planeTwo = Planes("Airbus","A350-900",2013, 115700)

flyPlaneRandomTimes(planeOne)
flyPlaneRandomTimes(planeTwo)

print(planeOne)
print(planeTwo)


