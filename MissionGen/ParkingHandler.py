from dcs import Mission
from dcs.unitgroup  import FlyingGroup
from dcs.country import Country
from dcs.terrain import Airport
def find_ship_by_id(country,ship_id):
    for ship_group in country.ship_group:
           for ship in ship_group:
               if ship.id==ship_id:
                   return ship
    return None
class ParkingHandler(object):
    """description of class"""
    airport:Airport=None
    start_lot:int
    def __init__(self, mission:Mission, template:FlyingGroup, country:Country):
        mission.flight_group_from_unit
        airport_id=template.airport_id()
        if airport_id:
            self.airport=mission.terrain.airport_by_id(airport_id)
            self.start_lot=template.units[0].parking
        else:
            self.start_lot=1

    def assign_parking(self,unit):
        lot=self.start_lot
        self.start_lot=self.start_lot+1

        if self.airport:
            unit.set_parking(self.airport.parking_slot(lot))
        else:
            unit.parking = lot
            unit.parking_id = str(lot)
        


        
        


