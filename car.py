import time

class Pack:
    def __init__(self, material, tightness, volume, expiration):
        if type(material) == str:
            self.material = material
            print("material:", material)
        if type(tightness) == bool:
            if tightness == True:
                self.tightness = tightness
                print("tightness:", 'yes')
            else:
                print("tightness:", 'no')
        if type(volume) == int or type(volume) == float:
            self.volume = volume
            print("volume:", volume, "liters")
        if type(expiration) == int:
            self.expiration = expiration
            print("expires in", expiration, "days")

class Product:
    def __init__(self, expiration_date, weight, recommended_temperature, current_temperature):
        if type(expiration_date) == int:
            self.expiration_date = expiration_date
            print("expires in", expiration_date, "days")
        if type(weight) == int or type(weight) == float:
            self.weight = weight
            print("weight:", weight, "kilograms")
        if type(recommended_temperature) == int or type(recommended_temperature) == float:
            self.recommended_temperature = recommended_temperature
            print("recommended temperature:", recommended_temperature, "celsius")
        if type(current_temperature) == int or type(current_temperature) == float:
            self.current_temperature = current_temperature
            print("current temperature:", current_temperature, "celsius")

class Milk(Product):
    def __init__(self, heat_treatment, fat_percent, volume, expiration_date, weight, recommended_temperature,
                 current_temperature):
        super().__init__(expiration_date, weight, recommended_temperature, current_temperature)
        if type(heat_treatment) == str:
            self.heat_treatment = heat_treatment
            print("heat_treatment:", heat_treatment)
        if type(volume) == int or type(volume) == float:
            self.volume = volume
            print("heat_treatment:", heat_treatment)
        if type(fat_percent) == int:
            self.fat_percent = fat_percent
            print("fats:", str(fat_percent) + "%")

    def mgnov_past(self):
        time.sleep(2)
        self.heat_treatment = 'sterilized'
        self.expiration_date += 3

    def fast_past(self):
        time.sleep(10)
        self.heat_treatment = 'pasterized'
        self.expiration_date += 7

    def long_past(self):
        time.sleep(20)
        self.heat_treatment = 'ultrapasterized'
        self.expiration_date += 14

    def info(self):
        print("heat_treatment:", self.heat_treatment)
        print("fats:", str(self.fat_percent)+"%")
        print("volume:", str(self.volume), 'liters')
        print("expiration date:", self.expiration_date)
        print("recommended temperature:", self.recommended_temperature)
        print("current temperature:", self.current_temperature)

#class PackedProduct(Pack):
#    def __init__(self, material, tightness, volume, expiration):
#        Pack.init(self, material, tightness, volume, expiration)

class Transport:
    def __init__(self, speed, volume, weight, temperature):
        if (type(speed) == int) or (type(speed) == float):
            self.speed = speed
        if (type(volume) == int) and not(type(volume) == float):
            self.volume = volume
        if type(weight) == int:
            self.weight = weight
        if type(temperature) == float:
            self.temperature = temperature
    def  load(self, weight,  volume, products):
        summary_weight, summary_volume = 0, 0
        for item in products:
            summary_weight += item.weight
            summary_volume += item.volume
            time.sleep(1)
        if (summary_weight <= self.weight) and (summary_volume <= self.volume):
            return True
        else:
            return False
    def transportation(self, distance):
        time.sleep(distance/self.speed)

    def unload(self, products):
        for item in products:
            time.sleep(1)

class TransportBox:
    def __init__(self, weight, volume, temperature, products):
        self.weight = weight
        self.volume = volume
        self.temperature = temperature
        self.products = products

class Truck_3_5(Transport):
    pass
#
class Truck_5(Transport):
    pass
#
class Truck_10(Transport):
    pass
#
class Truck_20(Transport):
    pass
#
class Truck_50(Transport):
    pass
#
class Truck_55(Transport):
    pass
#
a = Transport(10, 50, 100, 36.6)
print(a.speed)
