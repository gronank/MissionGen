from index import Index, findIndices
from dcs.unit import Unit
from dcs import Mission
from dcs.coalition import Coalition

name_offset = (0,2)
creator_offset = (2,2)
atc_freq_offset = (4,2)
package_freq_offset = (8,2)


atc_channel = (1, 1)
package_channel = (1, 2)
def refuel_channel(i):
    return  (1, 3 + i)

group_channel = (2, 1)

def frequency(f):
    if isinstance(f,str) and f != 'x':
        return float(f.replace(',','.'))
    else:
        return f

def findAllAirGroups(coalition:Coalition, condition):
    for country in coalition.countries.values():
        for plane_group in country.plane_group :
            if condition(plane_group):
                yield plane_group

class PackageHandler:
    def __init__(self,sheet, mission:Mission,side:str="blue"):
        index=findIndices(sheet,'PACKAGE')[0]
        self.package_name=index[name_offset]
        self.creator_name=index[creator_offset]
        self.atc_freq_offset=frequency(index[atc_freq_offset])
        self.package_freq=frequency(index[package_freq_offset])

        refuelers=sorted(findAllAirGroups(mission.coalition[side], lambda group: group.task=='Refueling'), key=lambda group: group.name)
        for i, refueler in enumerate(refuelers):
            channel=refuel_channel(i)[1]
            refueler.name=refueler.name.replace('MHz,',f'MHz (Ch {channel}),')
        self.refuel_freqs=[r.frequency for r in refuelers]

    def setupRadio(self,unit:Unit, flightFrequency:float):
        unit.set_radio_channel_preset(*atc_channel, self.atc_freq_offset)
        unit.set_radio_channel_preset(*package_channel, self.package_freq)
        unit.set_radio_channel_preset(*group_channel, flightFrequency)
        for i, refuelFreq in enumerate(self.refuel_freqs):
            unit.set_radio_channel_preset(*refuel_channel(i), refuelFreq)