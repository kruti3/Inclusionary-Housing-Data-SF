import pygeoj
import csv

def main():
	column_unique_elements = [ 'Bayview','Bernal', 'Castro', 'China','Crocker','Diamond','Downtown',
							'Excel','Finan','GGPark','Haight','InRich','InSun','Lakeshore','Marina',
							'Mission','MissBay','Nob','Noe','NorthB','OceanV','OutRich','OutMiss',
							'OutSun', 'PacHts', 'Parkside', 'Potrero','Presid','PresidHt','Russian',
							'Seacliff', 'SOMA', 'TIYBI', 'Twin' ,'Visit','WestTP','WestAdd' ]

	sf_data_geojson = pygeoj.load('../data/sf.geojson')

	
	for one in column_unique_elements:
		file = csv.reader(open('../data/'+one+'.csv', 'r'))
		count = sum(1 for row in file)
		count_per_year = count/15

		for one_neighborhood in sf_data_geojson:
			if one_neighborhood.properties['neighborho'] == one:
				one_neighborhood.properties.update({'num_houses':count_per_year})

	sf_data_geojson.save('../data/sf.geojson')
	

if __name__ == '__main__':
	main()