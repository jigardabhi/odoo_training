class Bill:
    def __init__(self,Name,PhoneNo,TotalAmount):
        self.Name=Name
        self.PhoneNo=PhoneNo
        self.TotalAmount=TotalAmount


    def Electricity_bill(self):
        print("Electricity bill Details",self.Name)
        print("Electricity bill Details",self.PhoneNo)
        print("Electricity bill Details",self.TotalAmount)


    def Water_bill(self):
        print("Water bill details",self.Name)
        print("Water bill details",self.PhoneNo)
        print("Water bill details",self.TotalAmount)

electricbill=Bill("Harsh", 8511281915, 11000)

print(electricbill.Electricity_bill())


waterbill=Bill("Karan", 9924034556, 19900)

print(waterbill.Water_bill())