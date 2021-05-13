import pandas as pa
import numpy as np
from FlightData import loadFlightData
from GroupGen import generateGroup
from dcs import Mission
from PackageHandler import PackageHandler
filename="../TestData/AirGoons DCS Weekly Package.ods"
templateMission="../TestData/GoonTest1.miz"
signup="Sign-Ups"
sheet=pa.read_excel(filename,sheet_name=signup,engine="odf").to_numpy()

flightData = loadFlightData(sheet)
package=PackageHandler(sheet)

mission=Mission()
mission.load_file(templateMission)
for flight in flightData:
    generateGroup(mission,flight, package)
mission.save("../TestData/Test.miz")

