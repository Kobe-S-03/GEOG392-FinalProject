import arcpy

# Define the layer name for Drought
input_layer = "Drought_2000_2021"  

# Select counties with least drought events
arcpy.management.SelectLayerByAttribute(input_layer, "NEW_SELECTION", '"DRGT_EVNTS" < 469')

# Write the selected features to a new feature class
output_feature_class = "Least_Drgt_events"
arcpy.management.CopyFeatures(input_layer, output_feature_class)

print("Selection and export completed successfully.")
