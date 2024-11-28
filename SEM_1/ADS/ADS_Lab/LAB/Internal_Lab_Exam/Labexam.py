import datetime

class Convocation:
    class Institute:
        def __init__(self, IName, Istdc):
            self.MAHE = {'MSIS': 'MSIS@123', 'ICAS': "ICAS@123", 'MTech': "MTech@123",
                         'BTech': "BTech@123", 'DAMP': "DAMP@123", 'admin': "admin"}
            self.inst = {IName: Istdc} 
            self.daily_slots = {IName: {1: 0, 2: 0, 3: 0}} 

        def getIName(self):
            return self.inst.keys()

        def getIstdc(self, IName):
            return self.inst[IName]

        def getTotalStd(self):
            return sum(self.inst.values())

        def validInstAdmin(self, IName, Password, Istdc):
            if IName in self.inst and Password == self.MAHE.get(IName):
                self.addInstitute(IName, Istdc)
            else:
                print("Invalid Institute Name or Password")

        def addInstitute(self, IName, Istc):
            if IName in self.inst:
                self.updateStdc(IName, Istc)
            else:
                self.inst[IName] = Istc

        def updateStdc(self, IName, Istc):
            if IName in self.inst:
                self.inst[IName] += Istc
            else:
                print("Invalid Institute Name")

        def deleteInstitute(self, IName):
            if IName in self.inst:
                del self.inst[IName]
            else:
                print("Invalid Institute Name")

    class Student:
        def __init__(self, inst):
            self.inst = inst  
            self.std = {}  
            self.Pass = {}  

        def studentSignUp(self, SName, RegNo, IName, MobNo, preferred_day):
            if IName in self.inst.getIName():
                if RegNo not in self.std:
                    self.std[RegNo] = [SName, IName, MobNo, preferred_day]
                    self.generatePassId(RegNo, SName, IName, MobNo, preferred_day)
                    print("Student Registered Successfully")
                else:
                    print("Student Already Registered")
            else:
                print("Invalid Institute Name")

        def generatePassId(self, RegNo, SName, IName, MobNo, preferred_day):
            max_daily_slots = self.inst.getIstdc(IName) // 2 
            current_day_slots = self.inst.daily_slots[IName][preferred_day]

            if current_day_slots < max_daily_slots:
                year = datetime.datetime.now().year
                reg_str = str(RegNo)
                passId = f"{year}{IName}{reg_str[-3:]}D{preferred_day}"
                self.Pass[passId] = [RegNo, SName, IName, MobNo]
                self.inst.daily_slots[IName][preferred_day] += 1  
                print(f"PassId Generated Successfully for Day {preferred_day}")
            else:
                print(f"No slots available for {IName} on Day {preferred_day}")

        def enterVenue(self, passId, day):
            if passId in self.Pass and passId.endswith(f"D{day}"):
                print(f"Welcome to Venue for Day {day}")
                self.sendDetailsToInstitute(passId)
            elif passId in self.Pass:
                print(f"Your pass is only valid for Day {passId[-1]}, not Day {day}")
            else:
                print("Invalid PassId")

        def sendDetailsToInstitute(self, passId):
            std_details = self.Pass.get(passId)
            if std_details:
                IName = std_details[2]
                print(f"Details sent to {IName} for Day {passId[-1]}:", std_details)

inst = Convocation.Institute("MSIS", 100)
student_obj = Convocation.Student(inst)

inst.validInstAdmin("MSIS", "MSIS@123", 100)
student_obj.studentSignUp("Nikhil", 101, "MSIS", "1234567890", 1)
student_obj.studentSignUp("Karthik", 102, "MSIS", "0987654321", 1)
student_obj.studentSignUp("Nithik", 103, "MSIS", "1122334455", 2)

# Enter the venue for a specific day
student_obj.enterVenue("2024MSIS101D1", 1)  
student_obj.enterVenue("2024MSIS101D1", 2)  
