import pandas as pa
import numpy as np
import dcs
from FlightData import loadFlightData
filename="../TestData/AirGoons DCS Weekly Package.ods"
signup="Sign-Ups"
sheet=pa.read_excel(filename,sheet_name=signup,engine="odf").to_numpy()

flightData = loadFlightData(sheet)

m=dcs.Mission()
m.remove_plane_group
a=8
