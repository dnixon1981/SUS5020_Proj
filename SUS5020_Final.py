#  Name:   SUS5050.py
#
#  Created: 11/10/2017
#
#  Purpose: Provide an interface to convert the Spectral WQ data from xls file to a table in
#               a geodatabase to provide a basis to corilate mulitple sample datasets for Water Quality comparison.
#
#  Author:  Dave Nixon
##################################################

import arcpy
from arcpy import env
import os
import pandas as pd
from collections import OrderedDict
import matplotlib.pyplot as plt
import numpy as np
#from sklearn import datasets, linear_model
#from sklearn.metrics import mean_squared_error, r2_score
#import PartialLeastSquares as PLS

arcpy.env.overwriteOutput = True


inSensor = arcpy.GetParameterAsText(0)
inWQ = arcpy.GetParameterAsText(1)
outfile = arcpy.GetParameterAsText(1) #as GDB

# Set environment variables
#Add input for files here:
Sensor_Path = os.path.dirname(inSensor)
Sensor_Sheet = os.path.basename(inSensor)
WaterQ_Path = os.path.dirname(inWQ)
WaterQ_Sheet = os.path.basename(inWQ)
#r"C:\Users\daven\Desktop\Sustainability Final Project\Spectral_Sensor.xlsx"
#r"C:\Users\daven\Desktop\Sustainability Final Project\WQ_Sensor_Data.xlsx"

try:
    SensorRead = pd.read_csv(inSensor)
    Readfile = 1
    arcpy.AddMessage("Read CSV")
except:
    SensorRead = pd.read_excel(Sensor_Path, sheetname = Sensor_Sheet[:-1])
    Readfile = 1
    arcpy.AddMessage("Read Excel")
try:
    WaterQRead = pd.read_csv(inWQ)
    Readfile = Readfile + 1
    arcpy.AddMessage("Read CSV")
except:
    WaterQRead = pd.read_excel(WaterQ_Path, sheetname = WaterQ_Sheet[:-1])
    Readfile = Readfile+ 1
    arcpy.AddMessage("Read Excel")
if Readfile <> 2:
    arcpy.AddMessage("One or more input files are not recognized as a .CSV file or Excel Sheet is not named Sheet1")
    sys.exit()

DF_Sensor = pd.DataFrame(SensorRead)
DF_WaterQ = pd.DataFrame(WaterQRead)

arcpy.AddMessage(DF_WaterQ)
#pls = PLS.PartialLeastSquares(XMatrix_file = XMatrix_file, YMatrix_file = YMatrix_file, epsilon = 0.0001)
#pls.get_XMatrix_from_csv()
#pls.get_YMatrix_from_csv()
#B = pls.PLS()
