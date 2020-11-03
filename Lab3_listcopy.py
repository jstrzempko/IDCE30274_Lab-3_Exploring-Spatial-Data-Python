# Name: Jess Strzempko 
# Python Version: 2.7.15
# Assignment: Lab 3 Exploring Spatial Data Exercise 4

# Description: This script demonstrates how to output lists of elements (files) from a specific file path.
# It then shows how a for loop can be used to iterate over the elements of a list, copying the files into a geodatabase. 
# File paths included in the script are specific to the local computer on which the script was initially run. 
# It was created as Exercise 4 in Lab 3 Exploring Spatial Data IDCE 30274 Computer Programming for GIS. 

# Inputs: files in Lab 3 Data folder
# Outputs: list of files in Lab 3 Data folder, list of files copied into the NM geodatabase

# Import acrpy library if working outside ArcMap
import arcpy

# Import the env class to set environment properties
from arcpy import env

# Give the boolean value of True to the option of overwriting the existing output
env.overwriteOutput = True

# Set workspace to Data folder for Lab 3
env.workspace = "C:\\Users\\JeStrzempko\\Documents\\Comp_Prog\\Lab3\\Data_Lab_3_Exploring_Spatial_Data"

# Create a geodatabase for data management named NM.gdb
arcpy.CreateFileGDB_management("/Results/", "NM.gdb")

# Create a variable named fclist using the arcpy function ListFeatureClass
# List functions can be used to work with many types of elements, including feature classes, rasters, tables, and fields
fclist = arcpy.ListFeatureClasses()
print fclist
''' Output:
[u'amtrak_stations.shp', u'cities.shp', u'counties.shp', u'new_mexico.shp', u'railroads.shp']
'''

# Use a for loop to copy the shapefiles into the NM geodatabase we just created with the same names 
for fc in fclist:
    fcdesc = arcpy.Describe(fc)
    arcpy.CopyFeatures_management(fc, "/Results/NM.gdb/" + fcdesc.basename)
''' Output:
[u'amtrak_stations.shp', u'cities.shp', u'counties.shp', u'new_mexico.shp', u'railroads.shp']
'''




