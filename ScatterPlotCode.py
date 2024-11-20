#Import arcpy & Mathplotlib
import arcpy
import matplotlib.pyplot as plt

#Input feature class
input_feature_class = r"C:\Users\kschw\OneDrive\Documents\GEOG392_FinalProject\Texas_Counties-20241115T022233Z-001\Texas_Counties\Texas_Counties.shp"

#Store data in lists
RISK_SCORE = []
F__of_Bale = []

#Create search cursor to get data
with arcpy.da.SearchCursor(input_feature_class, ["RISK_SCORE", "F__of_Bale"]) as cursor:
    for row in cursor:
        RISK_SCORE.append(row[0])
        F__of_Bale.append(row[1])

#Design ScatterPlot
plt.figure(figsize = (8,6))
plt.scatter(RISK_SCORE, F__of_Bale, color = 'blue')
plt.xlabel("Drought Severity Score")
plt.ylabel("Number of Cotton Bales")
plt.title("Scatter Plot of Drought Severity Score vs Number of Cotton Bales Per County")
#Customize y axis numbers
yvalue = [10000, 500000, 1000000, 5000000, 10000000]
yvalue_unit = ['10k', '500k', '1M', '5M', '10M']
plt.yticks(yvalue, yvalue_unit)

#Show ScatterPlot
plt.show()
