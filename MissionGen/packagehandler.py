from index import Index, findIndices
from dcs.flyingunit import FlyingUnit
from dcs import Mission
from dcs.coalition import Coalition

name_offset = (0,2)
creator_offset = (2,2)
atc_freq_offset = (4,2)
package_freq_offset = (8,2)

main_radio = 2
group_radio = 1

atc_channel = (main_radio, 1)
package_channel = (main_radio, 2)

group_channel = (group_radio , 1)
def refuel_channel(i):
    return  (group_radio, 2 + i)

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

    def setupRadio(self,unit:FlyingUnit, flightFrequency:float):
        unit.set_radio_channel_preset(*atc_channel, self.atc_freq_offset)
        unit.set_radio_channel_preset(*package_channel, self.package_freq)
        unit.set_radio_channel_preset(*group_channel, flightFrequency)
        for i, refuelFreq in enumerate(self.refuel_freqs):
            unit.set_radio_channel_preset(*refuel_channel(i), refuelFreq)
