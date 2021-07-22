class Bike:
    tyres = 2
    def __init__(self):
        self.name = 'Activa'
        self.year = '2017'
        self.mileage = '40KMPL'

Bike.tyres = 5
bike1 = Bike()
print(bike1.name, bike1.year, bike1.mileage, Bike.tyres)
#Bike.tyres = 5
bike2 = Bike()
bike2.name = 'Unicorn'
bike2.year = '2021'
bike2.mileage = '50KMPL'
print(bike2.name, bike2.year, bike2.mileage, Bike.tyres)