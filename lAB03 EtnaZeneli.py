#Etna Zeneli


class Patient:
    def __init__(self,name):
        self.name = name
                 
class nurse:
    pass
    def getpatient(self):
        pass
    def sendpatient(self):
        pass


class Physician:
    pass
    def examination(self):
        pass


class waitingRoom:
    def __init__(self):
        self.patientsWaiting = []
        self.patientWaiting = []
    def addPatients(self,Patient):
        self.patientsWaiting.append(Patient)
    def RPatients(self):
        return patientsWaiting.pop(0)
    def addPatients1(self,patient):
        self.patientsWaitingForever.append(patient)
    def RPatients1(self):
        return patientWaiting.pop(0)

class eRoom:
    def __init__(self,Physician1):
        self.Physician = Physician1
        self.roomT = 0
        self.Patient = None

    def addPatients2(self,waitingRoom):
        pass

    def RPatients2(self):
        pass
    
    def timeInRoom(self):
        return self.roomT
    


#advance time w/ for loop
while True:
    pat = Patient("Kusha")
    
    room = waitingRoom()
    
    r1 = eRoom()
    r2 = eRoom()
    r3 = eRoom()
    r4 = eRoom()
    r5 = eRoom()
    r6 = eRoom()

    
    
    
