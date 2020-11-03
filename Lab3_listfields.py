# Name: Jess Strzempko 
# Python Version: 2.7.15
# Assignment: Lab 3 Exploring Spatial Data Exercise 5

# Description: This script demonstrates how to access and output information on the fields within a shapefile. 
# The code lists the names of the fields in the attribute table of the cities shapefile along with their data type.
# File paths included in the script are specific to the local computer on which the script was initially run. 
# It was created as Exercise 5 in Lab 3 Exploring Spatial Data IDCE 30274 Computer Programming for GIS. 

# Inputs: files in Lab 3 Data folder
# Outputs: list of field names and types in the cities shapefile

# Import acrpy library if working outside ArcMap
import arcpy

# Import the env class to set environment properties
from arcpy import env

# Give the boolean value of True to the option of overwriting the existing output
env.overwriteOutput = True

# Set workspace to Data folder for Lab 3
env.workspace = "C:\\Users\\JeStrzempko\\Documents\\Comp_Prog\\Lab3\\Data_Lab_3_Exploring_Spatial_Data"

# Create a variable fieldlist with a list of the fields in the attribute table of cities.shp
fieldlist = arcpy.ListFields("cities.shp")

# Use a for loop to iterate through field list and print the field name and data type separated by a space
for field in fieldlist:
    print field.name + " " + field.type
''' Output:
FID OID
Shape Geometry
CITIESX020 Double
FEATURE String
NAME String
POP_RANGE String
POP_2000 Integer
FIPS55 String
COUNTY String
FIPS String
STATE String
STATE_FIPS String
DISPLAY SmallInteger
'''
