import numpy as np
def offset(a,b):
    return tuple(sum(x) for x in zip(a,b))

class Index:
    def __init__(self, sheet,position):
        self.sheet=sheet
        self.position=position
    def __getitem__(self, yx):
        return self.sheet[offset(self.position, yx)]
    def offset(self, yx):
        return Index(self.sheet,offset(self.position, yx))

def findIndices(sheet,cellValue:str):
    return [Index(sheet,yx) for yx in zip(*np.where(sheet==cellValue))]
   
        
