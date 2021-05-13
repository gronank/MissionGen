from Index import Index, findIndices
name_offset=(0,2)
creator_offset=(2,2)
package_freq_offset=(8,2)
def frequency(f):
    if isinstance(f,str) and f != 'x':
        return float(f.replace(',','.'))
    else:
        return f
class ComsManager:
    def __init__(self,sheet):
        index=findIndices(sheet,'PACKAGE')[0]
        self.package_name=index[name_offset]
        self.creator_name=index[creator_offset]
        self.package_freq=frequency(index[package_freq_offset])

