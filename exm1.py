#soyut sınıf oluşturma

from abc import ABC, abstractmethod
import json as js

class Vehicle(ABC):# soyut araç sınıfı
    def __init__( self, mileage, max_speed,name):
        self.milage = mileage
        self.max_speed = max_speed
        self.name = name

    @abstractmethod
    def show_info(self):
        pass



class Car(Vehicle): # binek araç sınıfı
    def __init__(self, mileage, max_speed, name):
        super().__init__(mileage, max_speed, name)
    
    def show_info(self):
        print(f"Araba Adı: {self.name}, Maksimum Hız:{self.max_speed}, Kilometre: {self.milage} ")

class Motorcycle(Vehicle): # motorsiklet sınıfı
    def __init__(self, mileage, max_speed, name):
        super().__init__(mileage, max_speed, name)
    def show_info(self):
        print(f"Motorsiklet Adı: {self.name}, Maksimum Hız: {self.max_speed}, Kilometre: {self.milage}")
 
class Truck(Vehicle): # kamyon sınıfı
    def __init__(self, mileage, max_speed, name):
        super().__init__(mileage, max_speed, name)
    def show_info(self):
        print(f"Kamyon Adı: {self.name}, Maksimum Hız: {self.max_speed}, Kilometre: {self.milage}")

# kullanıcıdan araç türünü alma

car, motorcycle, truck = Car(), Motorcycle(), Truck()

tur = input("Araç türünü giriniz (Car, Motorcycle, Truck): ")
if tur == "Car":
    data = input("Araç bilgilerini giriniz (Adı, Maksimum Hız, Kilometre): ")
    name, max_speed, milage = data.split()
    car = Car(milage, max_speed, name)
    car.show_info()
elif tur == "Motorcycle":
    data = input("Araç bilgilerini giriniz( Adı, Maksimum Hız, Kilometre): ")
    name, max_speed, milage = data.split()
    motorcycle = Motorcycle(milage, max_speed, name)
    motorcycle.show_info()
elif tur == "Truck":
    data = input("Araç bilgilerini giriniz( Adı, Maksimum Hız, Kilometre): ")
    name, max_speed, milage = data.split()
    truck = Truck(milage, max_speed, name)
    truck.show_info()
else:
    print("Geçersiz araç türü.")







