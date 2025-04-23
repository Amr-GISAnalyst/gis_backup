from datetime import date
import os
import arcpy
import arcpy.management

DATABASE = "D:\\projects\\Floyed\\gis.sde"
arcpy.env.overwriteOutput = True
arcpy.env.workspace = DATABASE

# listing datasets and featureclasses
datasets = arcpy.ListDatasets()
layers = arcpy.ListFeatureClasses()

# today's date with format 'dd-mm-yy'
today = date.today().strftime("%d-%m-%Y")

dest = "D:\\gisBackup"
geo_name = f"{today}.gdb"

# creating new geodatabase
arcpy.management.CreateFileGDB(dest, geo_name)


print(f"new geodatabse named {geo_name} has been created")

print("copying datasets ...")
for data_set in datasets:
  arcpy.Copy_management(f"D:\\projects\\Floyed\\gis.sde\\{data_set}", f"{dest}\\{geo_name}\\{data_set[4:]}")
  print(f"{data_set} dataset is copied!")

# print("copying featureclasses ...")
# for layer in layers:
#   arcpy.Copy_management(f"D:\\projects\\Floyed\\gis.sde\\{layer}", f"{dest}\\{geo_name}\\{layer[4:]}", "FeatureClass")
#   print(f"{layer} copied!")