# Name: Jess Strzempko 
# Python Version: 2.7.15
# Assignment: Lab 3 Exploring Spatial Data Exercise 2

# Description: This script uses many different functions to describe the properties of a shapefile.
# File paths included in the script are specific to the local computer on which the script was initially run. 
# It was created as Exercise 1 in Lab 3 Exploring Spatial Data IDCE 30274 Computer Programming for GIS. 

# Inputs: cities.shp [point shapefile of cities]
# Outputs: contained in the body of the script, all unicode string outputs describing properties of the data

# Import acrpy library if working outside ArcMap
import arcpy

# Import the env class to set environment properties
from arcpy import env

# Set workspace to Data folder for Lab 3
env.workspace = "C:\\Users\\JeStrzempko\\Documents\\Comp_Prog\\Lab3\\Data_Lab_3_Exploring_Spatial_Data"
# Define myshape variable as the application of the arcpy Describe function to cities.shp
myshape = arcpy.Describe("cities.shp")

# Alternatively, you can forgo setting the environment workspace
# and directly call on the layer with the full path name
myshape = arcpy.Describe("C:\\Users\\JeStrzempko\\Documents\\Comp_Prog\\Lab3\\Data_Lab_3_Exploring_Spatial_Data\\cities.shp")

# Within the description of the data, we ask for the data type
myshape.dataType
# Output: u'ShapeFile'

# Next, we can access cities.shp directly through the ArcMap file we were working in
# (this will not work outside an ArcMap environment)
# notice the lack of the .shp extension
mylayer = arcpy.Describe("cities")
# Similar to before, we can query the data type
# now a feature layer instead of shapefile because of where we are accessing it through (ArcMap vs. Files)
mylayer.dataType
# Output: u'FeatureLayer'

# Within the description, we query for the dataset type
mylayer.datasetType 
# Output: u'FeatureClass'

# Query for the catalog path
mylayer.catalogPath
# Output: u'C:\\Users\\JeStrzempko\\Documents\\Comp_Prog\\Lab3\\Data_Lab_3_Exploring_Spatial_Data\\cities.shp'

# Query for the base name of the file in mylayer
mylayer.basename
# Output: u'cities'

# Query for the file name withn appropriate extension
mylayer.file
# Output: u'cities.shp'

# Indicates whether the dataset is versioned or not
mylayer.isVersioned
# Output: False

# Outputs the shape type
mylayer.shapeType
# Output: u'Point'

# Query for the spatial reference
# however, this property consists of multiple objects that need to be accessed separately
mylayer.spatialReference
# Output: <geoprocessing spatial reference object object at 0x15CC6740>

# Within the spatial reference, get the name of the spatial reference
mylayer.spatialReference.name
# Output: u'GCS_North_American_1983'
# GCS stands for Geographic Coordinate System

# Get the type of spatial reference
mylayer.spatialReference.type 
# Output: u'Geographic'
# This data is in a geographic coordinate system, not a projected coordinate system currently
# In order to perform analysis on it, all layers should be projected into the same PCS

# This output lists the smallest and largest x and y coordinates of your data
mylayer.spatialReference.domain  
#Output: u'-400 -400 400 400'
