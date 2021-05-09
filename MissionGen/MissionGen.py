import pandas as pa
import numpy as np
from FlightData import loadFlightData
from GroupGen import generateGroup
from dcs import Mission

filename="../TestData/AirGoons DCS Weekly Package.ods"
signup="Sign-Ups"
sheet=pa.read_excel(filename,sheet_name=signup,engine="odf").to_numpy()

flightData = loadFlightData(sheet)


mission=Mission()
group=generateGroup(mission,flightData[0])

a=8
