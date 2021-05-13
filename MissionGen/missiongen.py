import pandas as pa
import numpy as n
from FlightData import loadFlightData
from GroupGen import generateGroup
from dcs import Mission
from PackageHandler import PackageHandler
filename="../TestData/AirGoons DCS Weekly Package.ods"
templateMission="../TestData/GoonTest1.miz"
testOut="../TestData"
signup="Sign-Ups"

def generateMission(sheetPath:str,templateMissionPath:str,outDir:str):
    sheet=pa.read_excel(sheetPath,sheet_name=signup,engine="odf").to_numpy()
    flightData = loadFlightData(sheet)


    mission=Mission()
    mission.load_file(templateMissionPath)
    package=PackageHandler(sheet, mission)
    for flight in flightData:
        generateGroup(mission,flight, package)
    mission.save(f"{outDir}/{package.package_name}.miz")
if __name__=="__main__":
    generateMission(filename, templateMission, testOut)


