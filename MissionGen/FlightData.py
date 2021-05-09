import numpy as np
def offset(a,b):
    return tuple(sum(x) for x in zip(a,b))



nameOffset = (0,1)
class FlightMember(object):
    aircraft_type: str
    pilot_name: str
    rio_name:str
    def __init__(self, sheet, index):
        self.aircraft_type=sheet[index]
        pilots=sheet[offset(index,nameOffset)]
        if not isinstance(pilots,str):
            pilots=(None,None)
        else:
            pilots=pilots.split("/")
        if(len(pilots)==1):
            pilots.append(None)
        self.pilot_name,self.rio_name = pilots
    def unitName(self):
        if self.rio_name:
            return self.pilot_name+"/"+self.rio_name
        else:
            return self.pilot_name
roleOffset=(0,2)
callsignOffset=(-1,2)
frequencyOffset=(1,2)
mids_chOffset=(1,4)
memberOffset=(3,2)
class FlightData(object):
    """contains flight data from sign-up spreadsheet"""
    callsign: str
    role: str
    frequency: str
    mids_ch: str
    members: list[FlightMember]
    def __init__(self, sheet, index):
        self.role=sheet[offset(index, roleOffset)]
        self.callsign=sheet[offset(index, callsignOffset)]
        self.frequency=sheet[offset(index, frequencyOffset)]
        self.mids_ch=sheet[offset(index, mids_chOffset)]
        if(self.mids_ch=="x"):
            self.mids_ch=None
        self.members=[]
        for i in range(4):
            memberIndex=offset(memberOffset,(i,0))
            member=FlightMember(sheet,offset(index,memberIndex))
            if(member.pilot_name):
                self.members.append(member);
    def isActive(self):
        return self.role!="(Flight Closed)"
        


def loadFlightData(sheet):
    flightIndices=list(zip(*np.where(sheet=="Tasking")))
    flightData=[FlightData(sheet,index) for index in flightIndices]
    return [fd for fd in flightData if fd.isActive()]