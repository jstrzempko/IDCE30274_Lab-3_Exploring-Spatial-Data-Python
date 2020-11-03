# Name: Jess Strzempko 
# Python Version: 2.7.15
# Assignment: Lab 3 Exploring Spatial Data Exercise 3

# Description: This script demonstrates how to output lists of elements (files) from a specific file path.
# It then shows how a for loop can be used to iterate over the elements of the list to carry out a repetitive task.
# File paths included in the script are specific to the local computer on which the script was initially run. 
# It was created as Exercise 3 in Lab 3 Exploring Spatial Data IDCE 30274 Computer Programming for GIS. 

#Describing data typically works on a single element, such as a feature class.
#List functions can be used to work with many types of elements, including feature classes, rasters, tables, and fields.

# Inputs: files in Lab 3 Data folder
# Outputs: list of files in Lab 3 Data folder, list of formatted Name & Data type for each file

# Import acrpy library if working outside ArcMap
import arcpy

# Import the env class to set environment properties
from arcpy import env

# Set workspace to Data folder for Lab 3
env.workspace = "C:\\Users\\JeStrzempko\\Documents\\Comp_Prog\\Lab3\\Data_Lab_3_Exploring_Spatial_Data"

# Create a variable named fclist using the arcpy function ListFeatureClass
# List functions can be used to work with many types of elements, including feature classes, rasters, tables, and fields.
fclist = arcpy.ListFeatureClasses()
print fclist
''' Output:
[u'amtrak_stations.shp', u'cities.shp', u'counties.shp', u'new_mexico.shp', u'railroads.shp']
'''

# Describe function can be used to access properties of each of the feature classes in a workspace
# using a for loop to iterate over the elements in the list
for fc in fclist:
    fcdescribe = arcpy.Describe(fc)
    print "Name: " + fcdescribe.name
    print "Data type: " + fcdescribe.dataType

''' Output:
Name: amtrak_stations.shp
Data type: ShapeFile
Name: cities.shp
Data type: ShapeFile
Name: counties.shp
Data type: ShapeFile
Name: new_mexico.shp
Data type: ShapeFile
Name: railroads.shp
Data type: ShapeFile
'''


