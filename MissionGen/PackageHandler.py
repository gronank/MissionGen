from Index import Index, findIndices
from dcs.unit import Unit
name_offset = (0,2)
creator_offset = (2,2)
atc_freq_offset = (4,2)
package_freq_offset = (8,2)


atc_channel = (1, 1)
package_channel = (1, 2)
refuel_channel = (1, 3)
group_channel = (2, 1)

def frequency(f):
    if isinstance(f,str) and f != 'x':
        return float(f.replace(',','.'))
    else:
        return f

class PackageHandler:
    def __init__(self,sheet):
        index=findIndices(sheet,'PACKAGE')[0]
        self.package_name=index[name_offset]
        self.creator_name=index[creator_offset]
        self.atc_freq_offset=frequency(index[atc_freq_offset])
        self.package_freq=frequency(index[package_freq_offset])
    def setupRadio(self,unit:Unit, flightFrequency:float):
        unit.set_radio_channel_preset(*atc_channel, self.atc_freq_offset)
        unit.set_radio_channel_preset(*package_channel, self.package_freq)
        unit.set_radio_channel_preset(*group_channel, flightFrequency)
        pass

