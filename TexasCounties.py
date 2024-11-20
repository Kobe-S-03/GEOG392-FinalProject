import arcpy

#Select Texas
arcpy.management.SelectLayerByAttribute("USCounties", "NEW_SELECTION", "STATE_NAME = 'Texas'")
input_layer = "USCounties"
output_shapefile = r"D:\GEOG 676\project\data\Texas_Counties.shp"
arcpy.management.CopyFeatures(input_layer, output_shapefile)
arcpy.management.SelectLayerByAttribute(input_layer, "CLEAR_SELECTION")
