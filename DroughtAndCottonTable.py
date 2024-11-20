import arcpy
import os

# Define paths
project_path = r"D:\GEOG 676\project\Group_10_arc\Group_10.aprx"
drought_excel_path = r"D:\GEOG 676\project\data\Drought_2000-2021.xlsx\Sheet1$"
cotton_excel_path = r"D:\GEOG 676\project\data\cotton.xlsx\Sheet2$"
output_gdb = r"D:\GEOG 676\project\Group_10_arc\Group_10.gdb"

# Output table names
drought_table = "Drought_2000_2021"
cotton_table = "Cotton"

# Check if the output geodatabase exists
if not arcpy.Exists(output_gdb):
    arcpy.CreateFileGDB_management(os.path.dirname(output_gdb), os.path.basename(output_gdb))

# Convert the drought Excel table to a geodatabase table
try:
    arcpy.conversion.TableToTable(drought_excel_path, output_gdb, drought_table)
    print(f"Successfully converted '{drought_excel_path}' to '{output_gdb}\\{drought_table}'.")
except Exception as e:
    print(f"Failed to convert drought table: {e}")

# Convert the cotton Excel table to a geodatabase table
try:
    arcpy.conversion.TableToTable(cotton_excel_path, output_gdb, cotton_table)
    print(f"Successfully converted '{cotton_excel_path}' to '{output_gdb}\\{cotton_table}'.")
except Exception as e:
    print(f"Failed to convert cotton table: {e}")

# Add the converted tables to the ArcGIS Project
aprx = arcpy.mp.ArcGISProject(project_path)
for m in aprx.listMaps():
    try:
        # Add drought table
        drought_tbl = m.addDataFromPath(f"{output_gdb}\\{drought_table}")
        print(f"Successfully added drought table '{drought_tbl.name}' to map '{m.name}'.")

        # Add cotton table
        cotton_tbl = m.addDataFromPath(f"{output_gdb}\\{cotton_table}")
        print(f"Successfully added cotton table '{cotton_tbl.name}' to map '{m.name}'.")

    except Exception as e:
        print(f"Failed to add tables to map '{m.name}': {e}")

# Cleanup
del aprx
