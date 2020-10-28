

#Parent Class
class Vehicles:
    Brand = "Unknown"
    Type = "Unknown"
    NumofWheels = 4
    Man_or_Auto = 'Automatic'
    color = 'White'
    drive = 'Front-Wheel Drive'

    def information(self):
        msg = "\nBrand: {}\nType: {}\nNumber of Wheels: {}\nManual or Automatic: {}\nColor: {}\nDrive {}".format(self.Brand,self.Type,self.NumofWheels,self.Man_or_Auto,self.color,self.drive)
        return msg
            


#Child Class 1
class Vehicles1(Vehicles):
    Brand = 'Nissan'
    Type = 'Pathfinder'
    color = 'Silver'
    drive = 'All-Wheel Drive'

    def suv(self):
        msg = "\nFamily friendly vehicle!"
        return msg



#Child Class 2
class Vehicles2(Vehicles):
    Brand = 'Toyota'
    Type = 'Tacoma'
    drive = 'All-Wheel Drive'
    color = 'Green'

    def moving(self):
        msg = "\nA great way to help move!"
        return msg


if __name__ == "__main__":
    vehicles1 = Vehicles1()
    print(vehicles1.information())
    print(vehicles1.suv())

    vehicles2 = Vehicles2()
    print(vehicles2.information())
    print(vehicles2.moving())
