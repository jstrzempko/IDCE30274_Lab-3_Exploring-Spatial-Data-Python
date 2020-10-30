# Name: Jess Strzempko 
# Python Version: 2.7.15
# Assignment: Lab 3 Exploring Spatial Data Exercise 1

# Description: This script uses the arcpy function Exists to test for the presence of a shapefile in the workspace. 
# File paths included in the script are specific to the local computer on which the script was initially run. 
# It was created as Exercise 1 in Lab 3 Exploring Spatial Data IDCE 30274 Computer Programming for GIS. 

# Inputs: cities.shp [shapefile of cities]
# Outputs: boolean values of shape_exists and shape_exists2 (True or False)

# Import acrpy library since I am working outside ArcMap
import arcpy

# Import the env class to set environment properties
from arcpy import env

# Set workspace to Data folder for Lab 3
env.workspace = "C:\\Users\\JeStrzempko\\Documents\\Comp_Prog\\Lab3\\Data_Lab_3_Exploring_Spatial_Data"

# Define a variable shape_exists that uses arcpy's Exist function to test for the presence of cities.shp
shape_exists = arcpy.Exists("cities.shp")
# Print the boolean output of the Exists function, since we only defined a variable in the previous line
print shape_exists

# Complete the same steps using all capital letters in the shapefile name
shape_exists2 = arcpy.Exists("CITIES.SHP")
print shape_exists2

# Output:
# >>> 
# RESTART: C:/Users/JeStrzempko/Documents/Comp_Prog/Lab3/Data_Lab_3_Exploring_Spatial_Data/Results/Lab3_shape_exists.py 
# True
# True
# >>> 
# This output means that cities does exist within the Data folder 
