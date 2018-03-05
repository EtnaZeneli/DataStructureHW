#Etna Zeneli
import random
name= [ "Kushtrim", "Arlinda", "Jora", "Hera", "Vitesa",\
        "Ardiana", "Davin", "Albin", "Ria", "Dren",\
        "Albi"]

waitingarea=[]
traiagearea=[]
examarea=[]
eSize= 6
doc= 6

def callN():
    traiagearea.append(waitingarea.pop(0))
    sort(traiagearea, key= patient.waitTime)

    
class Patient:
    def __init__(self,name):
        self.name = name
                 
def nurse(js):
    js.addPatient2(js.removePantient())


class waitingRoom:
    def __init__(self):
        self.patientsWaiting = []
        self.patientWaiting = []
    def addPatients(self,Patient):
        self.patientsWaiting.append(Patient)
    def RPatients(self):
        return patientsWaiting.pop(0)
    def addPatients1(self,patient):
        self.patientWaiting.append(patient)
    def RPatients1(self):
        return patientsWaiting.pop(0)
    def AreaE1(self):
        if self.patientsWaiting == []:
            return True
        else:
            return False
    def AreaE2(self):
        if self.patientsWaiting == []:
            return True
        else:
            return False
        
class eRoom:
    def __init__(self):
        self.roomT = 0
        self.Patient = None
        self.patientT = 0

    def addPatients2(self,js):
        self.patient = js.RPatients1()
        self.patientT = random.randrange(15,21)

    def Time(self):
        return self.roomT

    def AreaE3(self):
        if self.Patient == None:
            return True
        else:
            return False

    def RPatients2(self):
        x = self.Patient
        self.patient = None
        return x
    
    def timeInRoom(self):
        return self.roomT
    def ExtraTime(self):
        self.roomT +=1
    
    
room = waitingRoom()
    
r1 = eRoom()
r2 = eRoom()
r3 = eRoom()
r4 = eRoom()
r5 = eRoom()
r6 = eRoom()

def timeUpdate():
    nurse(room)
    if not R.AreaE3():
        R.ExtraTime()
        if R.Time() >= R.timeInRoom():
            R.RPatients2()

    if R.AreaE1():
        if not room.AreaE2():
            R.addPatients2(room)
            
    if not R1.AreaE3():
        R1.ExtraTime()
        if R1.Time() >= A2.timeInRoom():
            R1.RPatients2()

    if R1.AreaE1():
        if not room.AreaE2():
            R1.addPatients2(room)

    if not R2.AreaE3():
        R2.ExtraTime()
        if R2.Time() >= R2.timeInRoom():
            R2.RPatients2()

    if R2.AreaE1():
        if not room.AreaE2():
            R2.addPatients2(room)

    if not R3.AreaE3():
        R3.ExtraTime()
        if R3.Time() >= R3.timeInRoom():
            R3.RPatients2()

    if R3.AreaE1():
        if not room.AreaE2():
            R3.addPatients2(room)

    if not R4.AreaE3():
        R4.ExtraTime()
        if R4.Time() >= R4.timeInRoom():
            R4.RPatients2()

    if R4.AreaE1():
        if not rooom.AreaE2():
            R4.addPatients2(room)

    if not R5.AreaE3():
        R5.ExtraTime()
        if R5.Time() >= R5.timeInRoom():
            R5.RPatients2()

    if R5.AreaE1():
        if not room.AreaE2():
            R5.addPatients2(room)
    
    
    
