from dcs import Mission
from dcs.unitgroup  import FlyingGroup
from dcs.country import Country
from dcs.terrain import Airport
import copy
def find_ship_by_id(country,ship_id):
    for ship_group in country.ship_group:
           for ship in ship_group:
               if ship.id==ship_id:
                   return ship
    return None
class ParkingHandler(object):
    """description of class"""
    airport:Airport=None
    carrier=None
    start_lot:int
    def __init__(self, mission:Mission, template:FlyingGroup, country:Country):
        mission.flight_group_from_unit
        airport_id=template.airport_id()
        self.start_lot=template.units[0].parking
        if airport_id:
            self.airport=mission.terrain.airport_by_id(airport_id)
        else:
            self.location=template.units[0].position

    def assign_parking(self,unit):
        lot=self.start_lot
        self.start_lot=self.start_lot+1

        if self.airport:
            parking_slot=self.airport.parking_slot(lot)
            unit.set_parking(parking_slot)
            unit.position=copy.copy(parking_slot.position)
        else:
            unit.parking = lot
            unit.parking_id = str(lot)
            unit.position=copy.copy(self.location)
        


        
        


