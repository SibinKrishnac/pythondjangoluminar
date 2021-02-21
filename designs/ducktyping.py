class swift:
    def drive(self):
        print("driving swift")
class sonet:
    def drive(self):
        print("drive sonet")
class person:
    def start(self,car):
        car.drive()
sw=swift()
p=person()
p.start(sw)