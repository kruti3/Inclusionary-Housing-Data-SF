# Inclusionary-Housing-Data-SF


1. python create_parameter_list.py
   Generates file parameter_boolean:
   			parameter if True is unique for all rows
   								else constant

2. python filter_columns.py
   iterates through the dataset, separates repetitive and unique data (for each row) data for each year
   Common.csv contains constant data of all years ~1kB
   			  (	24 columns, 15 rows)
   Data_*.csv contains data for the respective year (Boolean representations converted to strings) ~15MB
   			  ( 13 columns, 154342 rows)

3. python create_regionwise_data.py
	iterates through Data_*.csv 
	Creates area wise files 





-------------------------------------------------------------------
 sf.geojson file was downloaded from:

 Two regionwise changes were made in the geojson file (on the online tool at geojson.io)
 : removed glan park merged with diamond heights
   Created mission bay from soma region

Number of houses in each area was calculated with help of a script and added as an attribute to geojson file.
(using pygeoj)
