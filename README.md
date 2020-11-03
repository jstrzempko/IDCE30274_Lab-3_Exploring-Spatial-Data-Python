# Lab 3: Exploring Spatial Data Using Python
Due: 6th November 2020

This repo was created to submit files for Lab 3 for IDCE 30274 Computer Programming for GIS taught by Professor Shadrock Roberts at Clark University. All scripts were created to learn functions within the arcpy library. It contains:
* `Lab3_shape_exists.py`: test for the presence of a shapefile in the workspace using function `.Exists()`
* `Lab3_describing_data`: describe the properties of a shapefile using function `.Describe()` (`.dataType`, `.datasetType`, `.catalogPath`, `.baseName`, `.file`, `.isVersioned`, `.shapeType`, `.spatialReference.name`, `.spatialReference.type`, `.spatialReference.domain`)
  + This script contains single lines of code run in the ArcPy window within ArcMap with comments that show the output of each line. These cannot be replicated outside of the ArcMap environment. This script solely serves as documentation of the many functions used. 
* `Lab3_list.py`:  output list of elements (files) from a specific file path and use a for loop to iterate over elements to carry out a repetitive task using functions `.ListFeatureClasses()` and `.Describe()`
* `Lab3_listcopy.py`: use a for loop to iterate over elements of a list to copy files into a geodatabase using function `.CopyFeatures_management()`
* `Lab3_listfields.py`: list the names and data types of the fields in the attribute table of the cities shapefile using function `.ListFields()`

# The Code
The script is meant to be run using shapefiles provided for this class with file paths and names specific to the student submission. If questions arise, users can contact Jess Strzempko at JeStrzempko@clarku.edu for more help and further information.
