from dcs import Mission
from FlightData import FlightData, FlightMember
from dcs.planes import plane_map
from  dcs  import unitgroup
from typing import List, Dict, Union, Optional, Type

def readAircraftType(member:FlightMember):
    aircraft_type=member.aircraft_type
    aircraft_type=aircraft_type.split(' ')[0]
    ac_type=plane_map.get(aircraft_type)
    if(ac_type):
        return ac_type
    else:
        raise Exception(f"Unrecognized aircraft type {aircraft_type}")
def createGroup(mission:Mission, flight:FlightData)->Union[unitgroup.PlaneGroup, unitgroup.HelicopterGroup]: 
    aircraft_types=[readAircraftType(member) for member in flight.members]
    if all(aircraft_type.helicopter for aircraft_type in aircraft_types):
        return mission.helicopter_group(flight.callsign)
    elif not any(aircraft_type.helicopter for aircraft_type in aircraft_types):
        return mission.plane_group(flight.callsign)
    else:
        raise Exception("A group must consist of all the same types: planes or helicopters")

def generateGroup(mission:Mission, flight:FlightData):
    if len(flight.members)>4:
        raise Exception("Too many units in flight, limit is 4")
    group=createGroup(mission,flight)
    country = mission.country("USA")
    for i, member in enumerate(flight.members):
            aircraft_type = readAircraftType(member)
            p = mission.aircraft(member.unitName(), aircraft_type, country)
            p.set_client()
            group.add_unit(p)
    group.task=flight.role
    country.add_aircraft_group(group)
    return group