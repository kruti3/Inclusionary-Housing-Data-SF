import csv

def main():
	column_unique_elements = [ 'Bayview','Bernal', 'Castro', 'China','Crocker','Diamond','Downtown',
							'Excel','Finan','GGPark','Haight','InRich','InSun','Lakeshore','Marina',
							'Mission','MissBay','Nob','Noe','NorthB','OceanV','OutRich','OutMiss',
							'OutSun', 'PacHts', 'Parkside', 'Potrero','Presid','PresidHt','Russian',
							'Seacliff', 'SOMA', 'TIYBI', 'Twin' ,'Visit','WestTP','WestAdd' ]

	
	year = [str(2001+i) for i in range(15)]
	row = ['year','MapBlkLot_Master','MapBlkLot_Year','LandUse_AsGiven','Zoning_AsGiven','ParkingMinReq','Area'
				,'Bldg_SqFt_Use','Env_1000_Dens','SHistoric1','DevPotential_Dens','Zoning','LandUse']
	
	for one in column_unique_elements:
		out_file = csv.writer(open('../data/'+one+'.csv', 'w+'))
		out_file.writerow(row)
	blg = set([])
	area = set([])
	for one_year in year:

		print one_year
		fp = open('../data/Data_'+one_year+'.csv')
		reader = csv.reader(fp)
		i = 0
		for row in reader:
			if i:
				final_row = [one_year]
				neighbor = row[-3]
				
				area.add(row[-1])
				blg.add(row[2])
				del row[-3]
				out_file = csv.writer(open('../data/'+neighbor+'.csv', 'a+'))
				final_row.extend(row)
				out_file.writerow(final_row)
			i+=1

	print area
	print blg
	

if __name__ == '__main__':
	main()