import pandas as pa
import numpy as np
filename="../TestData/AirGoons DCS Weekly Package.ods"
signup="Sign-Ups"
sheet=pa.read_excel(filename,sheet_name=signup,engine="odf").to_numpy()
flightIndices=list(zip(*np.where(sheet=="Tasking")))
flightData = [readFlightData(sheet,index) for index in flightIndices]
a=8
