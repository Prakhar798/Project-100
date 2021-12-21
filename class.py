class Car(object):
    def __init__(self, model, color, company, speedlimit):
        self.color = color
        self.model = model
        self.company = company
        self.speedlimit = speedlimit

    def start(self):
        print("Starting.........")

    def stop(self):
        print("Stopping.........")

    def accelerate(self):
        print("Accelerating.......")

    def changegear(self, geartype):
        print("Changing Gear........")


audi = Car("A6", "Red", "Audi", "100km")
audi.start()
audi.stop()
audi.accelerate()
audi.changegear(1)