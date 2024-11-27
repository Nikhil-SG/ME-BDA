import datetime
class Convaction:
    class Institute:
        def __confindetional__(self):
            self.MAHE = {'MSIS':'MSIS@123',
                    'ICAS':"ICAS@123",
                    'MTech':"MTech@123",
                    'BTech':"BTech@123",
                    'DAMP':"DAMP@123",
                    'admin':"admin"}

        def __init__(self, IName, Istdc):
            self.inst ={IName:Istdc}

        def getIName(self):
            return self.inst.keys()
        
        def getIstdc(self, IName):
            return self.inst[IName]
        
        def getTotalStd(self):
            return sum(self.inst.values())
        
        def ValidInstAdmin(self, IName, Password, Istdc):
            if IName in self.inst.keys():
                if Password ==self.MAHE[IName]:
                    self.addInstitute(IName, Istdc)
                else:
                    print("Invalid Password")
            else:
                print("Invalid Institute Name")
        
        def addInstitute(self, IName,Istc):
            if IName in self.inst.keys():
                self.UpdateStdc(IName,Istc)
            else:
                self.inst[IName] = Istc
        
        def UpdateStdc(self,IName,Istc):
            if IName in self.inst.keys():
                self.inst[IName] += Istc
            else:
                print("Invalid Institute Name")
        
        def deleteInstitute(self,IName):
            if IName in self.inst.keys():
                del self.inst[IName]
            else:
                print("Invalid Institute Name")
        
    class Student:
        def __init__(self, SName,RegNo, IName,MobNo,day):
            self.std = {RegNo: [SName, IName, MobNo]}

        def Student_SignUp(self, SName, RegNo, IName, MobNo):
            if IName in self.inst.getIName():
                if RegNo not in self.std.keys():
                    self.std[RegNo] = [SName,IName, MobNo]
                    print("Student Registered Successfully")
                    self.Generate_PassId(RegNo,SName,IName, MobNo,day)
                else:
                    print("Student Already Registered")
            else:
                print("Invalid Institute Name")

        def Student_Pass(self, passId,RegNo,SName,IName,MobNo):
            self.Pass={passId:[RegNo,SName,IName,MobNo]}

        def Generate_PassId(self,RegNo,SName,IName,MobNo,day):
            if IName in self.inst.getIName():
                day = day
                if day == 1:
                    if self.getIstdc(IName)/self.getTotalStd() < 50:
                        Pass = Pass("D1",RegNo,IName,MobNo)
                        self.Student_Pass(Pass,RegNo,SName,IName,MobNo)
                    else:
                        print("Institute is Full")
                elif day == 2:
                    if self.getIstdc(IName)/self.getTotalStd() < 50:
                        Pass=Pass("D2",RegNo,IName,MobNo)
                        self.Student_Pass(Pass,RegNo,SName,IName,MobNo)
                    else:
                        print("Institute is Full")
                elif day == 3:
                    if self.getIstdc(IName)/self.getTotalStd() < 50:
                        Pass=Pass("D3",RegNo,IName,MobNo)
                        self.Student_Pass(Pass,RegNo,SName,IName,MobNo)
                    else:
                        print("Institute is Full")
                else:
                    print("Invalid Day")
            else:
                print("Invalid Institute Name")

        def Pass(self,Day,RegNo, IName,MobNo):
            data = datetime.to_year.year()
            if IName in self.inst.getIName():
                reg= str(RegNo)
                if Day == "D1":
                    passId = +IName+reg[-3:]+Day
                    print("PassId Generated Successfully for Day 1")
                    return passId
                elif Day == "D2":
                    passId = to_year()+IName+reg[-3:]+Day
                    print("PassId Generated Successfully for Day 2")
                    return passId
                elif Day == "D3":
                    passId = to_year()+IName+reg[-3:]+Day
                    print("PassId Generated Successfully for Day 3")
                    return passId
                else:
                    print("Invalid Day")
            else:
                print("Invalid Institute Name")
            
        
        def Enter_to_Venue_Day1(self,passId):
            if passId in self.Pass.keys():
                if passId[-2:] == "D1":
                    print("Welcome to Venue")
                    self.Day1Details = {self.Pass[passId][2]:}
                    self.send_details_to_institute(passId)
                elif passId[-2:] == "D2":
                    print("Please come on Day 2")
                elif passId[-2:] == "D3":
                    print("Please come on Day 3")
            else:
                print("Invalid PassId")
            
        def Enter_to_Venue_Day2(self,passId):
            if passId in self.Pass.keys():
                if passId[-2:] == "D2":
                    print("Welcome to Venue")
                    self.Day2Details = {self.Pass[passId][2]:s}
                    self.send_details_to_institute(passId)
                elif passId[-2:] == "D1":
                    print("your pass was vaild on Day 1 only. So No Entry as you PassId is Expired")
                elif passId[-2:] == "D3":
                    print("Please come on Day 3")
            else:
                print("Invalid PassId")

        def Enter_to_Venue_Day3(self,passId):
            if passId in self.Pass.keys():
                if passId[-2:] == "D3":
                    print("Welcome to Venue")
                    self.Day3Details = {self.Pass[passId][2]:s}
                    self.send_details_to_institute(passId)
                elif passId[-2:] == "D2" or passId[-2:] == "D1":
                    print("your pass was vaild on Day 2 only. So No Entry as you PassId is Expired")
                else:
                    print("Invalid PassId")
            else:
                print("Invalid PassId")

        def send_details_to_institute(self,passId):
            if passId[-2:] == "D1":
                std_details = self.Student_Pass[passId]
                if self.Day1Details[std_details[2]] == 'MSIS':
                    print("Details sent to Institute for Day 1",std_details)
                if self.Day1Details[std_details[2]] == 'ICAS':
                    print("Details sent to Institute for Day 1",std_details)
                if self.Day1Details[std_details[2]] == 'MTech':
                    print("Details sent to Institute for Day 1",std_details)
                if self.Day1Details[std_details[2]] == 'BTech':
                    print("Details sent to Institute for Day 1",std_details)
                if self.Day1Details[std_details[2]] == 'DAMP':
                    print("Details sent to Institute for Day 1",std_details)

        def send_details_to_institute(self,passId):
            if passId[-2:] == "D2":
                std_details = self.Student_Pass[passId]
                if self.Day2Details[std_details[2]] == 'MSIS':
                    print("Details sent to Institute for Day 2",std_details)
                if self.Day2Details[std_details[2]] == 'ICAS':
                    print("Details sent to Institute for Day 2",std_details)
                if self.Day2Details[std_details[2]] == 'MTech':
                    print("Details sent to Institute for Day 2",std_details)
                if self.Day2Details[std_details[2]] == 'BTech':
                    print("Details sent to Institute for Day 2",std_details)
                if self.Day2Details[std_details[2]] == 'DAMP':
                    print("Details sent to Institute for Day 2",std_details)

        def send_details_to_institute(self,passId):

            
    


