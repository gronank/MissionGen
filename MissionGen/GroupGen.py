from dcs import Mission
from FlightData import FlightData, FlightMember
from dcs.planes import plane_map
from  dcs  import unitgroup
from ParkingHandler import ParkingHandler
from typing import List, Dict, Union, Optional, Type
from PackageHandler import PackageHandler

def getTemplateGroup(mission:Mission, flight:FlightData):
    template_group =  mission.find_group(flight.callsign)
    if not template_group:
        raise Exception(f"Could not find template for group {flight.callsign} in mission {mission.filename}")
    mission.remove_plane_group(template_group)
    return template_group

def assignFromTemplate(group:unitgroup.PlaneGroup,template:unitgroup.PlaneGroup)->unitgroup.PlaneGroup:
    for waypoint in template.points:
        waypoint.task=[]
        group.add_point(waypoint)

replacements = {'F-14A':'F-14A-135-GR',
                'F-18C':'FA-18C_hornet',
                'F-16C':'F-16C_50'}
def readAircraftType(member:FlightMember):
    aircraft_type=member.aircraft_type
    aircraft_type=aircraft_type.split(' ')[0]
    aircraft_type = replacements.get(aircraft_type) or aircraft_type
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

def generateGroup(mission:Mission, flight:FlightData, package:PackageHandler):
    template=getTemplateGroup(mission,flight)
    
    if len(flight.members)==0:
        return
    if len(flight.members)>4:
        raise Exception("Too many units in flight, limit is 4")
    group=createGroup(mission,flight)
    country = mission.country("USA")
    
    group.task=flight.role
    parkingHandler=ParkingHandler(mission,template,country)
    for i, member in enumerate(flight.members):
            aircraft_type = readAircraftType(member)
            p = mission.aircraft(member.unitName(), aircraft_type, country)
            parkingHandler.assign_parking(p)
            p.set_client()
            package.setupRadio(p, flight.frequency)
            group.add_unit(p)

    mission.flight_group_from_airport
    assignFromTemplate(group,template)
    country.add_aircraft_group(group)
    return