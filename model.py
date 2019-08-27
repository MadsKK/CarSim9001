from random import randint

#Klasse kaldet Wheel
class Wheel(object):
    #Metode som bliver kørt hvergang man instansiere Wheel
    def __init__(self):
        #Instansvariabel som bliver til en random int.
        self.orientation = randint(0,360)

    #Metode kaldet rotate, som har self og revolutions som parameter.
    def rotate(self, revolutions):
        self.orientation = (self.orientation + (revolutions * 360)) % 360

class Engine(object):
    def __init__(self):
        #Instansvariabler
        self.throttlePosition = 0
        #Instansvariabel instansiere Gearbox()
        self.theGearbox = Gearbox()
        self.currentRpm = 0
        self.consumptionConstant = 0.0025
        self.maxRpm = 100
        self.theTank = Tank()

    #Metode som opdatere modellen
    def updateModel(self,dt):
        #Tjekker om self.theTank.contents indhold ikke er 0
        if(self.theTank.contents != 0):
            #Gemmer self.throttlePosition * self.maxRpm i self.currentRpm
            self.currentRpm = self.throttlePosition * self.maxRpm
            #Der bruges self.currentRpm * self.consumptionConstant som parameter til metoden remove
            self.theTank.remove(self.currentRpm * self.consumptionConstant)
            self.theGearbox.rotate(self.currentRpm * (dt / 60))
        #Tjekker om self.theTank.contents er 0
        elif(self.theTank.contents == 0):
            self.currentRpm = 0

class Gearbox(object):
    def __init__(self):
        #Instansvariabler
        #Instansvariablen self.wheels er en dict, hvor der bliver instansiere Wheel() som dens value
        self.wheels = {"frontLeft": Wheel(), "frontRight": Wheel(), "rearLeft": Wheel(), "rearRight": Wheel()}
        self.currentGear = 0
        self.clutchEngaged = False
        self.clutchPosition = 0
        self.gears = [0, 0.8, 1, 1.4, 2.2, 3.8]

    #Metode som skal sørger for at skifte gear op
    def shiftUp(self):
        #Tjekker om det nuværende gear er det samme som længden af listen gear - 1 eller clutchEngaged er True.
        #Den bliver True hvis en af operanderne er true
        if(self.currentGear == len(self.gears)-1 or self.clutchEngaged == True or self.clutchPosition <= 0.3 or self.clutchPosition >= 0.4):
            pass
        else:
            self.currentGear += 1
    #Metode som skal sørger for at skifte gear ned
    def shiftDown(self):
        #Tjekker om det nuværende gear er lig 0 eller clutchEngaged er True.
        #Den bliver True hvis en af operanderne er true
        if(self.currentGear == 0 or self.clutchEngaged == True or self.clutchPosition <= 0.3 or self.clutchPosition >= 0.4):
            pass
        else:
            self.currentGear -= 1
    #Metode som kontrollere om hjulene skal rotere
    def rotate(self, revolutions):
        #Kigger om self.clutchEngaged er True
        if(self.clutchEngaged == True):
            #For-loop som går igennem alle keys i self.wheels
            for key in self.wheels:
                #Henter vi value som er på den tilsvarende key vi indsætter. Derefter bruger vi metoden rotate
                self.wheels[key].rotate(revolutions * self.gears[self.currentGear])

class Tank(object):

    def __init__(self):
        self.capacity = 100
        self.contents = 100

    def remove(self, amount):
        self.contents = self.contents - amount
        if self.contents < 0:
            self.contents = 0

    def refuel(self):
        self.contents = self.capacity

class Car(object):

    def __init__(self):
        self.theEngine = Engine()

    def updateModel(self, dt):
        self.theEngine.updateModel(dt)

#Debug
if __name__ == '__main__':
    pass
