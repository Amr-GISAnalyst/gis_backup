from datetime import date
import os
import arcpy
import arcpy.management
import shutil
import sys

DATABASE = "E:\\GIS Project\\gis_backup\\gis.sde"
arcpy.env.overwriteOutput = True
arcpy.env.workspace = DATABASE

# listing datasets and featureclasses
print("listing datasets and featureclasses\n---------------")
datasets = arcpy.ListDatasets()
layers = arcpy.ListFeatureClasses()

# today's date with format 'dd-mm-yy'
print("today's date with format 'dd-mm-yy'\n---------------")
today = date.today().strftime("%d-%m-%Y")

dest = "E:\\Projects\\gis_backup\\daily_backup"
geo_name = f"{today}.gdb"

def backup():
# creating new geodatabase
  print("creating new geodatabase\n---------------")
  arcpy.management.CreateFileGDB(dest, geo_name)

  print(f"new geodatabse named {geo_name} has been created\n---------------")

  print("copying datasets ...\n---------------")
  for data_set in datasets:
    arcpy.Copy_management(f"E:\\GIS Project\\gis_backup\\gis.sde\\{data_set}", f"{dest}\\{geo_name}\\{data_set[4:]}")
    print(f"{data_set} dataset is copied!")

  print("All Datasets are copied! ...\n---------------")

  print("copying featureclasses ...\n---------------")
  for layer in layers:
    arcpy.management.Copy(f"{DATABASE}\\{layer}", f"{dest}\\{geo_name}\\{layer[4:]}")
    print(f"{layer} dataset is copied!")

  print("All Featureclasses are copied! ...\n---------------")

  # zipping .gdb file.
  print("zipping geodatabase backup\n---------------")
  shutil.make_archive(f"{dest}\\{today}", 'zip', f"{dest}\\{geo_name}")

  shutil.rmtree(f"{dest}\\{geo_name}")
  print(f"File {geo_name} deleted successfully. \n and zipped file exixsts at \n {dest}\\{today}")
  

def retry(function):

  for i in range(3):
    try:
      function()
      break
    except:
      e = sys.exc_info()[1]
      print(e.args[0])
      if os.path.exists(f"{dest}\\{geo_name}"):
        shutil.rmtree(f"{dest}\\{geo_name}")
      continue

  print(f"You are all set and your GIS backup is at {dest}")


retry(backup)
