import arcpy

# Define the layer name for Cotton
input_layer = "Cotton"  

# Select counties with top 10 cotton production (rank less than 11)
arcpy.management.SelectLayerByAttribute(input_layer, "NEW_SELECTION", '"Rank" < 11')

# Write the selected features to a new feature class
output_feature_class = "Cotton_10"
arcpy.management.CopyFeatures(input_layer, output_feature_class)
print("Selection and export completed successfully.")
