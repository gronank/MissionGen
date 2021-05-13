import numpy as np
from Index import Index, findIndices
from PackageHandler import frequency

nameOffset = (0,1)

class FlightMember(object):
    aircraft_type: str
    pilot_name: str
    rio_name:str
    def __init__(self, index):
        self.aircraft_type=index[(0,0)]
        pilots=index[nameOffset]
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
    def __init__(self, index:Index):
        self.role=index[roleOffset]
        self.callsign=index[callsignOffset]
        self.frequency=frequency(index[frequencyOffset])
        self.mids_ch=index[mids_chOffset]
        if(self.mids_ch=="x"):
            self.mids_ch=None
        self.members=[]
        memberIndex=index.offset(memberOffset)
        for i in range(4):
            member=FlightMember(memberIndex.offset((i,0)))
            if(member.pilot_name):
                self.members.append(member);
    def isActive(self):
        return self.role!="(Flight Closed)"
        


def loadFlightData(sheet):
    flightIndices=findIndices(sheet,"Tasking")
    flightData=[FlightData(index) for index in flightIndices]
    return [fd for fd in flightData if fd.isActive()]