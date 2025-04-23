from datetime import date
import os
import arcpy

DATABASE = "D:\\projects\\Floyed\\gis.sde"
arcpy.env.overwriteOutput = True
arcpy.env.workspace = DATABASE

# listing datasets and featureclasses
datasets = arcpy.ListDatasets()
featureclasses = arcpy.ListFeatureClasses()

elements = []

for fc in featureclasses:
  elements.append(fc)
for set in datasets:
  elements.append(set)  

# today's date with format 'dd-mm-yy'
today = date.today().strftime('%d-%m-%Y')

dest = "D:\\gisBackup"
geo_name = f"{today}.gdb"

#creating new geodatabase
arcpy.management.CreateFileGDB(dest, geo_name)

print(f"new geodatabse named {geo_name} has been created")

print("copying featureclasses")

for element in elements:
  arcpy.management.Copy(f'{DATABASE}\\{element}', f"{dest}\\{geo_name}")

print('finished copying featureclasses and datasets')
