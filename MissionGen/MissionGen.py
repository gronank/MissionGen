import pandas as pa
import numpy as np
from FlightData import loadFlightData
filename="../TestData/AirGoons DCS Weekly Package.ods"
signup="Sign-Ups"
sheet=pa.read_excel(filename,sheet_name=signup,engine="odf").to_numpy()

flightData = loadFlightData(sheet)

a=8
